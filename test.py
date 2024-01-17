import os
import shutil
########################################################
# To-Do

# Problem
# Provided a folder of photos, smaller (<= 2mb), larger (> 2mb && <= 7mb), TIFF (can ignore TIFF)
# In each folder, various photos of artists' works. Files are titled by inventory number.

# Goal
# Create a new inventory folder, create high res and low res folders within, sort (Artist name)
# relevant files from the source folder into the new folders. 
# One new folder per inventory number (One folder = One artwork)
# All photos of a specific artwork are organized into a folder with high & low res subfolders
# The user should be able to easily drag the new folder into the server under the relevant Artist

#Example inventory number format
#LRAG2311001 (7 digit name/yy/mm/dd)
#Artist first initial (L), First three letters of last name (RAG)
#Year (23), Month (1), Day (1)
#Artwork num (001)p
#f = open("test.txt", "r")
########################################################
#1st push: script works when all files are in same directory as test.py
#2nd push: works when all files are organized as they arrive from the server
    #To do: Reduce repetitive code, check for edge cases 
        #(instead of matching by string length, match by exact phrasing (case insensitive))
        #could use split, then index[1] to target actual file name instead of checking substr


path = os.path.join('/Users/garebear/Desktop/Python Test')
jpgPath = os.path.join('/Users/garebear/Desktop/Python Test', 'JPG')
tiffPath = os.path.join('/Users/garebear/Desktop/Python Test', 'TIFF')

#Flexible push paths, work with current directory (Push #3/4)
currentDirPath = os.path.dirname(os.path.realpath(__file__))
testSmallJpgDirPath = os.path.join(currentDirPath, 'JPEG-2000-under2MB')
testLargeJpgDirPath = os.path.join(currentDirPath, 'JPEG-4800-under7MB')
testTiffDirPath = os.path.join(currentDirPath, 'TIFF')

#Trial 3 (Remove repetition, fix edge cases)
#splits folder names to get image folder (smart fix)
#Uses string length to get inventory name (original, brute fix. could cause issues if files are misnamed)
#does not move more than one high res image
for file in os.scandir(currentDirPath):
    fileNameString = str(file)[:-1] #convert file name to string
    splitStr = fileNameString.split()
    imgFolder = splitStr[1] #'JPEG-2000-under2MB'
    if imgFolder == "'JPEG-4800-under7MB'":
        for file in os.scandir(testLargeJpgDirPath):
            artistInventoryNumber = str(file)[11:22] #snip off inventory num of filename 
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
            
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)
            
            lowResJPGFolder = os.path.join(currentDirPath, inventoryNumberFolder, 'Low Res')
            if not os.path.exists(lowResJPGFolder): 
                os.makedirs(lowResJPGFolder)
            
            highResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'High Res')
            if not os.path.exists(highResJPGFolder):
                os.makedirs(highResJPGFolder)
                shutil.move(file, highResJPGFolder)

            tiffFolder = os.path.join(currentDirPath, inventoryNumberFolder, 'TIFF')
            if not os.path.exists(tiffFolder):
                os.makedirs(tiffFolder)
            
        shutil.move(file, highResJPGFolder)

    if imgFolder == "'JPEG-2000-under2MB'":
        for file in os.scandir(testSmallJpgDirPath):
            shutil.move(file, lowResJPGFolder)
    if imgFolder == "'TIFF'":
        for file in os.scandir(testTiffDirPath):
            shutil.move(file, tiffFolder)

#Delete old, empty folders when done
"""
testSmallJpgPath = os.path.join(currentDirPath, 'JPEG-2000-under2MB')
testLargeJpgPath = os.path.join(currentDirPath, 'JPEG-4800-under7MB')
testTiffPath = os.path.join(currentDirPath, 'TIFF')
os.rmdir(testSmallJpgPath)
os.rmdir(testLargeJpgPath)
os.rmdir(testTiffPath)
"""

