
import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Rectangle"


def draw_background():

    arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH , SCREEN_HEIGHT,
                                 arcade.color.SKY_BLUE)


def draw_blue(center_x, center_y,color):

    arcade.draw_rectangle_filled(center_x, center_y, 40, 40,color)


def Game():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Rectangle')

    arcade.start_render()

    draw_background()
    k=[]
    for x in range(90, SCREEN_WIDTH, 140):
         k.append(x)
         for i in range(len(k)):
             if i%2==0:
              draw_blue(x, SCREEN_HEIGHT / 3,arcade.color.BLUE)

             else:
              draw_blue(x, SCREEN_HEIGHT / 3, arcade.color.RED)


    for x in range(90, SCREEN_WIDTH, 140):
         k.append(x)
         for i in range(len(k)):
             if i%2==0:
              draw_blue(x, (SCREEN_HEIGHT / 3)+60,arcade.color.RED)

             else:
              draw_blue(x, (SCREEN_HEIGHT / 3)+60, arcade.color.BLUE)


    for x in range(90, SCREEN_WIDTH, 140):
         k.append(x)
         for i in range(len(k)):
             if i%2==0:
              draw_blue(x, (SCREEN_HEIGHT / 3)+120,arcade.color.BLUE)

             else:
              draw_blue(x, (SCREEN_HEIGHT / 3)+120, arcade.color.RED)


    for x in range(90, SCREEN_WIDTH, 140):
         k.append(x)
         for i in range(len(k)):
             if i%2==0:
              draw_blue(x, (SCREEN_HEIGHT / 3)+180,arcade.color.RED)

             else:
              draw_blue(x, (SCREEN_HEIGHT / 3)+180, arcade.color.BLUE)


    for x in range(90, SCREEN_WIDTH, 140):
        k.append(x)
        for i in range(len(k)):
            if i % 2 == 0:
                draw_blue(x, (SCREEN_HEIGHT / 3) + 240, arcade.color.BLUE)

            else:
                draw_blue(x, (SCREEN_HEIGHT / 3) + 240, arcade.color.RED)


    for x in range(90, SCREEN_WIDTH, 140):
         k.append(x)
         for i in range(len(k)):
             if i%2==0:
              draw_blue(x, (SCREEN_HEIGHT / 3)+300,arcade.color.RED)

             else:
              draw_blue(x, (SCREEN_HEIGHT / 3)+300, arcade.color.BLUE)


    arcade.finish_render()

my_game=Game()
arcade.run()





