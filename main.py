import os
import shutil
import json
import logging

def copy_files_to_files_folder(org_folder, files_folder):
    if not os.path.exists(files_folder):
        os.makedirs(files_folder)

    total_files = sum([len(files) for _, _, files in os.walk(org_folder)])
    copied_files = 0

    for root, dirs, files in os.walk(org_folder):
        for file in files:
            source_path = os.path.join(root, file)
            target_path = os.path.join(files_folder, file)

            if os.path.exists(target_path):
                logging.warning(f"Target file already exists: {target_path}")
            else:
                shutil.copy(source_path, target_path)
                logging.info(f"File copied: {target_path}")
                copied_files += 1
                print(f"\rCopying {copied_files}/{total_files} files from 'org' to 'files'.", end='', flush=True)

    print(f"\rCopying {copied_files} files from 'org' to 'files'.")

def configure_logging():
    logging.basicConfig(filename='errors.log', level=logging.ERROR, encoding='utf-8')

def parse_objects_json():
    minecraft_sounds_list = []

    with open('objects.json') as json_file:
        data = json.load(json_file)

    for key, value in data.get("objects", {}).items():
        if key.startswith("minecraft/sounds/"):
            minecraft_sound = MinecraftSound(path=key, hash_value=value["hash"])
            minecraft_sounds_list.append(minecraft_sound)

    return minecraft_sounds_list

def copy_minecraft_sounds(minecraft_sounds_list, base_folder, files_folder):
    total_sounds = len(minecraft_sounds_list)
    print(f"\nProcessing {total_sounds} Minecraft Sounds:")

    for index, sound in enumerate(minecraft_sounds_list, start=1):
        target_path = os.path.join(base_folder, 'sounds', sound.path[len("minecraft/sounds/"):])
        source_file_path = os.path.join(files_folder, sound.hash)

        if os.path.exists(source_file_path):
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            try:
                shutil.copyfile(source_file_path, target_path)
                logging.info(f"File copied: {target_path}")
                print(f"[{index}/{total_sounds}] File copied: {target_path}")
            except Exception as e:
                logging.error(f"Error copying file: {source_file_path} to {target_path}")
                logging.error(f"Error details: {e}")
        else:
            logging.error(f"Source file not found: {source_file_path} (for Minecraft Sound object with path: {sound.path})")

class MinecraftSound:
    def __init__(self, path, hash_value):
        self.path = path
        self.hash = hash_value

def delete_contents_in_sounds_folder(sounds_folder):
    try:
        for root, dirs, files in os.walk(sounds_folder):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                logging.info(f"File deleted: {file_path}")

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                shutil.rmtree(dir_path)
                logging.info(f"Folder deleted: {dir_path}")
        logging.info("All files and folders in 'sounds' directory have been deleted.")
    except Exception as e:
        logging.error(f"Error deleting files and folders in 'sounds' directory: {e}")

def delete_files_in_files_folder(files_folder):
    try:
        for file in os.listdir(files_folder):
            file_path = os.path.join(files_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                logging.info(f"File deleted: {file_path}")
        logging.info("All files in 'files' directory have been deleted.")
    except Exception as e:
        logging.error(f"Error deleting files in 'files' directory: {e}")

def delete_files_folder(files_folder):
    try:
        shutil.rmtree(files_folder)
        logging.info(f"Folder deleted: {files_folder}")
    except Exception as e:
        logging.error(f"Error deleting 'files' folder: {e}")

if __name__ == "__main__":
    org_folder = 'org'
    files_folder = 'files'
    sounds_folder = 'sounds'
    base_folder = os.path.dirname(__file__)

    configure_logging()
    delete_contents_in_sounds_folder(sounds_folder)
    print("\nAll files and folders in 'sounds' directory have been deleted.\n")

    # Create folders if not exists
    os.makedirs(os.path.join(base_folder, 'sounds'), exist_ok=True)
    os.makedirs(os.path.join(base_folder, 'files'), exist_ok=True)

    copy_files_to_files_folder(org_folder, files_folder)
    minecraft_sounds_list = parse_objects_json()
    copy_minecraft_sounds(minecraft_sounds_list, base_folder, files_folder)
    delete_files_in_files_folder(files_folder)
    delete_files_folder(files_folder)
    print("\nAll files in 'files' directory have been deleted, 'files' folder deleted, and Minecraft Sounds processed.\n")
