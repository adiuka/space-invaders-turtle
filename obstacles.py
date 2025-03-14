import turtle


class Block:
    def __init__(self, x, y):
        self.block = turtle.Turtle()
        self.block.shape("square")
        self.block.color("white")
        self.block.penup()
        self.block.goto(x, y)


    def destroy_block(self):
        self.block.hideturtle()
        self.block.goto(1000, 1000)


class Obstacle:
    def __init__(self, x, y):
        self.blocks = []
        self.create_obstacle(x, y)


    def create_obstacle(self, x, y):
        block_size = 20
        for i in range(-20, 40, block_size):
            for j in range(-20, 40, block_size):
                if (i, j) not in [(-20, 20), (20, 20)]:
                    block = Block(x + i, y + j)
                    self.blocks.append(block)


class Obstacles():
    def __init__(self):
        self.obstacles = []
        self.start_x = -300
        self.create_obstacles()


    def create_obstacles(self):
        for i in range(5):
            obstacle = Obstacle(self.start_x + (i * 150), -250)
            self.obstacles.append(obstacle)