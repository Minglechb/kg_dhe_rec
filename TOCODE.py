import numpy as np
import pandas as pd
from movie_info_main import *


def coding_main1(num):
    try:
        tag_all_index_list=Ranking_of_important_tag()
        gre_all_index_list=Ranking_of_important_genre()
        one_movie=movie_info(num,tag_all_index_list=tag_all_index_list,gre_all_index_list=gre_all_index_list)  # 得到一部电影的所有信息
        one_movie.show()
        one_movie_code=MOVIE_CODE(countriesList=countriesList(),movie=one_movie,director=DirLis(),genres=genresLis())
        one_movie_code=one_movie_code.CODE()
        print(num,one_movie_code)
        file_name = 'data/allcodingfile/' + str(num)  + '.txt'
        file = open(file_name, "w", encoding='utf-8')
        file.writelines(str(one_movie_code))
        return one_movie_code
    except:
        print("信息出错")
        pass





if __name__=="__main__":
# #'''单线程写'''
#     for index,j in enumerate(movieList()):
#         # print(j)
#         whole_code=coding_main1(j)
#         file_name='data/allcodingfile/'+str(j)+'code'+'.txt'
#         # print(index,whole_code)
#         file=open(file_name,"w",encoding='utf-8')
#         file.writelines(str(whole_code))
#         # file.close()

    # coding_main1(65133)



#    print(coding_main(418))

    # # 并行处理
    pool = multiprocessing.Pool()
    res = pool.map(coding_main1, movieList())
    print("DONE!!!!!")

    # print(len(coding_main1(3)))

