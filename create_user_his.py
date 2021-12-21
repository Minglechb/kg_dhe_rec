from neomodel import config
config.DATABASE_URL = 'bolt://neo4j:chb020218@127.0.0.1:7687'

from create_item_kg import *



class his_movie_rate(StructuredRel):
    rating=FloatProperty()
    timestamp=StringProperty()


class USER(StructuredNode):
    userID=StringProperty()
    his_movie_rate=RelationshipTo('MOVIEREL','评分',model=his_movie_rate)

def create_user():
    user=select_user_rank()
    # usermovie=select_user_rank("75.0")
    # print(len(user),user)
    for i in user:
        # print(i[:-2],user[i])
        userNODE=USER(userID=i[:-2]).save()
        try:

            for j in user[i]:
                # print(j)
                # print(str(j[0])[:-2])
                # print(j[1])
                # print(str(j[2])[:-2])

                try:

                    movieNODE=MOVIEREL.nodes.get(uid=int(str(j[0])[:-2])) #电影的节点
                    rel=userNODE.his_movie_rate.connect(movieNODE)
                    rel.rating=j[1]
                    rel.timestamp=str(j[2])[:-2]
                    rel.save()

                    print(movieNODE,rel)
                    '''  
                    str(j[0])[:-2]       #电影编号
                    j[1][:-2]       #电影评分
                    str(j[2][:-2])    #电影时间戳
                    '''
                    # break
                except:
                    print("创建连接错误！！！！！！！！！！")
                    pass

            # break

        except:
            print("错误***************************************")
            pass


if __name__=="__main__":
    # create_user()
    # allnode=USER.nodes.all()
    # print(len(allnode),allnode)
    print("**********")
