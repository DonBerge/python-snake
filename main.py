import msvcrt  # Esto sirve para leer sin presionar enter
import os
import sys
from pantalla import Pantalla
from snake import Snake

def getch():
   return msvcrt.getch()

def getMove():
   char = getch().lower()
   switch = {
      b'w':(0,1),
      b's':(0,-1),
      b'a':(-1,0),
      b'd':(1,0),
      b'\x1b': (0,0) # ESC
   }
   return switch.get(char)

def clrscr():
   comando_borra_pantalla = "cls" if sys.platform == "win32" else "clear"
   os.system(comando_borra_pantalla)

def main():
   scr = Pantalla()
   snk = Snake(scr)
   while(True):
      clrscr()
      print(scr)
      print("Pulsa escape para salir...")
      m = getMove()
      if(m==(0,0)):
         return
      else:
         snk.moveSnake(m)
      snk.printSnake()
         

main()


