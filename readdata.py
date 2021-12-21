#############################
#############################

# 数据处理 过程


'''

=======================
hetrec2011-movielens-2k
=======================

-------
Version
-------

Version 1.0 (May 2011)

-----------
Description
-----------

    This dataset is an extension of MovieLens10M dataset, published by GroupLeans
    research group.
    http://www.grouplens.org

    It links the movies of MovieLens dataset with their corresponding web pages at
    Internet Movie Database (IMDb) and Rotten Tomatoes movie review systems.
    http://www.imdb.com
    http://www.rottentomatoes.com

    From the original dataset, only those users with both rating and tagging information
    have been mantained.

    The dataset is released in the framework of the 2nd International Workshop on
    Information Heterogeneity and Fusion in Recommender Systems (HetRec 2011)
    http://ir.ii.uam.es/hetrec2011
    at the 5th ACM Conference on Recommender Systems (RecSys 2011)
    http://recsys.acm.org/2011

---------------
Data statistics
---------------

    2113 users
   10197 movies

      20 movie genres
   20809 movie genre assignments
         avg. 2.040 genres per movie

    4060 directors
   95321 actors
         avg. 22.778 actors per movie
      72 countries

   10197 country assignments
         avg. 1.000 countries per movie
   47899 location assignments
         avg. 5.350 locations per movie

   13222 tags
   47957 tag assignments (tas), i.e. tuples [user, tag, movie]
         avg. 22.696 tas per user
         avg. 8.117 tas per movie

  855598 ratings
         avg. 404.921 ratings per user
         avg. 84.637 ratings per movie

-----
Files
-----

   * movies.dat

   	This file contains information about the movies of the database.

   	The original movie information -title and year- available at MovieLens10M dataset
   	has been extended with public data provided in IMDb and Rotten Tomatoes websites:
   	   - Titles in Spanish
   	   - IMDb movie ids
   	   - IMDb picture URLs
           - Rotten Tomatoes movie ids
           - Rotten Tomatoes picture URLs
           - Rotten Tomatoes (all/top) critics' ratings, avg. scores, numbers of
             reviews/fresh_scores/rotten_scores
           - Rotten Tomatoes audience' avg. ratings, number of ratings, avg. scores

   * movie_genres.dat

        This file contains the genres of the movies.

   * movie_directors.dat

   	This file contains the directors of the movies.

   * movie_actors.dat

   	This file contains the main actores and actresses of the movies.

   	A ranking is given to the actors of each movie according to the order in which
   	they appear on the movie IMDb cast web page.

   * movie_countries.dat

        This file contains the countries of origin of the movies.

   * movie_locations.dat

        This file contains filming locations ot the movies.

   * tags.dat

   	This file contains the set of tags available in the dataset.

   * user_taggedmovies.dat - user_taggedmovies-timestamps.dat

        These files contain the tag assignments of the movies provided by each particular user.

        They also contain the timestamps when the tag assignments were done.

   * movie_tags.dat

        This file contains the tags assigned to the movies, and the number of times
        the tags were assigned to each movie.

   * user_ratedmovies.dat - user_ratedmovies-timestamps.dat

        These files contain the ratings of the movies provided by each particular user.

        They also contain the timestamps when the ratings were provided.

-----------
Data format
-----------

   The data is formatted one entry per line as follows (tab separated, "\t"):

   * movies.dat

        id \t title \t imdbID \t spanishTitle \t imdbPictureURL \t year \t rtID \t rtAllCriticsRating \t rtAllCriticsNumReviews \t rtAllCriticsNumFresh \t rtAllCriticsNumRotten \t rtAllCriticsScore \t rtTopCriticsRating \t rtTopCriticsNumReviews \t rtTopCriticsNumFresh \t rtTopCriticsNumRotten \t rtTopCriticsScore \t rtAudienceRating \t rtAudienceNumRatings \t rtAudienceScore \t rtPictureURL

        Example:
        1	Toy story	0114709	Toy story (juguetes)	http://ia.media-imdb.com/images/M/MV5BMTMwNDU0NTY2Nl5BMl5BanBnXkFtZTcwOTUxOTM5Mw@@._V1._SX214_CR0,0,214,314_.jpg	1995	toy_story	9	73	73	0	100	8.5	17	17	0	100	3.7	102338	81	http://content7.flixster.com/movie/10/93/63/10936393_det.jpg

   * movie_genres.dat

        movieID	\t genre

        Example:
        1	Adventure

   * movie_directors.dat

        movieID \t directorID \t directorName

        Example:
        1	john_lasseter	John Lasseter

   * movie_actors.dat

        movieID \t actorID \t actorName \t ranking

        Example:
        1	annie_potts	Annie Potts	10

   * movie_countries.dat

        movieID \t country

        Example:
        1	USA

   * movie_locations.dat

        movieID \t location1 \t location2 \t location3 \t location4

        Example:
        2	Canada	British Columbia	Vancouver

   * tags.dat

        id \t value

        Example:
        1	earth

   * movie_tags.dat

        movieID \t tagID \t tagWeight

        Example:
        1	13	3

   * user_taggedmovies-timestamps.dat

        userID \t movieID  \t tagID  \t timestamp

        Example:
        75	353	5290	1162160415000

   * user_taggedmovies.dat

        userID \t movieID \t tagID \t date_day \t date_month \t date_year \t date_hour \t date_minute \t date_second

        Example:
        75	353	5290	29	10	2006	23	20	15

   * user_ratedmovies-timestamps.dat

        userID \t movieID \t rating \t timestamp

        Example:
        75	3	1	1162160236000

   * user_ratedmovies.dat

        userID \t movieID \t rating \t date_day \t date_month \t date_year \t date_hour \t date_minute \t date_second

        Example:
        75	3	1	29	10	2006	23	17	16

-------
License
-------

   The data contained in hetrec2011-movielens-2k.zip is distributed with permission of GroupLens research group.

   The data is made available for non-commercial use.

   Those interested in using the data in a commercial context should contact GroupLens members:
   http://www.grouplens.org/contact

----------------
Acknowledgements
----------------

   We thank GroupLens research group at University of Minessota (http://www.grouplens.org)
   for hosting and allowing us to publish this dataset, which is an extension of MovieLens10M dataset.

   This work was supported by the Spanish Ministry of Science and Innovation (TIN2008-06566-C04-02),
   and the Regional Government of Madrid (S2009TIC-1542).

----------
References
----------

   When using this dataset you should cite:
      - the original Movielens dataset from GroupLens research group, http://www.grouplens.org
      - IMDb website, http://www.imdb.com
      - Rotten Tomatoes website, http://www.rottentomatoes.com

   You may also cite HetRec'11 workshop as follows:

   @inproceedings{Cantador:RecSys2011,
      author = {Cantador, Iv\'{a}n and Brusilovsky, Peter and Kuflik, Tsvi},
      title = {2nd Workshop on Information Heterogeneity and Fusion in Recommender Systems (HetRec 2011)},
      booktitle = {Proceedings of the 5th ACM conference on Recommender systems},
      series = {RecSys 2011},
      year = {2011},
      location = {Chicago, IL, USA},
      publisher = {ACM},
      address = {New York, NY, USA},
      keywords = {information heterogeneity, information integration, recommender systems},
   }

-------
Credits
-------

   This dataset was built by Iv�n Cantador with the collaboration of Alejandro Bellog�n and Ignacio Fern�ndez-Tob�as,
   members of the Information Retrieval group at Universidad Autonoma de Madrid (http://ir.ii.uam.es)

-------
Contact
-------

   Iv�n Cantador, ivan [dot] cantador [at] uam [dot] es

'''


