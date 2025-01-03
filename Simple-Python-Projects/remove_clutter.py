import os
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


if __name__ == '__main__':
    files = os.listdir()
    files.remove("clutter.py")
    print(files)
    createIfNotExists("Images")
    createIfNotExists("Media")
    createIfNotExists("Docs")
    createIfNotExists("CPP")
    createIfNotExists("Others")

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files
              if os.path.splitext(file)[1].lower() in imgExts]
    
    medExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files
              if os.path.splitext(file)[1].lower() in medExts]
    
    docExts = [".txt", ".docx", ".pdf", ".doc"]
    documents = [file for file in files
                 if os.path.splitext(file)[1].lower() in docExts]
    
    cppExts = [".cpp"]
    cpp = [file for file in files
           if os.path.splitext(file)[1].lower() in cppExts]
    
    others = []
    for file in files:
        exts = os.path.splitext(file)[1].lower()
        if ((exts not in medExts) and (exts not in imgExts)
            and (exts not in cppExts) and (exts not in docExts)
        and (os.path.isfile(file))):
            others.append(file)
    
    print(others)
    
    # for media in medias:
    #     os.replace(media, f"Media/{media}")
    # for doc in documents:
    #     os.replace(doc, f"Docs/{doc}")
    # for cpp in cpp:
    #     os.replace(cpp, f"CPP/{cpp}")
    # for img in images:
    #     os.replace(img, f"Images/{img}")
    
    move("Images", images)
    move("CPP", cpp)
    move("Docs", documents)
    move("Media", medias)
    move("Others", others)