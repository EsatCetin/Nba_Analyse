import sys
from NbaAnalyseU import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QInputDialog,QTableWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit,QMessageBox
from Nba_analyse import statistic
import matplotlib.pyplot as plt
import matplotlib as mp
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.analiz=statistic()
        self.adress="C:/Users/HP/Desktop/Python Projects/Python_Projeler/Nba/TeamLogos/"
        teamlist=["Atlanta Hawks","Boston Celtics","Brooklyn Nets","Charlotte Hornets","Chicago Bulls","Cleveland Cavaliers","Dallas Mavericks","Denver Nuggets","Detroit Pistons","Golden State Warriors" ,"Houston Rockets", "Indiana Pacers", "Los Angeles Clippers","Los Angeles Lakers","Memphis Grizzlies","Miami Heat", "Milwaukee Bucks","Minnesota Timberwolves", "New Orleans Pelicans","New York Knicks", "Oklohama City Thunder","Orlando Magic", "Philadelphia 76ers","Phoenix Suns","Portland Trail Blazers", "Sacramento Kings","San Antonio Spurs","Toronto Raptors","Utah Jazz","Washington Wizards"]
        self.ui.NbaLogo.setPixmap(QtGui.QPixmap(self.adress+"Nba"+".png"))
        self.ui.comboBox.addItems(teamlist)
        self.ui.comboBox_2.addItems(teamlist)
        self.ui.comboBox.activated.connect(self.getLogoHome)
        self.ui.comboBox_2.activated.connect(self.getLogoAway)
        self.ui.pushButton.clicked.connect(self.analyse)
        self.ui.radioButton_2.toggled.emit
    def addlabel(self,x,y):
      r=x.columns.tolist()
      for column in r:
       a=x[column].values.tolist()
       print(a,r)
       l=0
       for i in a:
        self.axes[y].text(l,i,str("{0:.2f}".format(i)))
        l=l+1
    def analyse(self):
        if self.ui.radioButton.isChecked():
         Team1=str(self.ui.comboBox_2.currentText()).split()
         Team2=str(self.ui.comboBox.currentText()).split()
         a=self.analiz.teamcompares(Team1[-1],Team2[-1])
         #print(a[0].values.tolist())
         b=a[0].values.tolist()
         c=a[0].columns.tolist()
         b2=a[1].values.tolist()
         r1=a[2].values.tolist()
         r2=a[3].values.tolist()
         #print(c,r1,r2,b2)
         self.ui.label.setText("HOME\n\n"+"Average point\n"+str("{0:.2f}".format(b[0][0]))+"\nMax point\n"+str(b[0][1])+"\nMin point\n"+str(b[0][2])+"\nWinning Rate\n"+str("{0:.2f}".format(r1[0])))
         self.ui.label_2.setText("AWAY\n\n"+"Average point\n"+str("{0:.2f}".format(b2[0][0]))+"\nMax point\n"+str(b2[0][1])+"\nMin point\n"+str(b2[0][2])+"\nWinning Rate\n"+str("{0:.2f}".format(r2[0])))
         #print(a)
        elif self.ui.radioButton_4.isChecked(): 
         Team1=str(self.ui.comboBox_2.currentText()).split()
         Team2=str(self.ui.comboBox.currentText()).split()
         #For Home Team Analyse:
         Team1A=self.analiz.teamstatslastmatches(Team2[-1])
         Team1AV=[]
         Team2AV=[]
         for i in range(len(Team1A[0].index)):
          Team1AV=Team1AV+Team1A[0].values[i].tolist()
         for i in range(len(Team1A[1].index)):
          Team2AV=Team2AV+Team1A[1].values[i].tolist()
         #Team1AV[1]=Team1A[0].columns.tolist()
         self.ui.label.setText("Away Games\n"+"Mean"+" "+str("{0:.2f}".format(Team1AV[0]))+"\nMax "+str("{0:.2f}".format(Team1AV[1]))+"\nMin "+str("{0:.2f}".format(Team1AV[2]))+"\nStd.Dev. "+str("{0:.2f}".format(Team1AV[3]))+"\nWinning Rate"+" "+str("{0:.2f}".format(Team1A[4]))+"\nHome Games\n"+"Mean"+" "+str("{0:.2f}".format(Team2AV[0]))+"\nMax "+str("{0:.2f}".format(Team2AV[1]))+"\nMin "+str("{0:.2f}".format(Team2AV[2]))+"\nStd.Dev. "+str("{0:.2f}".format(Team2AV[3]))+"\nWinning Rate"+" "+str("{0:.2f}".format(Team1A[2])))
         #print(Team1A[5],Team1A[6],Team1A[7])
         #For Away Team Analyse:
         Team2A=self.analiz.teamstatslastmatches(Team1[-1])
         Team1AV=[]
         Team2AV=[]
         for i in range(len(Team2A[0].index)):
          Team1AV=Team1AV+Team2A[0].values[i].tolist()
         for i in range(len(Team2A[1].index)):
          Team2AV=Team2AV+Team2A[1].values[i].tolist()
         #Team1AV[1]=Team1A[0].columns.tolist()
         self.ui.label_2.setText("Away Games\n"+"Mean"+" "+str("{0:.2f}".format(Team1AV[0]))+"\nMax "+str("{0:.2f}".format(Team1AV[1]))+"\nMin "+str("{0:.2f}".format(Team1AV[2]))+"\nStd.Dev. "+str("{0:.2f}".format(Team1AV[3]))+"\nWinning Rate"+" "+str("{0:.2f}".format(Team2A[4]))+"\nHome Games\n"+"Mean"+" "+str("{0:.2f}".format(Team2AV[0]))+"\nMax "+str("{0:.2f}".format(Team2AV[1]))+"\nMin "+str("{0:.2f}".format(Team2AV[2]))+"\nStd.Dev. "+str("{0:.2f}".format(Team2AV[3]))+"\nWinning Rate"+" "+str("{0:.2f}".format(Team2A[2])))
         #print(Team2A[5],Team2A[6],Team2A[7],Team2A)
        elif self.ui.radioButton_3.isChecked():
         Team1=str(self.ui.comboBox_2.currentText()).split()
         Team2=str(self.ui.comboBox.currentText()).split()
         dfA=self.analiz.bymonthperformance(Team1[-1],Team2[-1])
         s=" "
         print(dfA[0].index)
         fig,self.axes=plt.subplots(nrows=2,ncols=1)
         #dfA[0].plot(kind="line",marker="o",title=f"{s.join(Team2)} Monthly Performance")
         dfA[0].plot(ax=self.axes[0],kind="line",title=f"{s.join(Team2)} Monthly Performance",figsize=(13,7))
         self.axes[0].legend(loc="center right", ncols=3)
         self.addlabel(dfA[0],0)
         
        #  self.ui.label.setText(mp.pyplot.show())
         #mp.pyplot.show()
         #dfA[1].plot(kind="line",marker="o",title=f"{s.join(Team1)} Monthly Performance")
         dfA[1].plot(ax=self.axes[1],kind="line",title=f"{s.join(Team1)} Monthly Performance",figsize=(13,7))
         self.axes[1].legend(loc="center right", ncols=3)
         self.addlabel(dfA[1],1)
         plt.tight_layout()
         plt.show()
        elif self.ui.radioButton_2.isChecked():
         Team2=str(self.ui.comboBox_2.currentText()).split()
         Team1=str(self.ui.comboBox.currentText()).split()
         dfA=self.analiz.rbanalyse(Team2[-1])
         AwayTeamA=dfA[0].values.tolist()
         HomeTeamA=dfA[1].values.tolist()
         #print(AwayTeamA,HomeTeamA)
         self.ui.label_2.setText("Offensive Rebounds\n"+"Mean"+" "+str("{0:.2f}".format(AwayTeamA[0][0]))+"\nStd.Var"+" "+str("{0:.2f}".format(AwayTeamA[0][1]))+"\n\nDefensive Rebounds\n"+"Mean"+" "+str("{0:.2f}".format(AwayTeamA[0][2]))+"\nStd.Var"+" "+str("{0:.2f}".format(AwayTeamA[0][3]))+"\n\nTotal Rebounds\n"+"Mean"+" "+str("{0:.2f}".format(AwayTeamA[0][4]))+"\nStd.Var"+" "+str("{0:.2f}".format(AwayTeamA[0][5])))
         self.ui.label.setText("Offensive Rebounds\n"+"Mean"+" "+str("{0:.2f}".format(HomeTeamA[0][0]))+"\nStd.Var"+" "+str("{0:.2f}".format(HomeTeamA[0][1]))+"\n\nDefensive Rebounds\n"+"Mean"+" "+str("{0:.2f}".format(HomeTeamA[0][2]))+"\nStd.Var"+" "+str("{0:.2f}".format(AwayTeamA[0][3]))+"\n\nTotal Rebounds\n"+"Mean"+" "+str("{0:.2f}".format(HomeTeamA[0][4]))+"\nStd.Var"+" "+str("{0:.2f}".format(HomeTeamA[0][5])))

         
        # rb=self.sender()
        # if rb.isChecked():
        #     if rb.text()=="Score Analyze":
    def getLogoHome(self):
        print(str(self.ui.comboBox.currentText()))
        self.ui.HomeLogo.setPixmap(QtGui.QPixmap(self.adress+str(self.ui.comboBox.currentText())+".png"))
    def getLogoAway(self):
        self.ui.AwayLogo.setPixmap(QtGui.QPixmap(self.adress+str(self.ui.comboBox_2.currentText())+".png"))

def App():
    app=QApplication(sys.argv)
    win=MyApp()
    win.show()
    sys.exit(app.exec_())
App()