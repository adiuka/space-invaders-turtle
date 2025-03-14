import turtle


class ScoreBoard():
    def __init__(self):
        self.score_board = turtle.Turtle()
        self.score_board.color("white")
        self.score_board.penup()
        self.score_board.hideturtle()
        self.lives = 3
        self.points = 0


    def give_points(self):
        self.points += 5


    def update_scoreboard(self):
        self.score_board.clear()
        self.score_board.goto(-380, 365)
        self.score_board.write(f"Score: {self.points}", align='left', font=("Courier", 20, "normal"))
        self.score_board.goto(-380, 325)
        self.score_board.write(f"Lives: {self.lives}", align='left', font=("Courier", 20, "normal"))

    
    def game_over(self):
        self.score_board.goto(-120, 0)
        self.score_board.write(f"Game Over! Score: {self.points}", align='left', font=("Courier", 20, "normal"))

    def you_win(self):
        self.score_board.goto(-120, 0)
        self.score_board.write(f"You win! Score: {self.points}", align='left', font=("Courier", 20, "normal"))