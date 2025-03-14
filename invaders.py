import turtle
import random
from invader_bullet import InvaderBullet


class Invader:
    def __init__(self, x, y):
        self.invader = turtle.Turtle()
        turtle.register_shape("assets/invader2.gif")
        self.invader.shape("assets/invader2.gif")
        self.invader.penup()
        self.invader.goto(x, y)

    
    def get_position(self):
        return self.invader.xcor(), self.invader.ycor()


class Invaders:
    def __init__(self):
        self.y_start = 100
        self.y_end = 300
        self.invaders = []
        self.bullets = [InvaderBullet() for _ in range(3)] # Three Bullets Max, change for more
        self.invader_speed = 10
        self.direction = 1
        self.create_invaders()
        self.schedule_fire()

    
    def create_row(self, y):
        for i in range(-200, 200, 40):
            invader = Invader(i, y)
            self.invaders.append(invader)

    
    def create_invaders(self):
        for i in range(self.y_start, self.y_end, 30):
            self.create_row(i)

    
    def move_invaders(self):
        edge_reached = False
        for invader in self.invaders:
            new_x = invader.invader.xcor() + (self.invader_speed * self.direction)
            invader.invader.setx(new_x)
            if new_x > 360 or new_x < -360:
                edge_reached = True        
        if edge_reached:
            self.direction *= -1
            for invader in self.invaders:
                invader.invader.sety(invader.invader.ycor() - 10)
        turtle.ontimer(self.move_invaders, 1000)

    
    def schedule_fire(self):
        if self.invaders:
            shooter = random.choice(self.invaders)
            x, y = shooter.get_position()
            for bullet in self.bullets:
                if not bullet.active:
                    bullet.fire(x, y)
                    break
        turtle.ontimer(self.schedule_fire, random.randint(1000, 3000))
    