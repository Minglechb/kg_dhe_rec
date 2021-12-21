import random
from Crypto.Util import number
import numpy as np
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity
from Dnn import Five_NN

'''稠密哈希嵌入，输入特征值X，编码长度K，哈希桶m
    X为特征矩阵
'''
def DeepHashEncoding(X,K,M):
    # 返回具有k_Bit个随机比特位的非负python整数
    k_Bit = 32
    RanadomSeed = 0  # 设置随机种子为0
    '''n_length是素数的“大小”.它将返回大约2 ^ n_length的数字'''
    n_length = 32
    h = np.empty(shape=(len(X),K))
    list_ABP=[]
    for i in range(K):
        list_i_abp=[]
        # 生成随机数A
        a = random.getrandbits(k_Bit)  # 返回具有k个随机比特位的非负python整数
        list_i_abp.append(a)
        # 生成非零随机数B
        bool_B_is_0 = 0
        while (bool_B_is_0 == 0):
            b = random.getrandbits(k_Bit)
            if (b != 0):
                bool_B_is_0 = 1
        list_i_abp.append(b)
        p = number.getPrime(n_length)
        list_i_abp.append(p)
        # print("\n第%d个维度特征的哈希函数生成的参数a:%d，b:%d，p:%d的值"%(i,a,b,p))
        list_ABP.append(list_i_abp)
        filefullpath = "data/DHE_data/parameter.csv"
        if os.path.exists(filefullpath):
            os.remove(filefullpath)
        pd.DataFrame(np.array(list_ABP)).to_csv(filefullpath)
        for ww,val in enumerate(X):
            h[ww,i]=((a*val+b)%p)%M

    encod = Transform(h,K,M)
    # print("特征向量:**********\n",encod)
    return (encod)


# 转换函数 没有进行高斯转换
def Transform(h,K,M):
    encod_ = (h - 1) / (M - 1.1)
    encod = encod_ * 2 - 1
    # print(encod_)
    # for index,val in enumerate(encod_):
    #     print("第%d个的特征向量:"%index,val)
    #     i = 0
    #     while (i < K):
    #         j = i + 1
    #         encod[index][i] = math.sqrt(-2 * math.log(val[i])) * math.cos(2 * math.pi * val[j])
    #         encod[index][j] = math.sqrt(-2 * math.log(val[i])) * math.sin(2 * math.pi * val[j])
    #         i = i + 2
    # print("经过高斯变化处理后的特征向量", encod)
    return (encod)






def main():
    # # 输入x为特征数据
    # x = np.array([333, 233, 9089068,2131,23,456,334,5684,23,46,234251452,332,334,333222])
    # h = DeepHashEncoding(x, 1024, 32)
    # print("\n计算相似度直接使用哈希编码过的特征值计算相似度：************\n",cosine_similarity(h))
    # DHE_VEC=Five_NN(h)
    # print(DHE_VEC)
    # print(cosine_similarity(DHE_VEC))
    filepath="data/allcodingfile/1.txt"
    x=[]


    with open(filepath,"r") as f:
        x_num=int(f.read())
        print(x_num,'\n',type(x_num))
        x.append(x_num)
    h=DeepHashEncoding(x,1024,1000)
    print(h.shape)



if __name__ == "__main__":
    main()