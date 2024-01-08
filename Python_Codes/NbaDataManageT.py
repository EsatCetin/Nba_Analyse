from bs4 import BeautifulSoup
import os
from datetime import timedelta
from datetime import datetime
from datetime import date as dt
import urllib.request
import pandas as pd
import mysql.connector
class Nba:
     def __init__(self):
      #İnit function we open a cnonnection to MySql database
      self.connection=mysql.connector.connect(host="localhost",user="root",password="vm3cbm0m",database="nba")
      self.cursor=self.connection.cursor(buffered=True)
      query="Select Date from nba.nbaresults Where Date=(SELECT MAX(Date) FROM nba.nbaresults)"
      self.cursor.execute(query)
      self.list=self.cursor.fetchone()
     def Basic_Stats(self):
       self.toplam=[]
       print(self.list)
       startdate=self.list[0]+timedelta(days=1)
       print(startdate)
       start=str(self.list[0]).replace("-","/")
       Today=str(dt.today()).replace("-","/")
       print(Today)
       dateMax=datetime.strptime(start,"%Y/%m/%d")
       dateNow=datetime.strptime(Today,"%Y/%m/%d")
       date=[]
       date_range=dateNow-dateMax
       print(date_range.days)
       #We decide range of data loading from website 
       #Wtih this loop , i create a list of dates 
       for day in range(int(date_range.days)):
        tar=str(startdate+timedelta(days=day))
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
     def get_game_ids(self):
       #Game IDs are unique in the first database so with a simple querry , we call them
       print(self.list[0])
       query=f"Select IDT from nba.nbaresults Where Date >{self.list[0]}"
       self.cursor.execute(query)
       list=self.cursor.fetchall()
       liste=[]
       print(list)
       for i in list:
        liste.append(str(i[0]))
       return liste  
     def expanded_stats(self):
      #Call the Game's ID's
      self.toplam=self.get_game_ids()
      self.totalstats=[]
      #To visit every game , i created a loop with ID's
      for c in self.toplam:
        self.url=urllib.request.urlopen("https://www.espn.com/nba/boxscore/_/gameId/"+c)
        self.soup=BeautifulSoup(self.url,"html.parser")
        self.soup.prettify()
        # print(self.soup)
      # The rest is digging into html , actually my favoruite part it is like a puzzle
        liste=self.soup.find("div",{"class":"Boxscore Boxscore__ResponsiveWrapper"}).find_all("div",{"class":"Wrapper"})        
        self.stats=[]
        self.stats=[int(c)]
        for i in liste:
          l=len(i.find("div",{"class":"flex"}).find("div",{"class":"Table__ScrollerWrapper relative overflow-hidden"}).find("tbody",{"class":"Table__TBODY"}).find_all("tr"))
          k=i.find("div",{"class":"flex"}).find("div",{"class":"Table__ScrollerWrapper relative overflow-hidden"}).find("tr",{"data-idx":str(l-2)}).find_all("td")
          for x in k:
             try:
              if x.text.strip()!="":
               self.stats.append(x.text.strip())
              else:
                continue
             except:
              continue
        self.totalstats.append(self.stats)
     def savetodatabase2(self):
      # the last phase of these code series is to save datas to MySql database
      self.expanded_stats()
      print(self.totalstats)
      insert="INSERT into nba.nbaadvresults(IDT, FGAWAY, 3PTAWAY, FTAWAY, OREBAWAY, DREBAWAY, REBAWAY, ASTAWAY, STLAWAY, BLKAWAY, TOAWAY, PFAWAY, PTSAWAY, FGHOME, 3PTHOME, FTHOME, OREBHOME, DREBHOME, REBHOME, ASTHOME, STLHOME, BLKHOME, TOHOME, PFHOME, PTSHOME) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      self.cursor.executemany(insert,self.totalstats)
      try:
         self.connection.commit()
      except mysql.connector.Error as err:
            print("Hata:",err)
      self.connection.close()
     def savetodatabase(self):
      #Wtih this created function we can save datas to MySql database that we created
      self.Basic_Stats()
      print(self.toplam)
      insert="INSERT into nba.nbaresults(Date,Team1,loc1,Score1,Team2,loc2,Score2,IDT,AwayQ1,AwayQ2,AwayQ3,AwaYQ4,HomeQ1,HomeQ2,HomeQ3,HomeQ4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      self.cursor.executemany(insert,self.toplam)
      try:
         self.connection.commit()
      except mysql.connector.Error as err:
            print("Hata:",err)
      self.savetodatabase2()       
Analyse=Nba()
Analyse.savetodatabase2()




