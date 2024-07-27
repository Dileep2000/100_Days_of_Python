"""
Reborgs world
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
"""


def turn_left():

    pass


def move():
    pass


def at_goal():
    pass


def wall_in_front():
    return True


def front_is_clear():
    return True


def wall_on_front():
    return True


def right_is_clear():
    return True


def wall_on_right():
    return True

# Above functions are made and not used. Just created so that the file doesn't have any errors.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def make_a_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()


make_a_square()

# Hurdle 1


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()

# Hurdle 3


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if not (wall_in_front()):
        move()
    else:
        move()

# Hurdle 4


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if not (wall_in_front()):
        move()
    else:
        jump()

# Maze

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
