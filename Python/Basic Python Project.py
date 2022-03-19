# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]
liste = []
    
def flatten(l):
    for i in l:
        if type(i)==list:
            flatten(i)
        else:
            list.append(i)

flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(liste)

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]
liste = [[1,2],[3,4],[5,6,7]]
new_list = [e[::-1] for e in liste]
print(new_list[::-1])
