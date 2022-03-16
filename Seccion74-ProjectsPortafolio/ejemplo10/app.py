import random
from turtle import *
from time import sleep

BLACK = '#191A19'
GREEN = '#49FF00'
RED = '#FF1700'
BLUE = '#17D7A0'
WHITE = '#F0ECE3'
PURPLE = '#8E05C2'
GREY = '#87AAAA'
YELLOW = '#FFC300'
FONT_LIVES = ('Comic Sans', 14, 'normal')
FONT_GAME_OVER = ('Comic Sans', 40, 'bold')
FONT_SCOREBOARD = ('Comic Sans', 14, 'normal')


def make_alien(colour, color_hex, y_cord):
    """Generate aliens of different color, which are appended in lists."""
    for j in range(11):
        x = -375 + 75 * j
        alien = Turtle()
        alien.color(color_hex)
        alien.penup()
        alien.speed(10)
        alien.shape('alien')
        alien.setposition(x, y_cord)
        alien.setheading(90)
        colour.append(alien)


def make_scoreboard_element(colour, coordinates):

    name = Turtle()
    name.penup()
    name.color(colour)
    name.hideturtle()
    name.goto(coordinates)
    return name


def go_left():
    new_x = galaga.xcor() - 20
    galaga.goto(new_x, galaga.ycor())


def go_right():
    new_x = galaga.xcor() + 20
    galaga.goto(new_x, galaga.ycor())


def fire(alien, colour):
    """Creates the projectiles for each alien group"""
    projectile = Turtle()
    projectile.penup()
    projectile.shape('square')
    projectile.shapesize(stretch_len=0.2, stretch_wid=1.5)
    projectile.color(BLACK)
    projectile.fillcolor(colour)
    projectile.setposition(alien.xcor(), alien.ycor())
    projectiles_alien.append(projectile)


def fire_galaga():
    """Creates projectiles for galaga"""
    projectile = Turtle()
    projectile.penup()
    projectile.shape('square')
    projectile.shapesize(stretch_len=0.2, stretch_wid=1.5)
    projectile.color(BLACK)
    projectile.fillcolor(RED)
    projectile.setposition(galaga.xcor(), galaga.ycor() + 50)
    projectiles.append(projectile)


def fire_alien(group, colour, rng_chances):
    """Calls the fire function at random time instances"""
    for alien in group:
        rng = random.choice(list_of_numbers)
        if rng < rng_chances and alien.isvisible():
            fire(alien, colour)


def move_alien(direction, alien_speed_):
    """Creates the movement for the alien groups based on the direction given"""
    for group in aliens:
        for alien in group:
            x_pos = alien.xcor()
            y_pos = alien.ycor()
            if direction == 'right':
                new_x_pos = x_pos + alien_speed_
                alien.setposition(new_x_pos, y_pos)
            if direction == 'left':
                new_x_pos = x_pos - alien_speed_
                alien.setposition(new_x_pos, y_pos)
            if direction == 'down':
                y_pos = alien.ycor()
                new_y_pos = y_pos - alien_speed_
                alien.setposition(x_pos, new_y_pos)


def check_alien_hit(sensitivity):
    """Check if galaga gets hit, update lives"""
    for prj in projectiles_alien:
        if prj.distance(galaga) < 20 + 3*sensitivity:
            if len(galaga_lives) == 3:
                galaga_lives[2].hideturtle()
                galaga_lives.remove(galaga_lives[2])
            elif len(galaga_lives) == 2:
                galaga_lives[1].hideturtle()
                galaga_lives.remove(galaga_lives[1])
            elif len(galaga_lives) == 1:
                galaga_lives[0].hideturtle()
                galaga_lives.remove(galaga_lives[0])
            prj.hideturtle()
            projectiles_alien.remove(prj)


def check_galaga_hit():
    """Check igf galaga hits the aliens, hide the ones that got hit"""
    for prjc in projectiles:
        for group in aliens:
            for alien in group:
                if prjc.distance(alien) < 20 and prjc.isvisible() and alien.isvisible():
                    prjc.hideturtle()
                    alien.hideturtle()
                    return True


with open('highscore.txt', 'r+') as file:
    old_highscore = file.read()

