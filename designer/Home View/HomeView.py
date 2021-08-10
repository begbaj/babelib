# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\HomeView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(760, 850)
        Home.setMinimumSize(QtCore.QSize(760, 850))
        Home.setMaximumSize(QtCore.QSize(760, 850))
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.newreservButton = QtWidgets.QPushButton(self.centralwidget)
        self.newreservButton.setGeometry(QtCore.QRect(220, 680, 241, 51))
        self.newreservButton.setAutoFillBackground(False)
        self.newreservButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 14pt \"Source Code Pro for Powerline\";\n"
"border-radius:15px;\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 54, 65, 255), stop:1 rgba(56, 54, 65, 130))")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/Icona Prenotazione.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newreservButton.setIcon(icon)
        self.newreservButton.setIconSize(QtCore.QSize(36, 36))
        self.newreservButton.setObjectName("newreservButton")
        self.newuserButton = QtWidgets.QPushButton(self.centralwidget)
        self.newuserButton.setGeometry(QtCore.QRect(480, 680, 241, 51))
        self.newuserButton.setStyleSheet("background-color: rgb(27, 25, 39);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"Source Code Pro for Powerline\";\n"
"border-radius:15px;\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 54, 65, 255), stop:1 rgba(56, 54, 65, 130))")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\images/Icona User.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newuserButton.setIcon(icon1)
        self.newuserButton.setIconSize(QtCore.QSize(32, 32))
        self.newuserButton.setObjectName("newuserButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 30, 501, 621))
        self.frame.setStyleSheet("border-radius: 20px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color:rgb(27,25,39);\n"
"background-color:rgba(0, 192, 225, 85)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.service_reservation_calendar_widget = QtWidgets.QCalendarWidget(self.frame)
        self.service_reservation_calendar_widget.setGeometry(QtCore.QRect(24, 47, 451, 241))
        self.service_reservation_calendar_widget.setTabletTracking(False)
        self.service_reservation_calendar_widget.setAccessibleName("")
        self.service_reservation_calendar_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.service_reservation_calendar_widget.setAutoFillBackground(False)
        self.service_reservation_calendar_widget.setStyleSheet("background-color: rgb(46, 44, 55);\n"
"color:rgb(22, 162, 208);\n"
"selection-background-color: rgb(27, 213, 241);\n"
"border:none;")
        self.service_reservation_calendar_widget.setGridVisible(False)
        self.service_reservation_calendar_widget.setNavigationBarVisible(True)
        self.service_reservation_calendar_widget.setObjectName("service_reservation_calendar_widget")
        self.main_tab_widget = QtWidgets.QTabWidget(self.frame)
        self.main_tab_widget.setGeometry(QtCore.QRect(20, 310, 461, 291))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.main_tab_widget.setFont(font)
        self.main_tab_widget.setStyleSheet("font-size: 13pt;\n"
"color:rgb(20, 19, 28,255);\n"
"background-color: transparent;\n"
"border:none;")
        self.main_tab_widget.setObjectName("main_tab_widget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.reservation_table_widget = QtWidgets.QTableWidget(self.tab_3)
        self.reservation_table_widget.setEnabled(True)
        self.reservation_table_widget.setGeometry(QtCore.QRect(0, 0, 461, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.reservation_table_widget.sizePolicy().hasHeightForWidth())
        self.reservation_table_widget.setSizePolicy(sizePolicy)
        self.reservation_table_widget.setMinimumSize(QtCore.QSize(100, 200))
        self.reservation_table_widget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro for Powerline")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reservation_table_widget.setFont(font)
        self.reservation_table_widget.setTabletTracking(False)
        self.reservation_table_widget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.reservation_table_widget.setStyleSheet("background-color: rgb(27, 25, 39);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"Source Code Pro for Powerline\";\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 54, 65, 255), stop:1 rgba(56, 54, 65, 130));\n"
"qproperty-alignment: \'AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"alternate-background-color: rgb(27, 213, 241,190);\n"
"border:none;\n"
"border-radius:10px;")
        self.reservation_table_widget.setLineWidth(1)
        self.reservation_table_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.reservation_table_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.reservation_table_widget.setAlternatingRowColors(True)
        self.reservation_table_widget.setRowCount(5)
        self.reservation_table_widget.setObjectName("reservation_table_widget")
        self.reservation_table_widget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.reservation_table_widget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget.setItem(4, 0, item)
        self.reservation_table_widget.horizontalHeader().setVisible(False)
        self.reservation_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.reservation_table_widget.horizontalHeader().setDefaultSectionSize(120)
        self.reservation_table_widget.horizontalHeader().setHighlightSections(False)
        self.reservation_table_widget.horizontalHeader().setMinimumSectionSize(30)
        self.reservation_table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.reservation_table_widget.horizontalHeader().setStretchLastSection(True)
        self.reservation_table_widget.verticalHeader().setVisible(False)
        self.reservation_table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.reservation_table_widget.verticalHeader().setHighlightSections(True)
        self.reservation_table_widget.verticalHeader().setSortIndicatorShown(False)
        self.reservation_table_widget.verticalHeader().setStretchLastSection(False)
        self.main_tab_widget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.reservation_table_widget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.reservation_table_widget_2.setEnabled(True)
        self.reservation_table_widget_2.setGeometry(QtCore.QRect(0, 0, 461, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.reservation_table_widget_2.sizePolicy().hasHeightForWidth())
        self.reservation_table_widget_2.setSizePolicy(sizePolicy)
        self.reservation_table_widget_2.setMinimumSize(QtCore.QSize(100, 200))
        self.reservation_table_widget_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.reservation_table_widget_2.setTabletTracking(False)
        self.reservation_table_widget_2.setStyleSheet("background-color: rgb(27, 25, 39);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"Source Code Pro for Powerline\";\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 54, 65, 255), stop:1 rgba(56, 54, 65, 130));\n"
"qproperty-alignment: \'AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"alternate-background-color: rgb(27, 213, 241,190);\n"
"border:none;\n"
"border-radius:10px;")
        self.reservation_table_widget_2.setLineWidth(1)
        self.reservation_table_widget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.reservation_table_widget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.reservation_table_widget_2.setAlternatingRowColors(True)
        self.reservation_table_widget_2.setRowCount(4)
        self.reservation_table_widget_2.setObjectName("reservation_table_widget_2")
        self.reservation_table_widget_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.reservation_table_widget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_2.setItem(1, 0, item)
        self.reservation_table_widget_2.horizontalHeader().setVisible(False)
        self.reservation_table_widget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.reservation_table_widget_2.horizontalHeader().setDefaultSectionSize(120)
        self.reservation_table_widget_2.horizontalHeader().setHighlightSections(False)
        self.reservation_table_widget_2.horizontalHeader().setMinimumSectionSize(30)
        self.reservation_table_widget_2.horizontalHeader().setSortIndicatorShown(False)
        self.reservation_table_widget_2.horizontalHeader().setStretchLastSection(True)
        self.reservation_table_widget_2.verticalHeader().setVisible(False)
        self.reservation_table_widget_2.verticalHeader().setCascadingSectionResizes(False)
        self.reservation_table_widget_2.verticalHeader().setHighlightSections(True)
        self.reservation_table_widget_2.verticalHeader().setSortIndicatorShown(False)
        self.reservation_table_widget_2.verticalHeader().setStretchLastSection(False)
        self.main_tab_widget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.reservation_table_widget_3 = QtWidgets.QTableWidget(self.tab_5)
        self.reservation_table_widget_3.setEnabled(True)
        self.reservation_table_widget_3.setGeometry(QtCore.QRect(0, 0, 461, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.reservation_table_widget_3.sizePolicy().hasHeightForWidth())
        self.reservation_table_widget_3.setSizePolicy(sizePolicy)
        self.reservation_table_widget_3.setMinimumSize(QtCore.QSize(100, 200))
        self.reservation_table_widget_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.reservation_table_widget_3.setTabletTracking(False)
        self.reservation_table_widget_3.setStyleSheet("background-color: rgb(27, 25, 39);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"Source Code Pro for Powerline\";\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 54, 65, 255), stop:1 rgba(56, 54, 65, 130));\n"
"qproperty-alignment: \'AlignLeft\';\n"
"qproperty-wordWrap: true;\n"
"alternate-background-color: rgb(27, 213, 241,190);\n"
"border:none;\n"
"border-radius:10px;")
        self.reservation_table_widget_3.setLineWidth(1)
        self.reservation_table_widget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.reservation_table_widget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.reservation_table_widget_3.setAlternatingRowColors(True)
        self.reservation_table_widget_3.setRowCount(4)
        self.reservation_table_widget_3.setObjectName("reservation_table_widget_3")
        self.reservation_table_widget_3.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.reservation_table_widget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.reservation_table_widget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation_table_widget_3.setItem(3, 0, item)
        self.reservation_table_widget_3.horizontalHeader().setVisible(False)
        self.reservation_table_widget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.reservation_table_widget_3.horizontalHeader().setDefaultSectionSize(120)
        self.reservation_table_widget_3.horizontalHeader().setHighlightSections(False)
        self.reservation_table_widget_3.horizontalHeader().setMinimumSectionSize(30)
        self.reservation_table_widget_3.horizontalHeader().setSortIndicatorShown(False)
        self.reservation_table_widget_3.horizontalHeader().setStretchLastSection(True)
        self.reservation_table_widget_3.verticalHeader().setVisible(False)
        self.reservation_table_widget_3.verticalHeader().setCascadingSectionResizes(False)
        self.reservation_table_widget_3.verticalHeader().setHighlightSections(True)
        self.reservation_table_widget_3.verticalHeader().setSortIndicatorShown(False)
        self.reservation_table_widget_3.verticalHeader().setStretchLastSection(False)
        self.main_tab_widget.addTab(self.tab_5, "")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 17, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"background-color:transparent;")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 7, 41, 31))
        self.label_5.setStyleSheet("border:none;\n"
"background-color:transparent;")
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setPixmap(QtGui.QPixmap(".\\images/Calendario.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 201, 831))
        self.frame_2.setStyleSheet("border:none;\n"
"background-color:qlineargradient(spread:pad, x1:0.83936, y1:0, x2:1, y2:0, stop:0 rgba(32, 30, 39, 255), stop:0.571429 rgba(0, 178, 210, 48));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.serviceButton = QtWidgets.QPushButton(self.frame_2)
        self.serviceButton.setGeometry(QtCore.QRect(50, 620, 81, 51))
        self.serviceButton.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.499926, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(18, 125, 160, 249), stop:1 rgba(27, 213, 241, 241));\n"
"border-radius:16px;\n"
"")
        self.serviceButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\images/Icona Servizi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.serviceButton.setIcon(icon2)
        self.serviceButton.setIconSize(QtCore.QSize(40, 40))
        self.serviceButton.setObjectName("serviceButton")
        self.userButton = QtWidgets.QPushButton(self.frame_2)
        self.userButton.setGeometry(QtCore.QRect(50, 300, 81, 51))
        self.userButton.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.499926, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(18, 125, 160, 249), stop:1 rgba(27, 213, 241, 241));\n"
"border-radius:16px;")
        self.userButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\images/Icona Utenti.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon3)
        self.userButton.setIconSize(QtCore.QSize(40, 40))
        self.userButton.setObjectName("userButton")
        self.commButton = QtWidgets.QPushButton(self.frame_2)
        self.commButton.setGeometry(QtCore.QRect(50, 380, 81, 51))
        self.commButton.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.499926, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(18, 125, 160, 249), stop:1 rgba(27, 213, 241, 241));\n"
