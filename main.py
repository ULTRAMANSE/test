from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QSlider,
                             QFileDialog)
from PyQt5.QtCore import QUrl, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
import sys
import re
from time import localtime, strftime
# import mutagen

class frame(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(300,300)
        self.setFixedSize(300,300)
        self.playbtn = QPushButton(self)
        self.playbtn.setText("播放")
        self.playbtn.clicked.connect(self.play)
        self.stopbtn = QPushButton(self)
        self.stopbtn.setText("暂停")
        self.stopbtn.clicked.connect(self.stop)
        self.addbtn = QPushButton(self)
        self.addbtn.setText("添加")
        self.addbtn.clicked.connect(self.add)
        self.nextbtn = QPushButton(self)
        self.nextbtn.setText("下一首")
        self.nextbtn.clicked.connect(self.nextsong)
        self.previousbtn = QPushButton(self)
        self.previousbtn.setText("上一首")
        self.previousbtn.clicked.connect(self.previous)
        self.modebtn = QPushButton(self)
        self.modebtn.setText("列表循环")
        self.modebtn.clicked.connect(self.Playback_mode)
        self.deletebtn = QPushButton(self)
        self.deletebtn.setText("删除")
        self.deletebtn.clicked.connect(self.delete)
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.play)
        self.slider = QSlider(Qt.Horizontal, self)   #进度条
        self.slider.setMinimumHeight(5)
        self.slider.setMinimumWidth(250)
        
        # self.slider.setRange(0, 300)
        # self.slider.setOrientation(Qt.Horizontal) #设置水平方向
        self.timeLabel = QLabel(self)
        self.timeLabel.setText("00:00 / 00:00")
        
        self.volumeslilder = QSlider(Qt.Horizontal, self)    #音量
        self.volumeslilder.setMaximumHeight(4)
        self.volumeslilder.setMinimumWidth(50)
        self.volumeslilder.setRange(0, 100)
        self.volumeslilder.setValue(25)
        # self.volumeslilder.setOrientation(Qt.Horizontal)
        self.volumeslilder.valueChanged.connect(self.volume)    #滑块值变化信号
        # self.connect(self.volumeslilder, QtCore.SIGNAL('valueChanged(int)'),self.volume)
        
        self.sound = QLabel(self)
        # self.sound.setFixedWidth(20)
        # self.sound.setFixedHeight(20)
        self.sound.setFixedSize(20, 20)
        self.sound.setPixmap(QPixmap("F:\\untitled\\volume.png"))   #在label上显示图片
        self.sound.setScaledContents(True)  #让图片自适应label大小
        
        self.soundlayout = QHBoxLayout()
        self.soundlayout.addWidget(self.sound)
        self.soundlayout.addWidget(self.volumeslilder )
        self.soundlayout.addStretch()
        slqW = QWidget()
        slqW.setLayout(self.soundlayout)
        
        self.timelayout = QVBoxLayout()
        self.timelayout.addWidget(self.slider)
        self.timelayout.addWidget(self.timeLabel)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.stopbtn)
        self.layout.addWidget(self.playbtn)
        self.layout.addWidget(self.deletebtn)
        self.layout.addWidget(self.addbtn)
        self.la = QHBoxLayout()
        self.la.addWidget(self.previousbtn)
        self.la.addWidget(self.modebtn)
        self.la.addWidget(self.nextbtn)
        qW = QWidget()
        qW.setLayout(self.layout)
        qW2 = QWidget()
        qW2.setLayout(self.la)
        qW3 = QWidget()
        qW3.setLayout(self.timelayout)
        
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.list)
        self.layout2.addWidget(qW3)
        self.layout2.addWidget(slqW)
        self.layout2.addWidget(qW)
        self.layout2.addWidget(qW2)
        self.setLayout(self.layout2)
        
        
        self.player = QMediaPlayer( )  # 创建播放媒体
        self.player.setVolume(10)
        self.playlist = QMediaPlaylist()    # 创建播放列表
        self.player.setPlaylist(self.playlist)
        
        
        self.timer = QTimer(self)
        self.timer.setInterval(400)
        self.timer.timeout.connect(self.update)
        
        
        self.slider.sliderMoved.connect(self.timedate)
        self.slider.sliderReleased.connect(self.SliderMoved)
        
    def timedate(self):
        
        pass
    
    def add(self):
        FileName,FileType= QFileDialog.getOpenFileName(self,"添加音乐","F:\\M","All Files (*);;Mp3 Files (*.mp3);; Wma Files (*.wma);;M4a Files (*.m4a)")
        if FileName:
            search = re.compile(r".*/(.*)")
            SongName = search.search(FileName)
            self.list.addItem(SongName.group(1))
            self.player.playlist().addMedia(QMediaContent(QUrl.fromLocalFile(FileName)))#添加到播放列表
            # self.player.setPlaylist(self.playlist)
            
        else:
            pass
        # self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
        
        
    def play(self):
        if self.list.currentRow() == -1:
            pass
        else:
            # print(self.list.currentRow())
            self.player.playlist().setPlaybackMode(QMediaPlaylist.Loop)
            self.player.playlist().setCurrentIndex(self.list.currentRow())
            # self.player.positionChanged()
            self.player.play()
            self.timer.start()
            
    def stop(self):
        if self.player.playlist().currentIndex() == -1:
            pass
        else:
            print(self.player.playlist().currentIndex())
            if self.stopbtn.text()=="暂停":
                self.player.pause()
                self.timer.stop()
                self.stopbtn.setText("继续")
            else:
                self.player.play()
                self.timer.start()
                self.stopbtn.setText("暂停")

    def nextsong(self): #下一首
        if self.list.currentRow() != -1:
            self.player.playlist().next()
        
    def previous(self): #上一首
        print(self.list.currentRow())
        if self.list.currentRow() != -1:
            self.player.playlist().previous()
        
    def Playback_mode(self):
        if self.modebtn.text() == "列表循环":
            self.player.playlist().setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)  # 单曲循环
            self.modebtn.setText("单曲循环")
        else:
            self.player.playlist().setPlaybackMode(QMediaPlaylist.Loop)#列表循环
            self.modebtn.setText("列表循环")
    
    def delete(self):
        self.player.playlist().removeMedia(self.player.playlist().currentIndex())
        self.list.takeItem(self.list.currentRow())
        
        
    def volume(self):   #改变音量
        
        self.player.setVolume(self.volumeslilder.value()*2)
        
    def SliderMoved(self):  #滑动滑块
       
        self.player.setPosition(self.slider.value())
        self.slider.setSliderPosition(self.player.position())
        self.timer.start()
        
    def update(self):
        self.slider.setMaximum(self.player.duration())
        self.timeLabel.setText(str(strftime("%M:%S",localtime(self.player.position()/1000.0))+" / "+str(strftime("%M:%S",localtime(self.player.duration()/1000.0))))) #将毫秒转换为分秒（时间戳为秒，需要除以1000.0）
        self.slider.setSliderPosition(self.player.position())
        
        
        # print(self.player.position())
        # print(self.slider.value())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = frame()
    form.show()
    app.exec_()