'''
把每一个dat数据文件转换为json数据
保存到json文件夹中

查询数据加载已经处理好的json文件
转换为字典形式写入内存，转换为键值对，
输入ID查询值

'''
'''

详细数据统计：
2113个用户
10197部电影
20个电影类型
20809个电影分配类型
    平均每个电影2.040个标签
4060个导演
95321个演员
    平均每个电影22.778个演员
    共属于72个国家

 10197 country assignments
         avg. 1.000 countries per movie
   47899 location assignments
         avg. 5.350 locations per movie

   13222 标签
   47957 tag assignments (tas), i.e. tuples [user, tag, movie]
         平均每个用户打 22.696个标签
         平均每个电影 8.117 个标签

  855598 评分
         每个用户平均评分 404.921个
         平均每个电影84.637个评分
         
         
  * movies.dat
   
   	This file contains information about the movies of the database.
   	
   	The original movie information -title and year- available at MovieLens10M dataset 
   	has been extended with public data provided in IMDb and Rotten Tomatoes websites:
   	   - Titles in Spanish
   	   - IMDb movie ids
   	   - IMDb picture URLs
           - Rotten Tomatoes movie ids
           - Rotten Tomatoes picture URLs
           - Rotten Tomatoes (all/top) critics' ratings, avg. scores, numbers of 
             reviews/fresh_scores/rotten_scores
           - Rotten Tomatoes audience' avg. ratings, number of ratings, avg. scores
'''


