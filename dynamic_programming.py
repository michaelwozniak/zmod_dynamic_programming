"""
Program rozwiązujący dwukryterialne zagadnienie alokacji za pomocą programowania dynamicznego. 
autorzy: Michał Woźniak & Michał Wrzesiński - WNE UW
"""

import pandas as pd
import numpy as np
import matplotlib as mp

class dynamic_programming():

    def __init__(self, df):
        self.df = df

    def solve(self):
        lista4 = list()
        for i in range(len(self.df)):
            tmp = [self.df.iloc[i,7],self.df.iloc[i,8]]
            lista4.append(tmp)

        lista3 = list()
        lista3_tmp = list()
        for i in range(len(self.df)):
            foo = list()
            foo1 = list()
            for j in range(i+1):
                tmp = [self.df.iloc[j,5],self.df.iloc[j,6]]
                tmp1 = [self.df.iloc[j,7],self.df.iloc[j,8]]
                foo.append(tmp)
                foo1.append(tmp1)

            lista3.append(foo)
            foo1.reverse()
            lista3_tmp.append(foo1)

        for i in range(len(self.df)):
            for j in range(len(lista3[i])):
                lista3[i][j][0] = lista3[i][j][0] + lista3_tmp[i][j][0] 
                lista3[i][j][1] = lista3[i][j][1] * lista3_tmp[i][j][1] 

        max1_poz = 0
        max2_poz = 0
        repo = list()
        repo1 = list()
        lista3_tmp2 = list()
        for i in range(len(self.df)):
            for j in range(len(lista3[i])):
                repo.append(lista3[i][j][0])
                repo1.append(lista3[i][j][1])
            max1 = max(repo)
            max2 = max(repo1)
            for j in range(len(lista3[i])):
                if(lista3[i][j][0]==max1):
                    max1_poz = j
                if(lista3[i][j][1]==max2):
                    max2_poz = j
            if(max1_poz==max2_poz):
                lista3_tmp2.append(lista3[i][max1_poz])
            else:
                lista3_tmp2.append([lista3[i][max1_poz],lista3[i][max2_poz]])
        lista3_tmp2.reverse()

        lista2 = list()
        for i in range(len(self.df)):
            boolen_tmp = 0
            lista2_tmp = [self.df.iloc[i,3], self.df.iloc[i,4]]
            for j in range(len(lista3_tmp2[i])):
                if(type(lista3_tmp2[i][j]) == list):
                    tmp2 = [lista2_tmp[0]+lista3_tmp2[i][j][0], 
                    lista2_tmp[1]*lista3_tmp2[i][j][1]]
                    lista2.append(tmp2)
                    boolen_tmp = 1
            if(boolen_tmp==0):
                tmp2 = [lista2_tmp[0]+lista3_tmp2[i][0], 
                lista2_tmp[1]*lista3_tmp2[i][1]]
                lista2.append(tmp2)
            
        listaprint = lista2
        for i in range(len(listaprint)):
            print(listaprint[i])


if __name__ == '__main__':
    df = pd.read_excel("football.xlsx", sheet_name='Arkusz3')
    df = df.iloc[0:11,0:9]
    rozwiazanie = dynamic_programming(df)
    rozwiazanie.solve()
