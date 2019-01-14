import PyQt5.QtMultimedia as M
from PyQt5.QtMultimedia import QMediaPlaylist
import PyQt5.QtCore as C
import sys
from PyQt5.QtCore import *
import time
def a():
    print("1")
app = C.QCoreApplication(sys.argv)
playlist = QMediaPlaylist()
player = M.QMediaPlayer()
a=QUrl.fromLocalFile("F:\\PPlayer\\PPlayer-master\\music\\Angel.mp3")

playlist.addMedia(M.QMediaContent(a))
playlist.addMedia(M.QMediaContent(QUrl.fromLocalFile(u"F:\\M\\该死的温柔 - 马天宇.m4a")))
playlist.setCurrentIndex(1)

player.setPlaylist(playlist)

player.setVolume(50)
player.play()
time.sleep(5)
player.stateChanged.connect( app.quit )
app.exec()