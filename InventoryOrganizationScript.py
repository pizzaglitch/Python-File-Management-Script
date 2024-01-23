import os
import shutil

currentDirPath = os.path.dirname(os.path.realpath(__file__))
testSmallJpgDirPath = os.path.join(currentDirPath, 'JPEG-2000-under2MB')
testLargeJpgDirPath = os.path.join(currentDirPath, 'JPEG-4800-under7MB')
testTiffDirPath = os.path.join(currentDirPath, 'TIFF')
testJPGFullDirPath = os.path.join(currentDirPath, 'JPEG-FULL')

for file in os.scandir(currentDirPath):
    fileNameString = str(file)[:-1] #convert file name to string
    splitStr = fileNameString.split()
    imgFolder = splitStr[1] #'JPEG-2000-under2MB'
    if imgFolder == "'JPEG-4800-under7MB'":
        for subfile in os.scandir(testLargeJpgDirPath):
            artistInventoryNumber = str(subfile)[11:22] #snip off inventory num of filename 
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)
                
            highResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'High Res')
            if not os.path.exists(highResJPGFolder):
                os.makedirs(highResJPGFolder)
            
            shutil.move(subfile, highResJPGFolder)

    if imgFolder == "'JPEG-2000-under2MB'":
        for subfile in os.scandir(testSmallJpgDirPath):
            artistInventoryNumber = str(subfile)[11:22]  
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)

            lowResJPGFolder = os.path.join(currentDirPath, artistInventoryNumber, 'Low Res')
            if not os.path.exists(lowResJPGFolder): 
                os.makedirs(lowResJPGFolder)

            shutil.move(subfile, lowResJPGFolder)

    if imgFolder == "'TIFF'":
        for subfile in os.scandir(testTiffDirPath):
            artistInventoryNumber = str(subfile)[11:22] 
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)
                
            tiffFolder = os.path.join(currentDirPath, artistInventoryNumber, 'TIFF')
            if not os.path.exists(tiffFolder):
                os.makedirs(tiffFolder)

            shutil.move(subfile, tiffFolder)
    if imgFolder == "'JPEG-FULL'":
        for subfile in os.scandir(testJPGFullDirPath):
            artistInventoryNumber = str(subfile)[11:22] 
            inventoryNumberFolder = os.path.join(currentDirPath, artistInventoryNumber)
            if not os.path.exists(inventoryNumberFolder):
                os.makedirs(inventoryNumberFolder)
                
            JPGFullFolder = os.path.join(currentDirPath, artistInventoryNumber, 'JPG Full')
            if not os.path.exists(JPGFullFolder):
                os.makedirs(JPGFullFolder)

            shutil.move(subfile, JPGFullFolder)

#Delete old, empty folders when done
testSmallJpgPath = os.path.join(currentDirPath, 'JPEG-2000-under2MB')
testLargeJpgPath = os.path.join(currentDirPath, 'JPEG-4800-under7MB')
testTiffPath = os.path.join(currentDirPath, 'TIFF')
testJPGFullPath = os.path.join(currentDirPath, 'JPEG-FULL')
os.rmdir(testSmallJpgPath)
os.rmdir(testLargeJpgPath)
os.rmdir(testTiffPath)
os.rmdir(testJPGFullPath)