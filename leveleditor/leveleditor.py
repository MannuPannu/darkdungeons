import pygame, init, event, render

def main():

    quitProgram = False
    screen = init.init()

    #Main game loop
    while True:
        quitProgram = event.doEvent()

        if quitProgram == True:
            break

        render.doRender(screen)

        pygame.time.delay(150)

    pygame.quit()

main()



