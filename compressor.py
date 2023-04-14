from PIL import Image
import os

picturesFolder = "/Users/yourUserName/yourFolderName/"

if __name__ == "__main__":
    for filename in os.listdir(picturesFolder):
        name, extension = os.path.splitext(picturesFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(picturesFolder + filename)
            os.remove(picturesFolder + filename)
            picture.save(picturesFolder+filename, optimize=True, quality=60)
            print(name + ": " + extension)