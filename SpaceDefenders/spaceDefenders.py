import turtle
import math
import random

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #velocidad de animación
        self.speed(0)
        self.penup() 

class SpaceDefenders:
    
    def __init__(self, window):
        self.window = window
        self.window.setup(width=600, height=600)
        self.window.title("Space Defenders")
        self.window.bgcolor("black")
    #self.window.bgpic("SpaceDefenders/background.gif")
    #Detener actualizaciones de pantalla
    
        self.window.tracer(0)
        self.playerDefns = None
        self.asteroid = None
        self.missile = None
        self.missiles = []
        self.asteroids = []
        self.createGame()
    

    def createGame(self):
        self.ShapeGame()
        self.player()
        self.createMissiles()
        self.createAsteroid()
        self.fireMissile()
        self.actionKeyboard()
        self.loopGame()

    #Definir formas de jugador y asteroides
    def ShapeGame(self):        
        playerVertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
        self.window.register_shape("player", playerVertices)
        asteroidVertices = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10),
                                (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
        self.window.register_shape("asteroid", asteroidVertices)
        
    def getHeadingTo(self, player, asteroid):
        x1 = player.xcor()
        y1 = player.ycor()
        x2 = asteroid.xcor()
        y2 = asteroid.ycor()
        heading = math.atan2(y1 - y2, x1 - x2)
        heading = heading * 180.0 / 3.14159
        return heading

    #Definir jugador   
    def player(self):
        self.playerDefns = Sprite()
        self.playerDefns.color("#102C54")
        self.playerDefns.shape("player")
        self.playerDefns.score = 0
    
    #Creacion de missiles
    def createMissiles(self):
        for i in range(3):
            self.missile = Sprite()
            self.missile.color("red")
            self.missile.shape("arrow")
            self.missile.speed = 0.8
            self.missile.state = "ready"
            self.missile.hideturtle()
            self.missiles.append(self.missile)

    #Creacion de asteroides
    def createAsteroid(self):
        for i in range(5):   
            self.asteroid = Sprite()
            self.asteroid.color("#9B9B9B")
            self.asteroid.shape("asteroid")
            self.asteroid.speed = random.randint(2, 3)/40
            self.asteroid.goto(0, 0)
            heading = random.randint(0, 260)
            distance = random.randint(300, 400)
            self.asteroid.setheading(heading)
            self.asteroid.fd(distance)
            self.asteroid.setheading(self.getHeadingTo(self.playerDefns, self.asteroid))
            self.asteroids.append(self.asteroid)

    #Rotar jugador a la derecha e izquierda
    def rotateLeft(self):
        self.playerDefns.lt(15)
    def rotateRight(self):
        self.playerDefns.rt(15)

    #Disparar missiles    
    def fireMissile(self):
        for missile in self.missiles:
            if missile.state == "ready":
                missile.goto(0, 0)
                missile.showturtle()
                missile.setheading(self.playerDefns.heading())
                missile.state = "fire"
                break

    #Enlazar con teclado
    def actionKeyboard(self):
        self.window.listen()
        self.window.onkey(self.rotateLeft, "Left")
        self.window.onkey(self.rotateRight, "Right")
        self.window.onkey(self.fireMissile, "space")

    def exitGame(self):
        self.window.withdraw()
        #root = Tk()
        #Menu(root)
        #root.mainloop()

    #Loop del juego
    def loopGame(self):
        gameOver = False
        while True:
            self.window.update()
            self.playerDefns.goto(0, 0)            
            #Mover missil
            for missile in self.missiles:
                if missile.state == "fire":
                    missile.fd(missile.speed)
                #Comprobar borde
                if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
                    missile.hideturtle()
                    missile.state = "ready"
            #Iterar array de asteroides
            for asteroid in self.asteroids:    
                #Mover asteroides
                asteroid.fd(asteroid.speed)
                #Comprobar colision entre asteroide y missil
                for missile in self.missiles:
                    if asteroid.distance(missile) < 20:
                        #Restablecer asteroide
                        heading = random.randint(0, 260)
                        distance = random.randint(600, 800)
                        asteroid.setheading(heading)
                        asteroid.fd(distance)
                        asteroid.setheading(self.getHeadingTo(self.playerDefns, self.asteroid))
                        asteroid.speed += 0.01
                        #Restablecer Missile
                        missile.goto(600, 600)
                        missile.hideturtle()
                        missile.state = "ready"
                #Colision asteroide y jugador
                if asteroid.distance(self.playerDefns) < 20:
                    #Restablecer asteroide
                    heading = random.randint(0, 260)
                    distance = random.randint(600, 800)
                    asteroid.setheading(heading)
                    asteroid.fd(distance)
                    asteroid.setheading(self.getHeadingTo(self.playerDefns, self.asteroid))
                    asteroid.speed += 0.005
                    gameOver = True
                
            if gameOver == True:
                self.playerDefns.hideturtle()
                missile.hideturtle()
                for i in self.asteroids:
                    i.hideturtle()
                break
            
def runSpace():
    root = turtle.Screen()
    SpaceDefenders(root)
    root.mainloop()
#runSpace()