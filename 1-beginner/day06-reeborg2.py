## Hurdles - using while loops

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# altered to remove first move()
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
