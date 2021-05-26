class Pantalla:
    def __init__(self, _screen=[], _width=70, _height=23, hori='-', verti='|', borde='.'):
        self.screen = []
        self.width = _width
        self.height = _height

        barra_superior = [borde]  # La barras que estan tanto arriba como abajo
        barra_media = [verti]  # La barra que estan a los lados

        for i in range(0, _width-2):
            barra_superior.append(hori)
            barra_media.append(' ')
        else:
            barra_superior.append(borde)
            barra_media.append(verti)

        self.screen.append(barra_superior.copy())
        for i in range(0, _height-2):
            self.screen.append(barra_media.copy())
        else:
            self.screen.append(barra_superior.copy())

    def parseCoord(self, coords):
        return (coords[0], self.height-coords[1]-1)

    def insertChar(self, c, coords):
        coords = self.parseCoord(coords)
        x = coords[0]
        y = coords[1]
        self.screen[y][x] = c

    def borrarChar(self, coords):
        self.insertChar(' ', coords)

    def __getitem__(self, key):
        return self.screen[key]

    def __str__(self):
        s = ""
        for sc in self.screen:
            for c in sc:
                s += c
            s += '\n'
        return s
