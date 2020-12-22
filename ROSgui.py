# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ROSPyQT_Ex.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy, time
from std_msgs.msg import String

from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2

### DECLARING VARIABLES ###
global data, contS, contP, str_contS, str_contP
data=0
contS=0
contP=0
### --- ###

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 229)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Desktop/Despacho_U_M_V0.1/Imagens/dump-truck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 551, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        ### TITLE SUBSCRIBER ###
        self.label_Sub = QtWidgets.QLabel(self.widget)
        self.label_Sub.setObjectName("label_Sub")
        ### --- ###        
        self.horizontalLayout.addWidget(self.label_Sub)
        ### DATA SUBSCRIBED (CHANGE OVER LOOP) ###        
        self.label_Data_Sub = QtWidgets.QLabel(self.widget)
        self.label_Data_Sub.setObjectName("label_Data_Sub")
        ### --- ###        
        self.horizontalLayout.addWidget(self.label_Data_Sub)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        ### TITLE SUBSCRIBER COUNTER ###        
        self.label_ContS = QtWidgets.QLabel(self.widget)
        self.label_ContS.setObjectName("label_ContS")
        ### --- ###        
        self.horizontalLayout_4.addWidget(self.label_ContS)
        ### DATA CONT S (CHANGE OVER LOOP) ###        
        self.label_Data_ContS = QtWidgets.QLabel(self.widget)
        self.label_Data_ContS.setObjectName("label_Data_ContS")
        ### --- ###	
        self.horizontalLayout_4.addWidget(self.label_Data_ContS)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        ### TITLE PUBLISHER ###        
        self.label_Pub = QtWidgets.QLabel(self.widget)
        self.label_Pub.setObjectName("label_Pub")
        ### --- ###        
        self.horizontalLayout_2.addWidget(self.label_Pub)
        ### DATA PUBLISHED (CHANGE OVER TIME) ###
        self.label_Data_Pub = QtWidgets.QLabel(self.widget)
        self.label_Data_Pub.setObjectName("label_Data_Pub")
        ### --- ###        
        self.horizontalLayout_2.addWidget(self.label_Data_Pub)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        ### TITLE PUBLISHER COUNTER ###        
        self.label_ContP = QtWidgets.QLabel(self.widget)
        self.label_ContP.setObjectName("label_ContP")
        ### --- ###
        self.horizontalLayout_3.addWidget(self.label_ContP)
        ### DATA CONT P (CHANGE OVER LOOP) ###        
        self.label_Data_ContP = QtWidgets.QLabel(self.widget)
        self.label_Data_ContP.setObjectName("label_Data_ContP")
        ### --- ###
        self.horizontalLayout_3.addWidget(self.label_Data_ContP)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        ### PUBLISHER BUTTON ###        
        self.pushButton_Pub = QtWidgets.QPushButton(self.widget)
        self.pushButton_Pub.setObjectName("pushButton_Pub")
        ### --- ###        
        self.horizontalLayout_7.addWidget(self.pushButton_Pub)
        ### RESET BUTTON ###        
        self.pushButton_Reset = QtWidgets.QPushButton(self.widget)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        ### --- ###        
        self.horizontalLayout_7.addWidget(self.pushButton_Reset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.bridge = CvBridge()            
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
	### GUI MODIFICATIONS ###
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROS + PyQT GUI Example"))
        self.label.setText(_translate("MainWindow", "ROS + PyQT GUI"))
        self.label_Sub.setText(_translate("MainWindow", "Subscribed data:"))
        self.label_Data_Sub.setText(_translate("MainWindow", "                   No data subscribed"))
        self.label_ContS.setText(_translate("MainWindow", "ContS:"))
        self.label_Data_ContS.setText(_translate("MainWindow", "0"))
        self.label_Pub.setText(_translate("MainWindow", "Published data:"))
        self.label_Data_Pub.setText(_translate("MainWindow", "                      No data published"))
        self.label_ContP.setText(_translate("MainWindow", "ContP:"))
        self.label_Data_ContP.setText(_translate("MainWindow", "0"))
        self.pushButton_Pub.setText(_translate("MainWindow", "Publish"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset"))
	
	### DECLARING FUNCTIONS ###
        self.subCallback(data)
        # self.subImgCb(data)
        self.listener()
        self.pushButton_Reset.clicked.connect(self.reset)
        self.pushButton_Pub.clicked.connect(self.publish)
	
    def subCallback(self,data):
        global contS, str_contS
        contS=contS+1
        str_contS=str(contS)
        text_sub=str(data)
        self.label_Data_Sub.setText(text_sub)
        self.label_Data_ContS.setText(str_contS)
    def subImgCb(self, data):
        # pass
        cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        print(cv_image.shape)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        # cv2.imshow(" test", cv_image)
        # cv2.waitKey(10)

    def listener(self):
        rospy.init_node('ROSgui', anonymous=True)
        rospy.Subscriber('chatter', String, self.subCallback)
        rospy.Subscriber('/usb_cam/image_raw', Image, self.subImgCb)

    def reset(self):
        global contS, contP, str_contS
        contS=0
        contP=0
        str_contS=str(contS)
        str_contP=str(contP)
        self.label_Data_ContS.setText(str_contS)
        self.label_Data_Sub.setText('######')
        self.label_Data_ContP.setText(str_contP)
        self.label_Data_Pub.setText('######')

    def publish(self):
        global contP
        contP=contP+1
        str_contP=str(contP)
        pub=rospy.Publisher('ROSgui_published', String, queue_size=10)
        hello_gui="Hello from GUI"
        pub.publish(hello_gui)
        self.label_Data_ContP.setText(str_contP)
        self.label_Data_Pub.setText(hello_gui)

	
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        sys.exit(app.exec_())

