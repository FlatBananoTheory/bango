import glob
import os
import time
from random import randint
from PIL import Image, ImageDraw, ImageFont


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


def generateCardImage(indices, imagePaths, nbRows, nbCols, skipMiddle, bgPaths, positions, prefix, cardNum):
    sources = []
    maxSize = [0, 0]

    for index in indices:
        src = Image.open(imagePaths[index]).convert('RGBA')
        sources.append(src)

        if (src.size[0] > maxSize[0]):
            maxSize[0] = src.size[0]

        if (src.size[1] > maxSize[1]):
            maxSize[1] = src.size[1]

    if len(bgPaths) > 0:
        image = Image.open(bgPaths[0]).convert('RGBA')
    else:
        image = Image.new("RGBA", (maxSize[0] * nbCols, maxSize[1] * nbRows), (0, 0, 0, 0))

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

                    image.alpha_composite(sources[currentIndex], dest=position)
                    currentIndex = currentIndex + 1

        # Add text overlay to uniquely identify the card
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('FilsonProRegular.otf', 24)
        draw.text((25, 500), '{} {}'.format(prefix, cardNum), (255, 221, 17), font=font)

    except:
        print(currentIndex)

    return image


# Script directory
pwd = os.path.dirname(__file__)

# List of image paths
srcBackgrounds = os.path.join(pwd, 'images', 'background')
srcImages = os.path.join(pwd, 'images', 'squares')
outImages = os.path.join(pwd, 'result', time.strftime("%Y%m%d-%H%M%S"))
bgPaths = glob.glob(os.path.join(srcBackgrounds, '*'))
imagePaths = glob.glob(os.path.join(srcImages, '*'))
nbImages = len(imagePaths)

print(nbImages, "images found")

# Number of images in each card
nbSlots = 25

# Number of cards
nbCards = 1000

# Number of rows
nbRows = 5

# Number of columns
nbCols = 5

# Skip middle
skipMiddle = False

# Y Pixel y_offset
y_offset = -90
x_offset = 10

# Square positions in background
squarePositions = [
    (81 + x_offset, 892 + y_offset), (273 + x_offset, 892 + y_offset), (465 + x_offset, 892 +
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

# Text overlay prefix
prefix = "CardID:"

print("Generating {} cards with {} indices each".format(nbCards, nbSlots))
allCards = generateAllCardIndices(nbSlots, nbImages, nbCards)

if not os.path.exists(outImages):
    os.makedirs(outImages)

cardNum = 0

for indices in allCards:
    result = generateCardImage(
        indices, imagePaths, nbRows, nbCols, skipMiddle, bgPaths, squarePositions, prefix, cardNum)

    if result:
        result.save(os.path.join(outImages, 'Carnivalentines_Bango_R4C{}.png'.format(cardNum)), "PNG")
        print("creating card #" + str(cardNum) + ": " + str(indices))
        cardNum += 1
    else:
        print("Error generating card #" + str(cardNum))
