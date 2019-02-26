import pymongo
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#directory set-location "Z:\Purwadhika\Datasciencepython\DB"

url='mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)
#alldb= mydb.list_database_names()
#print(alldb)

newdb1 = mydb["kampus"]                                
newcol1 = newdb1["Dosen"]
newcol2 = newdb1["Mahasiswa"]

dosen = []
mahasiswa = []

a = []
b = []
for data in newcol1.find():                            
    dosen.append(data)

for data in newcol2.find():
    mahasiswa.append(data)

for data in dosen:
    dosen1 = {
        'asal': data['asal'],
        'nama': data['nama'],
        'status': 'dosen',
        'usia': int(data['usia'])
    }
    a.append(dosen1)

for data in mahasiswa:
    mahasiswa1 = {
        'asal': data['asal'],
        'nama': data['nama'],
        'status': 'mahasiswa',
        'usia': int(data['usia'])
    }
    b.append(mahasiswa1)

df = pd.DataFrame(a)
df2 = pd.DataFrame(b)
print(df)
print(df2)

plt.bar(df['nama'],df['usia'])
plt.bar(df2['nama'],df2['usia'])
plt.grid(True)
plt.legend()
plt.show()