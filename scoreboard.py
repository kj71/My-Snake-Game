from turtle import Turtle, color
ALIGNNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        with open("My-Snake-Game/data.txt", "r") as file:
            self.high_score = int(file.read())
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}" ,align=ALIGNNMENT, font=FONT)
    
    def game_over(self):
        self.high_score = max(self.score, self.high_score)
        with open("My-Snake-Game/data.txt", "w") as file:
            file.write(str(self.high_score))
        self.write_score()
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNNMENT, font=FONT)