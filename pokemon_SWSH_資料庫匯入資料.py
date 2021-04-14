import urllib.request as httplib  # 3.x
import ssl
import urllib.request
import matplotlib.pyplot as plt
import xlrd
import xlwt
import csv
import numpy as np
import pymysql as MySQLdb             #  pip install MySQLdb

rowlist = []

name1 = []               #平台資料
name2 = []           #平台銷售資料
HP = []
Attack = []             #平台銷售資料轉浮點數
Defense = []
Sp_Atk = []
Sp_Def = []
Speed = []
sum = []
type1 = []
type2 = []


#讀取CSV檔
with open('pokemon-swordshield-fin-utf8-new.csv', 'r',encoding="utf-8") as fin: #,encoding="utf-8"
    read = csv.reader(fin, delimiter=',')
    header = next(read)  # 讀取標題並跳過
    print(header)

    x = 0
    for row in read:
            rowlist.append(int(x))  # 列出row列的數字迴圈
            name1.append(row[0])
            name2.append(row[1])
            HP.append(int(row[2]))
            Attack .append(int(row[3]))
            Defense.append(int(row[4]))
            Sp_Atk.append(int(row[5]))
            Sp_Def.append(int(row[6]))
            Speed.append(int(row[7]))
            sum.append(int(row[8]))
            type1.append(row[9])
            type2.append(row[10])

            x = x + 1
print(name2)


db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
#db = MySQLdb.connect(host="172.19.107.140", user="powenko", passwd="powenko", db="mydatabase")
cursor = db.cursor()

with open('pokemon-swordshield-fin-utf8-new.csv', 'r',encoding="utf-8") as fin: #,encoding="utf-8"
    read = csv.reader(fin, delimiter=',')
    header = next(read)  # 讀取標題並跳過
#sql="INSERT INTO `project` (`sna`) VALUES ('pikachu');"

#sql="UPDATE `ubiketaoyuan` SET `sna` = 'canon' WHERE  `sna` = 'pikachu'"

    y = 0
    for row in read:
        str1 = "INSERT INTO `project` (`id`, `name01`, `name02`, `HP`, `Attack`, `Defense`, `Sp_Atk`, `Sp_Def`, `Speed`, `sum`, `type1`, `type2`, `datetime`) VALUES ('[value-1]', '[value-2]', '[value-3]', '[value-4]', '[value-5]', '[value-6]', '[value-7]', '[value-8]', '[value-9]', '[value-10]', '[value-11]', '[value-12]', '[value-12]');"
        str1 = str1.replace("[value-1]", "null")
        str1 = str1.replace("[value-2]", str(name1[y]))
        str1 = str1.replace("[value-3]", str(name2[y]))
        str1 = str1.replace("[value-4]", str(HP[y]))
        str1 = str1.replace("[value-5]", str(Attack[y]))
        str1 = str1.replace("[value-6]", str(Defense[y]))
        str1 = str1.replace("[value-7]", str(Sp_Atk[y]))
        str1 = str1.replace("[value-8]", str(Sp_Def[y]))
        str1 = str1.replace("[value-9]", str(Speed[y]))
        str1 = str1.replace("[value-10]", str(sum[y]))
        str1 = str1.replace("[value-11]", str(type1[y]))
        str1 = str1.replace("[value-12]", str(type2[y]))
        str1 = str1.replace("[value-13]", "now()")
        print(str1)

        y=y+1
        cursor.execute(str1)
        db.commit()
