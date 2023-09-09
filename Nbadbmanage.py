from bs4 import BeautifulSoup
import json
import os
import datetime
import requests
import urllib.request
import pandas as pd
import mysql.connector
class Nba:
     def __init__(self):
      #İnit function we open a cnonnection to MySql database
      self.connection=mysql.connector.connect(host="localhost",user="root",password="vm3cbm0m",database="nba")
      self.cursor=self.connection.cursor()
     def datacollect(self):
       self.toplam=[]
       #For the start , we declare starting date of data scrapping
       start=datetime.date(2023,4,13)
       date=[]
       #We decide range of data loading from website 
       #Wtih this loop , i create a list of dates 
       for day in range(4):
        tar=str(start+datetime.timedelta(days=day))
        date.append(tar.replace("-",""))
       #with the help of list of date , we create a loop that we can visit every website between these dates
       for c in date:
        self.url=urllib.request.urlopen("https://www.espn.com/nba/scoreboard/_/date/"+c)
       # BeaatifulSoup library is used to format html codes
        self.soup=BeautifulSoup(self.url,"html.parser")
        self.soup.prettify()
        # print(self.soup)
        #This is where we start to dig html codes it is really important to undestand html
        liste=self.soup.find("section",{"class":"Card gameModules"}).find_all("section")
        for i in liste:
         liste=[]
         try:
           if i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--loser"})==None:
            t1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--winner"}).find("div",{"class":"ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"}).text.strip()
            loc1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--winner"}).find("span",{"class":"ScoreboardScoreCell__Record--homeAway ttc"}).text.strip()
            q1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--winner"}).find("div",{"class":"ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"}).text.strip()
            id=i.get("id")
            C1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--winner"}).find("div",{"class":"ScoreboardScoreCell_Linescores basketball flex justify-end"}).text.strip()
            x=0
            y=2
            quarters=[]
            for l in C1:
               quarters.append(C1[x:y])
               if y==8:
                 break
               x=x+2
               y=y+2
           else:
            t1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--loser"}).find("div",{"class":"ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"}).text.strip()
            loc1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--loser"}).find("span",{"class":"ScoreboardScoreCell__Record--homeAway ttc"}).text.strip()
            q1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--loser"}).find("div",{"class":"ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"}).text.strip()
            id=i.get("id")
            C1=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--away ScoreboardScoreCell__Item--loser"}).find("div",{"class":"ScoreboardScoreCell_Linescores basketball flex justify-end"}).text.strip()
            x=0
            y=2
            quarters=[]
            for l in str(C1):
               quarters.append(C1[x:y])
               if y==8:
                 break
               x=x+2
               y=y+2
           if i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--loser"})==None:
            t2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--winner"}).find("div",{"class":"ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"}).text.strip()
            loc2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--winner"}).find("span",{"class":"ScoreboardScoreCell__Record--homeAway ttc"}).text.strip()
            q2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--winner"}).find("div",{"class":"ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"}).text.strip()
            id=i.get("id")
            C2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--winner"}).find("div",{"class":"ScoreboardScoreCell_Linescores basketball flex justify-end"}).text.strip()
            x=0
            y=2
            quarters2=[]
            for l in str(C2):
               quarters2.append(C2[x:y])
               if y==8:
                 break
               x=x+2
               y=y+2
           else:
            t2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--loser"}).find("div",{"class":"ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"}).text.strip()
            loc2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--loser"}).find("span",{"class":"ScoreboardScoreCell__Record--homeAway ttc"}).text.strip()
            q2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--loser"}).find("div",{"class":"ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"}).text.strip()
            id=i.get("id")
            C2=i.find("li",{"class":"ScoreboardScoreCell__Item flex items-center relative pb2 ScoreboardScoreCell__Item--home ScoreboardScoreCell__Item--loser"}).find("div",{"class":"ScoreboardScoreCell_Linescores basketball flex justify-end"}).text.strip()           
            x=0
            y=2
            quarters2=[]
            for l in str(C2):
               quarters2.append(C2[x:y])
               if y==8:
                 break
               x=x+2
               y=y+2
           liste=[c,t1,loc1,int(q1),t2,loc2,int(q2),int(id)]+quarters+quarters2
          
         except :
          continue
         self.toplam.append(liste)
     def savetodatabase(self):
      #Wtih this created function we can save datas to MySql database that we created
      self.datacollect()
      insert="INSERT into nbaresults(Date,Team1,loc1,Score1,Team2,loc2,Score2,IDT,AwayQ1,AwayQ2,AwayQ3,AwaYQ4,HomeQ1,HomeQ2,HomeQ3,HomeQ4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      self.cursor.executemany(insert,self.toplam)
      try:
         self.connection.commit()
      except mysql.connector.Error as err:
            print("Hata:",err)
      self.connection.close()
      
a=Nba()
a.savetodatabase()




