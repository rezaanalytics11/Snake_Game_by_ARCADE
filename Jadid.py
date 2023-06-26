
import arcade

COLUMN_SPACING = 50
ROW_SPACING = 50
LEFT_MARGIN = 25
BOTTOM_MARGIN = 25

class Object(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.r = 5

    def draw(self):
         i=0
         for row in range(10):
            for column in range(10):

                self.center_x = column * COLUMN_SPACING + LEFT_MARGIN
                self.center_y = row * ROW_SPACING + BOTTOM_MARGIN
                i=i+1
                print(i)
                if (row+column)%2==0 :
                    self.color=arcade.color.RED
                else:
                    self.color = arcade.color.BLUE

                arcade.draw_circle_filled(self.center_x, self.center_y, self.r,self.color )


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=500,title='snake game')
        arcade.set_background_color(arcade.color.WHITE)
        self.object=Object()

    def on_draw(self):
        arcade.start_render()
        self.object.draw()


mygame=Game()
arcade.run()