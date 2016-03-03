import Image
import os
import time
import sys
import pygame

#color = '8965$89?7>!:-;.'
color = 'MNHQ$OC?7>!:-;.'
bChar = '*'
wChar = ' '
pw = 100
ph = 40
page = 24

def imgToString(img):
    pix = img.load()
    width,height = img.size
    picStr = ''
    for h in xrange(height):
        for w in xrange(width):
            #picStr += color[int(pix[w,h]) * 14 / 255]
            if int(pix[w,h] < 128):
                picStr += bChar
            else:
                picStr += wChar
                
        picStr += '\n'

    return picStr

def loadImg(path):
    img = Image.open(path)
    w,h = img.size
    #de = max(w,h) / 100.0
    #w,h = int(w / de), int(h / de)
    w,h = pw,ph
    img = img.resize((w,h))
    img = img.convert('L')
    return img

def outputToFile(imgStr,path):
    f = open(path,'wb')
    f.write(imgStr)

def imgToCharImg(imgPath,filePath):
    img = loadImg(imgPath)
    picStr = imgToString(img)
    outputToFile(picStr,filePath)

def getImg():
    print 'starting ...'
    files = os.listdir('img')
    for f in files:
        imgPath = 'img/' + f
        filePath = 'charImg/' + f.split('.')[0] + '.txt'
        imgToCharImg(imgPath,filePath)
    print files

def getMp3(name):
    os.system('ffmpeg -i ' + name + ' -vn -ar 44100 -ac 2 -ab 192 -f mp3 ' + 'badapple.mp3')

def playMusic(name):
    pygame.init()
    pygame.mixer.init()
    mus = pygame.mixer.music.load(name)
    pygame.mixer.music.play()

def setColor(color):
    if color:
        print '\033[0;34;47m'
    else:
        print '\033[0m'

def rmFiles(path):
    os.system('rm -rf ' + path)

def mkdir(path):
    os.system('mkdir ' + path)

def mexec(cmd):
    os.system(cmd)

def clear():
    os.system('clear')

def file_cmp(x,y):
    a = int(x.split('.')[0].split('-')[1])
    b = int(y.split('.')[0].split('-')[1])
    if a == b:
        return 0
    if a > b:
        return 1
    else:
        return -1

def play():
    playMusic('badapple.mp3')
    files = os.listdir('charImg')
    files.sort(cmp=file_cmp)
    for f in files:
        path = 'charImg/' + f
        f = open(path,'r')
        charImg = f.read()
        clear()
        setColor(True)
        print charImg
        setColor(False)
        time.sleep(1.0 / (page + 3))

def init():
    rmFiles('charImg/*')
    rmFiles('img/*')
    rmFiles('badapple.mp3')
    mexec('ffmpeg -i badapple.flv -r ' + str(page) + ' -s 200x200 -f image2 img/badapple-%06d.jpeg')
    getMp3('badapple.flv')

def main():
    arg = sys.argv
    ifInit = False
    if len(arg) >= 2:
        c = arg[1]
        if c == 'f':
            ifInit = True

    if ifInit:
        init()
        getImg()

    play()

main()
