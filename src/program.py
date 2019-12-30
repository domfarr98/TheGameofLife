import pygame
import random


def main_program(xValue, yValue, seedValue):

    # define box and margin sizes
    BoxSizeP = 20
    BoxSpaceMarginP = 2

    # define number of boxes
    BoxNoX = round(int(xValue))
    BoxNoY = round(int(yValue))

    # bool to show smaller scaling
    smallScale = False

    # scale for larger sizes
    if BoxNoX > 40 or BoxNoY > 40:
        BoxSizeP = 10
        smallScale = True

    # define the window size depending on number of boxes, box sizes and margin sizes
    ScreenSize = ((BoxNoX * (BoxSizeP + BoxSpaceMarginP) + BoxSpaceMarginP),
                  (BoxNoY * (BoxSizeP + BoxSpaceMarginP)) + BoxSpaceMarginP)

    # define the drawing points for the boxes
    DrawingPointX = 0
    DrawingPointY = 0

    # define colours used in drawings
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # create seeded playing field
    PlayingField = create_seeded_playing_field(BoxNoX, BoxNoY, seedValue)

    # initialise PyGame
    pygame.init()

    # set the width and height of the screen [width, height]
    screen = pygame.display.set_mode(ScreenSize)

    # set window name
    pygame.display.set_caption("The Game of Life - Press space to evolve")

    # used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # used to count the number of evolutions
    evo = 0

    # main loop
    while True:

        # check if user requests exit, or if user requests game advance
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                PlayingField = calculate_moves(PlayingField)
                evo += 1
                pygame.display.set_caption("The Game of Life - Evolution " + str(evo))

        # set screen background
        screen.fill(BLACK)

        # reset drawing points before drawing
        DrawingPointX = BoxSpaceMarginP
        DrawingPointY = BoxSpaceMarginP

        # redraw the grid
        for x in range(BoxNoX):
            for y in range(BoxNoY):

                # draw the grid boxes
                pygame.draw.rect(screen, WHITE, (DrawingPointX, DrawingPointY, BoxSizeP, BoxSizeP))

                # if dot is required, draw dot
                if PlayingField[x][y]:
                    if smallScale:
                        pygame.draw.circle(screen, BLACK, (DrawingPointX + 5, DrawingPointY + 5), 3)
                    else:
                        pygame.draw.circle(screen, BLACK, (DrawingPointX+10, DrawingPointY+10), 5)
                DrawingPointX += BoxSizeP + BoxSpaceMarginP
            DrawingPointY += BoxSizeP + BoxSpaceMarginP
            DrawingPointX = BoxSpaceMarginP

        # set to 30 FPS
        clock.tick(30)

        # update window with the redrawing
        pygame.display.flip()


def calculate_moves(array):

    new_array = []
    score = 0
    iy = 0

    # for every element in this array
    for y in array:
        new_array.append([])
        for x in range(len(y)):

            # reset score
            score = 0

            # reset checked elements
            left_border = False
            right_border = False
            top_border = False
            bottom_border = False

            # check to see if elements should not be checked
            if iy == 0:
                top_border = True
            if iy == len(array)-1:
                bottom_border = True
            if x == 0:
                left_border = True
            if x == len(y)-1:
                right_border = True

            # if not on the top left
            if not top_border and not left_border:

                # check top left
                if array[iy-1][x-1]:
                    score += 1

            # if not on the top centre
            if not top_border:

                # check top centre
                if array[iy-1][x]:
                    score += 1

            # if not on the top right
            if not top_border and not right_border:

                # check top right
                if array[iy-1][x+1]:
                    score += 1

            # if not on centre left
            if not left_border:

                # check centre left
                if array[iy][x-1]:
                    score += 1

            # if not on centre right
            if not right_border:

                # check right centre
                if array[iy][x+1]:
                    score += 1

            # if not on bottom left
            if not left_border and not bottom_border:

                # check bottom left
                if array[iy+1][x-1]:
                    score += 1

            # if not on bottom centre
            if not bottom_border:

                # check bottom centre
                if array[iy+1][x]:
                    score += 1

            # if not on bottom right
            if not right_border and not bottom_border:

                # check bottom right
                if array[iy+1][x+1]:
                    score += 1

            # if the cell is dead, check if it should come to life
            if not array[iy][x] and score == 3:
                new_array[iy].append(True)

            # else if the cell is alive, check if it should die
            elif array[iy][x] and score < 2 or score > 3:
                new_array[iy].append(False)

            # else keep the cell alive/dead
            else:
                new_array[iy].append(array[iy][x])
        iy += 1

    return new_array


def create_seeded_playing_field(xValue, yValue, userSeed):

    # create the playing field
    PlayingField = []

    # seed the random using user seed
    random.seed(userSeed)

    # initialise the rolling seed
    rollingSeed = random.randint(1, 100000)

    for y in range(yValue):

        # create new x-axis line to populate
        PlayingField.append([])

        for x in range(xValue):

            # seed the random
            random.seed(rollingSeed)

            # add seeded random bool to playing field
            PlayingField[y].append(bool(random.getrandbits(1)))

            # re-seed the random
            rollingSeed = random.randint(1, 100000)

    # return the seeded playing field
    return PlayingField
