import turtle
import time
import random

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #velocidad de animación
        self.speed(0)
        self.penup()

posponer = 0.1

class Ventana:
    def __init__(self, windown):
        self.windown = windown
        self.windown.title("Juego de Snake")
        self.windown.bgcolor("Black")
        #self.windown.bgpic("borde.gif")
        self.windown.setup(width=600, height=600)
        self.windown.tracer(0)
        self.windown.listen()
        self.windown.onkeypress(self.up, "Up")
        self.windown.onkeypress(self.down, "Down")
        self.windown.onkeypress(self.left, "Left")
        self.windown.onkeypress(self.right, "Right")
        self.segment = []
        self.head = None
        self.text = None
        self.food = None
        self.createGame()
        
    def createGame(self):
        self.cabeza()
        self.comida()
        self.textos()
        self.controlSnake()

    def cabeza(self):
        self.head = Sprite()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Stop"
    
    def comida(self):
        self.food = Sprite()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("blue")
        self.food.penup()
        self.food.goto(0, 100)

    def textos(self):
        self.text = Sprite()
        self.text.speed(0)
        self.text.color("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.goto(0, 260)
        self.text.write("Score: 0       High Score: 0",
        align="center", font = ("Courier", 18, "normal"))

    def up(self):
        self.head.direction = "up"

    def down(self):
        self.head.direction = "down"

    def left(self):
        self.head.direction = "left"

    def right(self):
        self.head.direction = "right"

    def moveSnake(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)
    
    def controlSnake(self):
        score = 0
        highScore = 0
        windown = turtle.Screen()
        while True:
            windown.update()

            #Colisiones bordes 
            if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
                time.sleep(1)
                self.head.goto(0, 0)
                self.head.direction = "stop"
                #Esconder segmentos
                for seg in self.segment:
                    seg.goto(1000, 1000)
                #Limpiar lista de segmentos
                self.segment.clear()
            
                #Resetear marcador
                score = 0
                self.text.clear()
                self.text.write("Score: {}       High Score: {}".format(score, highScore),
                align="center", font = ("Courier", 18, "normal"))

            #Colision con la comida
            if self.head.distance(self.food) < 20:
                #Mover la comida a posicion random
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                self.food.goto(x, y)

                newSegment = turtle.Turtle()
                newSegment.speed(0)
                newSegment.shape("square")
                newSegment.color("grey")
                newSegment.penup() 
                self.segment.append(newSegment)

                #Aumentar marcador
                score += 10
                if score > highScore:
                    highScore = score

                self.text.clear()
                self.text.write("Score: {}       High Score: {}".format(score, highScore),
                align="center", font = ("Courier", 18, "normal"))
    
            #Mover cuerpo de la serpiente
            totalSeg = len(self.segment)
            for index in range(totalSeg - 1, 0, -1):
                x = self.segment[index - 1].xcor()
                y = self.segment[index - 1].ycor()
                self.segment[index].goto(x, y)
            if totalSeg > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segment[0].goto(x, y)

            ventana = Ventana
            ventana.moveSnake(self)

            #Colisiones con el cuerpo
            for seg in self.segment:
                if seg.distance(self.head) < 20:
                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"
                    #Esconder segmentos
                    for seg in self.segment:
                        seg.goto(1000, 1000)
                    self.segment.clear()

                    #Resetear marcador
                    score = 0
                    self.text.clear()
                    self.text.write("Score: {}       High Score: {}".format(score, highScore),
                    align="center", font = ("Courier", 18, "normal"))            
            time.sleep(posponer)   

def runSnake():
    window = turtle.Screen()
    Ventana(window)
    window.mainloop()
