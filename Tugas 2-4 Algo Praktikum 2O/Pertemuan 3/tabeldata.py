import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('tabelwid.ui', self)
        self.setWindowTitle("PYTHON GUI TABLEWIDGET")
        self.pushButton.clicked.connect(self.hapus)
        self.pushButton_2.clicked.connect(self.sqlLoad)
        self.pushButton_3.clicked.connect(self.sqlInsertData)

    def hapus(self):
        self.tableWidget.clear()

    def sqlInsertData(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )

            nama = self.lineEdit.text().strip()
            jurusan = self.lineEdit_2.text().strip()

            if nama == "" or jurusan == "":
                self.label.setText("Nama dan Jurusan tidak boleh kosong")
                return
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO mhs (nama,jurusan) VALUES (%s,%s)", (nama, jurusan))
            mydb.commit()
            self.label.setText("Data berhasil disimpan")

            self.lineEdit.clear()
            self.lineEdit_2.clear()

            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.sqlLoad()
        except mc.Error as err:
            self.label.setText("Data Gagal disimpan")

    def sqlLoad(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM mhs ORDER BY nama ASC")
            result = mycursor.fetchall()
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
            self.label.setText("Data berhasil ditampilkan")
        except mc.Error as err:
            self.label.setText("Data Gagal ditampilkan")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())