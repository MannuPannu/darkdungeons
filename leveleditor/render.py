import pygame

def doRender(main):

    black = 0, 0, 0

    main.screen.fill(black)

    #Draw map
    main.level.draw(main.screen)

    #Draw user help info
    main.screen.blit(main.newMapText, (10, 380))
    main.screen.blit(main.saveMapText, (10, 410))
    main.screen.blit(main.loadMapText, (10, 440))

    #Draw palette
    main.palette.draw(main.screen)

    pygame.display.flip()

    
