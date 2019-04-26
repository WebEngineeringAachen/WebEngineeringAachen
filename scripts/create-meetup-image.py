# coding=utf8
from PIL import Image, ImageFont, ImageDraw


class Speaker:
    def __init__(self, talk, imagePath):
        self.talk = talk
        self.imagePath = imagePath

speakers = []

# speakers.append(Speaker("This is a talk description", "/path/to/the/image.png"))

countSpeakers = len(speakers)

fullHeight = 335;
if (countSpeakers > 1):
    fullHeight = (countSpeakers * 200 ) + 335

img = Image.new('RGBA', (1200, fullHeight), (255,255,255))

speakerImagePath = ""
meetupLogoPath = "./Assets/WEM_Logo-Complete.png"

currentPositionX = 50
currentPositionY = 50

for speaker in speakers:
    speakerImage = Image.open(speaker.imagePath)
    speakerImage = speakerImage.resize((200, 200))
    img.paste(speakerImage, (currentPositionX, currentPositionY))

    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 28, encoding="utf-8")
    draw = ImageDraw.Draw(img)
    draw.text((275,currentPositionY + 90), speaker.talk, 'black', font)

    currentPositionY = currentPositionY + 250

meetupImage = Image.open(meetupLogoPath)
size = 320, 80
meetupImage = meetupImage.resize(size)
img.paste(meetupImage, (850, fullHeight - 90 ), meetupImage)

img.save('web-engineering-aachen-11-06-2019.png')
