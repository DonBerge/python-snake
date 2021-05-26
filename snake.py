from pantalla import Pantalla


class Snake:
    def __init__(self, pantalla, charini='O', charfini='X'):
        self.pantalla = pantalla
        self.coords_list = []
        self.charfini = charfini
        medio = (self.pantalla.width//2, pantalla.height//2)
        self.coords_list.append((charini, medio))
        self.pantalla.insertChar(self.coords_list[0][0],self.coords_list[0][1])

    def printSnake(self):
        for t in reversed(self.coords_list):
            self.pantalla.insertChar(t[0], t[1])

    def cleanSnake(self):
        for t in reversed(self.coords_list):
            self.pantalla.borrarChar(t[1])

    def moveSnake(self, new_coords):
        cl = self.coords_list
        new_x=cl[0][1][0]+new_coords[0]
        new_y=cl[0][1][1]+new_coords[1]
        if(new_x<=0 or new_x>=self.pantalla.width-1 or new_y<=0 or new_y>=self.pantalla.height-1):
            return 
        self.cleanSnake()
        for i in reversed(range(1, len(cl))):
            cl[i] = cl[i-1]
        else:
            cl[0]=(cl[0][0],(new_x,new_y))
        self.printSnake()

    def addNode(self):
        self.coords_list.append((self.charfini, self.coords_list[-1][1]))