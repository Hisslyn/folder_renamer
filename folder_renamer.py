import os
import re

def rename_folders():
    # Get the current working directory
    current_dir = os.getcwd()

    # Regular expression to match mm.dd.yyyy format
    pattern = re.compile(r'^(\d{2})\.(\d{2})\.(\d{4})$')

    # Loop through all items in the current directory
    for folder_name in os.listdir(current_dir):
        folder_path = os.path.join(current_dir, folder_name)

        # Check if the item is a folder and matches the pattern
        if os.path.isdir(folder_path):
            match = pattern.match(folder_name)
            if match:
                # Extract month, day, year
                mm, dd, yyyy = match.groups()

                # Create the new folder name in yyyy.mm.dd format
                new_folder_name = f"{yyyy}.{mm}.{dd}"
                new_folder_path = os.path.join(current_dir, new_folder_name)

                # Rename the folder
                os.rename(folder_path, new_folder_path)
                print(f"Renamed: {folder_name} -> {new_folder_name}")
            else:
                print(f"Skipped: {folder_name} (Does not match mm.dd.yyyy format)")

if __name__ == "__main__":
    rename_folders()

# This code renames all mm.dd.yyyy format folder names in the current directory into yyyy.mm.dd format