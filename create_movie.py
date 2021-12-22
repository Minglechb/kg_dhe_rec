from neomodel import config
config.DATABASE_URL = 'bolt://neo4j:chb020218@127.0.0.1:7687'

from create_item_kg import *




def create_movie_connet(movie):
    # movie = readmovie()
    # for i in movie:
    #     print(i)
    movieNode=MOVIEREL(uid=movie[0],movie=movie[1],year=movie[5],rtAllCriticsRating=movie[7],rtAllCriticsNumReviews=movie[8],rtAudienceRating=movie[17],rtAudienceNumRatings=movie[18]).save()


    '''创建演员关联'''

    try:

        movieACTOR = select_movie_actor(str(movie[0]))
        # print(movieACTOR)
        for j in movieACTOR:
            try:

                actorid=j[0]
                # print(actorid)
                actorNode=ACTOR.nodes.get(actorid=actorid)
                # print(actorNode)
                rel= movieNode.actor.connect(actorNode)
                print("movieNode.actor********************:",rel)
                # break
            except:
                print("演员列表错误",movie)
                pass
    except:
        print("创建演员关联错误",movie)
        pass

    '''创建导演'''
    try:

        movieDIR=select_movie_directir(str(movie[0]))
        # print(movieDIR[0][0])
        movieDIRNode=DIRECTORS.nodes.get(uid=movieDIR[0][0])
        # print(movieDIRNode)
        rel=movieNode.directors.connect(movieDIRNode)
        print("movieNode.directors.*****************",rel)
    except:
        print("创建导演错误",movie)
        pass



    '''创建标签权重关系 '''
    # 查出电影的所有的标签列表
    try:
        movie_tag_wight = select_movie_tags_wight(str(movie[0]))
        # print(movie_tag_wight, len(movie_tag_wight))
        for j in movie_tag_wight:
            '''j[0]为电影标签序号'''
            tag = select_tags_directir(j[0])  # 查找到了电影的一个标签
            '''j[1]为标签的权重'''  # 查找到了电影的一个标签的权重
            print(tag, j[1])
            # 查处标签列表所对应的标签
            tag_node = TAG.nodes.get(uid=j[0])
            rel = movieNode.tag.connect(tag_node)
            rel.wight = j[1]
            rel.save()
            print("movieNode.tag",rel)
    except:
        print("创建标签错误",movie)
        pass



    '''创建类型关联'''
    try:

        movieDIR = select_genre_directir(str(movie[0]))
        # print(movieDIR)
        for j in movieDIR:
            # print(j)
            genrensNode=GENRES.nodes.get(name=j)
            # print(genrensNode)
            rel= movieNode.genre.connect(genrensNode)
            print("movieNode.genre***********",rel)
    except:
        print("创建类型关联错误",movie)
        pass


    '''创建国家关联'''
    try:

        movieCountry= select_countries_directir(str(movie[0]))
        print(movieCountry)
        countryNode=COUNTRIES.nodes.get(COUNTRIES_name=movieCountry)
        print(countryNode)
        rel= movieNode.countries.connect(countryNode)
        print("movieNode.countries**********",rel)
    except:
        print("创建国家关联错误",movie)
        pass




if __name__=="__main__":
    import multiprocessing
    # create_movie_connet()
    # print("nice!!!!!!!!!!!")

    pool = multiprocessing.Pool()
    res = pool.map(create_movie_connet,readmovie())
    print("**********")

