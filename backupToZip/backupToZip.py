import zipfile
import os

def zip2file(folder):
    number = 1
    zipname = os.path.basename(folder) + "_" + str(number) + ".zip"
    while True:
        if not os.path.exists(zipname):
            break
        number += 1
        zipname = os.path.basename(folder) + "_" + str(number) + ".zip"
    
    print(f"saving folder as: {zipname}")
    zipf = zipfile.ZipFile(zipname, "w")
    
    for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, os.path.abspath(folder))
            zipf.write(file_path, arcname)
    
    zipf.close()
    print('Done.')

print("What is the folder's name:")
inputed_name = input()
zip2file(inputed_name)