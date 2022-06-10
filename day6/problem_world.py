def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not wall_in_front():
        move()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
