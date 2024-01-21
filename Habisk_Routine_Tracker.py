from PyQt5 import QtCore, QtGui, QtWidgets
import random
import mysql.connector as sqlcon
import datetime as dt

td_day=dt.datetime.now().strftime("%A")
td_date=dt.datetime.now()
dmaker=''
dmaker+=td_date.strftime("%Y")
dmaker+='-'
dmaker+=td_date.strftime("%m")
dmaker+='-'
dmaker+=td_date.strftime("%d")
td_date=dmaker
# Replace ("password") in the next line with your own password
con1=sqlcon.connect(host="localhost",user="root",passwd="0904")
cur=con1.cursor()
cur.execute("SHOW DATABASES LIKE 'project'")
a = cur.fetchall()

if len(a) == 0:
        cur.execute("create database project")

cur.execute("use project")

cur.execute("SHOW Tables LIKE 'Habit';")
flg10 = cur.fetchall()
if len(flg10) == 0:
        cur.execute("create table Habit(Habit_Name varchar(50), Start_Time char(6), End_Time char(6), Mon char(3), Tue char(3), Wed char(3), Thurs char(3), Fri char(3), Sat char(3), Sun char(3))")

cur.execute("SHOW Tables LIKE 'Task';")
flg10 = cur.fetchall()
if len(flg10) == 0:
        cur.execute("create table task(Tk_Name varchar(50), Description varchar(200), Tk_date date, Tk_Time char(6))")

cur.execute("SHOW Tables LIKE 'hb_hb';")
flg10 = cur.fetchall()
if len(flg10) == 0:
        cur.execute("create table hb_hb(Habit_Name varchar(50), Description varchar(200), frequency varchar(10), Counter int)")


#Quotes

qt_list=["All our dreams can come true, if we have the courage to pursue them."
                ,"The secret of getting ahead is getting started."
                ,"Only the paranoid survive."
                ,"Everything you can imagine is real."
                ,"Do one thing every day that scares you."
                ,"Whatever you are, be a good one."
                ,"If we have the attitude that it's going to be a great day it usually is."
                ,"Hold the vision, trust the process."
                ,"Don't be afraid to give up the good to go for the great."
                ,"One day or day one. You decide."
                ,"Everything comes to him who hustles while he waits."
                ,"Don't be afraid to stand on a mountain of no's for one yes."
                ,"Life is 10% what happens to you and 90% how you react to it."
                ,"Keep a little fire burning; however small, however hidden."
                ,"Never look back, it distracts from the now."
                ,"You carry the ticket to your own happiness."
                ,"If you don't risk anything, you risk even more."
                ,"A surplus of effort could overcome a deficit of confidence."
                ,"Some people want it to happen, some wish it would happen, others make it happen."
                ,"Keep your eyes on the stars, and your feet on the ground."
                ]

qt_placeholder=random.choice(qt_list)

#Window Setup

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, -20, 1931, 1101))
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        
        self.Quote_label = QtWidgets.QLabel(self.page)
        self.Quote_label.setGeometry(QtCore.QRect(20, 890, 1880, 100))
        
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(28)
        font.setItalic(True)
        
        self.Quote_label.setFont(font)
        self.Quote_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Quote_label.setStyleSheet("border-color: rgb(29, 29, 29);\n"
"background-color: rgb(30, 30, 30);\n"
"color: rgb(229, 229, 229)")
        
        self.Quote_label.setObjectName("Quote_label")
        
        self.Bt_Routine = QtWidgets.QPushButton(self.page)
        self.Bt_Routine.setGeometry(QtCore.QRect(630, 210, 611, 141))
        self.Bt_Routine.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(81, 81, 81);\n"
