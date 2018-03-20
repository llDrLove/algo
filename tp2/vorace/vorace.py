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

    bloc = Bloque(5)
    print(bloc.getLongueur())
