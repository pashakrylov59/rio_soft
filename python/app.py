"В строках 90, 91, 200 необходимо скорректировать путь для корректной работы программы."

from PyQt5 import QtCore, QtGui, QtWidgets
import re, datetime


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Окно")
        Form.setEnabled(True)
        Form.resize(500, 500)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.label_6.setObjectName("фон")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(65, 450, 93, 28))
        self.pushButton.setObjectName("кнопка старт")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(55, 190, 113, 22))
        self.lineEdit.setObjectName("ввод даты")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(45, 160, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("текст дата")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(45, 220, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("текст шага")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(55, 295, 113, 22))
        self.lineEdit_2.setObjectName("шаг")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 325, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("текст n")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(55, 400, 113, 22))
        self.lineEdit_3.setObjectName("n")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 40, 181, 91))
        self.label_4.setObjectName("логотип")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(210, 160, 256, 261))
        self.listWidget.setObjectName("список для дат")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(35, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("название программы")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 450, 93, 28))
        self.pushButton_2.setObjectName("кнопка сохранить")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Планировщик"))
        self.pushButton.setText(_translate("Form", "Старт"))
        self.label.setText(_translate("Form", "Введите дату:"))
        self.label_2.setText(_translate("Form", "Введите шаг (день, неделя, квартал, год):"))
        self.label_3.setText(_translate("Form", "Введите количество дат (до 1000):"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\"C:/Users/pasha/OneDrive/Рабочий стол/Программа/рио.png\"/></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><img src=\"C:/Users/pasha/OneDrive/Рабочий стол/Программа/fon.png\"/></p></body></html>"))
        self.label_5.setText(_translate("Form", "Планировщик"))
        self.pushButton_2.setText(_translate("Form", "Сохранить"))
        self.pushButton.clicked.connect(self.clickme)
        self.pushButton_2.clicked.connect(self.clicksave)
        self.pushButton_2.clicked.connect(self.show_info_messagebox)

    def clickme(self): #Функция запускает цикл работы с датами при нажатии на кнопку "старт"
        s_day = 0
        s_mon = 0
        s_year = 0
        n = 0
        ndate = datetime.datetime.now()
        ndate = ndate.strftime("%m/%d/%Y %I:%M:%S %p")
        fst_str = 'Планирование, выполненное ' + str(ndate) + ':'
        save_str = [fst_str]
        date = self.lineEdit.text()
        step = self.lineEdit_2.text()
        nn = self.lineEdit_3.text()
        s_date = re.split('[- /.]+', date)       
# Проверка введенной даты        
        if len(s_date) == 3:
            if s_date[0].isdigit():
                s_day = int(s_date[0])
            if s_date[1].isdigit():
                s_mon = int(s_date[1])
            if s_date[2].isdigit():
                s_year = int(s_date[2])
            else:
                self.show_warning_messagebox()
            if s_day > 31 or s_mon > 12 or s_day < 1 or s_mon < 1 or s_year < 1000:
                self.show_warning_messagebox()
        else:
           self.show_warning_messagebox()        
# Проверка числа n
        if len(nn) >= 1 and len(nn) <= 4:
            if nn.isdigit():
                n = int(nn)
            else:
                self.show_warning_messagebox_n()
        else:
            self.show_warning_messagebox_n()