"font: 36pt \"Californian FB\";\n"
"border: 1px solid white;")
        
        self.Bt_Routine.setObjectName("Bt_Routine")
        self.Rtview = QtWidgets.QTableWidget(self.page)
        self.Rtview.setGeometry(QtCore.QRect(20, 40, 581, 831))
        self.Rtview.setColumnCount(1)
        self.Rtview.setHorizontalHeaderLabels([td_day])
        
        if td_day=="Monday":
                
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Mon'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Mon'))
        
        elif td_day=="Tuesday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Tue'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Tue'))
        
        elif td_day=="Wednesday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Wed'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Wed'))
        
        elif td_day=="Thursday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Thurs'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Thurs'))
        
        elif td_day=="Friday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Fri'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Fri'))
        
        elif td_day=="Saturday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sat'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sat'))
        
        elif td_day=="Sunday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sun'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sun'))
        
        irow = 0
        
        self.Rtview.horizontalHeader().resizeSection(0,600)
        
        while True:
        
                hbsqlRow = cur.fetchone()
        
                if hbsqlRow == None:
        
                        break
        
                else:
        
                        hbsqlRow=hbsqlRow[0]
                        self.Rtview.setItem(irow,0,QtWidgets.QTableWidgetItem(hbsqlRow))
        
                irow += 1
        
        self.Rtview.setStyleSheet("QWidget {background-color: #333333; color: #fffff8;}"

"QHeaderView::section {"
    "background-color: #646464;"
    "padding: 4px;"
    "border: 1px solid #fffff8;"
    "font-size: 14pt;}"

"QTableWidget {gridline-color: #fffff8; font-size: 12pt;}"

"QTableWidget QTableCornerButton::section {background-color: #646464;border: 1px solid #fffff8;}")
        
        self.Rtview.setObjectName("Rtview")
        self.Bt_Task = QtWidgets.QPushButton(self.page)
        self.Bt_Task.setGeometry(QtCore.QRect(630, 480, 611, 141))
        self.Bt_Task.setStyleSheet("color: rgb(245, 245, 245);\n"
"background-color: rgb(81, 81, 81);\n"
"font: 36pt \"Californian FB\";\n"
"border: 1px solid white;")
        
        self.Bt_Task.setObjectName("Bt_Task")        
        self.ttkview = QtWidgets.QTableWidget(self.page)
        self.ttkview.setGeometry(QtCore.QRect(1270, 50, 641, 801))
        self.ttkview.setColumnCount(2)
        self.ttkview.setHorizontalHeaderLabels(["Today's Task",'Time'])
        
        cur.execute("select * from task where Tk_date='{}'".format(td_date))
        ttallrows=cur.fetchall()
        
        self.ttkview.setRowCount(len(ttallrows))
        
        cur.execute("select Tk_Name, Tk_time from task where Tk_date='{}'".format(td_date))
        irow = 0
        
        self.ttkview.horizontalHeader().resizeSection(0,305)
        self.ttkview.horizontalHeader().resizeSection(1,302)

        while True:

                tkRow = cur.fetchone()

                if tkRow == None:
                        break

                else:

                        for col in range(2):

                                Row=tkRow[col]
                                self.ttkview.setItem(irow,col,QtWidgets.QTableWidgetItem(Row))

                irow += 1

        self.ttkview.setStyleSheet("QWidget {background-color: #333333; color: #fffff8;}"

"QHeaderView::section {"
    "background-color: #646464;"
    "padding: 4px;"
    "border: 1px solid #fffff8;"
    "font-size: 14pt;}"

"QTableWidget {gridline-color: #fffff8; font-size: 12pt;}"

"QTableWidget QTableCornerButton::section {background-color: #646464;border: 1px solid #fffff8;}")

        self.ttkview.setObjectName("ttkview")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Rtfullview = QtWidgets.QTableWidget(self.page_2)
        
        cur.execute('select * from habit')
        hballSQLRows= cur.fetchall()
        
        self.Rtfullview.setRowCount(len(hballSQLRows))
        self.Rtfullview.setColumnCount(7)
        self.Rtfullview.setHorizontalHeaderLabels(["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"])
        
        cur.execute('select * from habit')
        irow = 0

        while True:

                hbsqlRow = cur.fetchone()

                if hbsqlRow == None:
                        break

                else:

                        hb_rtin=[]

                        for i in range(3,10):

                                if hbsqlRow[i]=="Yes":
                                        hb_rtin.append(hbsqlRow[0])

                                else:
                                        hb_rtin.append('')

                for icol in range(0, 7):
                        self.Rtfullview.setItem(irow,icol,QtWidgets.QTableWidgetItem(hb_rtin[icol]))

                irow += 1

        self.Rtfullview.setGeometry(QtCore.QRect(20, 60, 910, 900))
        self.Rtfullview.setStyleSheet("QWidget {background-color: #333333; color: #fffff8;}"

"QHeaderView::section {"
    "background-color: #646464;"
    "padding: 4px;"
    "border: 1px solid #fffff8;"
    "font-size: 14pt;}"

"QTableWidget {gridline-color: #fffff8; font-size: 12pt;}"

"QTableWidget QTableCornerButton::section {background-color: #646464;border: 1px solid #fffff8;}")
        self.Rtfullview.setObjectName("Rtfullview")
        self.hab_in = QtWidgets.QTabWidget(self.page_2)
        self.hab_in.setGeometry(QtCore.QRect(1000, 40, 811, 351))
        self.hab_in.setStyleSheet("font: 10pt \"Mongolian Baiti\";")
        self.hab_in.setObjectName("hab_in")
        
        self.tab_rt = QtWidgets.QWidget()
        self.tab_rt.setObjectName("tab_rt")

        self.rt_err = QtWidgets.QMessageBox()
        self.rt_err.setWindowTitle("Habit not added")
        self.rt_err.setText("Please select when and try again!!!")
        
        self.Start_time = QtWidgets.QTimeEdit(self.tab_rt)
        self.Start_time.setGeometry(QtCore.QRect(130, 250, 151, 41))
        self.Start_time.setStyleSheet("font: 20pt \"Haettenschweiler\";\n"
"color: rgb(255, 255, 255);")

        self.Start_time.setObjectName("Start_time")
        
        self.End_time = QtWidgets.QTimeEdit(self.tab_rt)
        self.End_time.setGeometry(QtCore.QRect(420, 250, 141, 41))
        self.End_time.setStyleSheet("font: 20pt \"Haettenschweiler\";\n"
"color: rgb(255, 255, 255);")

        self.End_time.setObjectName("End_time")
        
        self.lbl_starttime = QtWidgets.QLabel(self.tab_rt)
        self.lbl_starttime.setGeometry(QtCore.QRect(30, 240, 91, 51))
        self.lbl_starttime.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lbl_starttime.setObjectName("lbl_starttime")
        self.lbl_endtime = QtWidgets.QLabel(self.tab_rt)
        self.lbl_endtime.setGeometry(QtCore.QRect(330, 240, 81, 51))
        self.lbl_endtime.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.lbl_endtime.setObjectName("lbl_endtime")
        
        self.Check_mon = QtWidgets.QCheckBox(self.tab_rt)
        self.Check_mon.setGeometry(QtCore.QRect(30, 110, 111, 31))
        self.Check_mon.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);")

        self.Check_mon.setObjectName("Check_mon")
        self.Check_tues = QtWidgets.QCheckBox(self.tab_rt)
        self.Check_tues.setGeometry(QtCore.QRect(160, 110, 131, 31))
        self.Check_tues.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);")

        self.Check_tues.setObjectName("Check_tues")
        self.Check_wed = QtWidgets.QCheckBox(self.tab_rt)
        self.Check_wed.setGeometry(QtCore.QRect(320, 110, 151, 31))
        self.Check_wed.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);")

        self.Check_wed.setObjectName("Check_wed")
        self.Check_thurs = QtWidgets.QCheckBox(self.tab_rt)
        self.Check_thurs.setGeometry(QtCore.QRect(500, 110, 131, 31))
        self.Check_thurs.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);")

        self.Check_thurs.setObjectName("Check_thurs")
        self.Check_fri = QtWidgets.QCheckBox(self.tab_rt)
        self.Check_fri.setGeometry(QtCore.QRect(670, 110, 101, 41))
        self.Check_fri.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);")

        self.Check_fri.setObjectName("Check_fri")
        self.Check_sat = QtWidgets.QCheckBox(self.tab_rt)
        self.Check_sat.setGeometry(QtCore.QRect(140, 170, 121, 41))
        self.Check_sat.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);")

        self.Check_sat.setObjectName("Check_sat")
        self.Check_sun = QtWidgets.QCheckBox(self.tab_rt)
        self.Check_sun.setGeometry(QtCore.QRect(450, 170, 111, 41))
        self.Check_sun.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);")

        self.Check_sun.setObjectName("Check_sun")
                
        self.Rt_Hb_name = QtWidgets.QLineEdit(self.tab_rt)
        self.Rt_Hb_name.setGeometry(QtCore.QRect(20, 10, 301, 61))
        self.Rt_Hb_name.setStyleSheet("font: 25pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white\n"
"")
        self.Rt_Hb_name.setObjectName("Rt_Hb_name")
        
        self.Rt_addhb = QtWidgets.QPushButton(self.tab_rt)
        self.Rt_addhb.setGeometry(QtCore.QRect(620, 250, 171, 51))
        self.Rt_addhb.setStyleSheet("font: 75 20pt \"Segoe UI\";\n"
"color: rgb(250,250,250);\n"
"background-color: rgb(67, 67, 67)")
        
        self.Rt_addhb.setObjectName("Rt_addhb")
        
        self.hab_in.addTab(self.tab_rt, "")
        self.tab_hb = QtWidgets.QWidget()
        self.tab_hb.setObjectName("tab_hb")
        
        self.Daily_rd = QtWidgets.QRadioButton(self.tab_hb)
        self.Daily_rd.setGeometry(QtCore.QRect(50, 250, 101, 51))
        self.Daily_rd.setStyleSheet("font: 18pt \"Mongolian Baiti\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: 2px rgb(117, 117, 117);\n"
"")
        
        self.Daily_rd.setObjectName("Daily_rd")
        
        self.Weekly_rd = QtWidgets.QRadioButton(self.tab_hb)
        self.Weekly_rd.setGeometry(QtCore.QRect(220, 250, 131, 51))
        self.Weekly_rd.setStyleSheet("font: 18pt \"Mongolian Baiti\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: 2px rgb(117, 117, 117);")
        
        self.Weekly_rd.setObjectName("Weekly_rd")
        
        self.Hb_hb_name = QtWidgets.QLineEdit(self.tab_hb)
        self.Hb_hb_name.setGeometry(QtCore.QRect(40, 20, 301, 51))
        self.Hb_hb_name.setStyleSheet("font: 25pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white")
        
        self.Hb_hb_name.setObjectName("Hb_hb_name")
        
        self.Hb_hb_desc = QtWidgets.QPlainTextEdit(self.tab_hb)
        self.Hb_hb_desc.setGeometry(QtCore.QRect(40, 80, 741, 141))
        self.Hb_hb_desc.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);\n"
