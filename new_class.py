from cityhash import CityHash32
class Moive:
    def __init__(self,MOVIE_ID,countries,directors,genre,tags,actor):
        self.ID = MOVIE_ID
        self.countries = countries
        self.directors = directors
        self.genre = genre
        self.tags = tags
        self.actor = actor
    def show(self):
        print('电影信息：',self.ID,
              self.countries,
              self.directors,"\n",
              self.genre,len(self.genre),"\n",
              self.tags,len(self.tags),"\n",
              self.actor,len(self.actor),"\n")




class MOVIE_CODE:  #对属性进行编码
    def __init__(self,movie,countriesList,director,genres):
        self.countriesList=countriesList
        self.Movie=movie
        self.Director=director
        self.genreList=genres

    def code_ID(self):
        id = '{:0>7s}'.format(self.Movie.ID)
        id = '{:1>8s}'.format(id)
        # print(id)
        # print(type(MOVIE.ID))
        return id

    def code_get_country_Index(self):
        if self.Movie.countries in self.countriesList:
            index=self.countriesList.index(self.Movie.countries)
            # print(type(index))
            index='{:0>3d}'.format(index)
            return index
        else:
            return "111"

    def code_get_director_Inde(self):
        # print(self.Director)
        if self.Movie.directors in self.Director:
            index=self.Director.index(self.Movie.directors)
        # print(index)
            index='{:0>5d}'.format(index)
        # print(type(index))
            return index
        else:
            return '11111'

    def code_get_genre_index(self):
        genres_Index_List=[]
        for i in self.Movie.genre:
            index=self.genreList.index(i)
            index='{:0>3d}'.format(index)
            genres_Index_List.append(index)
        return genres_Index_List


    def code_tag(self):
        tag_list=[]
        for i in self.Movie.tags:
            tag_list.append('{:0>6d}'.format(i))
        return tag_list
    def code_actor(self):
        actor_code_list=[]
        actLIS=list(self.Movie.actor)
        for i in actLIS:
            code_act=CityHash32(i[1])
            code_act='{:0>13d}'.format(code_act)
            # print(len(code_act))
            actor_code_list.append(code_act)
        return actor_code_list

    def CODE(self):
        code=self.code_ID()+self.code_get_country_Index()+self.code_get_director_Inde()
        print("ID+国家，+导演编码：",code,len(code))
        g_L=len(self.code_get_genre_index())   #'''类型的个数，全部都统一为2个'''
        g_List=self.code_get_genre_index()
        if g_L>=2:
            # print("类型值大于等于2")
            g_List=g_List[:2]
        else:
            g_List.append("111")
        print(g_List)
        for i in g_List:
            code = code + i


        tag_L=len(self.code_tag())
        tag_list=self.code_tag()
        if tag_L>=10:
            tag_list=tag_list[:10]
        else:
            less=10-tag_L
            for i in range(less):
                tag_list.append("111111")
        tag_list=tag_list[::-1]
        for i in tag_list:
            code=code+i
        print(tag_list,len(tag_list))

        act_List=self.code_actor()
        act_L=len(act_List)

        if act_L>=22:
            act_List=act_List[:22]
        else:
            less=22-act_L
            for i in range(less):
                act_List.append('1111111111111')

        act_List=act_List[::-1]
        print(act_List,len(act_List))
        for i in act_List:
            code=code+i
        # print(code)
        return code