#############################
#############################

import  json
import numpy as np
import  pandas as pd



#############################
# 用户评分 的词典，输入用户id可查询电影评分及时间戳
#############################
#  把用户电影评分+时间戳转换为字典形式并保存问文件
def User_rated_transTXT2dict():

    user_ratedmovies_timestamps = pd.read_table("user_ratedmovies-timestamps.txt")

    user_ratedmovies_timestamps = np.array(user_ratedmovies_timestamps)
    user_ratedmovies_timestamps=user_ratedmovies_timestamps.astype(np.float)
    # print(user_ratedmovies_timestamps)
    user_ratedmovie_dict = {}  # 把用户评分过的电影转换为字典，可通过字典查找评分过的电影
    for i in user_ratedmovies_timestamps:
        #     print(i)
        #     user_ratedmovie_dict[i[0]]=list(i[1:4])

        if ((i[0] in user_ratedmovie_dict)):  # 若user已经添加进字典中，则值更新

            d = user_ratedmovie_dict[i[0]]
            d.append(list(i[1:4]))
            user_ratedmovie_dict[i[0]] = d
        else:
            d = []
            d.append(list(i[1:4]))
            user_ratedmovie_dict[i[0]] = d  # user还未添加进字典中，则重新添加
    #     break
    # print(user_ratedmovie_dict)
    # print(len(user_ratedmovie_dict[75]))
    filename = "json/user_ratedmovie_dict.json"
    with open(filename, 'w') as f:
        json.dump(user_ratedmovie_dict, f)


    # with open("user_ratedmovie_dict.txt", 'w') as u_r_dict:
    #     u_r_dict.write(str(user_ratedmovie_dict))

#查询用户评分的电影
def select_user_rank():
    with open("json/user_ratedmovie_dict.json") as dict:
        dic=json.load(dict)
        # print(type(dic))
        # print(dic["1"])
        # print(type(dic))
        # print("用户评论电影个数：",len(dic[userID]),"\n","电影列表：",dic[userID])
        return dic


#############################
# 电影演员查询#电影演员
#############################
def movie_actor_transTXT2dict():
    movie_actors = pd.read_table("movie_actors.txt")
    # print(movie_actors)
    movie_actors = np.array(movie_actors)
    # print(movie_actors)

    user_actor_dict = {}  # 把电影的演员转换为字典，可通过字典查找评分过的电影
    for i in movie_actors:
        if(i[0] in user_actor_dict):
           # print(user_actor_dict[i[0]])
           d = user_actor_dict[i[0]]
           d.append((list(i[1:4])))
           user_actor_dict[i[0]]=d

        else:
            d=[]
            d.append(list(i[1:4]))
            user_actor_dict[i[0]]=d
        # break
    # print(user_actor_dict)

    print(len(user_actor_dict))
    filename= "json/user_actor_dict.json"
    with open(filename,'w') as f:
        json.dump(user_actor_dict,f)

#查电影演员
def select_movie_actor(movirID):
    with open("json/user_actor_dict.json") as dict:
        dic=json.load(dict)
        if movirID in dic:
            return dic[movirID]
        else:
            return []





#############################
# 电影导演
#############################
def movie_directors_transTXT2dict():
    movie_directors = pd.read_table("movie_directors.txt")
    # print(movie_actors)
    movie_actors = np.array(movie_directors)
    # print(movie_actors)

    movie_directors_dict = {}  # 把电影的演员转换为字典，可通过字典查找评分过的电影
    for i in movie_actors:
        if(i[0] in movie_directors_dict):
           # print(user_actor_dict[i[0]])
           d = movie_directors_dict[i[0]]
           d.append((list(i[1:3])))
           movie_directors_dict[i[0]]=d

        else:
            d=[]
            d.append(list(i[1:3]))
            movie_directors_dict[i[0]]=d
        # break
    # print(user_actor_dict)

    print(len(movie_directors_dict))
    filename= "json/movie_directors_transTXT2dict.json"
    with open(filename,'w') as f:
        json.dump(movie_directors_dict,f)



