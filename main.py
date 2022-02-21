import sys
import psycopg2
from PyQt5.QtWidgets import (QApplication,QWidget,QAbstractScrollArea,QVBoxLayout,QHBoxLayout,
                             QTableWidgetItem,QGroupBox,QPushButton,QMessageBox,QTableWidget,QTabWidget)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Shedule')
        self._connect_to_db()

        self.vbox = QHBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self.update_schedule_button = QPushButton('Update')
        self.vbox.addWidget(self.update_schedule_button)

        self.update_schedule_button.clicked.connect(self._update_schedule)

        self._create_teacher_tab()
        self._create_subject_tab()
        self._create_schedule_tab()
        self._create_schedule_tab1()
        self._create_schedule_tab2()
        self._create_schedule_tab3()
        self._create_schedule_tab4()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database = "shedule",
                                     user = "postgres",
                                     password = "1234",
                                     host = "localhost",
                                     port = "5432")
        self.cursor = self.conn.cursor()

    def _create_teacher_tab(self):
        self.t_tab = QWidget()
        self.tabs.addTab(self.t_tab, 'Teachers')

        self.t_gbox = QGroupBox('Teachers')

        self.svbox = QVBoxLayout()
        self.shbox1 = QVBoxLayout()
        self.shbox2 = QHBoxLayout()



        self.shbox1.addWidget(self.t_gbox)

        self._create_t_table()

        self.t_tab.setLayout(self.svbox)

    def _create_subject_tab(self):
        self.sub_tab = QWidget()
        self.tabs.addTab(self.sub_tab, 'Subjects')

        self.sub_gbox = QGroupBox('Subjects')

        self.svbox = QVBoxLayout()
        self.shbox1 = QVBoxLayout()
        self.shbox2 = QHBoxLayout()



        self.shbox1.addWidget(self.sub_gbox)

        self._create_sub_table()

        self.sub_tab.setLayout(self.svbox)

    def _create_schedule_tab(self):
        self.schedule_tab = QWidget()
        self.tabs.addTab(self.schedule_tab, 'Schedule')

        self.monday_gbox = QGroupBox('Monday')

        self.svbox = QVBoxLayout()
        self.shbox1 = QVBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_monday_table()

        self.schedule_tab.setLayout(self.svbox)

    def _create_schedule_tab1(self):
        self.tuesday_gbox = QGroupBox('Tuesday')

        self.shbox1.addWidget(self.tuesday_gbox)

        self._create_tuesday_table()

    def _create_schedule_tab2(self):
        self.wednesday_gbox = QGroupBox('Wednesday')

        self.shbox1.addWidget(self.wednesday_gbox)

        self._create_wednesday_table()

    def _create_schedule_tab3(self):
        self.thursday_gbox = QGroupBox('Thursday')

        self.shbox1.addWidget(self.thursday_gbox)

        self._create_thursday_table()

    def _create_schedule_tab4(self):
        self.friday_gbox = QGroupBox('Friday')

        self.shbox1.addWidget(self.friday_gbox)

        self._create_friday_table()

        self.schedule_tab.setLayout(self.svbox)

    def _create_t_table(self):
        self.t_table = QTableWidget()
        self.t_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.t_table.setColumnCount(5)
        self.t_table.setHorizontalHeaderLabels(['id','Full name', 'Subject','',''])

        self._update_t_table()

        self.svbox = QVBoxLayout()
        self.svbox.addWidget(self.t_table)
        self.t_gbox.setLayout(self.svbox)

    def _create_sub_table(self):
        self.sub_table = QTableWidget()
        self.sub_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.sub_table.setColumnCount(4)
        self.sub_table.setHorizontalHeaderLabels(['id','Subject','',''])

        self._update_sub_table()

        self.svbox = QVBoxLayout()
        self.svbox.addWidget(self.sub_table)
        self.sub_gbox.setLayout(self.svbox)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(6)
        self.monday_table.setHorizontalHeaderLabels(['id','Subject','Room','Time','',''])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(6)
        self.tuesday_table.setHorizontalHeaderLabels(['id', 'Subject', 'Room', 'Time', '', ''])

        self._update_tuesday_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.tvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(6)
        self.wednesday_table.setHorizontalHeaderLabels(['id', 'Subject', 'Room', 'Time', '', ''])

        self._update_wednesday_table()

        self.wvbox = QVBoxLayout()
        self.wvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.wvbox)

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(6)
        self.thursday_table.setHorizontalHeaderLabels(['id', 'Subject', 'Room', 'Time', '', ''])

        self._update_thursday_table()

        self.thvbox = QVBoxLayout()
        self.thvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.thvbox)

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(6)
        self.friday_table.setHorizontalHeaderLabels(['id', 'Subject', 'Room', 'Time', '', ''])

        self._update_friday_table()

        self.fvbox = QVBoxLayout()
        self.fvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.fvbox)

    def _update_t_table(self):
        self.cursor.execute("SELECT teacher_id, full_name, subject FROM teacher")
        records = list(self.cursor.fetchall())
        self.t_table.setRowCount(len(records)+1)
        try:
            for i, r in enumerate(records):
                r = list(r)
                self.t_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.t_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
                self.t_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
                joinButton = QPushButton("Join")
                self.t_table.setCellWidget(i, 3, joinButton)

                joinButton.clicked.connect(lambda ch, num=i: self._change_data_from_t(num))

                deleteButton = QPushButton("Delete")
                self.t_table.setCellWidget(i, 4, deleteButton)

                deleteButton.clicked.connect(lambda ch, num=i: self._delete_data_from_t(num))

            addButton = QPushButton("Add")
            self.t_table.setCellWidget(i+1, 3, addButton)
            addButton.clicked.connect(lambda ch, num=i+1: self._add_t(num))
            self.t_table.resizeRowsToContents()
        except:
            addButton = QPushButton("Add")
            self.t_table.setCellWidget(0, 3, addButton)
            addButton.clicked.connect(lambda ch, num=0: self._add_t(num))
            self.t_table.resizeRowsToContents()

    def _update_sub_table(self):
        self.cursor.execute("SELECT subject FROM subject")
        records = list(self.cursor.fetchall())
        self.sub_table.setRowCount(len(records)+1)
        try:
            for i, r in enumerate(records):
                r = list(r)
                self.sub_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.sub_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
                joinButton = QPushButton("Join")
                self.sub_table.setCellWidget(i, 2, joinButton)

                joinButton.clicked.connect(lambda ch, num=i: self._change_data_from_sub(num))

                deleteButton = QPushButton("Delete")
                self.sub_table.setCellWidget(i, 3, deleteButton)

                deleteButton.clicked.connect(lambda ch, num = i: self._delete_data_from_sub(num))

            addButton = QPushButton("Add")
            self.sub_table.setCellWidget(i+1, 2, addButton)
            addButton.clicked.connect(lambda ch, num=i+1: self._add_sub(num))
            self.sub_table.resizeRowsToContents()
        except:
            addButton = QPushButton("Add")
            self.sub_table.setCellWidget(0, 2, addButton)
            addButton.clicked.connect(lambda ch, num=0: self._add_sub(num))
            self.sub_table.resizeRowsToContents()


    def _update_monday_table(self):
        self.cursor.execute("SELECT id, subject, room_numb, start_time FROM timetable WHERE day = 'monday'")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records)+1)
        try:
            for i,r in enumerate(records):
                r = list(r)
                self.monday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.monday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
                self.monday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
                self.monday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
                joinButton = QPushButton("Join")
                self.monday_table.setCellWidget(i, 4, joinButton)

                joinButton.clicked.connect(lambda ch, num = i: self._change_data_from_table(num))

                deleteButton = QPushButton("Delete")
                self.monday_table.setCellWidget(i, 5, deleteButton)

                deleteButton.clicked.connect(lambda ch, num=i: self._delete_data_from_table(num))

            addButton = QPushButton("Add")
            self.monday_table.setCellWidget(i+1, 4, addButton)
            addButton.clicked.connect(lambda ch, num = i+1: self._add_data(num))
            self.monday_table.resizeRowsToContents()
        except:
            addButton = QPushButton("Add")
            self.monday_table.setCellWidget(0, 4, addButton)
            addButton.clicked.connect(lambda ch, num=0: self._add_data(num))
            self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT id, subject, room_numb, start_time FROM timetable WHERE day = 'tuesday'")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)
        try:
            for i, r in enumerate(records):
                r = list(r)
                self.tuesday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.tuesday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
                self.tuesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
                self.tuesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
                joinButton = QPushButton("Join")
                self.tuesday_table.setCellWidget(i, 4, joinButton)

                joinButton.clicked.connect(lambda ch, num=i: self._change_data_from_table1(num))

                deleteButton = QPushButton("Delete")
                self.tuesday_table.setCellWidget(i, 5, deleteButton)

                deleteButton.clicked.connect(lambda ch, num=i: self._delete_data_from_table1(num))

            addButton = QPushButton("Add")
            self.tuesday_table.setCellWidget(i + 1, 4, addButton)
            addButton.clicked.connect(lambda ch, num=i + 1: self._add_data1(num))
            self.tuesday_table.resizeRowsToContents()
        except:
            addButton = QPushButton("Add")
            self.tuesday_table.setCellWidget(0, 4, addButton)
            addButton.clicked.connect(lambda ch, num=0: self._add_data1(num))
            self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT id, subject, room_numb, start_time FROM timetable WHERE day = 'wednesday'")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)
        try:
            for i, r in enumerate(records):
                r = list(r)
                self.wednesday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.wednesday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
                self.wednesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
                self.wednesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
                joinButton = QPushButton("Join")
                self.wednesday_table.setCellWidget(i, 4, joinButton)

                joinButton.clicked.connect(lambda ch, num=i: self._change_data_from_table2(num))

                deleteButton = QPushButton("Delete")
                self.wednesday_table.setCellWidget(i, 5, deleteButton)

                deleteButton.clicked.connect(lambda ch, num=i: self._delete_data_from_table2(num))

            addButton = QPushButton("Add")
            self.wednesday_table.setCellWidget(i + 1, 4, addButton)
            addButton.clicked.connect(lambda ch, num=i + 1: self._add_data2(num))
            self.wednesday_table.resizeRowsToContents()
        except:
            addButton = QPushButton("Add")
            self.wednesday_table.setCellWidget(0, 4, addButton)
            addButton.clicked.connect(lambda ch, num=0: self._add_data2(num))
            self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
        self.cursor.execute("SELECT id, subject, room_numb, start_time FROM timetable WHERE day = 'thursday'")
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records) + 1)
        try:
            for i, r in enumerate(records):
                r = list(r)
                self.thursday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.thursday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
                self.thursday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
                self.thursday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
                joinButton = QPushButton("Join")
                self.thursday_table.setCellWidget(i, 4, joinButton)

                joinButton.clicked.connect(lambda ch, num=i: self._change_data_from_table3(num))

                deleteButton = QPushButton("Delete")
                self.thursday_table.setCellWidget(i, 5, deleteButton)

                deleteButton.clicked.connect(lambda ch, num=i: self._delete_data_from_table3(num))

            addButton = QPushButton("Add")
            self.thursday_table.setCellWidget(i + 1, 4, addButton)
            addButton.clicked.connect(lambda ch, num=i + 1: self._add_data3(num))
            self.thursday_table.resizeRowsToContents()
        except:
            addButton = QPushButton("Add")
            self.thursday_table.setCellWidget(0, 4, addButton)
            addButton.clicked.connect(lambda ch, num=0: self._add_data3(num))
            self.thursday_table.resizeRowsToContents()

    def _update_friday_table(self):
        self.cursor.execute("SELECT id, subject, room_numb, start_time FROM timetable WHERE day = 'friday'")
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records) + 1)
        try:
            for i, r in enumerate(records):
                r = list(r)
                self.friday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
                self.friday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
                self.friday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
                self.friday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
                joinButton = QPushButton("Join")
                self.friday_table.setCellWidget(i, 4, joinButton)

                joinButton.clicked.connect(lambda ch, num=i: self._change_data_from_table4(num))

                deleteButton = QPushButton("Delete")
                self.friday_table.setCellWidget(i, 5, deleteButton)

                deleteButton.clicked.connect(lambda ch, num=i: self._delete_data_from_table4(num))

            addButton = QPushButton("Add")
            self.friday_table.setCellWidget(i + 1, 4, addButton)
            addButton.clicked.connect(lambda ch, num=i + 1: self._add_data4(num))
            self.friday_table.resizeRowsToContents()
        except:
            addButton = QPushButton("Add")
            self.friday_table.setCellWidget(0, 4, addButton)
            addButton.clicked.connect(lambda ch, num=0: self._add_data4(num))
            self.friday_table.resizeRowsToContents()

    def _change_data_from_t(self, rowNumb):
        row = list()
        for i in range(self.t_table.columnCount()):
            try:
                row.append(self.t_table.item(rowNumb, i).text())
            except:
                row.append(None)
            print(row)
            try:
                self.cursor.execute("UPDATE teacher set full_name =%s, subject =%s WHERE id =%s",
                                    (str(row[1]),str(row[2]),str(row[0])))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_data_from_sub(self, rowNumb):
        row = list()
        for i in range(self.sub_table.columnCount()):
            try:
                row.append(self.sub_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute("UPDATE timetable set name =%s WHERE id =%s",
                                (str(row[1]),str(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields-_-")

    def _change_data_from_table(self, rowNumb):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable set subject =%s, room_numb =%s, start_time =%s WHERE id =%s",
                                (str(row[1]),str(row[2]),str(row[3]),str(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields-_-")

    def _change_data_from_table1(self, rowNumb):
        row = list()
        for i in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable set subject =%s, room_numb =%s, start_time =%s WHERE id =%s",
                                (str(row[1]),str(row[2]),str(row[3]),str(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields-_-")

    def _change_data_from_table2(self, rowNumb):
        row = list()
        for i in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable set subject =%s, room_numb =%s, start_time =%s WHERE id =%s",
                                (str(row[1]),str(row[2]),str(row[3]),str(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields-_-")

    def _change_data_from_table3(self, rowNumb):
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE shedule set subject =%s, room_numb =%s, start_time =%s WHERE id =%s",
                                (str(row[1]),str(row[2]),str(row[3]),str(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields-_-")

    def _change_data_from_table4(self, rowNumb):
        row = list()
        for i in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE shedule set subject =%s, room_numb =%s, start_time =%s WHERE id =%s",
                                (str(row[1]),str(row[2]),str(row[3]),str(row[0])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields-_-")

    def _delete_data_from_t(self, rowNumb):
        row = self.t_table.item(rowNumb, 0).text()
        print(row)
        self.cursor.execute(f"DELETE FROM teacher WHERE id={row}")
        self.conn.commit()
        self.t_table.setRowCount(0)
        self._update_t_table()

    def _delete_data_from_sub(self, rowNumb):
        row = self.sub_table.item(rowNumb, 0).text()
        print(row)
        self.cursor.execute(f"DELETE FROM subject WHERE id={row}")
        self.conn.commit()
        self.sub_table.setRowCount(0)
        self._update_sub_table()

    def _delete_data_from_table(self, rowNumb):
        row = self.monday_table.item(rowNumb, 0).text()
        print(row)
        self.cursor.execute(f"DELETE FROM shedule WHERE id={row}")
        self.conn.commit()
        self.monday_table.setRowCount(0)
        self._update_monday_table()

    def _delete_data_from_table1(self, rowNumb):
        row = self.tuesday_table.item(rowNumb, 0).text()
        print(row)
        self.cursor.execute(f"DELETE FROM shedule WHERE id={row}")
        self.conn.commit()
        self.tuesday_table.setRowCount(0)
        self._update_tuesday_table()

    def _delete_data_from_table2(self, rowNumb):
        row = self.wednesday_tab.item(rowNumb, 0).text()
        print(row)
        self.cursor.execute(f"DELETE FROM shedule WHERE id={row}")
        self.conn.commit()
        self.wednesday_table.setRowCount(0)
        self._update_wednesday_table()

    def _delete_data_from_table3(self, rowNumb):
        row = self.thursday_table.item(rowNumb, 0).text()
        print(row)
        self.cursor.execute(f"DELETE FROM shedule WHERE id={row}")
        self.conn.commit()
        self.thursday_table.setRowCount(0)
        self._update_thursday_table()

    def _delete_data_from_table4(self, rowNumb):
        row = self.friday_table.item(rowNumb, 0).text()
        print(row)
        self.cursor.execute(f"DELETE FROM shedule WHERE id={row}")
        self.conn.commit()
        self.friday_table.setRowCount(0)
        self._update_friday_table()

    def _add_t(self, rowNumb):
        row = list()
        for i in range(self.t_table.columnCount()):
            try:
                row.append(self.t_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row[1])
        try:
            self.cursor.execute("INSERT INTO teacher (full_name,subject) values (%s,%s)", (str(row[1]),str(row[2])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields")
        #self._update_t_table()

    def _add_sub(self, rowNumb):
        row = list()
        for i in range(self.sub_table.columnCount()):
            try:
                row.append(self.sub_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row[1])
        try:
            self.cursor.execute("INSERT INTO subject (name) values ('None')", (str(row[1])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields")
        #self._update_sub_table()

    def _add_data(self, rowNumb):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute("INSERT INTO shedule (day, subject, room_numb, start_time) values ('monday',%s,%s,%s)",
                                (str(row[1]),str(row[2]),str(row[3])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields")
        #self._update_monday_table()

    def _add_data1(self, rowNumb):
        row = list()
        for i in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute("INSERT INTO shedule (day, subject, room_numb, start_time) values ('tuesday',%s,%s,%s)",
                                (str(row[1]),str(row[2]),str(row[3])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields")
        #self._update_tuesday_table()

    def _add_data2(self, rowNumb):
        row = list()
        for i in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute("INSERT INTO shedule (day, subject, room_numb, start_time) values ('wednesday',%s,%s,%s)",
                                (str(row[1]),str(row[2]),str(row[3])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields")
        #self._update_wednesday_table()

    def _add_data3(self, rowNumb):
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute("INSERT INTO shedule (day, subject, room_numb, start_time) values ('thursday',%s,%s,%s)",
                                (str(row[1]),str(row[2]),str(row[3])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields")
        #self._update_thursday_table()

    def _add_data4(self, rowNumb):
        row = list()
        for i in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNumb, i).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute("INSERT INTO shedule (day, subject, room_numb, start_time) values ('friday',%s,%s,%s)",
                                (str(row[1]),str(row[2]),str(row[3])))
            self.conn.commit()
        except:
            QMessageBox.about(self,"Error","Enter all fields")
        #self._update_friday_table()

    def _update_schedule(self):
        self._update_t_table()
        self._update_sub_table()
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

