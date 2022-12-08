import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        #back Button
        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        #forward Button
        For_btn = QAction('Forward',self)
        For_btn.triggered.connect(self.browser.forward)
        navbar.addAction(For_btn)
        #reload Button
        Rel_btn = QAction('Reload',self)
        Rel_btn.triggered.connect(self.browser.reload)
        navbar.addAction(Rel_btn)
        #Home button
        Hom_btn = QAction('Home',self)
        Hom_btn.triggered.connect(self.navigate_home)
        navbar.addAction(Hom_btn)
        #url Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.UrlEnter)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.UpdateUrl)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))
    def UrlEnter(self):
        url = self.url_bar.text()
        if "https://" not in url:
            url = "https://" + url
        self.browser.setUrl(QUrl(url))
    def UpdateUrl(self,q="hello"):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Gary Browser')
window = MainWindow()
app.exec_()