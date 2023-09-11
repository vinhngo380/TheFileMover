# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os, time, shutil, re


def moooove():
    files = [f for f in os.listdir(downloadDirectory) if valid_filetypes in f.lower(f.split('\.'))]
    images = [f for f in files if image_filetypes in f.lower()]
    documents = [f for f in files if document_filetypes in f.lower()]


    for image in images:
        print(re.split('; |, |\*|\n|\.|\s|', image))
        new_path =  'downloaded_images/' + image
        shutil.move(downloadDirectory + '/' + image, new_path)
        print("moved", image, "to", new_path)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    string = "hi      everyone my name is markplier"
    words = ['blahblahblah', 'is', 'uhhh']
    list_of_string = string.split()
    print(word for word in list_of_string if word in words) #[i for i in L1 if i in L2]
    """
    downloadDirectory = '/Users/vinhngo/Downloads'
    image_filetypes = ['.jpg', '.png']
    document_filetypes = ['.docx', '.pdf']
    valid_filetypes = image_filetypes + document_filetypes

    while(True):
        moooove()
        print("mooove")
        time.sleep(5)
    """


# See PyCharm help at https://www.jetbrains.com/help/pycharm/