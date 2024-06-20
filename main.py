import os
import pathlib
import shutil
fileFormat ={
    "Web" :[".html", ".htm", ".xhtml"],
    
    "Pictures" :[".jpeg", ".jpg", ".tiff", ".svg", ".png", ".bmp",".webp",".gif",".eps"],

    "Video" :[".avi", ".mkc", ".flv",".mov", ".mp4", ".webm",".vob", ".mng", ".mpg", ".3gp"],

    "Document" :[".txt", ".pdf", ".rtf", ".docx",".csv", ".doc", ".wps", ".msg", ".wpd",".docm",".dotx",""],


    "Audio" :[".aac", ".aa",".dvf",".m4a",".mp4",".mp3"],

    "CompressedCompressed" :[ ".cpio", ".tar", ".rz", ".7z",".rar",".zip",".xar"],
}

fileTypes = list(fileFormat.keys())
fileFormats = list(fileFormat.values())

# print(fileTypes)
# print(fileFormats)


for file in os.scandir():
    fileName = pathlib.Path(file)
    fileFormatType= fileName.suffix.lower()

    # print(fileName)
    
    # print(fileFormats)

    src = str(fileName)
    destination = "Other"
    if fileFormatType =="":
        print(f"{src} has no file format")
    else:
         for formats in fileFormats:
             if fileFormatType in formats:
                 folder = fileTypes[fileFormats.index(formats)]
                #  print(folder)
                 if os.path.isdir(folder) == False:
                    os.mkdir(folder)
                 destination = folder
             else:
                 if os.path.isdir("Other") == False:
                     os.mkdir("Other")
    print(src, "moved to", destination, "!")
    shutil.move(src, destination)


print("File organizer started")
input("\n Press enter to EXIT")