import turtle
import time

class PingPong:
    def __init__(self,ventana) :
        self.windows = ventana.Screen()
        self.scoreA = 0
        self.scoreB = 0
        self.paddleA = ventana.Turtle()
        self.paddleB = ventana.Turtle()
        self.line = ventana.Turtle()
        self.ball = ventana.Turtle()
        self.static = True
        self.pen = ventana.Turtle()
        self.penEnter = ventana.Turtle()
        

    def areaJuego(self):
        self.windows.title("Pong")
        self.windows.bgcolor("#A9A9A9")
        self.windows.setup(width=800, height=600)
        self.windows.tracer(0)
    
    def playerA(self):
        self.paddleA.speed(0)
        self.paddleA.shape("square")
        self.paddleA.color("white")
        self.paddleA.shapesize(stretch_wid=5, stretch_len=1)
        self.paddleA.penup()
        self.paddleA.goto(-350, 0)

    def playerB(self):
        #PALA B
        self.paddleB.speed(0)
        self.paddleB.shape("square")
        self.paddleB.color("white")
        self.paddleB.shapesize(stretch_wid=5, stretch_len=1)
        self.paddleB.penup()
        self.paddleB.goto(350, 0)

    def lineaMedio(self):
        #LINEA DIVISORIA
        self.line.speed(0)
        self.line.shape("square")
        self.line.color("gray")
        self.line.shapesize(stretch_wid=30, stretch_len=0.07)
        self.line.penup()
        self.line.goto(0, 0)  

    def pelota(self):
        #PELOTA
        
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        #velocidad
        self.ball.dx = 0.3
        self.ball.dy = 0.3
        self.static = True      

    def marcadorInicial(self):
        #MARCADOR INICIAL
        
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-2.5, 220)
        self.pen.write("0       0",align="center", font=("Fixedsys", 60, "bold"))

    def marcadorEnter(self):
        #MENSAJE "ENTER".
        
        self.penEnter.speed(0)
        self.penEnter.color("black")
        self.penEnter.penup()
        self.penEnter.hideturtle()
        self.penEnter.goto(0, 120)
        self.penEnter.write("Presione la Tecla Enter",align="center", font=("Fixedsys", 24, "bold"))
    
    def updateScore(self):
        #ACTUALIZA MARCADOR.
        self.pen.clear()
        self.pen.write("{}       {}".format(self.scoreA,self.scoreB),
        align="center", font=("Fixedsys", 60, "bold"))  

    def movePlayerAUP(self):
        #MOVER PALA "A" HACIA ARRIBA
        y = self.paddleA.ycor()
        if y <= 240:
            y += 20
            self.paddleA.sety(y)

    
    def movePlayerADown(self):
        #MOVER PALA "A" HACIA ABAJO
        y = self.paddleA.ycor()
        if y >= -220:
            y -= 20
            self.paddleA.sety(y)

    
    def movePlayerBUP(self):
        #MOVER PARA "B" HACIA ARRIBA
        y = self.paddleB.ycor()
        if y <= 240:
            y += 20
            self.paddleB.sety(y)

    
    def movePlayerBDown(self):
        #MOVER PALA "B" HACIA ABAJO
        y = self.paddleB.ycor()
        if y >= -220:
            y -= 20
            self.paddleB.sety(y)

    
    def initGame(self):
        #INICIAR JUEGO 
        global static
        self.static = False
        self.penEnter.clear()
    
    
    def resetScreen(self):
        #RESTAURAR PANTALLA DE INICIO
        self.ball.goto(0, 0)
        self.ball.dx *= -1    
        self.penEnter.write("PRESIONE LA TECLA ENTER PARA EMPEZAR",
        align="center", font=("Fixedsys", 24, "bold"))
        self.paddleA.goto(-350, 0)
        self.paddleB.goto(350, 0)

    def registroEventos(self):

        #REGISTRAR EVENTOS DE TECLADO.    
        self.windows.listen()
        self.windows.onkeypress(self.movePlayerAUP, "w")
        self.windows.onkeypress(self.movePlayerADown, "s")
        self.windows.onkeypress(self.movePlayerBUP, "Up")
        self.windows.onkeypress(self.movePlayerBDown, "Down")
        self.windows.onkeypress(self.initGame, "Return")

    def desarrolloJuego(self):
        #DESARROLLO DEL JUEGO.
        while True:
            try:
                self.windows.update()
                #MOVER PELOTA
                if self.static == False:
                    self.ball.setx(self.ball.xcor() + self.ball.dx)
                    self.ball.sety(self.ball.ycor() + self.ball.dy)

                #REBOTE EN EL MARGEN SUPERIOR.
                if self.ball.ycor() > 290:
                    self.ball.sety(290)
                    self.ball.dy *= -1

                #REBOTE EN EL MARGEN INFERIOR.
                if self.ball.ycor() < -290:
                    self.ball.sety(-290)
                    self.ball.dy *= -1

                #PELOTA SOBREPASA LA PALA B
                if self.ball.xcor() > 390:
                    self.score_a += 1
                    self.updateScore()
                    self.static = True
                    time.sleep(1)
                    self.resetScreen()

                #PELOTA SOBREPASA LA PALA A
                if self.ball.xcor() < -390:
                    self.score_b += 1
                    self.updateScore()
                    self.static = True
                    time.sleep(1)
                    self.resetScreen()

                #REBOTE EN LA PALA B.
                if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (self.ball.ycor() < self.paddleB.ycor() + 50 and self.ball.ycor() > self.paddleB.ycor() - 50):
                    self.ball.setx(340)
                    self.ball.dx *= -1
                    
                #REBOTE EN LA PALA A
                if (self.ball.xcor() < -340 and self.ball.xcor() > -350) and (self.ball.ycor() < self.paddleA.ycor() + 50 and self.ball.ycor() > self.paddleA.ycor() - 50):
                    self.ball.setx(-340)
                    self.ball.dx *= -1        
                    
            except:
                break
    
    def correr(self):
        self.areaJuego()
        self.playerA()
        self.playerB()
        self.lineaMedio()
        self.pelota()
        self.marcadorInicial()
        self.marcadorEnter()
        #-------------------------
        
        #self.updateScore()
        #self.movePlayerAUP()
        #self.movePlayerADown()
        #self.movePlayerBUP()
        #self.movePlayerBDown()
        #--------------------------
        
        #self.initGame()
        #self.resetScreen()
        #-------------------------
        
        self.registroEventos()
        self.desarrolloJuego()
        
def runPong():        
    windows = turtle
    juego = PingPong(windows)
    juego.correr()
