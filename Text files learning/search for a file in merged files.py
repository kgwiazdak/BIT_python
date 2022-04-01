import os


def search(file, path):
    file = file[:-4]
    files = os.listdir(path)
    text_files = [file for file in files if file.endswith(".txt")]
    target_filename = None
    for filename in text_files:
        if file in filename:
            target_filename = filename
            break
    if target_filename == None:
        raise FileNotFoundError
    tfilenames = target_filename[:-4].split("_")
    for i in range(len(tfilenames)):
        if file == tfilenames[i]:
            index = i
            break
    with open(path+target_filename) as f:
        merged_text = f.read()
    arr_text = merged_text.split("\n---EOF---\n")
    return arr_text[index]


if __name__ == '__main__':
    path = r"C:\Users\User\Desktop\Articles\\"
    text = search("article02.txt", path)
    print(text)