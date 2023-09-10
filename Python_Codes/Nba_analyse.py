import pandas as pd
import numpy as np
import mysql.connector
import datetime
import matplotlib as mp
class statistic:
 def __init__(self):
  connection=mysql.connector.connect(host="localhost",user="root",password="vm3cbm0m",database="nba")
  self.df=pd.read_sql_query("SELECT * FROM nba.nbaresults FULL JOIN nba.nbaadvresults USING(IDT)",connection)
  self.df["Team1D"]=np.where((self.df["Score1"]>self.df["Score2"]),"W","L")
  self.df["Team2D"]=np.where((self.df["Score1"]<self.df["Score2"]),"W","L")
  self.df["Margin"]=self.df.Score1-self.df.Score2
  self.df["TotalP"]=self.df.Score1+self.df.Score2
  self.df["Month"]=self.df.Date
  self.df["Year"]=self.df.Date
  for i in range(len(self.df["Month"])):
   self.df["Month"][i]=self.df["Month"][i].month
  for i in range(len(self.df["Year"])):
   self.df["Year"][i]=self.df["Year"][i].year
  self.df["Month/Year"]=self.df.__str__
  for i in range(len(self.df.Month)):
   self.df["Month/Year"][i]=f"{self.df.Month[i]}"+"/"+f"{self.df.Year[i]}"
  print(self.df["Month/Year"])
