import turtle


class InvaderBullet():

    def __init__(self):
        self.bullet = turtle.Turtle()
        self.bullet.shape("square")
        self.bullet.shapesize(stretch_wid=0.8, stretch_len=0.2)
        self.bullet.color("red")
        self.bullet.penup()
        self.bullet.hideturtle()
        self.bullet_speed = 15
        self.active = False
        
    
    def move(self):
        if self.active:
            new_y = self.bullet.ycor() - self.bullet_speed
            self.bullet.sety(new_y)
            if self.bullet.ycor() <= -400:
                self.bullet_reset()
            else:
                turtle.ontimer(self.move, 50)

    
    def fire(self, x, y):
        if not self.active:
            self.active = True
            self.bullet.goto(x, y - 10)
            self.bullet.showturtle()
            self.move()

    
    def bullet_reset(self):
        self.active = False
        self.bullet.hideturtle()
        self.bullet.goto(1000, 1000)