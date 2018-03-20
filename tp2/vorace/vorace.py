import sys
import os
from bloque import Bloque


def vorace(fileToRead):
    print(fileToRead)


if __name__ == '__main__':
    txtFiles = os.listdir("../data")
    i = 12
    for file in txtFiles:
        vorace(file)
        if i == 12:
            temp = open("../data/"+file)
            i = i+1

    bloc = Bloque.makeBloque(temp.readline(), 12, 12)
    print(bloc.largeur)


#block = Block(12, 22, 33)
#print block.longueur
#print block.hauteur
#print block.largeur

#F = open("../data/b100_1.txt")
#print F.readline()

