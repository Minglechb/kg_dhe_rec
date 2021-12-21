import os
import pandas as pd

from  DHE import *

path = 'data/allcodingfile'
path_list = os.listdir(path)
path_list.sort(key=lambda x:int(x.split('.')[0]))
# print(path_list)
x=[]
for i in path_list:
    with open(path+'/'+i,'r') as file:
        x.append(int(file.read()))
# print(len(x))
# print(x)


s= DeepHashEncoding(x,1024,1000)
# print(s,s.shape)
filefullpath="data/DHE_data/identifivec.csv"
if os.path.exists(filefullpath):
    os.remove(filefullpath)
pd.DataFrame(s).to_csv(filefullpath)
print("DONE!!!!!!!")