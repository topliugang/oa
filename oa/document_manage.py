# -*- coding:utf-8 -*- 
from lib_of_db_and_xls import *

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class DocumentRecorder(QWidget):
    def __init__(self, parent=None):
        super(DocumentRecorder, self).__init__(parent)

        self._font = QFont()
        self._font.setPointSize(36)

        serial_number_label = QLabel(u"顺序号:")
        serial_number_label.setFont(self._font)
        self.serial_number_line = QLineEdit(u'1')
        self.serial_number_line.setFont(self._font)

        received_date_label = QLabel(u"收文日期:")
        received_date_label.setFont(self._font)
        self.received_date_line = QLineEdit(u'2017-02-07')
        self.received_date_line.setFont(self._font)

        from_department_label = QLabel(u"来文机关:")
        from_department_label.setFont(self._font)
        self.from_department_line = QLineEdit(u'枣组通字')
        self.from_department_line.setFont(self._font)

        document_number_label = QLabel(u"文件号码:")
        document_number_label.setFont(self._font)
        self.document_number_line = QLineEdit(u'3')
        self.document_number_line.setFont(self._font)

        secret_degree_label = QLabel(u"秘密程度:")
        secret_degree_label.setFont(self._font)
        self.secret_degree_line = QLineEdit(u'')
        self.secret_degree_line.setFont(self._font)

        document_date_label = QLabel(u"文件日期:")
        document_date_label.setFont(self._font)
        self.document_date_line = QLineEdit(u'2017-01-23')
        self.document_date_line.setFont(self._font)

        document_name_label = QLabel(u"文件名称:")
        document_name_label.setFont(self._font)
        self.document_name_line = QLineEdit(u'关于转发鲁组字[2016]63号文件的通知')
        self.document_name_line.setFont(self._font)

        copy_label = QLabel(u"份数:")
        copy_label.setFont(self._font)
        self.copy_line = QLineEdit()
        self.copy_line.setFont(self._font)

        to_staff_label = QLabel(u"交办人:")
        to_staff_label.setFont(self._font)
        self.to_staff_line = QLineEdit(u'陈')
        self.to_staff_line.setFont(self._font)

        recycle_date_label = QLabel(u"收回日期:")
        recycle_date_label.setFont(self._font)
        self.recycle_date_line = QLineEdit()
        self.recycle_date_line.setFont(self._font)

        self.submit_button = QPushButton('&submit')
        self.submit_button.setFont(self._font)
        self.submit_button.show()
        self.submit_button.clicked.connect(self.submit)

        # self.reset_button = QPushButton('&reset')
        # self.reset_button.show()
        # self.reset_button.clicked.connect(self.reset)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.submit_button)

        mainLayout = QGridLayout()
        mainLayout.addWidget(serial_number_label, 0, 0)
        mainLayout.addWidget(self.serial_number_line, 0, 1)

        mainLayout.addWidget(received_date_label, 1, 0)
        mainLayout.addWidget(self.received_date_line, 1, 1)

        mainLayout.addWidget(from_department_label, 2, 0)
        mainLayout.addWidget(self.from_department_line, 2, 1)

        mainLayout.addWidget(document_number_label, 3, 0)
        mainLayout.addWidget(self.document_number_line, 3, 1)

        mainLayout.addWidget(secret_degree_label, 4, 0)
        mainLayout.addWidget(self.secret_degree_line, 4, 1)

        mainLayout.addWidget(document_date_label, 5, 0)
        mainLayout.addWidget(self.document_date_line, 5, 1)

        mainLayout.addWidget(document_name_label, 6, 0)
        mainLayout.addWidget(self.document_name_line, 6, 1)

        mainLayout.addWidget(copy_label, 7, 0)
        mainLayout.addWidget(self.copy_line, 7, 1)

        mainLayout.addWidget(to_staff_label, 8, 0)
        mainLayout.addWidget(self.to_staff_line, 8, 1)

        mainLayout.addWidget(recycle_date_label, 9, 0)
        mainLayout.addWidget(self.recycle_date_line, 9, 1)

        mainLayout.addLayout(buttonLayout, 10, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("收文登记")

    def submit(self):
        serial_number = self.serial_number_line.text()
        received_date = self.received_date_line.text()
        from_department = self.from_department_line.text()
        document_number = self.document_number_line.text()
        secret_degree = self.secret_degree_line.text()
        document_date = self.document_date_line.text()
        document_name = self.document_name_line.text()
        copy = self.copy_line.text()
        to_staff = self.to_staff_line.text()
        recycle_date = self.recycle_date_line.text()

        sql = """
    	insert into document(
		serial_number, received_date, from_department, document_number, secret_degree, 
		document_date, document_name, copy, to_staff, recycle_date) values
		(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
		"""
        data = (serial_number, received_date, from_department, document_number, secret_degree, \
                document_date, document_name, copy, to_staff, recycle_date)
        insert(sql, data)



        # def reset(self):
        # 	pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dr = DocumentRecorder()
    # dr.resize(800, 600)
    # w.setWindowTitle('fuck')
    dr.show()

    sys.exit(app.exec_())
