import os
import shutil
import datetime

image_extensions = ["jpg", "JPG", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp", "svg", "heic", "heif", "raw", "ico"]
video_extensions = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "webm", "m4v", "3gp", "mpeg", "mpg"]
audio_extensions = ["mp3", "wav", "aac", "flac", "ogg", "wma", "m4a", "alac"]
document_extensions = ["doc", "docx", "pdf", "txt", "odt", "rtf", "html", "htm", "md", "epub", "ppt", "pptx", "xls", "xlsx", "log", "ini"]


def select_method():
    while True:
        print("List of sorting methods:")
        print("'y' - Sort by year of creation")
        print("'t' - Sort by type of file")
        print()
        sorting_method = input("> Please select sorting method: ")
        if not sorting_method in ["y", "t"]:
            raise TypeError("Enter only displayed option.")
        else:
            break
    return sorting_method

def sort_method(item, file_path, folder_path, SM):
    if SM == "y":
        item_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        new_file_path = os.path.join(folder_path, str(item_date.year))
    
    elif SM == "t":
        extension = os.path.splitext(item)[1]
        E = extension.lstrip(".")
        if E in image_extensions:
            E = "Obrázky"
        elif E in audio_extensions:
            E = "Audio"
        elif E in video_extensions:
            E = "Videa"
        elif E in document_extensions:
            E = "Dokumenty"

        new_file_path = os.path.join(folder_path, E)

    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)
    new_file_path = os.path.join(new_file_path, item)
    shutil.move(file_path, new_file_path)

def sort_files(folder_path, SM):
    moved_files = []
    folder_items = os.listdir(folder_path)
    for item in folder_items:
        file_path = os.path.join(folder_path, item)
        if os.path.isfile(file_path):
            item = sort_method(item, file_path, folder_path, SM)
            moved_files.append(item)

    return moved_files

def count_files(MF):
    num = 1
    if MF:
        print("")
        for item in MF:
            print(f"Item '{item}' changed path. ({num})")
            num += 1
        print("")
    elif not MF:
            print("\nNo item changed path.\n")


def main():
    while True:
        print()
        folder_path = input("> Enter folder path: ")
        print()
        sorting_method = select_method()
        moved_files = sort_files(folder_path, sorting_method)
        count_files(moved_files)

        if not input("> Again? (Y/any): ") in["Y", "y"]:
            print("Bye!")
            break


if __name__ == "__main__":
    main()

