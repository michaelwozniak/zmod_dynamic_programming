"""
Program rozwiązujący dwukryterialne zagadnienie alokacji za pomocą programowania dynamicznego. 
autorzy: Michał Woźniak & Michał Wrzesiński - WNE UW
"""

import pandas as pd

class dynamic_programming():

    def __init__(self, filename):
        self.df = pd.read_excel(filename) 

    def wydruk(self,listaprint):
        for i in range(len(listaprint)):
            listaprint = self.zakraglenie(listaprint)
            print(listaprint[i])

    def zakraglenie(self,listaprint):
        for i in range(len(listaprint)):
            for j in range(len(listaprint[i])):
                try:
                    listaprint[i][j] = round(listaprint[i][j], 4)
                except:
                    listaprint[i][j][1] = round(listaprint[i][j][1], 4)
        return listaprint

    def solve(self):
        lista4 = list()
        for i in range(len(self.df)):
            tmp = [self.df.iloc[i,5],self.df.iloc[i,6]]
            lista4.append(tmp)

        lista3 = list()
        lista3_tmp = list()
        for i in range(len(self.df)):
            foo = list()
            foo1 = list()
            for j in range(i+1):
                tmp = [self.df.iloc[j,3],self.df.iloc[j,4]]
                tmp1 = [self.df.iloc[j,5],self.df.iloc[j,6]]
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
            lista2_tmp = [self.df.iloc[i,1], self.df.iloc[i,2]]
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
        lista1 = list()
        max_lvl = 0
        pos_lvl = 0
        for i in lista2:
            if(i[0]>max_lvl):
                max_lvl = i[0]
                pos_lvl = i
        lista1.append(pos_lvl)
        max_lvl = 0
        pos_lvl = 0
        for i in lista2:
            if(i[1]>max_lvl):
                max_lvl = i[1]
                pos_lvl = i
        lista1.append(pos_lvl)
        
        lista3_tmp2.reverse()                   
        
        print("REZULTATY: \n")
        print("Wynik ETAPU III")
        self.wydruk(lista4)
        print()
        print("Wynik ETAPU II")
        self.wydruk(lista3_tmp2)
        print()
        print("Wynik ETAPU I - część 1")
        self.wydruk(lista2)
        print()
        print("Wynik ETAPU I - część 2")
        self.wydruk(lista1)
        
    

if __name__ == '__main__':
    print("Proszę podaj nazwę pliku Excel np. 'football_yhat.xlsx'")
    filename = input()
    rozwiazanie = dynamic_programming(filename)
    rozwiazanie.solve()


