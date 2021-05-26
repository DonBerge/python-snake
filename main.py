import msvcrt  # Esto sirve para leer sin presionar enter
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

def main():
   while(True):
      m = getMove()
      if(m==(0,0)):
         return
      else:
         print(m)

main()