######
######
#Trial code for solution based on proper downloaded file format. Works. Need to reduce repetitive code.
#Push #2
""""
for file in os.scandir(currentDirPath):
    #fileNameString = str(file) #convert file name to string
    #fileSizeFolder = fileNameString[11:29] #JPEG-2000-under2MB
    #tiffSizeFolder = fileNameString[11:15]

    fileNameString = str(file)[:-1] #convert file name to string
    splitStr = fileNameString.split()
    imgFolder = splitStr[1] #JPEG-2000-under2MB

    #for subFolder in os.scandir(path):
    if imgFolder == "'JPEG-2000-under2MB'":
        for subFile in os.scandir(testSmallJpgDirPath):
            artistInventoryNumber = str(subFile)[11:22] #snip off inventory num of filename 
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
                      
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)
            lowResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'Low Res')
            if not os.path.exists(lowResJPGFolder): 
                os.makedirs(lowResJPGFolder)
            highResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'High Res')
            if not os.path.exists(highResJPGFolder):
                os.makedirs(highResJPGFolder)
            tiffFolder = os.path.join(currentDirPath, artistInventoryNumber, 'TIFF')
            if not os.path.exists(tiffFolder):
                os.makedirs(tiffFolder)
            
            shutil.move(subFile, lowResJPGFolder)

    if imgFolder == "'JPEG-4800-under7MB'":
        for subFile in os.scandir(testLargeJpgDirPath):
            artistInventoryNumber = str(subFile)[11:22] #snip off inventory num of filename 
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
                     
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)
            lowResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'Low Res')
            if not os.path.exists(lowResJPGFolder): 
                os.makedirs(lowResJPGFolder)
            highResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'High Res')
            if not os.path.exists(highResJPGFolder):
                os.makedirs(highResJPGFolder)
            tiffFolder = os.path.join(currentDirPath, artistInventoryNumber, 'TIFF')
            if not os.path.exists(tiffFolder):
                os.makedirs(tiffFolder)

            shutil.move(subFile, highResJPGFolder)

    if imgFolder == "'TIFF'":
        for subFile in os.scandir(testTiffDirPath):
            artistInventoryNumber = str(subFile)[11:22] #snip off inventory num of filename 
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
            
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)
            lowResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'Low Res')
            if not os.path.exists(lowResJPGFolder): 
                os.makedirs(lowResJPGFolder)
            highResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'High Res')
            if not os.path.exists(highResJPGFolder):
                os.makedirs(highResJPGFolder)
            tiffFolder = os.path.join(currentDirPath, artistInventoryNumber, 'TIFF')
            if not os.path.exists(tiffFolder):
                os.makedirs(tiffFolder)       

            shutil.move(subFile, tiffFolder)
"""

#Push #1: Works only when all files are in same folder.
""" for file in os.scandir(path):
    ext = os.path.splitext(file)[-1].lower() #get file ext
    fileSize = os.path.getsize(file) #get file size
    fileNameString = str(file) #convert file name to string
    artistInventoryNumber = fileNameString[11:22] #snip off inventory num of filename
    inventoryNumberFolder = os.path.join(path, artistInventoryNumber)
    
    if ext == '.jpg' or ext == '.jpeg' or ext == '.tif':
        #Create inventory Num Folder and subfolders
        if not os.path.exists(inventoryNumberFolder):
            os.makedirs(inventoryNumberFolder)

        lowResJPGFolder = os.path.join(path, artistInventoryNumber, 'Low Res')
        if not os.path.exists(lowResJPGFolder): 
            os.makedirs(lowResJPGFolder)

        highResJPGFolder = os.path.join(path, artistInventoryNumber, 'High Res')
        if not os.path.exists(highResJPGFolder):
            os.makedirs(highResJPGFolder)
       
        tiffFolder = os.path.join(path, artistInventoryNumber, 'TIFF')
        if not os.path.exists(tiffFolder):
            os.makedirs(tiffFolder)

        #move files into folders according to type and size
        if ext == '.tif':
            shutil.move(file, tiffFolder)
        
        if fileSize <= maxSmallFileSize: #move <2mb files
            shutil.move(file, lowResJPGFolder)
        if fileSize > maxSmallFileSize and fileSize <= maxLargeFileSize: #move <7mb files 
            shutil.move(file, highResJPGFolder)
 """

#Optional code: 
#Optional inventory number code
"""
imgFileString = str(subFile)[:-1]
imgFileString = imgFileString.split()
imgInvenNum = imgFileString[1]
imgInvenNum = imgInvenNum.split('-')
imgInvenNum = imgInvenNum[0][1:]

#Push #2 variables. Includes static directory and file sizes

testSmallJpgPath = os.path.join(path, 'JPEG-2000-under2MB')
testLargeJpgPath = os.path.join(path, 'JPEG-4800-under7MB')
testTiffPath = os.path.join(path, 'TIFF')
#File Size Variables
maxSmallFileSize = 2000000
maxLargeFileSize = 7100000
"""

