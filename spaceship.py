import turtle
from spaceship_bullet import SpaceShipBullet



class SpaceShip():

    def __init__(self):
        self.player = turtle.Turtle()
        turtle.register_shape("assets/spaceship.gif")
        self.player.shape("assets/spaceship.gif")
        self.player.penup()
        self.spaceship_speed = 10
        self.player.goto(0, -370)
        self.moving_left = False
        self.moving_right = False

        self.bullet = SpaceShipBullet()


    def shoot(self):
        self.bullet.fire(self.player.xcor(), self.player.ycor())


    def move_left(self):
        self.moving_left = True
        self.move_spaceship()


    def more_right(self):
        self.moving_right = True
        self.move_spaceship()


    def stop_left(self):
        self.moving_left = False

    
    def stop_right(self):
        self.moving_right = False


    def move_spaceship(self):
        if self.moving_left:
            if self.player.xcor() >= -370:
                x = self.player.xcor()
                self.player.setx(x - self.spaceship_speed)
        if self.moving_right:
            if self.player.xcor() <= 370:
                x = self.player.xcor()
                self.player.setx(x + self.spaceship_speed)

        