winner = True
level_num = 0
for level_index in range(10):
    while level_num == level_index and winner:

        game_is_on = True
        projectiles_alien = []
        galaga_lives = []
        projectiles = []
        turquoise = []
        royal = []
        goo = []
        aliens = [turquoise, royal, goo]
        list_of_numbers = list(range(0, 999))

        # Shapes for aliens and galaga
        GALAGA_SHAPE = ((0.5, 12), (0.5, 8), (1.5, 8), (1.5, 6), (2.5, 6), (2.5, 2), (3.5, 2), (3.5, 1), (4.5, 1), (4.5, 4),
                        (5.5, 4), (5.5, -2), (6.5, -2), (6.5, -3), (6.5, -4), (7.5, -4), (7.5, 0), (8.5, 0), (8.5, -8),
                        (7.5, -8), (7.5, -7), (6.5, -7), (6.5, -6), (5.5, -6), (5.5, -5), (4.5, -5), (4.5, -7), (2.5, -7),
                        (2.5, -6), (1.5, -6), (1.5, -9), (-1.5, -9), (-1.5, -6), (-2.5, -6), (-2.5, -7), (-4.5, -7), (-4.5, -5),
                        (-5.5, -5), (-5.5, -6), (-6.5, -6), (-6.5, -7), (-7.5, -7), (-7.5, -8), (-8.5, -8), (-8.5, 0),
                        (-7.5, 0), (-7.5, -4), (-6.5, -4), (-6.5, -3), (-6.5, -2), (-5.5, -2), (-5.5, 4), (-4.5, 4),
                        (-4.5, 1), (-3.5, 1), (-3.5, 2), (-2.5, 2), (-2.5, 6), (-1.5, 6), (-1.5, 8), (-0.5, 8), (-0.5, 12))

        ALIEN_SHAPE = ((-7.5, -10), (-7.5, -15), (-2.5, -15), (-2.5, -20), (-12.5, -20), (-12.5, -15), (-17.5, -15),
                       (-17.5, -5), (-22.5, -5), (-22.5, -15), (-27.5, -15), (-27.5, 0), (-22.5, 0), (-22.5, 5),
                       (-12.5, 5), (-12.5, 0), (-7.5, 0), (-7.5, 5), (-17.5, 5), (-17.5, 10), (-12.5, 10), (-12.5, 15),
                       (-17.5, 15), (-17.5, 20), (-12.5, 20), (-12.5, 15), (-7.5, 15), (-7.5, 10), (7.5, 10), (7.5, 15),
                       (12.5, 15), (12.5, 20), (17.5, 20), (17.5, 15), (12.5, 15), (12.5, 10), (17.5, 10), (17.5, 5),
                       (7.5, 5), (7.5, 0), (12.5, 0), (12.5, 5), (22.5, 5), (22.5, 0), (27.5, 0), (27.5, -15), (22.5, -15),
                       (22.5, -5), (17.5, -5), (17.5, -15), (12.5, -15), (12.5, -20), (2.5, -20), (2.5, -15), (7.5, -15),
                       (7.5, -10))

        screen = Screen()
        screen.title('Space Invaders')
        screen.bgcolor(BLACK)
        screen.setup(width=1500, height=900)
        screen.tracer(0)

        screen.register_shape('galaga', shape=GALAGA_SHAPE)
        screen.register_shape('alien', shape=ALIEN_SHAPE)

        galaga = Turtle()
        galaga.color(RED)
        galaga.fillcolor(GREY)
        galaga.shape('galaga')
        galaga.penup()
        galaga.setheading(90)
        galaga.goto(0, -350)
        galaga.shapesize(stretch_wid=3, stretch_len=3)

        # scoreboard elements
        score = make_scoreboard_element(YELLOW, (0, 410))
        highscore = make_scoreboard_element(YELLOW, (680, 410))
        level = make_scoreboard_element(YELLOW, (-650, 420))

        level_text = make_scoreboard_element(YELLOW, (-730, 420))
        level_text.write('LEVEL', font=FONT_SCOREBOARD)

        lives_text = make_scoreboard_element(WHITE, (-730, -420))
        lives_text.write('LIVES: ', font=FONT_LIVES, align='left')

        game_over_text = make_scoreboard_element(WHITE, (0, 0))
        game_over_text.fillcolor(WHITE)

        for i in range(3):
            life = Turtle()
            life.color(RED)
            life.fillcolor(GREY)
            life.shape('galaga')
            life.penup()
            life.setheading(90)
            x_cor = -650 + 30*i
            life.goto(x_cor, -409)
            galaga_lives.append(life)

        make_alien(royal, PURPLE, 170)
        make_alien(royal, PURPLE, 220)
        make_alien(turquoise, BLUE, 270)
        make_alien(turquoise, BLUE, 320)
        make_alien(goo, GREEN, 370)

        screen.listen()
        screen.onkey(go_left, 'Left')
        screen.onkey(go_right, 'Right')
        screen.onkey(fire_galaga, 'space')

        score_value = 0 + 5500*level_index
        loops = 1
        level_value = level_index+1
        direction_sign = 1
        alien_speed = 15 + level_index*4
        projectile_speed = 20 + level_index*4

        while len(galaga_lives) > 0 and game_is_on:
            sleep(0.05)
            screen.update()
            score.clear()
            score.write(f'{score_value}', font=FONT_SCOREBOARD)
            highscore.write(f'{int(old_highscore)}', font=FONT_SCOREBOARD)
            level.write(f'{level_value}', font=FONT_SCOREBOARD)

            # hide all turtles who escape screen form galaga
            for proj in projectiles:
                y_cor = proj.ycor()
                x_cor = proj.xcor()
                new_y_cor = y_cor + projectile_speed
                if new_y_cor > 450:
                    proj.hideturtle()
                    projectiles.remove(proj)
                else:
                    proj.goto(x_cor, new_y_cor)
            # hide all turtles who escape screen from aliens
            for proj in projectiles_alien:
                y_cor = proj.ycor()
                x_cor = proj.xcor()
                new_y_cor = y_cor - projectile_speed
                if new_y_cor < -450:
                    proj.hideturtle()
                    projectiles_alien.remove(proj)
                else:
                    proj.goto(x_cor, new_y_cor)

            # fire projectiles form all aliens
            fire_alien(turquoise, BLUE, level_index + 2)
            fire_alien(royal, PURPLE, level_index + 2)
            fire_alien(goo, GREEN, level_index + 2)

            # set the grouped movement of all aliens
            if direction_sign == 1 and goo[10].xcor() < 700:
                move_alien('right', alien_speed)
                if goo[10].xcor() > 699:
                    direction_sign *= -1
                    loops += 1
                    if loops % 4 == 0:
                        move_alien('down', alien_speed)
            elif direction_sign == -1 and goo[0].xcor() > -700:
                move_alien('left', alien_speed)
                if goo[0].xcor() < -699:
                    direction_sign *= -1
                    loops += 1
                    if loops % 4 == 0:
                        move_alien('down', alien_speed)

            # Added points per hit
            if check_galaga_hit():
                score_value += 100
            check_alien_hit(level_index)
            screen.update()

            # check if all aliens are nit visible
            win_condition = []
            for group in aliens:
                for alien in group:
                    if not alien.isvisible():
                        win_condition.append(1)
                    else:
                        win_condition.append(0)

            if all(win_condition):
                game_is_on = False
        # Check if aliens reach galaga's height
        for group in aliens:
            for alien in group:
                if alien.ycor() < galaga.ycor() and alien.isvisible():
                    winner = False

        if len(galaga_lives) == 0:
            winner = False
        else:
            level_num += 1
            if level_index != 9:
                screen.clear()

# Print message depending on the result
if winner:
    game_over_text.write('GG', align='center', font=FONT_GAME_OVER)
if not winner:
    game_over_text.write('GAME OVER', align='center', font=FONT_GAME_OVER)

# Updates highscore value
if score_value > int(old_highscore):
    new_highscore = score_value
    with open('highscore.txt', 'w') as file:
        new_highscore_text = old_highscore.replace(old_highscore, str(new_highscore))
        file.write(new_highscore_text)

screen.exitonclick()