"border-radius:16px;")
        self.commButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\images/Icona Comunicazioni.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commButton.setIcon(icon4)
        self.commButton.setIconSize(QtCore.QSize(40, 40))
        self.commButton.setObjectName("commButton")
        self.statsButton = QtWidgets.QPushButton(self.frame_2)
        self.statsButton.setGeometry(QtCore.QRect(50, 460, 81, 51))
        self.statsButton.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.499926, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(18, 125, 160, 249), stop:1 rgba(27, 213, 241, 241));\n"
"border-radius:16px;")
        self.statsButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\images/Icona Statistiche.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statsButton.setIcon(icon5)
        self.statsButton.setIconSize(QtCore.QSize(40, 40))
        self.statsButton.setObjectName("statsButton")
        self.catolgingButton = QtWidgets.QPushButton(self.frame_2)
        self.catolgingButton.setGeometry(QtCore.QRect(50, 220, 81, 51))
        self.catolgingButton.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.499926, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(18, 125, 160, 249), stop:1 rgba(27, 213, 241, 241));\n"
"border-radius:16px;")
        self.catolgingButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\images/Icona Catalogazione.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.catolgingButton.setIcon(icon6)
        self.catolgingButton.setIconSize(QtCore.QSize(40, 40))
        self.catolgingButton.setObjectName("catolgingButton")
        self.labelicon = QtWidgets.QLabel(self.frame_2)
        self.labelicon.setGeometry(QtCore.QRect(44, 20, 91, 81))
        self.labelicon.setStyleSheet("background-color:transparent;")
        self.labelicon.setText("")
        self.labelicon.setTextFormat(QtCore.Qt.RichText)
        self.labelicon.setPixmap(QtGui.QPixmap(".\\../img/Babelib.icns"))
        self.labelicon.setScaledContents(True)
        self.labelicon.setObjectName("labelicon")
        self.movementButton = QtWidgets.QPushButton(self.frame_2)
        self.movementButton.setGeometry(QtCore.QRect(50, 140, 81, 51))
        self.movementButton.setStyleSheet("border-radius:16px;\n"
"background-color:qradialgradient(spread:pad, cx:0.499926, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(18, 125, 160, 249), stop:1 rgba(27, 213, 241, 241));")
        self.movementButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\images/Icona Movimenti.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.movementButton.setIcon(icon7)
        self.movementButton.setIconSize(QtCore.QSize(40, 40))
        self.movementButton.setObjectName("movementButton")
        self.reportButton = QtWidgets.QPushButton(self.frame_2)
        self.reportButton.setGeometry(QtCore.QRect(50, 540, 81, 51))
        self.reportButton.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.499926, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(18, 125, 160, 249), stop:1 rgba(27, 213, 241, 241));\n"
