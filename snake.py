from pantalla import Pantalla
import random

def printFruit(screen):
    coords = (random.randint(1,screen.width-2),random.randint(1,screen.height-2)) 
    while(screen[coords[1]][coords[0]]!=' '):
        coords = (random.randint(1,screen.width),random.randint(1,screen.height))
    screen.insertChar('F',coords)

class Snake:
    def __init__(self, pantalla, charini='O', charfini='X'):
        self.pantalla = pantalla
        self.coords_list = []
        self.charfini = charfini
        medio = (self.pantalla.width//2, pantalla.height//2)
        self.coords_list.append((charini, medio))
        self.pantalla.insertChar(self.coords_list[0][0],self.coords_list[0][1])
        printFruit(self.pantalla)

    def printSnake(self):
        for t in reversed(self.coords_list):
            self.pantalla.insertChar(t[0], t[1])

    def cleanSnake(self):
        for t in reversed(self.coords_list):
            self.pantalla.borrarChar(t[1])

    def addNode(self):
        self.coords_list.append((self.charfini, self.coords_list[-1][1]))

    def moveSnake(self, new_coords):
        cl = self.coords_list
        new_x=cl[0][1][0]+new_coords[0]
        new_y=cl[0][1][1]+new_coords[1]
        if(new_x<=0 or new_x>=self.pantalla.width-1 or new_y<=0 or new_y>=self.pantalla.height-1):
            return
        new_pos_cabeza =self.pantalla[self.pantalla.height-new_y-1][new_x]
        if(new_pos_cabeza!=' ' and new_pos_cabeza!='F'):
            return False
        addFruit = (new_pos_cabeza=='F')
        if(addFruit):
            self.addNode()
        self.cleanSnake()
        for i in reversed(range(1, len(cl))):
            cl[i] = cl[i-1]
        else:
            cl[0]=(cl[0][0],(new_x,new_y))
        self.printSnake()
        if(addFruit):
            printFruit(self.pantalla)
        return True