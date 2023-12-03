# Minecraft Sound Converter

The Minecraft Sound Converter is a tool designed for extracting Minecraft sounds and creating custom soundpacks. It simplifies the process of organizing sound files from the `%appdata%\.minecraft\assets\objects` directory into the tool's designated `sounds` folder. This tool allows users to create their own custom soundpacks with the organized sound files.

## Usage

1. **Extract the Sound Files Data:**
    - Open the `%appdata%\.minecraft\assets\indexes` folder and locate the file with the name corresponding to your desired Minecraft version.
    - Open this file using a text editor (for example Notepad++), and copy its content.
    - Paste the copied content into the `objects.json` file within the Minecraft Sound Converter directory. This step ensures that the tool has the necessary information about the sound files associated with the chosen Minecraft version.

2. **Prepare Sound Files:**
   - Copy the contents of `%appdata%\.minecraft\assets\objects` to the `org` folder. **Note: Use copy, not move, to avoid potential Minecraft errors.**

3. **Run the Tool:**
   - Execute the `main.py` script to start the Minecraft Sound Converter.

4. **Review Logs:**
   - Check the `errors.log` file for any issues encountered during the conversion process.

5. **Complete:**
   - After completion, the `sounds` folder will reflect the correct directory structure, including all necessary files. This structure is designed to be compatible with soundpack creation, ensuring a seamless integration of the organized sound files into your custom soundpack.

## Important Notes

- **Copy, Don't Move:**
  - Ensure you copy sound files to the `org` folder instead of moving them to prevent potential errors in Minecraft.

- **Log File:**
  - Review the `errors.log` file for detailed information about any errors encountered during the process.

- **Usage Disclaimer:**
  - This tool is intended for personal use only. Original Minecraft sounds must not be published or distributed.

---

**Disclaimer:** This tool is provided as-is and should be used with caution. Backup your Minecraft assets before running the tool to avoid data loss.
