import requests
from bs4 import BeautifulSoup
import re
#https://www.whoscored.com/Players/21501/History/
count=1
f=open("mackolik.csv","w");
k=0
for i in range(0,100000):
    print("-------->",k)
    k+=1
    mackolikurl="http://arsiv.mackolik.com/Player/Default.aspx?id="+str(i)
    mackolikurl2 = "http://arsiv.mackolik.com/AjaxHandlers/PlayerHandler.aspx?command=statTabs&id="+str(i)+"&type=2"
    head = {
        "Host" : "arsiv.mackolik.com",
        "Connection": "keep-alive",
        "Accept":"*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",
        "Referer" : "http://arsiv.mackolik.com/Player/Default.aspx?id="+str(i),
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    r = requests.get(mackolikurl)
    req=requests.get(mackolikurl2,headers=head)
    soup = BeautifulSoup(r.content,"html.parser")
    soup2=BeautifulSoup(req.content,"html.parser")
    try:
        ligbazında_veri=soup2.find_all("tr",{"class":"total_row2"})
        dakika=(ligbazında_veri[0].contents)[len(ligbazında_veri[0].contents)-2].text.strip()
        ilk11=(ligbazında_veri[0].contents)[len(ligbazında_veri[0].contents)-4].text.strip()
        golsayisi=(ligbazında_veri[0].contents)[len(ligbazında_veri[0].contents)-10].text.strip()
        ülke_veri=soup.find("div",{"style":"color: #16387C;font-family: Arial; font-size: 16px; font-weight: bold;padding-top:5px"})
        ülke=ülke_veri.text.strip()
        if golsayisi=="":
            golsayisi=0
        if ilk11=="":
            ilk11=0
            
        ###################################################################################
        #golsayisi_veri=soup.find_all("div",{"style":"float:right;width:300px;"})
        #golsayisi=(golsayisi_veri[0].contents)[len(golsayisi_veri[0].contents)-6]
        #golsayisi=golsayisi.find_all("b")
        #golsayisi=golsayisi[2].text
        
        ########################################################################
        team=soup.find_all("a",{"class":"normal org"})
        for p in team:
            team2=p.find("span",{"itemprop":"name"}).text
        #####################################################################
        gelen_veri = soup.find_all("div",{"style": "background-color: #f1f1f1;"})
        name=soup.find_all("div",{"style":"float: left;margin-top: 20px;text-align: left"})
        pozisyon=soup.find_all("div",{"id":"dvPlayerInfo"})
        yas=soup.find_all("div",{"id":"dvPlayerInfo"})
        istatistik=soup.find_all("div",{"id":"playerFirstTab"})
        ####################################################################
        for j in istatistik:
            yas1=j.find("div",{"style":"width: 140px;"}).text.split()
        yas=yas1[2].replace("(","").replace(")","")
        ######################################################################
        maas_veri=soup.find_all("div",{"style":"float:right;font-family: Arial;  font-size:18px; font-weight: bold;margin-top: 20px;"})
        for h in maas_veri:
            maas=h.find("div",{"style":"font-size:14px"}).text.strip().split()
        maas[0]=maas[0].replace(".","")
        maasresult=maas[0]
        maas=maasresult[:-3]
        ####################################################################
        for a in gelen_veri:
            
                name=a.find("h1",{"itemprop":"name"}).text.strip()
                nameb=name.split("'")
                name=""
                for l in nameb:
                    name+=l
        #########################################################################
                pozisyon=a.find("div",{"class":"role"}).text.strip()
                if int(yas) < 40:
                    if int(golsayisi)>=0 and int(golsayisi)<=100:
                        golsayisi="0-100"
                    elif int(golsayisi)>100 and int(golsayisi)<=200:
                        golsayisi="100-200"
                    elif int(golsayisi)>200 and int(golsayisi)<=500:
                        golsayisi="200-500"
                    elif int(golsayisi)>500 and int(golsayisi)<=1000:
                        golsayisi="500-1000"
                    macsayisi=(ligbazında_veri[0].contents)[len(ligbazında_veri[0].contents)-12].text 
                    dakika=(ligbazında_veri[0].contents)[len(ligbazında_veri[0].contents)-2].text.strip()
                    season=(ligbazında_veri[0].contents)[len(ligbazında_veri[0].contents)-14].text
                 

                
                    print("******",count,"*********")
                    if int(maas)>0 and int(maas)<=500:
                        maas="0-500"
                    elif int(maas)>500 and int(maas)<=1000:
                        maas="500-1000"
                    elif int(maas)>1000 and int(maas)<=10000:
                        maas="1000-10000"
                    elif int(maas)>10000 and int(maas)<=50000:
                        maas="10000-50000"
                    elif int(maas)>50000 and int(maas)<=100000:
                        maas="50000-100000"
                    elif int(maas)>100000 and int(maas)<=1000000:
                        maas="100000-1000000"
                  
                    
                    if int(yas)>=18 and int(yas)<25:
                        yas="18-25"
                    elif int(yas)>=25 and int(yas)<30:
                        yas="25-30"
                    elif int(yas)>=30 and int(yas)<40:
                        yas="30-40"
                    print(name,team2,ülke,pozisyon[2:],maas,yas,season,macsayisi,golsayisi,dakika,ilk11,end="")
                    print()
                    count+=1
                    f.write(name+","+team2+","+ülke+","+maas+","+ pozisyon[2:]+","+yas+","+season+","+macsayisi+","+golsayisi+","+dakika+","+ilk11+"\n")
                else:
                    continue
    except:
        continue

f.close()
#isim,takim,ülke,maas,pozisyon,yas,sezon,macsayisi,golsayisi,dakika,ilkonbir