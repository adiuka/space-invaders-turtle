from turtle import Screen
from spaceship import SpaceShip
from invaders import Invaders
from obstacles import Obstacles
from scoreboard import ScoreBoard



class Game():
    def __init__(self):
        # Screen Set Up
        self.screen = Screen()
        self.screen.setup(800, 800)
        self.screen.bgcolor("black")
        self.screen.title("turtle_space_invader")
        self.screen.tracer(0)
        # Objects
        self.invaders = Invaders()
        self.obstacles = Obstacles()
        self.player_spaceship = SpaceShip()
        self.scoreboard = ScoreBoard()
        # Starting Function Calls
        self.invaders.move_invaders()
        self.scoreboard.update_scoreboard()
        # Starting Game State
        self.game_on = True


    def check_player_bullets(self):
        for invader in self.invaders.invaders:
            if self.player_spaceship.bullet.bullet.distance(invader.invader) < 15:
                invader.invader.hideturtle()
                self.invaders.invaders.remove(invader)
                invader.invader.goto(400, 400)
                self.scoreboard.give_points()
                self.scoreboard.update_scoreboard()
                self.player_spaceship.bullet.bullet_reset()
        for obstacle in self.obstacles.obstacles:
            for block in obstacle.blocks:
                if self.player_spaceship.bullet.bullet.distance(block.block) < 15:
                    block.destroy_block()
                    obstacle.blocks.remove(block)
                    self.player_spaceship.bullet.bullet_reset()

    
    def check_invader_bullets(self):
        for obstacle in self.obstacles.obstacles:
            for block in obstacle.blocks:
                for bullet in self.invaders.bullets:
                    if bullet.bullet.distance(block.block) < 15:
                        block.destroy_block()
                        bullet.bullet_reset()
        for bullet in self.invaders.bullets:
            if bullet.bullet.distance(self.player_spaceship.player) < 15:
                self.scoreboard.lives -= 1
                bullet.bullet_reset()
                self.scoreboard.update_scoreboard()

    def game_over(self):
        if self.scoreboard.lives == 0:
            self.game_on = False
            self.scoreboard.game_over()
            self.screen.update()
            self.screen.mainloop()


    def you_win(self):
        if len(self.invaders.invaders) == 0:
            self.game_on = False
            self.scoreboard.you_win()
            self.screen.update()
            self.screen.mainloop()



    def game_start(self):
        self.screen.listen()
        self.screen.onkeypress(self.player_spaceship.move_left, "Left")
        self.screen.onkeyrelease(self.player_spaceship.stop_left, "Left")
        self.screen.onkeypress(self.player_spaceship.more_right, "Right")
        self.screen.onkeyrelease(self.player_spaceship.stop_right, "Right")
        self.screen.onkeypress(self.player_spaceship.shoot, "space")

        while self.game_on:
            self.screen.update()

            self.check_player_bullets()
            self.check_invader_bullets()
            self.game_over()
            self.you_win()