import pygame

def doRender(main):

    black = 0, 0, 0

    main.screen.fill(black)

    #draw map
    main.level.draw(main.screen)

    #Draw player
    main.player.draw(main.screen)

    pygame.display.flip()