#查电影导演
def select_movie_directir(movirID):
    movie_directors = np.array(pd.read_table("data/movie_directors.txt"))
    if int(movirID)  in movie_directors[:,0]:
        index=np.where(movie_directors[:,0]==int(movirID))
        return movie_directors[index[0][0]][2]
    else:
        return ""








#############################
# 电影类型
#############################
def movie_genre_transTXT2dict():
    movie_genre = pd.read_table("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movieID genre.txt")
    movie_genre = np.array(movie_genre)
    print(movie_genre)


    movie_genre_dict = {}  # 把电影的演员转换为字典，可通过字典查找评分过的电影
    for i in movie_genre:
        # print(i[0],type(i[0]),i[1],type(i[1]))
        if(i[0] in movie_genre_dict):
           # print(user_actor_dict[i[0]])
           d = movie_genre_dict[i[0]]
           d.append((i[1]))
           movie_genre_dict[i[0]]=d
        else:
            d=[]
            d.append(i[1])
            movie_genre_dict[i[0]]=d
        # break
    print(movie_genre_dict)

    # print(len(movie_genre))
    filename= "json/movie_genre_transTXT2dict.json"
    with open(filename,'w') as f:
        json.dump(movie_genre_dict,f)

def genrens_list():
    movie_genre = pd.read_table("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movie_genres.txt")
    movie_genre = np.array(movie_genre)
    movie_genre_list=list(set(movie_genre[:,1]))
    # print(movie_genre_list,len(movie_genre_list))
    return movie_genre_list


#查电影类型
def select_genre_directir(movirID):
    with open("json/movie_genre_transTXT2dict.json") as dict:
        dic=json.load(dict)
        # print(type(dic))
        # print(dic["1"])
        # print("类型个数：",len(dic[movirID]),"\n","类型列表：",dic[movirID])
        return dic[movirID]







#############################
# 电影国家
#############################
def movie_countries_list():
    movie_countries = pd.read_table("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movie_countries.txt")
    movie_countries = np.array(movie_countries)
    print(movie_countries[:,1])
    countries=set(movie_countries[:,1])
    print(len(countries),countries)
    return countries



def movie_countries_transTXT2dict():
    movie_countries = pd.read_table("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movie_countries.txt")
    movie_countries = np.array(movie_countries)


    # 保存为json文件
    movie_countries_dict = {}  # 把电影的演员转换为字典，可通过字典查找评分过的电影

    for i in movie_countries:
        movie_countries_dict[i[0]]=i[1]

    # print(len(movie_genre))
    filename= "json/movie_countries_transTXT2dict.json"
    with open(filename,'w') as f:
        json.dump(movie_countries_dict,f)
    





#查电影国家
def select_countries_directir(movirID):
    with open("json/movie_countries_transTXT2dict.json") as dict:
        dic=json.load(dict)
        # print(type(dic))
        # print(dic["1"])
        # print(len(dic))
        # print("电影国家：",dic[movirID])
        return dic[movirID]



#############################
# 电影标签
#############################
def movie_tags_transTXT2dict():
    movie_tags = pd.read_table("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/tags.txt")
    movie_tags = np.array(movie_tags)
    # print(movie_countries)


    movie_tags_dict = {}  # 把电影的演员转换为字典，可通过字典查找评分过的电影

    for i in movie_tags:
        movie_tags_dict[i[0]]=i[1]

    # print(len(movie_genre))
    filename= "json/movie_tags_transTXT2dict.json"
    with open(filename,'w') as f:
        json.dump(movie_tags_dict,f)

#查电影类型
def select_tags_directir(movirID):
    with open("json/movie_tags_transTXT2dict.json") as dict:
        dic=json.load(dict)
        # print(type(dic))
        # print(dic["1"])
        # print("tags：",dic[movirID])
        return dic[movirID]


