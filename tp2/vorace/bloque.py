class Bloque:
    longueur = 0
    largeur = 0
    hauteur = 0

    def makeBloque(longueur, largeur, hauteur):
        bloc = Bloque()
        bloc.longueur = longueur
        bloc.largeur = largeur
        bloc.hauteur = hauteur
        print(bloc.longueur)
        return bloc

    def test(self):
        print("test")

