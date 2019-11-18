import turtle as trtl
import random as rand

apple_image = "apple.gif"
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50

screen_height = 400
screen_width = 400
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 

active_apple = trtl.Turtle()
wn.bgpic("tree.gif")
active_apple.penup()
wn.tracer(False)

def draw_letter(letter,active_apple):
  active_apple.color("blue")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 50, "bold"))
  active_apple.setpos(remember_position)

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_letter("A", active_apple)
  wn.update()

draw_apple(active_apple)
wn.onkeypress(draw_letter, "a")
wn.listen()

def drop_apple():
  wn.tracer(True)
  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.clear()
  active_apple.ht()
  wn.tracer(False)
  
def reset_apple(active_apple):
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2) , rand.randint(-(screen_height)/2, (screen_height)/2))
    draw_apple (active_apple, letter_list.pop(index))
  
wn.onkeypress(drop_apple, "a")    
wn = trtl.Screen()
trtl.mainloop()