"border-radius:16px;")
        self.reportButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\images/Icona Report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reportButton.setIcon(icon8)
        self.reportButton.setIconSize(QtCore.QSize(40, 40))
        self.reportButton.setObjectName("reportButton")
        self.settingButton = QtWidgets.QPushButton(self.frame_2)
        self.settingButton.setGeometry(QtCore.QRect(60, 740, 71, 51))
        self.settingButton.setStyleSheet("background-color:transparent;")
        self.settingButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(".\\images/Icona Impostazioni.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingButton.setIcon(icon9)
        self.settingButton.setIconSize(QtCore.QSize(40, 40))
        self.settingButton.setObjectName("settingButton")
        self.newloanButton = QtWidgets.QPushButton(self.centralwidget)
        self.newloanButton.setGeometry(QtCore.QRect(350, 750, 241, 51))
        self.newloanButton.setStyleSheet("background-color: rgb(27, 25, 39);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"Source Code Pro for Powerline\";\n"
"border-radius:15px;\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 54, 65, 255), stop:1 rgba(56, 54, 65, 130));\n"
"qproperty-alignment: \'AlignLeft\';\n"
"qproperty-wordWrap: true;")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(".\\images/Icona Prestito.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newloanButton.setIcon(icon10)
        self.newloanButton.setIconSize(QtCore.QSize(40, 40))
        self.newloanButton.setObjectName("newloanButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 0, 1201, 1001))
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setPixmap(QtGui.QPixmap(".\\../img/background_blur.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.frame.raise_()
        self.newreservButton.raise_()
        self.newuserButton.raise_()
        self.frame_2.raise_()
        self.newloanButton.raise_()
        Home.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)
        self.actionModifica = QtWidgets.QAction(Home)
        self.actionModifica.setObjectName("actionModifica")

        self.retranslateUi(Home)
        self.main_tab_widget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Babelib"))
        self.newreservButton.setText(_translate("Home", "Nuova Prenotazione"))
        self.newuserButton.setText(_translate("Home", "Registra Utente"))
        item = self.reservation_table_widget.verticalHeaderItem(0)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget.verticalHeaderItem(1)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget.verticalHeaderItem(2)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget.verticalHeaderItem(3)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget.verticalHeaderItem(4)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Home", "Nome"))
        item = self.reservation_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("Home", "Data"))
        item = self.reservation_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("Home", "Fascia Oraria"))
        item = self.reservation_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("Home", "Posto"))
        __sortingEnabled = self.reservation_table_widget.isSortingEnabled()
        self.reservation_table_widget.setSortingEnabled(False)
        self.reservation_table_widget.setSortingEnabled(__sortingEnabled)
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_3), _translate("Home", "Prenotazioni"))
        item = self.reservation_table_widget_2.verticalHeaderItem(0)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_2.verticalHeaderItem(1)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_2.verticalHeaderItem(2)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_2.verticalHeaderItem(3)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_2.horizontalHeaderItem(0)
        item.setText(_translate("Home", "Movimento"))
        item = self.reservation_table_widget_2.horizontalHeaderItem(1)
        item.setText(_translate("Home", "Utente"))
        item = self.reservation_table_widget_2.horizontalHeaderItem(2)
        item.setText(_translate("Home", "Documento"))
        __sortingEnabled = self.reservation_table_widget_2.isSortingEnabled()
        self.reservation_table_widget_2.setSortingEnabled(False)
        self.reservation_table_widget_2.setSortingEnabled(__sortingEnabled)
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_4), _translate("Home", "Movimenti"))
        item = self.reservation_table_widget_3.verticalHeaderItem(0)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_3.verticalHeaderItem(1)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_3.verticalHeaderItem(2)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_3.verticalHeaderItem(3)
        item.setText(_translate("Home", "New Row"))
        item = self.reservation_table_widget_3.horizontalHeaderItem(0)
        item.setText(_translate("Home", "Utente"))
        item = self.reservation_table_widget_3.horizontalHeaderItem(1)
        item.setText(_translate("Home", "Documento"))
        item = self.reservation_table_widget_3.horizontalHeaderItem(2)
        item.setText(_translate("Home", "Prorogato"))
        __sortingEnabled = self.reservation_table_widget_3.isSortingEnabled()
        self.reservation_table_widget_3.setSortingEnabled(False)
        self.reservation_table_widget_3.setSortingEnabled(__sortingEnabled)
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_5), _translate("Home", "Scadenze"))
        self.label.setText(_translate("Home", "Calendario"))
        self.newloanButton.setText(_translate("Home", "Nuovo Prestito"))
        self.actionModifica.setText(_translate("Home", "Modifica"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())