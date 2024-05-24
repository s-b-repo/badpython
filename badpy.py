import os

def make_flash_drive_detect_as_keyboard():
    # Get the path of the mounted flash drive
    flash_drive_path = "/dev/sdb"  # Replace with the appropriate path of the flash drive on your Linux system
    
    # Unmount the flash drive
    os.system(f"sudo umount {flash_drive_path}")

    # Change the partition type of the flash drive to 0x0E (FAT16)
    os.system(f"sudo parted {flash_drive_path} set 1 0E")

def create_script_file():
    # Specify the script content to simulate keystrokes
    script_content = """
    #!/bin/bash
    # Simulate keystrokes as user input on Windows
    echo "Hello, World!" | sudo tee /dev/hidg0
    """

    # Create the script file and write the content
    script_file_path = "/path/to/flash/drive/script.sh"  # Replace with the desired path on the flash drive
    with open(script_file_path, "w") as file:
        file.write(script_content)

    # Set the appropriate permissions for the script file
    os.system(f"sudo chmod +x {script_file_path}")

if __name__ == "__main__":
    make_flash_drive_detect_as_keyboard()
    create_script_file()
