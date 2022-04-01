import os

def merge(path, files):
    contents = []
    for f in files:
        with open(path+f) as file:
            text = file.read()
            contents.append(text)

    new_text = "\n---EOF---\n".join(contents)
    names = [file[:-4] for file in files]
    merged_name = '_'.join(names)+'.txt'
    with open(path+merged_name, "w") as file:
        file.write(new_text)

def merge_files(path):
    os.chdir(path)
    files = os.listdir()
    text_files = [file for file in files if file.endswith(".txt")]
    arr = []
    i = 0
    while i < len(text_files):
        merge(path, text_files[i:i + 10])
        i += 10
    for name in text_files:
        os.remove(name)

if __name__ == '__main__':
    path = r"C:\Users\User\Desktop\Articles\\"
    os.chdir(path)
    for i in range(1, 26):
        title = "article"+str(i).zfill(2)+".txt"
        with open(path+title, "w") as file:
            file.write("anything")
    merge_files(path)



