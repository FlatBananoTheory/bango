import glob
import os
import time
from random import randint
from PIL import Image
import image


def printAll(strings):
    for name in strings:
        print(name)
    print("----")
    return


def getNewRandomIndex(max, currentIndices):
    if max < len(currentIndices):
        num = 0
    else:
        num = randint(0, max)

        while currentIndices.count(num):
            num = randint(0, max)

    return num


def generateCard(nbSlots, maxIndex):

    currentCard = []

    for i in range(0, nbSlots):
        currentCard.append(getNewRandomIndex(maxIndex, currentCard))

    return currentCard


def generateAllCardIndices(nbSlots, nbImages, nbCards):

    allCards = []

    for i in range(0, nbCards):
        singleCard = generateCard(nbSlots, nbImages - 1)

        while allCards.count(singleCard) >= 1:
            singleCard = generateCard(nbSlots, nbImages - 1)

        allCards.append(singleCard)

    return allCards


def generateCardImage(indices, imagePaths, nbRows, nbCols, skipMiddle, bgPaths, positions):

    sources = []
    maxSize = [0, 0]

    for index in indices:
        src = Image.open(imagePaths[index])
        sources.append(src)

        if (src.size[0] > maxSize[0]):
            maxSize[0] = src.size[0]

        if (src.size[1] > maxSize[1]):
            maxSize[1] = src.size[1]

    if len(bgPaths) > 0:
        image = Image.open(bgPaths[0])
    else:
        image = Image.new("RGBA", (maxSize[0] * nbCols, maxSize[1] * nbRows))

    currentIndex = 0
    try:
        for col in range(0, nbCols):
            for row in range(0, nbRows):
                if ((skipMiddle and col == nbCols / 2 and row == nbRows / 2) == False):
                    if len(positions) == 0:
                        position = (maxSize[0] * col + maxSize[0] / 2 - sources[currentIndex].size[0] / 2,
                                    maxSize[1] * row + maxSize[1] / 2 - sources[currentIndex].size[1] / 2)
                    else:
                        position = positions[currentIndex]

                    image.paste(sources[currentIndex], position)
                    currentIndex = currentIndex + 1
    except:
        print(currentIndex)
    return image


################################
# script folder
pwd = os.path.dirname(__file__)

# list of image paths
srcBackgrounds = pwd + '/images/background'
srcImages = pwd + '/images/squares'
outImages = pwd + '/result/' + time.strftime("%Y%m%d-%H%M%S") + '/'
bgPaths = glob.glob(srcBackgrounds + '/*')
imagePaths = glob.glob(srcImages + '/*')
nbImages = len(imagePaths)

print(nbImages, "images found")

# number of images in each card
nbSlots = 25

# number of cards
nbCards = 1

# number of rows
nbRows = 5

# number of columns
nbCols = 5

# skip middle
skipMiddle = False

# pixel offset 
y_offset = -145
x_offset = 10

# Square positions in background
squarePositions = [
    (81 + x_offset, 892 + y_offset), (273 + x_offset, 892 + y_offset), (465  + x_offset, 892 +
                                              y_offset), (657 + x_offset, 892 + y_offset), (849 + x_offset, 892 + y_offset),
    (81 + x_offset, 1084 + y_offset), (273 + x_offset, 1084 + y_offset), (465 + x_offset, 1084 +
                                                y_offset), (657 + x_offset, 1084 + y_offset), (849 + x_offset, 1084 + y_offset),
    (81 + x_offset, 1276 + y_offset), (273 + x_offset, 1276 + y_offset),  (465 + x_offset, 1276 +
                                                 y_offset), (657 + x_offset, 1276 + y_offset), (849 + x_offset, 1276 + y_offset),
    (81 + x_offset, 1468 + y_offset), (273 + x_offset, 1468 + y_offset), (465 + x_offset, 1468 +
                                                y_offset), (657 + x_offset, 1468 + y_offset), (849 + x_offset, 1468 + y_offset),
    (81 + x_offset, 1660 + y_offset), (273 + x_offset, 1660 + y_offset), (465 + x_offset, 1660 +
                                                y_offset), (657 + x_offset, 1660 + y_offset), (849 + x_offset, 1660 + y_offset)
]

print("Generating {} cards with {} indices each".format(nbCards, nbSlots))
allCards = generateAllCardIndices(nbSlots, nbImages, nbCards)


if (os.path.exists(outImages) == False):
    os.makedirs(outImages)

cardNum = 0


for indices in allCards:
    result = generateCardImage(
        indices, imagePaths, nbRows, nbCols, skipMiddle, bgPaths, squarePositions)
    result.save(
        outImages + 'FuckoBango69-R1C{}.png'.format(cardNum), "PNG")
    print("indices: " + str(indices))
    cardNum = cardNum + 1
