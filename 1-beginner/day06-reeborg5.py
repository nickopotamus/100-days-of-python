## Final challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move until we hit a wall
while front_is_clear():
    move()
turn_left()
# Follow the right
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
