import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as mc

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('tabelwid.ui', self)
        self.setWindowTitle("PYTHON GUI TABLEWIDGET")
        self.tableWidget.cellClicked.connect(self.loadById)
        self.pushButton_simpan.clicked.connect(self.sqlSimpanData)
        self.pushButton_edit.clicked.connect(self.sqlEditData)
        self.pushButton_hapus.clicked.connect(self.sqlHapusData)
        self.pushButton_batal.clicked.connect(self.batal)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_loadData.clicked.connect(self.sqlLoadData)
        
    def loadById(self, row):
        try:
            rownama = self.tableWidget.item(row,0)
            rowjur = self.tableWidget.item(row,1)
            if rownama :
                nama = rownama.text()
                jurusan = rowjur.text()
                self.lineEdit.setText(nama)
                self.lineEdit_2.setText(jurusan)
            self.label_info.setText("Data berhasil ditampilkan")
        except mc.Error as err:
            self.label_info.setText("Data gagal ditampilkan")

    def sqlSimpanData(self):
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
                self.label_info.setText("Data tidak boleh kosong")
                return
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO mhs (nama,jurusan) VALUES (%s,%s)", (nama, jurusan))
            mydb.commit()
            self.label_info.setText("Data berhasil disimpan")

            self.lineEdit.clear()
            self.lineEdit_2.clear()

            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.sqlLoadData()
        except mc.Error as err:
            self.label_info.setText("Data Gagal disimpan")

    #def updatekategori(self), di bawah ini alternatif penamaan
    def sqlEditData(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )

            cursor = mydb.cursor()
            nama = self.lineEdit.text()
            jurusan = self.lineEdit_2.text()
            
            sql = "UPDATE mhs set jurusan = %s WHERE nama = %s"
            val = (jurusan, nama)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_info.setText("Data berhasil di Update")

            self.lineEdit.setText("")
            self.lineEdit_2.setText("")

            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.sqlLoadData()
        except mc.Error as err:
            self.label_info.setText("Data Gagal di Update")

    def sqlHapusData(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "db_python2o"
            )

            cursor = mydb.cursor()
            nama = self.lineEdit.text()
            #jurusan = self.lineEdit_2.text()
            
            sql = "DELETE FROM mhs WHERE nama = %s"
            val = (nama,)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_info.setText("Data berhasil di Hapus")

            self.lineEdit.setText("")
            self.lineEdit_2.setText("")

            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.sqlLoadData()
        except mc.Error as err:
            print(err.msg)
            self.label_info.setText("Data Gagal di Hapus")

    def batal(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_info.setText("Aksi dibatalkan")

    def clear(self):
        #self.tableWidget.clear()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.label_info.setText("Tabel dibersihkan")
    
    def sqlLoadData(self):
        try:
            self.clear()

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
            self.label_info.setText("Data berhasil di Load")
        except mc.Error as err:
            self.label_info.setText("Data Gagal di Load")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())