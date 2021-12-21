import os

path = 'data/allcodingfile'
path_list = os.listdir(path)
# path_list=path_list.sort(key=lambda x:int(x[:-4]))
print(path_list)