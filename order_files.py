import os
import shutil
import argparse

# Organize folders by file extension
# Enter command: python order_files.py "your_path" 


def organize_folders(folder):
    moved_files = []

    folder_items = os.listdir(folder)

    for item in folder_items:

        file_path = os.path.join(folder, item)
        if os.path.isfile(file_path):
            extension = os.path.splitext(item)[1]
            new_folder_path = os.path.join(folder, extension.lstrip("."))

            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            new_file_path = os.path.join(new_folder_path, item)
            shutil.move(file_path, new_file_path)

            moved_files.append(item)

    return moved_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize folders by file extension.")
    parser.add_argument("folder", help="Path to the folder you want to organize.")
    args = parser.parse_args()

    folder_path = args.folder
    moved_files = organize_folders(folder_path)

    num = 1
    if moved_files:
        print("")
        for item in moved_files:
            print(f"Item '{item}' changed path. ({num})")
            num += 1
        print("")
    elif not moved_files:
            print("\nNo item changed path.\n")