#############################
# 电影标签权重
#############################
def movie_tags_wight_transTXT2dict():
    movie_tags = pd.read_table("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movie_tags.txt")
    movie_tags = np.array(movie_tags)
    movie_tags=movie_tags.astype(np.str)
    # print(movie_tags)
    # print(movie_tags,movie_tags[1,1],type(movie_tags[1,1]),movie_tags[1:1],type(movie_tags[1:2]))
    # print(movie_tags)
    movie_tags_wight_dict = {}  # 把用户评分过的电影转换为字典，可通过字典查找评分过的电影
    for i in movie_tags:
        # print(i)
        if ((i[0] in movie_tags_wight_dict)):  # 若user已经添加进字典中，则值更新
            d = movie_tags_wight_dict[i[0]]
            d.append(list(i[1:3]))
            movie_tags_wight_dict[i[0]] = d
        else:
            d = []
            d.append(list(i[1:3]))
            movie_tags_wight_dict[i[0]] = d  # user还未添加进字典中，则重新添加
        # break
        # print(len(user_ratedmovie_dict[75]))
    print(movie_tags_wight_dict)
    filename = "json/movie_tags_wight_dict.json"
    with open(filename, 'w') as f:
        json.dump(movie_tags_wight_dict, f)


    # with open("user_ratedmovie_dict.txt", 'w') as u_r_dict:
    #     u_r_dict.write(str(user_ratedmovie_dict))



# 电影标签权重
def select_movie_tags_wight(userID):
    with open("json/movie_tags_wight_dict.json","r") as dict:
        dic=json.load(dict)
        list=[]
        if userID in dic:
            return dic[userID]
        else:
            return list



#############################
# 电影信息
#############################
def movie_dict():
    movie = pd.read_table("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movies.txt")
    movie = np.array(movie)
    print(movie)
    movie_dict={}
    for i in movie:
        i_dict={}
        i_dict["title"] = i[1]
        i_dict["imdbID"] = i[2]
        i_dict["spanishTitle"] = i[3]
        i_dict["imdbPictureURL"] = i[4]
        i_dict["year"] = i[5]
        i_dict["rtID"] = i[6]
        i_dict["rtAllCriticsRating"] = i[7]
        i_dict["rtAllCriticsNumReviews"] = i[8]
        i_dict["rtAllCriticsNumFresh"] = i[9]
        i_dict["rtAllCriticsNumRotten"] = i[10]
        i_dict["rtAllCriticsScore"] = i[11]
        i_dict["rtTopCriticsRating"] = i[12]
        i_dict["rtTopCriticsNumReviews"] = i[13]
        i_dict["rtTopCriticsNumFresh"] = i[14]
        i_dict["rtTopCriticsNumRotten"] = i[15]
        i_dict["rtTopCriticsScore"] = i[16]
        i_dict["rtAudienceRating"] = i[17]
        i_dict["rtAudienceNumRatings"] = i[18]
        movie_dict[i[0]]=i_dict
        # print(i)
        print(movie_dict)
        # break

    print(movie_dict)
    filename = "json/movie_dict.json"
    with open(filename, 'w') as f:
        json.dump(movie_dict, f)



def select_movie(userID):
    with open("json/movies.json", "r") as dict:
        dic = json.load(dict)
        print(dic[userID])
        # print(len(dic))



def readactor():
    movie_actors = pd.read_csv("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movie_actors.csv",header=None)
    # print(movie_actors)
    movie_actors = np.array(movie_actors)
    #
    # print(movie_actors[:,1:4])
    return movie_actors[:,1:4]


def readmovie():
    movie = pd.read_csv("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movies.csv")
    movie = np.array(movie)
    return movie

def readdirector():
    movie_directors=np.array(pd.read_csv("/Users/mingle/Documents/myitem/code/hetrec2011-movielens-2k-v2/data/movie_directors.csv",header=None))
    # print(movie_directors)
    # print(len(movie_directors))
    return movie_directors[:,1:3]



if __name__=="__main__":
    # User_rated_transTXT2dict()
    # select_user_rank('75.0')               #  数字userID 保留意味小数点 可得出评分列表和评分[电影id，评分，时间戳]  输入电影ID为带小数点字符串
    # movie_actor_transTXT2dict()
    # select_movie_actor("3")     #   字符串movieID 可得到演员 列表[演员ID，演员name，排名]
    # movie_directors_transTXT2dict()
    # print(select_movie_directir("99"))
    # movie_genre_transTXT2dict()
    # select_genre_directir("788")
    # movie_countries_transTXT2dict()
    # select_countries_directir("778")
    # movie_tags_transTXT2dict()
    # select_tags_directir()
    # movie_tags_wight_transTXT2dict()
    # print(select_movie_tags_wight("1701"))
    # movie_dict()
    # select_movie("1701")
    # movie_countries_list()
    # genrens_list()
    # readactor()
    # readdirector()
    # readactor()
    select_movie_directir("418")
    print("*****************")
