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
    pygame.display.set_caption("My Game")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # main loop
    while True:

        # check if user requests exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

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

    return True


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
