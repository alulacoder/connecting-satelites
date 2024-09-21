# import pgzrun
# from random import randint
# from time import time

# WIDTH = 1000
# HEIGHT = 800

# satellites = []
# lines = []
# next_satellite = 0


# start_time = 0
# total_time = 0
# end_time = 0

# number_of_satellite = 8



# def create_satellites():
#     global start_time
#     for count in range(0, number_of_satellite):
#         satellite = Actor("satellite")
#         satellite.pos = randint(40,WIDTH- 40), randint(40, HEIGHT-40)
#         satellites.append(satellite)
#     start_time = time()    


# def draw():
#     global total_time


#     screen.blit("space",(0,0))
#     number = 1
#     for satellite in satellites:
#         screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))
#         satellite.draw()
#         number = number + 1

#     for line in lines:
#         screen.draw.line(line[0], line[1], (255,100,150))

#     if next_satellite < number_of_satellite:
#         total_time = time() - start_time
#         screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)
#     else:
#         screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)


# def update():
#     pass

# def on_mouse_down(pos):
#     global next_satellite, lines


#     if next_satellite < number_of_satellite:
#         if satellites[next_satellite].collidepoint(pos):
#             if next_satellite:
#                 lines.append((satellites[next_satellite-1].pos, satellites[next_satellites].pos))

#             next_satellites = next_satellite + 1
#         else:
#             lines = []
#             next_satellite = 0  

# create_satellites()

# pgzrun.go()
import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0
game_over = False

number_of_satellite = 8

def create_satellites():
    global start_time 
    for count in range(0, number_of_satellite):
        satellite = Actor("satellite")
        satellite.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satellites.append(satellite)
    start_time = time()

def draw():
    global total_time

    screen.blit("space", (0,0))
    number = 1
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))
        satellite.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if not game_over:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        if next_satellite == number_of_satellite:
            screen.draw.text("You Win!", color="green", midtop=(WIDTH/2, HEIGHT/2 - 50), fontsize=60)
        else:
            screen.draw.text("You Lose!", color="red", midtop=(WIDTH/2, HEIGHT/2 - 50), fontsize=60)

def update():
    global game_over, total_time

    if not game_over:
        total_time = time() - start_time
        if total_time >= 30:  # Changed to 30 seconds
            game_over = True

def on_mouse_down(pos):
    global next_satellite, lines, game_over

    if not game_over:
        if next_satellite < number_of_satellite:
            if satellites[next_satellite].collidepoint(pos):
                if next_satellite:
                    lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
                next_satellite = next_satellite + 1
            else:
                lines = []
                next_satellite = 0

create_satellites()

pgzrun.go()