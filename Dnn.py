import torch
from torch import nn
from torch.nn import  functional as F
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os
'''
定义5层前馈神经网络，激活函数为mish
输入np.array()类型数据，输出转换后的结果
'''
def Five_NN(inputs):
    class MLP(nn.Module):
        def __init__(self, input_dim, hidden1_dim, hidden2_dim, hidden3_dim, hidden4_dim, outcome_dim):
            super(MLP, self).__init__()

            self.linear1 = nn.Linear(input_dim, hidden1_dim)
            self.linear2 = nn.Linear(hidden1_dim, hidden2_dim)
            self.linear3 = nn.Linear(hidden2_dim, hidden3_dim)
            self.linear4 = nn.Linear(hidden3_dim, hidden4_dim)
            self.linear5 = nn.Linear(hidden4_dim, outcome_dim)

        def forward(self, inputs):
            hidden1 = self.linear1(inputs)
            activation1 = F.mish(hidden1)

            hidden2 = self.linear2(activation1)
            activation2 = F.mish(hidden2)

            hidden3 = self.linear3(activation2)
            activation3 = F.mish(hidden3)

            hidden4 = self.linear4(activation3)
            activation4 = F.mish(hidden4)

            hidden5 = self.linear5(activation4)
            activation5=F.mish(hidden5)
            return activation5

    mlp = MLP(input_dim=1024, hidden1_dim=1024, hidden2_dim=1024, hidden3_dim=1024, hidden4_dim=1024, outcome_dim=32)
    # inputs = torch.rand(3, 5)
    # inputs=[[0.3349, 0.7129, 0.0478, 0.6471, 0.5913],
    #     [0.8916, 0.5058, 0.6135, 0.3106, 0.6715],
    #     [0.3273, 0.5561, 0.9530, 0.9191, 0.3938]]
    # print(cosine_similarity(inputs))
    # inputs=torch.Tensor(inputs)
    # probs = mlp(inputs)
    # # print(inputs)
    # # print(mlp)
    # # print("\n")
    # # probs=torch.from_numpy(probs)
    # # print(probs)
    # print(probs)
    inputs=torch.Tensor(inputs)
    probs=mlp(inputs)


    '''查看网络结构信息'''
    # for name, parameters in mlp.named_parameters():
    #     print(name, ':', parameters)

    probs = probs.detach().numpy()
    return probs


def clu_Similarity(x):
    '''输入矩阵，计算两两相似度'''
    x=x.detach().numpy()
    print(x)
    Similarity=cosine_similarity(x)

    print(Similarity)

def main():


    # inputs = [[0.3349, 0.7129, 0.0478, 0.6471, 0.5913],
    #           [0.8916, 0.5058, 0.6135, 0.3106, 0.6715],
    #           [0.3273, 0.5561, 0.9530, 0.9191, 0.3938]]
    #
    #
    #
    #
    # y_pre = Five_NN(inputs)
    # print("5层全连接神经网络处理数据")
    # print(y_pre)
    # # clu_Similarity(pytorch_learn())
    # print("DNN  * !!!!!*****DONE!")


    data_file_path="data/DHE_data/identifivec.csv"
    inputs=np.array(pd.read_csv(data_file_path))[:,1:]
    print(inputs)
    y_pre = Five_NN(inputs)
    print(y_pre,type(y_pre))

    our_DHE_vec_path="data/DHE_data/our_DHE_VEC.csv"
    if os.path.exists(our_DHE_vec_path):
        os.remove(our_DHE_vec_path)
    pd.DataFrame(y_pre).to_csv(our_DHE_vec_path)

if __name__=="__main__":
   main()