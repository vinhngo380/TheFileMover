# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os, time, shutil, re


def image_filter(file):
    image_filetypes = ['.jpg', '.png']
    for file_type in image_filetypes:
        if file_type in file:
            return True
    return False


def document_filter(file):
    document_filetypes = ['.docx', '.pdf', '.doc']
    for file_type in document_filetypes:
        if file_type in file:
            return True
    return False


def moooove():
    files = [file for file in os.listdir(downloadDirectory)]

    images = list(filter(image_filter, files))
    documents = list(filter(document_filter, files))
    print("images", images)
    print("doucments", documents)

    print(os.listdir())
    parent_directory = 'C:/Users/vinh-school/PycharmProjects/TheFileMover/'
    if images:
        if not os.path.isdir(parent_directory + 'downloaded_images/'):
            os.mkdir(parent_directory + 'downloaded_images')
            print("downloaded_images made")
        for image in images:
            new_path = parent_directory + 'downloaded_images/' + image
            shutil.move(downloadDirectory + '/' + image, new_path)
            print("moved", image, "to", new_path)

    if documents:
        if not os.path.isdir(parent_directory + 'downloaded_documents/'):
            os.mkdir(parent_directory + 'downloaded_documents')
            print("downloaded_documents made")
        for document in documents:
            new_path = parent_directory + 'downloaded_documents/' + document
            shutil.move(downloadDirectory + '/' + document, new_path)
            print("moved", document, "to", new_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    downloadDirectory = 'C:/Users/vinh-school/Downloads'
    while(True):
        moooove()
        print("mooove")
        time.sleep(5)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/