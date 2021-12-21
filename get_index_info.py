import  numpy as np
import pandas as pd
'''得到所有信息的不重复列表'''



'''电影列表'''
def movieList():
    moviedata=np.array(pd.read_csv('data/movies.csv'))
    # print(moviedata[:,0])
    return moviedata[:,0]

'''国家列表'''
def countriesList():
    countries_List=[]
    countries=np.array(pd.read_table("data/movie_countries.txt"))[:,1]
    # print(countries)
    for i in countries:
        # print(i)
        if i not in countries_List:
            countries_List.append(i)
    return  countries_List


'''导演列表'''
def DirLis():
    Dir_list=[]
    Dir_list_all=np.array(pd.read_csv("data/movie_directors.csv",header=None))[:,2]
    for i in Dir_list_all:
        if i not in Dir_list:
            Dir_list.append(i)
    # print(Dir_list)
    return Dir_list



def genresLis():
    genresLIST=[]
    genres_Lis=list(np.array(pd.read_table("data/movie_genres.txt"))[:,1])
    for i in genres_Lis:
        if i not in genresLIST:
            genresLIST.append(i)
    return genres_Lis



def tagList():
    tag_list=np.array(pd.read_table("data/tags.txt"))
    return tag_list
