from readdata import *
from get_index_info  import *
from new_class import *


import numpy as np
import  pandas as pd
from collections import Counter
import multiprocessing


def Ranking_of_important_tag(): #统计所有标签的次数  相当度值
    "统计标签，类型数量"
    movie_tag=np.array(pd.read_table("data/movie_tags.txt"))
    # print(movie_tag)
    # print("统计出了每个标签的重要程度")
    tag_times=Counter(movie_tag[:,1])#每个标签的统计次数都得到了
    # print(tag_times)
    # print(type(tag_times))
    return tag_times

def Ranking_of_important_genre():      #统计所有类型的次数相当于度值
    movie_genre=np.array(pd.read_table("data/movie_genres.txt"))
    # print(movie_genre)
    genre_times=Counter(movie_genre[:,1])
    # print(genre_times)
    return genre_times




def sort_genre(genre):    #电影的类型也按照连接数量最多的进行排序  类型的重要成都排序
    gen_timesList_dic={}
    genre_times = Ranking_of_important_genre()
    for i in genre:
        # print(genre_times[i])
        gen_timesList_dic[i]=genre_times[i]
    # print(timesList.items())
    genre_order=sorted(gen_timesList_dic.items(),key=lambda x:x[1],reverse=True)
    # print(timesList)
    # print(genre_order)
    genre_order_list=[]
    for i in genre_order:
        genre_order_list.append(i[0])
        # print(i[0])
    # print(genre_order_list)
    return genre_order_list

def sort_tag(tags):  # 按照标签连接最大的顺序排列，标签的重要程度排序
    tag_timesList_dic = {}
    tag_times = Ranking_of_important_tag()
    for i in tags:
        # print(int(i[0]))
        tag_timesList_dic[int(i[0])] = tag_times[int(i[0])]
    # print(tag_timesList_dic)
    tag_order = sorted(tag_timesList_dic.items(), key=lambda x: x[1], reverse=True)
    tag_order_list = []
    for i in tag_order:
        tag_order_list.append(i[0])
    return tag_order_list


def sortactor(actor):
    actorList=actor
    # print(a1701ctorList)
    actorList=sorted(actorList,key=lambda x:x[2])
    # print(actorList)
    return actorList

def movie_info(movie_ID,tag_all_index_list,gre_all_index_list):
    '''从文件中得到查询id号的信息'''
    movie_ID=str(movie_ID)
    # print(movie_ID)
    country=select_countries_directir(movie_ID)
    # print(country)
    directors=select_movie_directir(movie_ID)
    # print(directors)
    genre=sort_genre(select_genre_directir(movie_ID))
    # print(genre)
    tags=sort_tag(select_movie_tags_wight(movie_ID))
    # print(tags)
    actor=sortactor(select_movie_actor(movie_ID))
    # print(actor)

    movie = Moive(MOVIE_ID=movie_ID, countries=country, directors=directors, genre=genre, tags=tags, actor=actor)
    # print("得到了一部电影的所有信息：")
    # movie.show()
    return movie



def coding_main(num):
    try:
        tag_all_index_list=Ranking_of_important_tag()
        gre_all_index_list=Ranking_of_important_genre()
        one_movie=movie_info(num,tag_all_index_list=tag_all_index_list,gre_all_index_list=gre_all_index_list)  # 得到一部电影的所有信息
        one_movie_code=MOVIE_CODE(countriesList=countriesList(),movie=one_movie,director=DirLis(),genres=genresLis())
        one_movie_code=one_movie_code.CODE()
        print(num,one_movie_code)
        return one_movie_code

    except:
        print("信息错误:",num)
        pass




if __name__=="__main__":

    # allMovie_code=[]
    # for i in movieList():
    #      allMovie_code.append(coding_main(i))
    # code_file = open("Process_data/code.txt", "w")
    # code_file.writelines(allMovie_code)
    # code_file.close()
    print("******************")

