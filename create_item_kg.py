from neomodel import config
config.DATABASE_URL = 'bolt://neo4j:chb020218@127.0.0.1:7687'


from neomodel import *
from readdata import *

class ACTOR(StructuredNode):
    actorid=StringProperty(StringProperty=True)
    actorName = StringProperty()
    ranking=IntegerProperty()


def create_actor():
    actor=readactor()
    for i in actor:
        print(i,"\n")
        print(i[0],type(i[0]),i[1],type(i[1]),i[2],type(i[2]))
        actorNode=ACTOR(actorid=i[0],actorName=i[1],ranking=i[2]).save()
    # actorNode=ACTOR(actorid=actor[0][0],actorName=actor[0][1],ranking=actor[0][2]).save()
    # print(actorNode)

class COUNTRIES(StructuredNode):
    COUNTRIES_name=StringProperty(unique_index=True)


class DIRECTORS(StructuredNode):
    uid=StringProperty(StringProperty=True)
    name=StringProperty()

def createdirect():
    Dir=readdirector()
    # print(Dir)
    for i in Dir:
        # print(i,"\n")
        # print(i[0],i[1])
        dirNode = DIRECTORS(uid=i[0], name=i[1]).save()
        # break
        print(dirNode)


class TAG(StructuredNode):
    uid=StringProperty(StringProperty=True)
    tag = StringProperty()


class RATE(StructuredRel):
    rate = StringProperty()
    time = StringProperty()





class GENRES(StructuredNode):
    name=StringProperty(unique_index=True)

def create_tag():
    with open("json/movie_tags_transTXT2dict.json") as dict:
        dic = json.load(dict)
        # print(dic)
        for i in dic:
            print(i,dic[i])
            node=TAG(uid=i,tag=dic[i]).save()
            # node.refresh()

def create_countries():
    countries_list=movie_countries_list()
    for i in countries_list:
        print(i)
        COUNTRIES_node=COUNTRIES(COUNTRIES_name=i).save()

def create_genres():
    movie_genre_list=genrens_list()
    # print(movie_genre_list)
    for i in movie_genre_list:
        print(i)
        node=GENRES(name=i).save()





class tag_wight(StructuredRel):
    wight=StringProperty()

class MOVIEREL(StructuredNode):
    uid=IntegerProperty()
    movie=StringProperty(StringProperty=True)
    year=IntegerProperty()
    rtAllCriticsRating=StringProperty()
    rtAllCriticsNumReviews=StringProperty()
    rtAudienceRating=StringProperty()
    rtAudienceNumRatings=StringProperty()

    actor=RelationshipTo (ACTOR,'演员')
    directors=RelationshipTo(DIRECTORS,'导演')
    tag=RelationshipTo("TAG",'标签',model=tag_wight)
    genre=RelationshipTo(GENRES,'类型')
    countries=RelationshipTo(COUNTRIES,'国家')







if __name__=="__main__":

    # create_tag()
    # create_countries()
    # create_genres()
    # create_actor()
    # createdirect()

    # allnode=TAG.nodes.all()
    # print(len(allnode))
    # create_movie_connet()
    node=DIRECTORS.nodes.all()
    print(len(node))
    print("**************")