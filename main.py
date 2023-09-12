# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os, time, shutil, re
global DEBUG
DEBUG = False

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


class fileType:
    def __init__(self, extensions, name, parentDirectory, downloadDirectory):
        self.extensions = extensions
        self.name = name
        self.filesList = []
        self.parentDirectory = parentDirectory
        self.downloadDirectory = downloadDirectory
        self.targetDirectory = self.parentDirectory + 'downloaded_' + self.name

    def baseFilter(self, file):
        for type in self.extensions:
            if type in file:
                return True
        return False

    def createFileList(self, files):
        self.filesList = list(filter(self.baseFilter, files))
        if DEBUG: print(self.filesList)

    def createNewDirectory(self):
        if not os.path.isdir(self.targetDirectory + '/'):
            os.mkdir(self.targetDirectory)
            if DEBUG: print("downloaded", self.name, "made")

    def moveFiles(self, files):
        self.createFileList(files)
        self.createNewDirectory()
        if self.filesList:
            for file in self.filesList:
                new_path = self.targetDirectory + '/' + file
                shutil.move(self.downloadDirectory + '/' + file, new_path)
                if DEBUG: print("moved", file, "from", self.downloadDirectory, "to", new_path)

    def getList(self):
        return self.filesList


def moooove():
    if DEBUG: print(os.listdir())
    files = [file for file in os.listdir(downloadDirectory)]

    images = fileType(['.png', '.jpg'], 'images', '', downloadDirectory)
    if DEBUG: print(images.getList())
    images.moveFiles()

    documents = fileType(['.docx', '.pdf', '.xls'], 'documents', '', downloadDirectory)
    if DEBUG: print(documents.getList())
    documents.moveFiles()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #mac downloadDirectory = '/Users/vinhngo/Downloads'
    #windows downloadDirectory = 'C:/Users/vinh-school/Downloads'
    downloadDirectory = '/Users/vinhngo/Downloads'
    while(True):
        moooove()
        print("mooove")
        time.sleep(5)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/