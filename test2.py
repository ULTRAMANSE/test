import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import sys

b=["F:\\M\\该死的温柔 (Live) - 王嘉尔.m4a","F:\\M\\该死的温柔 - 马天宇.m4a","F:\\PPlayer\\PPlayer-master\\music\\Angel.mp3"]

def a(i):
    app = C.QCoreApplication(sys.argv)
    url = C.QUrl.fromLocalFile(i)
    content= M.QMediaContent(url)
    player = M.QMediaPlayer()
    player.setMedia(content)
    player.play()
    # time.sleep(5)
    player.stateChanged.connect( app.quit )
    app.exec()
    

for i in b:
    a(i)

    
    




    
    

