import os
import shutil

# To Change the Drive
def ChangeDrive(driveName):
    driveName = driveName.replace(":","").upper().strip()
    driveName = driveName+":"
    os.chdir(driveName)

#To Check if the Folder is Present or Not
def CheckFolderPresent(fldrName):
    if os.path.isdir(fldrName): return True
    else: return False

def ChangeFolder(folderName):
    if '/' in folderName:
        folderName = os.path.normcase(folderName)
        os.chdir(folderName)
    else:
        if CheckFolderPresent(folderName):
            os.chdir(folderName)
        else:
            folderChoice = input("Enter whole Path of the folder or else Enter 'Back' to check the folder in previous folder: ")
            if folderChoice.upper().strip() == 'BACK':
                os.chdir('../')
                if CheckFolderPresent(folderName): os.chdir(folderName)
                else: print("Folder '"+folderName+"' is not present in the current Directory")
            else:
                folderName = os.path.normcase(folderName)
                if CheckFolderPresent(folderName): os.chdir(folderName)
                else: print("Enter Valid Path of the directory")

def CreateFolder(folderName):
    folderName = os.path.normcase(folderName)
    if CheckFolderPresent(folderName) == False: os.mkdir(folderName)
    else: print("Folder '"+folderName+"' is already present in the current Directory")

def CheckEmptyFolder(folderName):
    folderName = folderName.strip()
    if len(os.listdir(folderName)) == 0: return True
    else: return False

def RemoveFolder(folderName):
    folderName = folderName.strip()
    if CheckFolderPresent(folderName):
        if(CheckEmptyFolder(folderName) == False):
            userPermission = input("Press 'Y' to delete the "+folderName+" with all its components or 'N' for entering the folder to delete a file: ").upper()
            invalidChoiceCount = 0
            while (userPermission != 'Y' and userPermission != 'N') and invalidChoiceCount<3:
                invalidChoice += 1
                print("\nInvalid input. Select the option again")
                userPermission = input("Press 'Y' to delete the "+folderName+" with all its components or 'N' for entering the folder to delete a file: ").upper()
            if invalidChoiceCount!=3:
                if userPermission == "Y":
                    shutil.rmtree(folderName)
                    print("Folder '"+folderName+"' has been deleted with all its components.")
                elif userPermission == 'N':
                    print("Entering the '"+folderName+"'")
                    os.chdir(folderName)
                    print("\nList of Files Present in the folder: "+folderName)
                    for i in os.listdir(os.getcwd()): print(i)
                    newFileName = input("\nEnter the 'file name(with extension)' you want to Delete or Enter 'N' to go back to Main Menu: ")
                    if(newFileName.upper() != "N"): RemoveFile(newFileName)
                    else: print("Navigating Back to Main Menu")
            else: print("\nMax Attempts Performed. Navigating Back to Main Menu")
        else:
            os.rmdir(folderName)
            print("Folder '"+folderName+"' has been deleted.")
    else: print("Folder '"+folderName+"' is not present in the current Directory")

def CreateFile(newFile, ext):
    fileName = newFile.strip()+"."+ext.strip()
    if(CheckFilePresent(fileName)): print("File "+fileName+" is already present.")
    else:
        with open(fileName, mode="w") as file:
            pass

def CheckFilePresent(completeFileName):
    if '/' in completeFileName:
        completeFileName = os.path.normcase(completeFileName)
        if os.path.isfile(completeFileName): return True
        else: False
    else:
        if completeFileName in os.listdir(os.getcwd()): return True
        else: return False

def RemoveFile(fileToRemove):
    fileName = fileToRemove.strip()
    if CheckFilePresent(fileName):
        os.remove(fileName)
        print("File '"+fileName+"' has been deleted.")
    else: print("File '"+fileName+"' is not present in the current Directory")

def ReadFile(fileName,ext):
    fileName = fileName.strip()+"."+ext.strip()
    if CheckFilePresent(fileName):
        with open(fileName, mode="r") as file: print(fileToOpen.read())
    else: print("File '"+fileName+"' is not present in the current Directory")

def WriteFile(fileName,ext,data):
    fileName = fileName.strip()+"."+ext.strip()
    if CheckFilePresent(fileName):
        with open(fileName, mode="w+") as file:
            fileName.write(data)
    else: print("File '"+fileName+"' is not present in the current Directory")

def AppendFile(fileName,ext,data):
    fileName = fileName.strip()+"."+ext.strip()
    if CheckFilePresent(fileName):
        with open(fileName, mode="a+") as file:
            fileName.write("\n"+data)
    else: print("File '"+fileName+"' is not present in the current Directory")

def ListFilesFolders():
    files = []
    folders = []
    for i in os.listdir(os.getcwd()):
        if os.path.isdir(i): folders.append(i)
        elif os.path.isfile(i): files.append(i)

    print("List of Folders:")
    for i in range(len(folders)): print(f"{i+1}. {folders[i]}")

    print("\nList of Files:")
    for j in range(len(folders)): print(f"{j+1}. {files[j]}")

#Show Menu for To Make User Choices
def ShowMenu():
    choicesList = ['Change Drive','Change Folder','Create New Folder','Create New File','Read File','Write File','Append File','Delete Folder','Delete File','List of all Files and Folders']
    while True:
        print("\n----MENU----")
        for i in range(len(choicesList)): print(f'{i+1}. {choicesList[i]}')
        print("0. Exit")
        choice = int(input("\nEnter your Choice: "))
        if(choice == 0): exit(1)
        elif choice == 1:
            newFolder = input("Enter the Drive Letter you want to Navigate to: ")
            ChangeDrive(newFolder)
            print(f"Current Working Drive is {os.getcwd()}:")
        elif choice == 2:
            changeableFolder = input("Enter the Folder name you want to Navigate to or Give the whole path(/ instead of \): ")
            ChangeFolder(changeableFolder)
            print("Folder has been Changed")
        elif choice == 3:
            newFolder = input("Enter folder name you want to create in the current directory or give the whole path(/ instead of \) where you want to create the folder: ")
            CreateFolder(newFolder)
        elif choice == 4:
            newFileCreation = input("Enter file name(with extension) you want to create in the current directory or give the whole path(/ instead of \) where you want to create the file(with extension): ")
            CreateFile(newFileCreation)
        elif choice == 5:
            file = input("Enter file name without extension: ")
            exten = input("Enter extension of the file: ")
            ReadFile(file, exten)
        elif choice == 6:
            file = input("Enter file name without extension: ")
            exten = input("Enter extension of the file: ")
            WriteFile(file, exten)
        elif choice == 7:
            file = input("Enter file name without extension: ")
            exten = input("Enter extension of the file: ")
            AppendFile(file, exten)
        elif choice == 8:
            delFolder = input("Enter folder name you want to delete in the current directory or give the whole path(/ instead of \) of the folder you want to delete: ")
            RemoveFolder(newFolder)
        elif choice == 9:
            delFile = input("Enter file name(with extension) you want to delete in the current directory or give the whole path(/ instead of \) of the file(with extension) you want to delete: ")
            RemoveFile(delFile)
        elif choice == 10:
            ListFilesFolders()

# while
ShowMenu()
