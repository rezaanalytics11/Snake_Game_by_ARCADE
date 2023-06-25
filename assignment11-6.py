
import arcade
import random

screen_width=500
screen_height=500

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width=8
        self.height=8
        self.color=arcade.color.BLUE
        self.color1 = arcade.color.RED
        self.change_x=0
        self.chage_y=0
        self.center_x= screen_width//2
        self.center_y= screen_height//2
        self.speed= 3
        self.score=0
        self.body=[]



    def move(self):

        self.body.append([self.center_x,self.center_y])
        if len(self.body)>self.score:
            self.body.pop(0)

        if self.change_x >0:
            self.center_x += self.speed

        if self.change_x < 0:
            self.center_x -= self.speed

        if self.change_y > 0:
                self.center_y += self.speed

        if self.change_y < 0:
                self.center_y -= self.speed



    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

        for i in range(len(self.body)):

            if i%2==0:
             arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1], self.width, self.height, self.color1)
            else:
              arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color)

    def eat(self):
        self.score +=1
        if self.score == 0:
            print('Game Over')

    def eat_2(self):
        self.score +=2
        if self.score == 0:
            print('Game Over')

    def eat_minus1(self):
        self.score -=1
        if self.score == 0:
            print('Game Over')


class Apple(arcade.Sprite):
    def __init__(self):
            super().__init__()
            self.width = 30
            self.height = 30
            self.r=30
            self.color=arcade.color.GREEN
            self.center_x= random.randint(0,screen_width)
            self.center_y= random.randint(0,screen_height)

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)


class Text():
    def __init__(self,text):
            self.text =text
            self.width = 1000
            self.height = 1000
            self.color=arcade.color.ORANGE
    def draw(self):
            arcade.draw_text(self.text,start_x=20, start_y=450,color=self.color,font_size=28)


class Golabi(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 60
        self.color = arcade.color.GREEN
        self.center_x = random.randint(0, screen_width)
        self.center_y = random.randint(0, screen_height)

    def draw(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y,self.width,self.height, self.color)

class Shit(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 60
        self.color = arcade.color.BROWN
        self.center_x = random.randint(0, screen_width)
        self.center_y = random.randint(0, screen_height)

    def draw(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y,self.width,self.height, self.color)

class Divar(arcade.Sprite):
    def __init__(self):
            super().__init__()
            self.width = 10
            self.height = 500
            self.color=arcade.color.RED
            self.center_x= 0
            self.center_y= 250

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,self.height, self.color)


class Divar1(arcade.Sprite):
    def __init__(self):
            super().__init__()
            self.width = 10
            self.height = 500
            self.color=arcade.color.RED
            self.center_x= 500
            self.center_y= 250

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,self.height, self.color)


class Divar2(arcade.Sprite):
    def __init__(self):
            super().__init__()
            self.width = 500
            self.height = 10
            self.color=arcade.color.RED
            self.center_x= 250
            self.center_y= 500

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,self.height, self.color)


class Divar3(arcade.Sprite):
    def __init__(self):
            super().__init__()
            self.width = 500
            self.height = 10
            self.color=arcade.color.RED
            self.center_x= 250
            self.center_y= 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,self.height, self.color)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=500,title='snake game')
        arcade.set_background_color(arcade.color.SAND)
        self.snake=Snake()
        self.apple=Apple()
        self.divar=Divar()
        self.divar1=Divar1()
        self.divar2=Divar2()
        self.divar3=Divar3()
        self.golabi=Golabi()
        self.shit=Shit()
        self.text=Text(' ')



    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.divar.draw()
        self.divar1.draw()
        self.divar2.draw()
        self.divar3.draw()
        self.golabi.draw()
        self.shit.draw()
        self.text.draw()




    def on_update(self,delta_time:float):
         self.snake.move()
         if arcade.check_for_collision(self.snake,self.apple):
             self.snake.eat()
             self.apple=Apple()
             self.text=Text('Winner')
             print(self.snake.score)

         elif arcade.check_for_collision(self.snake,self.golabi):
             self.snake.eat_2()
             self.golabi=Golabi()
             self.text=Text('Winner')
             print(self.snake.score)



         elif arcade.check_for_collision(self.snake,self.shit):
             self.snake.eat_minus1()
             self.shit=Shit()
             self.text=Text('Loser')
             print(self.snake.score)






         elif arcade.check_for_collision(self.snake, self.divar):
             self.snake.change_x = 1
             self.snake.change_y = 0


         elif arcade.check_for_collision(self.snake, self.divar1):
             self.snake.change_x = -1
             self.snake.change_y = 0

         elif arcade.check_for_collision(self.snake, self.divar1):
            self.snake.change_x = -1
            self.snake.change_y = 0


         elif arcade.check_for_collision(self.snake, self.divar2):
            self.snake.change_x = 0
            self.snake.change_y = -1


         elif arcade.check_for_collision(self.snake, self.divar3):
            self.snake.change_x = 0
            self.snake.change_y = 1



    def on_key_release(self,key:int,modifiers:int):
        if key==arcade.key.LEFT:
           self.snake.change_x= -1
           self.snake.change_y = 0

        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1



my_game=Game()
arcade.run()
