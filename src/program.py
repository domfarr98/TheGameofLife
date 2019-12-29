import pygame

def main_program(xValue, yValue, seedValue):

    # define box and margin sizes
    BoxSizeP = 20
    BoxSpaceMarginP = 2

    # define number of boxes
    BoxNoX = round(int(xValue))
    BoxNoY = round(int(yValue))

    # scale for larger sizes
    if BoxNoX > 40 or BoxNoY > 40:
        BoxSizeP = 10

    # define the window size depending on number of boxes, box sizes and margin sizes
    ScreenSize = ((BoxNoX * (BoxSizeP + BoxSpaceMarginP) + BoxSpaceMarginP),
                  (BoxNoY * (BoxSizeP + BoxSpaceMarginP)) + BoxSpaceMarginP)

    # define the drawing points for the boxes
    DrawingPointX = 0
    DrawingPointY = 0

    # define colours used in drawings
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

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
        for _ in range(BoxNoX):
            for _ in range(BoxNoY):
                pygame.draw.rect(screen, WHITE, (DrawingPointX, DrawingPointY, BoxSizeP, BoxSizeP))
                DrawingPointX += BoxSizeP + BoxSpaceMarginP
            DrawingPointY += BoxSizeP + BoxSpaceMarginP
            DrawingPointX = BoxSpaceMarginP

        # set to 30 FPS
        clock.tick(30)

        # update window with the redrawing
        pygame.display.flip()


def calculate_moves():
    pass