#   print(self.df)
  connection.close()
 def teamlist(self):
   print(self.df["Team1"])
 def genstats(self):
    results=self.df.groupby(["Team1","Team1D"])["Score1"].agg([np.mean,np.max,np.min,np.std])
    #results1=self.df.groupby(["Loser"])["Score1","Score2"].agg([np.mean,np.max,np.min,np.std]).filter(like=Team1,axis=0)
    print(results)
    #print(results1)
 def teamstats(self,Team1):
    resultsA=self.df.groupby(["Team1","Team1D"])["Score1"].agg([np.mean,np.max,np.min,np.std]).filter(like=Team1,axis=0)
    resultsW=self.df.groupby(["Team2","Team2D"])["Score2"].agg([np.mean,np.max,np.min,np.std]).filter(like=Team1,axis=0)
    rateA=self.df[self.df["Team1D"]=="W"].groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0)/self.df.groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0)
    rateH=self.df[self.df["Team2D"]=="W"].groupby("Team2")["Team2D"].count().filter(like=Team1,axis=0)/self.df.groupby("Team2")["Team2D"].count().filter(like=Team1,axis=0)
    rateT=(self.df[self.df["Team1D"]=="W"].groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0)+self.df[self.df["Team2D"]=="W"].groupby("Team2")["Team2D"].count().filter(like=Team1,axis=0))/(self.df.groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0)+self.df.groupby("Team2")["Team2D"].count().filter(like=Team1,axis=0))
    #results1=self.df.groupby(["Loser"])["Score1","Score2"].agg([np.mean,np.max,np.min,np.std]).filter(like=Team1,axis=0)
    return resultsA,resultsW
   #  print("AWAY\n",resultsA,"\n","Away Win Percentage\n",rateA.values[0],"\n")
   #  print("HOME\n",resultsW,"\n","Home Win Percentage\n",rateH.values[0])
   #  print("Total Win Percentage\n",rateT.values[0])
 def teamstatslastmatches(self,Team1):
    df1=self.df[self.df["Team1"]==Team1].tail(10)
    df2=self.df[self.df["Team2"]==Team1].tail(10)
    try:
     awayw=df1[df1["Team1D"]=="W"].groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0).values[0]
    except:
     awayw=0
    try:
     homew=df2[df2["Team2D"]=="W"].groupby("Team2")["Team2D"].count().filter(like=Team1,axis=0).values[0]
    except:
     homew=0
    resultsA=df1.groupby("Team1")["Score1"].agg([np.mean,np.max,np.min,np.std]).filter(like=Team1,axis=0)
    resultsW=df2.groupby("Team2")["Score2"].agg([np.mean,np.max,np.min,np.std]).filter(like=Team1,axis=0)
    rateA=awayw/df1.groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0).values[0]
    rateH=homew/df2.groupby("Team2")["Team2D"].count().filter(like=Team1,axis=0).values[0]
    rateT=(homew+awayw)/(df1.groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0)+df2.groupby("Team2")["Team2D"].count().filter(like=Team1,axis=0)).values[0]
    Totalgame=df1.groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0).values[0]
    #results1=self.df.groupby(["Loser"])["Score1","Score2"].agg([np.mean,np.max,np.min,np.std]).filter(like=Team1,axis=0)
    return resultsA,resultsW,rateH,rateT,rateA,homew,awayw,Totalgame
    #rateA.values[0]
    #rateH.values[0],rateT.values[0]
 def teamcompares(self,Team1,Team2):
    resultsA=self.df.groupby(["Team1"])[["Score1","TotalP"]].agg([np.mean,np.max,np.min]).filter(like=Team1,axis=0)
    resultsH=self.df.groupby(["Team2"])[["Score2","TotalP"]].agg([np.mean,np.max,np.min]).filter(like=Team2,axis=0)
    rateA=self.df[self.df["Team1D"]=="W"].groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0)/self.df.groupby("Team1")["Team1D"].count().filter(like=Team1,axis=0)
    rateH=self.df[self.df["Team2D"]=="W"].groupby("Team2")["Team2D"].count().filter(like=Team2,axis=0)/self.df.groupby("Team2")["Team2D"].count().filter(like=Team2,axis=0)
    return resultsH , resultsA,rateH,rateA
   #  print(resultsA)
   #  print(resultsH)
   #  print("Away Team Win Percantage\n",rateA)
   #  print("Home Team Win Percantage\n",rateH)
 def bymonthperformance(self,team1,Team2):
   ResultsA=self.df[self.df["Team1"]==team1].groupby(["Month/Year"])["Score1"].agg(["mean","max","min","std","count"])
   ResultsH=self.df[self.df["Team2"]==Team2].groupby(["Month/Year"])["Score2"].agg(["mean","max","min","std","count"])
   return ResultsA,ResultsH
 def analysequarter(self,team1,No):
   ResultsAl1=self.df[self.df["Team1"]==team1].groupby(["Team1","Team1D"])[["AwayQ1","AwayQ2","AwayQ3","AwayQ4"]].agg([np.mean])
   Results=self.df[self.df["Team1"]==team1].groupby(["Team1","Team1D"])["AwayQ"+No].agg([np.mean,np.std])
   print("AWAY\n",Results,"\n",ResultsAl1)
   ResultsAl2=self.df[self.df["Team2"]==team1].groupby(["Team2","Team2D"])[["HomeQ1","HomeQ2","HomeQ3","HomeQ4"]].agg([np.mean])
   Results1=self.df[self.df["Team2"]==team1].groupby(["Team2","Team2D"])["HomeQ"+No].agg([np.mean,np.std])
   print("HOME\n",Results1,"\n",ResultsAl2)
 def rbanalyse(self,Team1):
    self.df["OREBAWAY"]=self.df["OREBAWAY"].astype("int")
    self.df["DREBAWAY"]=self.df["DREBAWAY"].astype("int")
    self.df["REBAWAY"]=self.df["REBAWAY"].astype("int")
    self.df["OREBHOME"]=self.df["OREBHOME"].astype("int")
    self.df["DREBHOME"]=self.df["DREBHOME"].astype("int")
    self.df["REBHOME"]=self.df["REBHOME"].astype("int")

    RBanalyse=self.df[self.df["Team1"]==Team1].groupby("Team1")[["OREBAWAY","DREBAWAY","REBAWAY"]].agg(["mean","std"])
    RBanalyse1=self.df[self.df["Team2"]==Team1].groupby("Team2")[["OREBHOME","DREBHOME","REBHOME"]].agg(["mean","std"])
    return RBanalyse,RBanalyse1

#a=statistic()
# a.teamstats("76ers")
# a.teamcompares("76ers","Bulls")
# while True:
#    x=input("Analiz yapmak istediğiniz bölümü seçiniz\n1.Genel İstatistik\n2.Takım İstatistikleri\n3.Karşılaştırmalı İstatistik\n4.Zaman Serisi Analiz\n5.Çeyrek Analizi\n6.Rebaund Analyse\n7.Çıkış\n")
#    if x=="7":
#       break
#    elif x=="1":
#       a.genstats()
#    elif x=="5":
#        y=input("Analiz yapmak istediğiniz takımı seçiniz ")
#        x=input("Analiz yapmak istediğiniz Çevreği seçiniz ")
#        a.analysequarter(y,x)
#    elif x=="2":
#       y=input("Analiz yapmak istediğiniz takımı seçiniz ")
#       a.teamstatslastmatches(y)
#    elif x=="3":
#       away=input("Deplasman Takımını Giriniz ")
#       Home=input("Ev Sahibi Takımını Giriniz ")
#       a.teamcompares(away,Home)
#    elif x=="4":
#       team=input("Takımı Giriniz ")
#       a.bymonthperformance(team)
#    elif x=="6":
#       team=input("Takımı Giriniz ")
#       a.rbanalyse(team)