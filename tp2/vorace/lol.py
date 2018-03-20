import sys
import os
from .bloque import Block

txtFiles = os.listdir("../data")


def vorace(fileToRead):
    print(fileToRead)


for file in txtFiles:
    vorace(file)

#block = Block(12, 22, 33)
#print block.longueur
#print block.hauteur 
#print block.largeur

#F = open("../data/b100_1.txt")
#print F.readline()