# Запускаем цикл работы с датами           
        if s_mon > 0 and s_year > 0 and s_day > 0 and n > 0 and n <= 1000 and s_mon <= 12 and s_year >= 1000:
            if s_mon == 2:
                if s_year % 4 == 0:
                    if  s_year % 400 == 0 or s_year % 100 != 0 and s_day < 30:
                        self.listWidget.clear()
                        for i in range(n):
                            date = self.date_operations(date, step)
                            date = self.sunday_saturday_definer(date)
                            save_str.append(str(date))
                            self.listWidget.addItem(str(date))
                            self.pushButton_2.setEnabled(True)
                    elif s_day < 29:
                        self.listWidget.clear()
                        for i in range(n):
                            date = self.date_operations(date, step)
                            date = self.sunday_saturday_definer(date)
                            save_str.append(str(date))
                            self.listWidget.addItem(str(date))
                            self.pushButton_2.setEnabled(True)
                    else:
                        self.show_warning_messagebox()
                elif s_day < 29:
                    self.listWidget.clear()
                    for i in range(n):
                        date = self.date_operations(date, step)
                        date = self.sunday_saturday_definer(date)
                        save_str.append(str(date))
                        self.listWidget.addItem(str(date))
                        self.pushButton_2.setEnabled(True) 
                else:
                    self.show_warning_messagebox()
            elif s_mon in [4, 6, 9, 11]:
                if s_day < 31:
                    self.listWidget.clear()
                    for i in range(n):
                        date = self.date_operations(date, step)
                        date = self.sunday_saturday_definer(date)
                        save_str.append(str(date))
                        self.listWidget.addItem(str(date))
                        self.pushButton_2.setEnabled(True)
                else:
                    self.show_warning_messagebox()
            elif s_day < 32:
                self.listWidget.clear()
                for i in range(n):
                    date = self.date_operations(date, step)
                    date = self.sunday_saturday_definer(date)
                    save_str.append(str(date))
                    self.listWidget.addItem(str(date)) 
                    self.pushButton_2.setEnabled(True) 
            else:
                self.show_warning_messagebox()
        return save_str


    def show_warning_messagebox(self): #Функция выдает ошибку при вводе некорректного значения в поле даты
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("В поле ввода даты введено некорректное значение!")
        self.msg.setWindowTitle("Ошибка")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = self.msg.exec_()
        
        
    def clicksave(self, save_str): #Функция записи дат из приложения при нажатии на кнопку "сохранить"
        strr = (self.clickme())
        my_file = open(r"C:\Users\pasha\OneDrive\Рабочий стол\Программа\result_date.txt", "a+")
        for i in range (len(strr)):
            my_file.write(strr[i] + '\n')
        my_file.close()
        
        
        
    def show_warning_messagebox_n(self): #Функция выдает ошибку при вводе некорректного значения в поле n
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("В поле ввода количества дат введено некорректное значение!")
        self.msg.setWindowTitle("Ошибка")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = self.msg.exec_()
        
        
    def show_info_messagebox(self): #Функция выдает сообщение о сохранении данных
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setText("Сохранение выполнено успешно.")
        self.msg.setWindowTitle("Готово")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.pushButton_2.setDisabled(True)
        retval = self.msg.exec_()
        
        
    def sunday_saturday_definer(self, date): #Функция заменяет дату выходного дня на предшествующую пятницу
        date_string = str(date)
        s = re.split('[- /.]+', date_string)
        year=int(s[0])
        mon=int(s[1])
        day=int(s[2])
        date_for_checking = datetime.datetime(day = day, month = mon, year = year)
        if date_for_checking.weekday() == 5:
            if day == 1:
                if mon == 3:
                    if year % 4 == 0:
                        if  year % 400 == 0 or year % 100 != 0:
                            day = 29
                            mon -= 1
                        else:
                            day = 28
                            mon -= 1
                    else:
                        day = 28
                        mon -= 1
                elif mon in [5, 7, 10, 12]:
                    day = 30
                    mon -= 1
                elif mon == 1:
                    day = 31
                    year -= 1
                    mon = 12
                else:
                    day = 31
                    mon -= 1
            else:
                day -= 1
            if mon < 10:
                mon = '0'+str(mon)
            if day < 10:
                day = '0'+str(day)
            date = str(day) + '.' + str(mon) + '.' + str(year)
            return date
        
        elif date_for_checking.weekday() == 6:
            if day == 1:
                if mon == 3:
                    if year % 4 == 0:
                        if  year % 400 == 0 or year % 100 != 0:
                            day = 28
                            mon -= 1
                        else:
                            day = 27
                            mon -= 1
                    else:
                        day = 27
                        mon -= 1
                elif mon in [5, 7, 10, 12]:
                    day = 29
                    mon -= 1
                elif mon == 1:
                    day = 30
                    year -= 1
                    mon = 12
                else:
                    day = 30
                    mon -= 1
            elif day == 2:
                if mon == 3:
                    if year % 4 == 0:
                        if  year % 400 == 0 or year % 100 != 0:
                            day = 29
                            mon -= 1
                        else:
                            day = 28
                            mon -= 1
                    else:
                        day = 28
                        mon -= 1
                elif mon in [5, 7, 10, 12]:
                    day = 30
                    mon -= 1
                elif mon == 1:
                    day = 31
                    year -= 1
                    mon = 12
                else:
                    day = 31
                    mon -= 1
            else:
                day -= 2
            if mon < 10:
                mon = '0'+str(mon)
            if day < 10:
                day = '0'+str(day)
            date = str(day) + '.' + str(mon) + '.' + str(year)
            return date
        else:
            if mon < 10:
                mon = '0'+str(mon)
            if day < 10:
                day = '0'+str(day)
            date = str(day) + '.' + str(mon) + '.' + str(year)
            return date
        
        
    def date_operations(self, date, step): #Функция проводит манипуляции с датой в зависимости от шага
        s = re.split('[- /.]+', date)
        day=int(s[0])
        mon=int(s[1])
        year=int(s[2])
        if (step.lower() == 'день'):
            if mon == 2: #февраль
        #Проверяем високосность года
                if year % 4 == 0:
                    if  year % 400 == 0 or year % 100 != 0 and day < 30:
                        if day == 29:
                            day = 1
                            mon += 1
                        else:
                            day += 1
                    elif day < 29:
                        if day == 28:
                            day = 1
                            mon += 1
                        else:
                            day += 1
                elif day < 29:
                    if day == 28:
                        day = 1
                        mon += 1
                    else:
                        day += 1
            elif mon == 12 and day == 31:#31 Декабря
                day = 1
                mon = 1
                year += 1
        #Апрель, июнь, сентябрь, ноябрь
            elif mon in [4, 6, 9, 11] and day < 31:
                if day == 30:
                    day = 1
                    mon += 1
                else:
                    day += 1
            else:
                if day == 31:
                    day = 1
                    mon += 1
                else:
                    day += 1
            if mon < 10:
                    mon = '0'+str(mon)
            if day < 10:
                    day = '0'+str(day)
            date = str(day) + str(mon) + str(year)
            date = (datetime.datetime.strptime(date, '%d%m%Y').date())
            return date
               
                    
        #Вычисляем дату, если step = week
        elif (step.lower() == 'неделя'):
            if mon == 2: #февраль
        #Проверяем високосность года
                if year % 4 == 0:
                    if  year % 400 == 0 or year % 100 != 0 and day < 30:
                        if day > 22:
                            day -= 22
                            mon += 1
                        else:
                            day += 7
                    elif day < 29:
                        if day > 21:
                            day -= 21
                            mon += 1
                        else:
                            day += 7
                else:
                    if day > 21:
                        day -= 21
                        mon += 1
                    else:
                        day += 7
            elif mon == 12 and day > 24 and day < 32:#Декабрь
                day -= 24
                mon = 1
                year += 1
            elif mon in [4, 6, 9, 11] and day < 31:
                if day > 23:
                    day -= 23
                    mon += 1
                else:
                    day += 7
            else:
                if day > 24:
                    day -= 24
                    mon += 1
                else:
                    day += 7
            if mon < 10:
                    mon = '0'+str(mon)
            if day < 10:
                    day = '0'+str(day)
            date = str(day) + str(mon) + str(year)
            date = (datetime.datetime.strptime(date, '%d%m%Y').date())
            return date


        #Вычисляем дату, если step = quarter. Будем считать, что если искомая дата в 1 квартале,
        #то к ней добавляется 90(91 если високосный) дней. 2-й квартал +91 день. 3-й квартал +92 дня. 4-й квартал +92 дня.
        elif (step.lower() == 'квартал'):
            if mon in [1, 2, 3]:
        #Проверяем високосность года
                if year % 4 == 0:
                    if  year % 400 == 0 or year % 100 != 0 and day < 30:
                        q_day = 91
                        while q_day > 0:
                            if mon == 2:
                                while day != 29 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                            elif mon in [4, 6, 9, 11]:
                                while day != 30 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                            else:
                                while day != 31 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if mon != 12 and q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                                else:
                                    if q_day > 0:
                                        mon += 1
                                        day = 1
                                        q_day -= 1
                    else:
                        q_day = 90
                        while q_day > 0:
                            if mon == 2:
                                while day != 28 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                            elif mon in [4, 6, 9, 11]:
                                while day != 30 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                            else:
                                while day != 31 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                else:
                    q_day = 90
                    while q_day > 0:
                        if mon == 2:
                            while day != 28 and q_day > 0:
                                q_day -= 1
                                day += 1
                            if q_day > 0:
                                mon += 1
                                day = 1
                                q_day -= 1
                        elif mon in [4, 6, 9, 11]:
                            while day != 30 and q_day > 0:
                                q_day -= 1
                                day += 1
                            if q_day > 0:
                                mon += 1
                                day = 1
                                q_day -= 1
                        else:
                            while day != 31 and q_day > 0:
                                q_day -= 1
                                day += 1
                            if q_day > 0:
                                mon += 1
                                day = 1
                                q_day -= 1
                                
            elif mon in [4, 5, 6]:
                q_day = 91
                while q_day > 0:
                    if mon in [4, 6, 9, 11]:
                        while day != 30 and q_day > 0:
                            q_day -= 1
                            day += 1
                        if q_day > 0:
                            mon += 1
                            day = 1
                            q_day -= 1
                    elif q_day > 0:
                        while day != 31 and q_day > 0:
                            q_day -= 1
                            day += 1
                        if q_day > 0:
                            mon += 1
                            day = 1
                            q_day -= 1
                            
            else:
                q_day = 92
                while q_day > 0:
                    if mon == 2:
                        if year % 4 == 0:
                            if  year % 400 == 0 or year % 100 != 0 and day < 30:
                                while day != 29 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                            else:
                                while day != 28 and q_day > 0:
                                    q_day -= 1
                                    day += 1
                                if q_day > 0:
                                    mon += 1
                                    day = 1
                                    q_day -= 1
                        else:
                            while day != 28 and q_day > 0:
                                q_day -= 1
                                day += 1
                            if q_day > 0:
                                mon += 1
                                day = 1
                                q_day -= 1
                    elif mon in [4, 6, 9, 11]:
                        while day != 30 and q_day > 0:
                            q_day -= 1
                            day += 1
                        if q_day > 0:
                            mon += 1
                            day = 1
                            q_day -= 1
                    else:
                        while day != 31 and q_day > 0:
                            q_day -= 1
                            day += 1
                        if mon != 12 and q_day > 0:
                            mon += 1
                            day = 1
                            q_day -= 1
                        else:
                            if q_day > 0:
                                mon = 1
                                day = 1
                                q_day -= 1
                                year += 1
            if mon < 10:
                mon = '0'+str(mon)
            if day < 10:
                day = '0'+str(day)
            date = str(day) + str(mon) + str(year)
            date = (datetime.datetime.strptime(date, '%d%m%Y').date())
            return date


        elif (step.lower() == 'год'):
            if mon == 2:
                if year % 4 == 0:
                    if  year % 400 == 0 or year % 100 != 0:
                        day = 1
                        mon = 3
            year += 1
            if mon < 10:
                mon = '0'+str(mon)
            if day < 10:
                day = '0'+str(day)
            date = str(day) + str(mon) + str(year)
            date = (datetime.datetime.strptime(date, '%d%m%Y').date())
            return date
            

        else:
            if mon < 10:
                mon = '0'+str(mon)
            if day < 10:
                day = '0'+str(day)
            date = str(day) + str(mon) + str(year)
            date = (datetime.datetime.strptime(date, '%d%m%Y').date())
            return date


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
