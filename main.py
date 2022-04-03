#создай тут фоторедактор Easy Editor!
import os #Работа с ос
from PyQt5.QtWidgets import (QApplication,QLabel, QFileDialog, QWidget, QPushButton,
QListWidget,QHBoxLayout,QVBoxLayout) #Библиоабтека ПуКути5

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageFilter import ( BLUR,CONTOUR,DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
GaussianBlur, UnsharpMask )
# Кибер ОкНо-5001

app = QApplication([])
win = QWidget()
win.resize(800,600)
win.setWindowTitle('Ez Editor')
lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка') #Нет блин мамка
lw_files = QListWidget()
#Кнопы кнопочки как же я их обажаю

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')
btn_blur = QPushButton('Блюр')
btn_ee = QPushButton('Зашакалить')
btn_emboss = QPushButton('Все серое')
#ЛеййАУТ

row = QHBoxLayout()              #основная строчка
col1 = QVBoxLayout()             #Два столба
col2 = QVBoxLayout()                         
col1.addWidget(btn_dir)          #Первый столб - кнопка выбора директории
col1.addWidget(lw_files)         #Список файлов
col2.addWidget(lb_image, 95)     #Картмнка
row_tools = QHBoxLayout()        #Строка кнопкок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_blur)
row_tools.addWidget(btn_ee)
row_tools.addWidget(btn_emboss)
col2.addLayout(row_tools)
#И опяяяяяяяять

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
#Кибер ОкНо-5001 показывается

win.show()

workdir = ''
#Фюнкция
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
#И ещё
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
#И тут
def showFilenamesList():
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    
    def loadImage(self, dir, filename):
        '''Запоминаем путт и имя фОйла'''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    
    def do_bw(self):   #Мне лень постоянно делать комментарии, так что это просто функции  для работы кнопАк
        self.image = self.image.convert("L") #Верно, он Кира
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_sharp(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_emboss(self):
        self.image = self.image.filter(EMBOSS)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)  

    def do_ee(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)  
    
    def saveImage(self):
        #Сахраняим копейу файела
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

workimage = ImageProcessor()
lw_files.currentRowChanged.connect(showChosenImage)

btn_dir.clicked.connect(showFilenamesList)
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_flip.clicked.connect(workimage.do_flip)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharp)
btn_blur.clicked.connect(workimage.do_blur)
btn_emboss.clicked.connect(workimage.do_emboss)
btn_ee.clicked.connect(workimage.do_ee)
app.exec()

#Йа фсе