from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFontDatabase, QFont
import requests
import ui

url = "https://api.tgju.online/v1/data/sana/json"


def currency():
    try:
        get = requests.get(url)
        currency_json = get.json()
        currency = ""
        for key, item_master in currency_json.items():
            for item in item_master['data']:
                currency += str(item['title']) + ":" + str(item['p']) + "\n"
        return(currency.replace('سامانه سنا', '(سامانه سنا)'))
    except:
        return False


class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet('font-size: 15px;')

    @pyqtSlot()
    def button_pressed(self):
        re = currency()
        self.output.setText("")
        if not re:
            self.output.setText("لطفا اینترنت خود را چک کنید")
        else:
            self.output.setText(re)


def main():
    mainApp = QApplication(['ارز ایران'])

    fontdata = QFontDatabase()
    vazirfont = fontdata.addApplicationFont('Vazir.ttf')
    mainApp.setFont(QFont('Vazir'))

    mainWindow = App()
    mainWindow.show()
    mainApp.exec_()


if __name__ == "__main__":
    main()
