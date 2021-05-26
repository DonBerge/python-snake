from pantalla import Pantalla


class Snake:
    def printSnake(self):
        for t in reversed(self.coords_list):
            self.pantalla.insertChar(t[0], t[1])

    def moveSnake(self, new_coords):
        cl = self.coords_list
        for i in reversed(range(1, len(cl))):
            cl[i] = cl[i-1]
        else:
            cl[0]=(cl[0][0],cl[0][1]+new_coords)

    def cleanSnake(self):
        for t in reversed(self.coords_list):
            self.pantalla.borrarChar(t[1])

    def __init__(self, pantalla, charini='O', charfini='X'):
        self.pantalla = pantalla
        self.coords_list = []
        self.charfini = charfini
        medio = (pantalla.width//2, pantalla.height//2)
        self.coords_list.append((charini, medio))

    def addNode(self):
        self.coords_list.append((self.charfini, self.coords_list[-1][1]))