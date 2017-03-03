import PyQt5.QtCore as Qc
import PyQt5.QtGui as Qg
import PyQt5.QtWidgets as Qw
import sys
import sms


class Main(Qw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(u'Αποστολή SMS από otenet')
        mainLayout = Qw.QVBoxLayout(self)
        glay = Qw.QGridLayout()
        buttonLayout = Qw.QHBoxLayout()
        mainLayout.addLayout(glay)
        mainLayout.addLayout(buttonLayout)
        self.email = Qw.QLineEdit()
        self.email.setToolTip('Το email του λογαριασμού σας της otenet')
        self.passw = Qw.QLineEdit()
        self.passw.setToolTip('Ο κωδικός πρόσβασης')
        self.mobil = Qw.QLineEdit()
        self.mobil.setToolTip('Το τηλέφωνο που θα σταλεί το μύνημα')
        self.mssag = Qw.QTextEdit()
        self.mssag.setToolTip('Το μύνημα δεν μπορεί να είναι μεγαλύτερο από 160 χαρακτήρες')
        self.passw.setEchoMode(Qw.QLineEdit.Password)
        glay.addWidget(Qw.QLabel(u'email'), 0, 0)
        glay.addWidget(self.email, 0, 1)
        glay.addWidget(Qw.QLabel(u'password'), 1, 0)
        glay.addWidget(self.passw, 1, 1)
        glay.addWidget(Qw.QLabel(u'mobile'), 2, 0)
        glay.addWidget(self.mobil, 2, 1)
        glay.addWidget(Qw.QLabel(u'Message'), 3, 0)
        glay.addWidget(self.mssag, 3, 1)
        self.bSave = Qw.QPushButton(u'Αποστολή sms')
        self.bSave.setFocusPolicy(Qc.Qt.NoFocus)
        self.bSave.clicked.connect(self.sent_sms)
        buttonLayout.addWidget(self.bSave)

    def sent_sms(self):
        email = self.email.text()
        passw = self.passw.text()
        mobil = self.mobil.text()
        messg = self.mssag.toPlainText()
        errors = ''
        if '@' not in email:
            errors += 'To email δεν είναι σωστό\n'
        if len(passw) == 0:
            errors += 'Δεν δώσατε κωδικό πρόσβασης\n'
        if len(mobil) < 10:
            errors += 'Ο αριθμός του κινητού δεν είναι σωστός\n'
        if len(messg) == 0:
            errors += 'Το μύνημα δεν μπορεί να είναι κενό\n'
        if len(messg) > 160:
            errors += 'Το μύνημα δεν μπορεί μεγαλύτερο από 160 χαρακτήρες\n'
        if errors:
            Qw.QMessageBox.critical(self, u"Υπάρχουν λάθη", '%s' % errors)
        else:
            sms.send_sms(email, passw, mobil, messg)
            self.accept()


if __name__ == '__main__':
    APP = Qw.QApplication(sys.argv)
    UI = Main()
    UI.show()
    sys.exit(APP.exec_())
