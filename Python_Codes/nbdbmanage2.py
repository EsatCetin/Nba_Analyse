from bs4 import BeautifulSoup
import json
import os
import datetime
import urllib.request
import pandas as pd
import mysql.connector
class Nba2:
     def __init__(self):
      self.connection=mysql.connector.connect(host="localhost",user="root",password="vm3cbm0m",database="nba")
      self.cursor=self.connection.cursor()
     def getid(self):
       query="Select IDT from nba.nbaresults Where Date>'2023-04-02'"
       self.cursor.execute(query)
       list=self.cursor.fetchall()
       liste=[]
       for i in list:
        liste.append(str(i[0]))
       return liste  
       
     def wholestats(self):
      self.toplam=self.getid()
      self.totalstats=[]
      for c in self.toplam:
        self.url=urllib.request.urlopen("https://www.espn.com/nba/boxscore/_/gameId/"+c)
        self.soup=BeautifulSoup(self.url,"html.parser")
        self.soup.prettify()
        # print(self.soup)
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
      self.wholestats()
      print(self.totalstats)
      insert="INSERT into nba.nbaadvresults(IDT, FGAWAY, 3PTAWAY, FTAWAY, OREBAWAY, DREBAWAY, REBAWAY, ASTAWAY, STLAWAY, BLKAWAY, TOAWAY, PFAWAY, PTSAWAY, FGHOME, 3PTHOME, FTHOME, OREBHOME, DREBHOME, REBHOME, ASTHOME, STLHOME, BLKHOME, TOHOME, PFHOME, PTSHOME) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      self.cursor.executemany(insert,self.totalstats)
      try:
         self.connection.commit()
      except mysql.connector.Error as err:
            print("Hata:",err)
      self.connection.close()

        
a=Nba2()
a.savetodatabase2()