"border: 3px double white\n"
"")
        
        self.Hb_hb_desc.setObjectName("Hb_hb_desc")
        
        self.Hb_addhb = QtWidgets.QPushButton(self.tab_hb)
        self.Hb_addhb.setGeometry(QtCore.QRect(420, 250, 361, 51))
        self.Hb_addhb.setStyleSheet("font: 75 20pt \"Segoe UI\";\n"
"color: rgb(250,250,250);\n"
"background-color: rgb(67, 67, 67)")
        
        self.Hb_addhb.setObjectName("Hb_addhb")
        
        self.hab_in.addTab(self.tab_hb, "")
        self.Hbt_select = QtWidgets.QComboBox(self.page_2)
        self.Hbt_select.setGeometry(QtCore.QRect(1000, 470, 461, 111))
        self.Hbt_select.setStyleSheet("font: 25pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white\n"
"")
        
        self.Hbt_select.setObjectName("Hbt_select")
        
        cur.execute('select * from hb_hb')
        hbsql=cur.fetchall()
        for i in range(len(hbsql)):
                self.Hbt_select.addItem("")
        
        self.Hbt_Done = QtWidgets.QPushButton(self.page_2)
        self.Hbt_Done.setGeometry(QtCore.QRect(1500, 470, 165, 110))
        self.Hbt_Done.setStyleSheet("font: 75 20pt \"Segoe UI\";\n"
"color: rgb(250,250,250);\n"
"background-color: rgb(67, 67, 67)")
        
        self.Hbt_Done.setObjectName("Hbt_Done")

        self.Del_routine = QtWidgets.QPushButton(self.page_2)
        self.Del_routine.setGeometry(QtCore.QRect(500, 975, 220, 50))
        self.Del_routine.setStyleSheet("font: 75 20pt \"Segoe UI\";\n"
"color: rgb(250,250,250);\n"
"background-color: rgb(67, 67, 67)")
        
        self.Del_routine.setObjectName("Hbt_Done")
        
        self.progress_bar = QtWidgets.QTableWidget(self.page_2)
        self.progress_bar.setGeometry(QtCore.QRect(1000, 610, 811, 341))
        
        cur.execute('select * from hb_hb')
        hbitall=cur.fetchall()
        
        self.progress_bar.setRowCount(len(hbitall))
        self.progress_bar.setColumnCount(4)
        self.progress_bar.setHorizontalHeaderLabels(['Name','Description','Frequency','Counter'])
        
        header = self.progress_bar.horizontalHeader()
        header.resizeSection(0,165)
        header.resizeSection(1,360)
        header.resizeSection(2,150)
        header.resizeSection(3,100)
        
        cur.execute('select * from hb_hb')
        irow = 0
        while True:
                hsqlRow = cur.fetchone()
                if hsqlRow == None:
                        break
                else:
                        for icol in range(0,4):
                                item=hsqlRow[icol]
                                item=str(item)
                                self.progress_bar.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
                irow += 1
        self.progress_bar.setStyleSheet("QWidget {background-color: #333333; color: #fffff8;}"

"QHeaderView::section {"
    "background-color: #646464;"
    "padding: 4px;"
    "border: 1px solid #fffff8;"
    "font-size: 14pt;}"

"QTableWidget {gridline-color: #fffff8; font-size: 12pt;}"

"QTableWidget QTableCornerButton::section {background-color: #646464;border: 1px solid #fffff8;}")
        
        self.progress_bar.setObjectName("progress_bar")
        
        self.Hbt_remove = QtWidgets.QPushButton(self.page_2)
        self.Hbt_remove.setGeometry(QtCore.QRect(1670, 470, 165, 110))
        self.Hbt_remove.setStyleSheet("font: 75 20pt \"Segoe UI\";\n"
"color: rgb(250,250,250);\n"
"background-color: rgb(67, 67, 67)")
        
        self.Hbt_remove.setObjectName("Hbt_remove")
        
        self.Back_btn = QtWidgets.QCommandLinkButton(self.page_2)
        self.Back_btn.setGeometry(QtCore.QRect(30, 975, 220, 50))
        self.Back_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Back_btn.setObjectName("Back_btn")
        self.stackedWidget.addWidget(self.page_2)
        
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(40, 50, 800, 915))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.Add = QtWidgets.QPushButton(self.frame_2)
        self.Add.setGeometry(QtCore.QRect(610, 10, 70, 70))
        self.Add.setStyleSheet("font: 75 20pt \"Segoe UI\";\n"
"color: rgb(250,250,250);\n"
"background-color: rgb(67, 67, 67)")
        
        self.Add.setObjectName("Add")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(40, 100, 150, 70))
        self.dateEdit.setStyleSheet("font: 20pt \"Haettenschweiler\";\n"
"color: rgb(255, 255, 255);\n"
"")
        
        self.dateEdit.setObjectName("dateEdit")
        self.Tk_desc = QtWidgets.QTextEdit(self.frame_2)
        self.Tk_desc.setGeometry(QtCore.QRect(40, 190, 450, 140))
        self.Tk_desc.setStyleSheet("font: 15pt;\n"
"color: rgb(255, 255, 255);\n"
"border: 3px double white\n"
"")
        
        self.Tk_desc.setObjectName("Tk_desc")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit.setGeometry(QtCore.QRect(220, 100, 160, 70))
        self.timeEdit.setStyleSheet("font: 20pt \"Haettenschweiler\";\n"
"color: rgb(255, 255, 255);")
        
        self.timeEdit.setObjectName("timeEdit")
        self.Tk_name = QtWidgets.QLineEdit(self.frame_2)
        self.Tk_name.setGeometry(QtCore.QRect(40, 10, 450, 80))
        self.Tk_name.setStyleSheet("font: 25pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white\n"
"")
        
        self.Tk_name.setObjectName("Tk_name")

        self.tasktable = QtWidgets.QTableWidget(self.frame_2)
        self.tasktable.setGeometry(QtCore.QRect(40, 370, 800, 520))
        
        cur.execute('select * from task')
        tkallSQLRows= cur.fetchall()
        
        self.tasktable.setRowCount(len(tkallSQLRows))
        self.tasktable.setColumnCount(4)
        self.tasktable.setHorizontalHeaderLabels(["Name","Description","Date","Time",])
        
        theader = self.tasktable.horizontalHeader()
        theader.resizeSection(0,95)
        theader.resizeSection(1,355)
        theader.resizeSection(2,200)
        theader.resizeSection(3,100)
        
        cur.execute('select * from task')
        irow = 0
        
        while True:
        
                tksqlRow = cur.fetchone()
        
                if tksqlRow == None:
                        break
        
                else:
        
                        for icol in range(0,4):
        
                                item=tksqlRow[icol]
                                item=str(item)
                                self.tasktable.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
        
                irow += 1
        
        self.tasktable.setStyleSheet("QWidget {background-color: #333333; color: #fffff8;}"

"QHeaderView::section {"
    "background-color: #646464;"
    "padding: 4px;"
    "border: 1px solid #fffff8;"
    "font-size: 14pt;}"

"QTableWidget {gridline-color: #fffff8; font-size: 12pt;}"

"QTableWidget QTableCornerButton::section {background-color: #646464;border: 1px solid #fffff8;}")
        
        self.tasktable.setObjectName("tasktable")
        
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page_3)
        self.calendarWidget.setGeometry(QtCore.QRect(950, 50, 950, 570))
        self.calendarWidget.setStyleSheet("QWidget {background-color: #333333; color: #fffff8;}"

"QCalendarWidget {gridline-color: #fffff8; font-size: 12pt;}"

)

        self.calendarWidget.setObjectName("calendarWidget")
        
        self.Tk_select = QtWidgets.QComboBox(self.page_3)
        self.Tk_select.setGeometry(QtCore.QRect(950, 690, 950, 150))
        self.Tk_select.setStyleSheet("font: 25pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white\n"
"")

        self.Tk_select.setObjectName("Tk_select")
        
        cur.execute('select * from task')
        tksql=cur.fetchall()
        for i in range(len(tksql)):
                self.Tk_select.addItem("")

        self.Tk_Done = QtWidgets.QPushButton(self.page_3)
        self.Tk_Done.setGeometry(QtCore.QRect(950, 850, 950, 150))
        self.Tk_Done.setStyleSheet("font: 75 20pt \"Segoe UI\";\n"
"color: rgb(250,250,250);\n"
"background-color: rgb(67, 67, 67)")

        self.Hbt_Done.setObjectName("Tk_Done")
        
        self.Back_btn_2 = QtWidgets.QCommandLinkButton(self.page_3)
        self.Back_btn_2.setGeometry(QtCore.QRect(30, 975, 222, 48))
        self.Back_btn_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Back_btn_2.setObjectName("Back_btn_2")
        self.stackedWidget.addWidget(self.page_3)

        MainWindow.setCentralWidget(self.centralwidget)        

        self.Rt_addhb.clicked.connect(self.Rt_Hb_in)
        self.Hb_addhb.clicked.connect(self.Hb_Hb_in)
        self.Daily_rd.clicked.connect(self.Wkut)
        self.Weekly_rd.clicked.connect(self.Dlut)
        self.Add.clicked.connect(self.Tk_in)
        self.Hbt_Done.clicked.connect(self.Hb_ct_up)
        self.Hbt_remove.clicked.connect(self.Hb_del)
        self.Del_routine.clicked.connect(self.clear_rt)

        self.Tk_Done.clicked.connect(self.del_task)

        self.Bt_Routine.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Bt_Task.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Back_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.Back_btn_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.retranslateUi(MainWindow)
        self.hab_in.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Defining input functions:
    
    def Rt_Hb_in(self):
    
        Rt_habname=(self.Rt_Hb_name.text())
        Rt_hbsttime=(self.Start_time.text())
        RT_hbedtime=(self.End_time.text())
        list_days=[]
        flg = 0
        flg_1= "No"
        flg_2= "No"
        flg_3= "No"
        flg_4= "No"
        flg_5= "No"
        flg_6= "No"
        flg_7= "No"
    
        if self.Check_mon.isChecked():
    
                list_days.append("Mon")
                flg_1= "Yes"
                flg = 1
    
        if self.Check_tues.isChecked():
    
                list_days.append("Tues")
                flg_2= "Yes"
                flg = 1
        if self.Check_wed.isChecked():
                list_days.append("Wed")
                flg_3= "Yes"
                flg = 1
        if self.Check_thurs.isChecked():
                list_days.append("Thurs")
                flg_4= "Yes"
                flg = 1
        if self.Check_fri.isChecked():
                list_days.append("Fri")
                flg_5= "Yes"
                flg = 1
        if self.Check_sat.isChecked():
                list_days.append("Sat")
                flg_6= "Yes"
                flg = 1
        if self.Check_sun.isChecked():
                list_days.append("Sun")
                flg_7= "Yes"
                flg = 1
        if flg==1:
    
                cur.execute("insert into Habit values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Rt_habname,Rt_hbsttime,RT_hbedtime,flg_1,flg_2,flg_3,flg_4,flg_5,flg_6,flg_7))
                con1.commit()
    
        else:
    
                x=self.rt_err.exec_()
                x
        
        cur.execute('select * from habit')
        allSQLRows= cur.fetchall()
    
        self.Rtfullview.setRowCount(len(allSQLRows))
    
        cur.execute('select * from habit')
        irow = 0
    
        while True:
    
                hbsqlRow = cur.fetchone()
    
                if hbsqlRow == None:
                        break
    
                else:
                        hb_rtin=[]
    
                        for i in range(3,10):
    
                                if hbsqlRow[i]=="Yes":
                                        hb_rtin.append(hbsqlRow[0])
    
                                else:
                                        hb_rtin.append('')
    
                for icol in range(0, 7):
    
                        self.Rtfullview.setItem(irow,icol,QtWidgets.QTableWidgetItem(hb_rtin[icol]))
    
                irow += 1
        
        self.Rtview.setRowCount(0)
        self.Rtview.setColumnCount(1)
        self.Rtview.setHorizontalHeaderLabels([td_day])
        
        if td_day=="Monday":
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Mon'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Mon'))
        
        elif td_day=="Tuesday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Tues'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Tues'))
        
        elif td_day=="Wednesday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Wed'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Wed'))
        
        elif td_day=="Thursday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Thurs'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Thurs'))
        
        elif td_day=="Friday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Fri'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Fri'))
        
        elif td_day=="Saturday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sat'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sat'))
        
        elif td_day=="Sunday":
        
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sun'))
                hallSQLRows= cur.fetchall()
                self.Rtview.setRowCount(len(hallSQLRows))
                cur.execute('select Habit_Name from habit where {}="yes"'.format('Sun'))
        
        irow = 0
        
        self.Rtview.horizontalHeader().resizeSection(0,600)
        
        while True:
        
                hbsqlRow = cur.fetchone()
        
                if hbsqlRow == None:
                        break
        
                else:
        
                        hbsqlRow=hbsqlRow[0]
                        self.Rtview.setItem(irow,0,QtWidgets.QTableWidgetItem(hbsqlRow))
        
                irow += 1
        
    def Wkut(self):
 
        self.Weekly_rd.setChecked(False)
 
    def Dlut(self):
 
        self.Daily_rd.setChecked(False)
    
    def Hb_Hb_in(self):
        if self.Daily_rd.isChecked():
                frenq="Daily"
                Hb_hbname=(self.Hb_hb_name.text())
                Hb_hbdesc=(self.Hb_hb_desc.toPlainText())
                c=0
                cur.execute("insert into hb_Hb values('{}','{}','{}','{}')".format(Hb_hbname,Hb_hbdesc,frenq,c))
                con1.commit()
                self.progress_bar.setRowCount(0)
                cur.execute('select * from hb_hb')
                hrow=cur.fetchall()
                self.progress_bar.setRowCount(len(hrow))
                cur.execute('select * from hb_hb')
                irow = 0
                
                while True:
                        hsqlRow = cur.fetchone()
                        if hsqlRow == None:
                                break
                        else:
                                for icol in range(0,4):
                                        item=hsqlRow[icol]
                                        item=str(item)
                                        self.progress_bar.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
                        irow += 1

                cur.execute('select * from hb_hb')
                hbsql=cur.fetchall()
                hbnewi=hbsql[len(hbsql)-1][0]
                self.Hbt_select.addItem(hbnewi)
        elif self.Weekly_rd.isChecked():
                frenq="Weekly"
                Hb_hbname=(self.Hb_hb_name.text())
                Hb_hbdesc=(self.Hb_hb_desc.toPlainText())
                c=0
                cur.execute("insert into hb_Hb values('{}','{}','{}','{}')".format(Hb_hbname,Hb_hbdesc,frenq,c))
                con1.commit()
                self.progress_bar.setRowCount(0)
                cur.execute('select * from hb_hb')
                hrow=cur.fetchall()
                self.progress_bar.setRowCount(len(hrow))
                cur.execute('select * from hb_hb')
                irow = 0
                
                while True:
                        hsqlRow = cur.fetchone()
                        if hsqlRow == None:
                                break
                        else:
                                for icol in range(0,4):
                                        item=hsqlRow[icol]
                                        item=str(item)
                                        self.progress_bar.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
                        irow += 1

                cur.execute('select * from hb_hb')
                hbsql=cur.fetchall()
                hbnewi=hbsql[len(hbsql)-1][0]
                self.Hbt_select.addItem(hbnewi)
        else:
                x=self.rt_err.exec_()
                x
        
    def Tk_in(self):
        Tk_tkname=(self.Tk_name.text())
        Tk_tkdesc=(self.Tk_desc.toPlainText())
        Tk_tkdate=(self.dateEdit.text())
        Tk_tktime=(self.timeEdit.text())
        date = Tk_tkdate[-4:] + "-" +   Tk_tkdate[-7:-5] +"-"+ Tk_tkdate[-10:-8]
        cur.execute("insert into task values('{}','{}','{}','{}')".format(Tk_tkname,Tk_tkdesc,date,Tk_tktime))
        con1.commit()
        cur.execute('select * from task')
        taskall=cur.fetchall()
        tknew=taskall[len(taskall)-1][0]
        self.Tk_select.addItem(tknew)
        self.tasktable.setRowCount(len(taskall))
        cur.execute('select * from task')
        irow = 0
        
        while True:
                
                tksqlRow = cur.fetchone()
                
                if tksqlRow == None:
                        break
                
                else:
                        
                        for icol in range(0,4):
                        
                                item=tksqlRow[icol]
                                item=str(item)
                                self.tasktable.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
                irow += 1
        self.ttkview.setRowCount(0)
        cur.execute("select * from task where Tk_date='{}'".format(td_date))
        ttallrows=cur.fetchall()
        self.ttkview.setRowCount(len(ttallrows))
        cur.execute("select Tk_Name, Tk_time from task where Tk_date='{}'".format(td_date))
        irow = 0
        while True:
                tkRow = cur.fetchone()
                if tkRow == None:
                        break
                else:
                        for col in range(2):
                                Row=tkRow[col]
                                self.ttkview.setItem(irow,col,QtWidgets.QTableWidgetItem(Row))
                irow += 1

    def Hb_ct_up(self):
        up_index=(self.Hbt_select.currentIndex())
        Hup_name=(self.Hbt_select.itemText(up_index))
        cur.execute('update hb_hb set counter=counter+1 where Habit_name="{}"'.format(Hup_name))
        con1.commit()
        self.progress_bar.setRowCount(0)
        cur.execute('select * from hb_hb')
        hrow=cur.fetchall()
        self.progress_bar.setRowCount(len(hrow))
        cur.execute('select * from hb_hb')
        irow = 0
        
        while True:
                hsqlRow = cur.fetchone()
                if hsqlRow == None:
                        break
                else:
                        for icol in range(0,4):
                                item=hsqlRow[icol]
                                item=str(item)
                                self.progress_bar.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
                irow += 1
    
    def Hb_del(self):
        H_index=(self.Hbt_select.currentIndex())
        H_name=(self.Hbt_select.itemText(H_index))
        cur.execute('delete from hb_hb where Habit_name="{}"'.format(H_name))
        con1.commit()
        self.progress_bar.setRowCount(0)
        cur.execute('select * from hb_hb')
        hrow=cur.fetchall()
        self.progress_bar.setRowCount(len(hrow))
        cur.execute('select * from hb_hb')
        irow = 0
        while True:
                hsqlRow = cur.fetchone()
                if hsqlRow == None:
                        break
                else:
                        for icol in range(0,4):
                                item=hsqlRow[icol]
                                item=str(item)
                                self.progress_bar.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
                irow += 1
        self.Hbt_select.removeItem(H_index)

    def clear_rt(self):
       
        cur.execute('truncate table habit')
        con1.commit()
      
        self.Rtfullview.setRowCount(0)
        self.Rtview.setRowCount(0)
    
    def del_task(self):
       
        tk_deli=self.Tk_select.currentIndex()
        tk_del=(self.Tk_select.itemText(tk_deli))
        cur.execute('delete from task where Tk_Name="{}"'.format(tk_del))
        con1.commit()
      
        self.Tk_select.removeItem(tk_deli)
      
        self.tasktable.setRowCount(0)
        cur.execute('select * from task')
        taskall=cur.fetchall()
      
        self.tasktable.setRowCount(len(taskall))
        cur.execute('select * from task')
        irow = 0
       
        while True:
       
                tksqlRow = cur.fetchone()
       
                if tksqlRow == None:
                        break
       
                else:
                        for icol in range(0,4):
                                item=tksqlRow[icol]
                                item=str(item)
                                self.tasktable.setItem(irow,icol,QtWidgets.QTableWidgetItem(item))
       
                irow += 1
      
        self.ttkview.setRowCount(0)
    
    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Habisk"))
      
        self.Quote_label.setText(_translate("MainWindow", qt_placeholder))
        self.Bt_Routine.setText(_translate("MainWindow", "Routine"))
        self.Bt_Task.setText(_translate("MainWindow", "Tasks"))
        self.lbl_starttime.setText(_translate("MainWindow", "Start Time:"))
        self.lbl_endtime.setText(_translate("MainWindow", "End Time:"))
        self.Check_mon.setText(_translate("MainWindow", "Monday"))
        self.Check_tues.setText(_translate("MainWindow", "Tuesday"))
        self.Check_wed.setText(_translate("MainWindow", "Wednesday"))
        self.Check_sat.setText(_translate("MainWindow", "Saturday"))
        self.Check_sun.setText(_translate("MainWindow", "Sunday"))
        self.Check_fri.setText(_translate("MainWindow", "Friday"))
        self.Check_thurs.setText(_translate("MainWindow", "Thursday"))
        self.Rt_Hb_name.setText(_translate("MainWindow", "Habit Name"))
        self.Rt_addhb.setText(_translate("MainWindow", "Add Habit"))
        self.hab_in.setTabText(self.hab_in.indexOf(self.tab_rt), _translate("MainWindow", "Routine"))
        self.Daily_rd.setText(_translate("MainWindow", "Daily"))
        self.Weekly_rd.setText(_translate("MainWindow", "Weekly"))
        self.Hb_hb_name.setText(_translate("MainWindow", "Habit Name"))
        self.Hb_hb_desc.setPlainText(_translate("MainWindow", "Describe your Habit......"))
        self.Hb_addhb.setText(_translate("MainWindow", "Add Habit"))
        self.hab_in.setTabText(self.hab_in.indexOf(self.tab_hb), _translate("MainWindow", "Habit"))
        
        cur.execute('select * from hb_hb')
        habsql=cur.fetchall()
        
        for i in range(len(habsql)):
                self.Hbt_select.setItemText(i, _translate("MainWindow", habsql[i][0]))
        
        self.Hbt_Done.setText(_translate("MainWindow", "Mark Done"))
        self.Hbt_remove.setText(_translate("MainWindoe","Delete"))
        self.Del_routine.setText(_translate("MainWindow","Clear Routine"))
        self.Back_btn.setText(_translate("MainWindow", "Back"))
        self.Add.setText(_translate("MainWindow", "+"))
        self.Tk_desc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Task desc...</p></body></html>"))
      
        self.Tk_name.setText(_translate("MainWindow", "Task name..."))
      
        cur.execute('select * from task')
        tasksql=cur.fetchall()
        
        for i in range(len(tasksql)):
                self.Tk_select.setItemText(i, _translate("MainWindow", tasksql[i][0]))
        self.Back_btn_2.setText(_translate("MainWindow", "Back"))
        self.Tk_Done.setText(_translate("MainWindow","Mark as Done"))

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#Yay