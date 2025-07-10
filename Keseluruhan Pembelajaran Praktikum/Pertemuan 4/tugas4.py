import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('tugas4.ui', self)
        self.setWindowTitle("TUGAS Praktikum Pertemuan 4 ALGO - Muhammad Zulfy")
        self.sqlLoadData()
        self.tableWidget.cellClicked.connect(self.loadById)
        self.pushButton_simpan.clicked.connect(self.sqlSimpanData)
        self.pushButton_ubah.clicked.connect(self.sqlEditData)
        self.pushButton_hapus.clicked.connect(self.sqlHapusData)
        self.pushButton_batal.clicked.connect(self.clearField)
        
    def loadById(self, row):
        try:
            rownpm              = self.tableWidget.item(row,0)
            rownama_lengkap     = self.tableWidget.item(row,1)
            rownama_panggilan   = self.tableWidget.item(row,2)
            rowhp               = self.tableWidget.item(row,3)
            rowemail            = self.tableWidget.item(row,4)
            rowkelas            = self.tableWidget.item(row,5)
            rowmatkul           = self.tableWidget.item(row,6)
            rowlok_kampus       = self.tableWidget.item(row,7)
            if rownpm :
                npm            = rownpm.text()
                nama_lengkap   = rownama_lengkap.text()
                nama_panggilan = rownama_panggilan.text()
                telepon        = rowhp.text()
                email          = rowemail.text()
                kelas          = rowkelas.text()
                matkul         = rowmatkul.text()
                lok_kampus     = rowlok_kampus.text()
                self.lineEdit.setText(npm)
                self.lineEdit_2.setText(nama_lengkap)
                self.lineEdit_3.setText(nama_panggilan)
                self.lineEdit_4.setText(telepon)
                self.lineEdit_5.setText(email)
                self.lineEdit_6.setText(kelas)
                self.lineEdit_7.setText(matkul)
                self.lineEdit_8.setText(lok_kampus)

                  
        except mc.Error as err:
            print(err.msg)

    def sqlSimpanData(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )

            npm             = self.lineEdit.text().strip()
            nama_lengkap    = self.lineEdit_2.text().strip()
            nama_panggilan  = self.lineEdit_3.text().strip()
            telepon         = self.lineEdit_4.text().strip()
            email           = self.lineEdit_5.text().strip()
            kelas           = self.lineEdit_6.text().strip()
            matkul          = self.lineEdit_7.text().strip()
            lok_kampus      = self.lineEdit_8.text().strip()
            
            mycursor = mydb.cursor()
            
            sql = "INSERT INTO mhs4 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (npm,nama_lengkap,nama_panggilan,telepon,email,kelas,matkul,lok_kampus)
            mycursor.execute(sql,val)
            mydb.commit()

            self.clearField()
            self.sqlLoadData()
        except mc.Error as err:
            return

    def sqlEditData(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )

            cursor = mydb.cursor()

            npm             = self.lineEdit.text().strip()
            nama_lengkap    = self.lineEdit_2.text().strip()
            nama_panggilan  = self.lineEdit_3.text().strip()
            telepon         = self.lineEdit_4.text().strip()
            email           = self.lineEdit_5.text().strip()
            kelas           = self.lineEdit_6.text().strip()
            matkul          = self.lineEdit_7.text().strip()
            lok_kampus      = self.lineEdit_8.text().strip()
            
            sql = "UPDATE mhs4 set nama_lengkap = %s, nama_panggilan = %s, telepon = %s, email = %s, kelas = %s, matkul = %s, lok_kampus = %s WHERE npm = %s"
            val = (nama_lengkap, nama_panggilan, telepon, email, kelas, matkul, lok_kampus, npm)
            cursor.execute(sql, val)
            mydb.commit()
            
            self.clearField()
            self.sqlLoadData()
        except mc.Error as err:
            return

    def sqlHapusData(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )

            cursor = mydb.cursor()
            npm = self.lineEdit.text()

            sql = "DELETE FROM mhs4 WHERE npm = %s"
            val = (npm,)
            cursor.execute(sql, val)
            mydb.commit()
        
            self.clearField()
            self.sqlLoadData()
        except mc.Error as err:
            print(err.msg)

    def clearField(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")

    def clearTable(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
    
    def sqlLoadData(self):
        try:
            self.clearTable()

            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM mhs4 ORDER BY npm ASC")
            result = mycursor.fetchall()
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        except mc.Error as err:
            print(err.msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())