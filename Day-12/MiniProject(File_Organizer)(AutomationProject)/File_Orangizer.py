import os, shutil

def organize(folder):
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        ext = ext[1:]

        if ext == "":
            continue

        folder_path = os.path.join(folder, ext.upper())

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(os.path.join(folder, filename), os.path.join(folder_path, filename))

path = input("Enter folder path: ")
organize(path)
print("✅ Files Organized Successfully!")


# ✅ What it does:
# Automatically sorts files into folders by extension (e.g. .jpg, .pdf, .txt).