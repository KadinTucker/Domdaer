import random
import pygame
from pygame.locals import *
import sys

SOUND_NAMES = ['fanfare']
SOUND_FILES = {'fanfare' : 'Intrepid.mp3'}

MUSIC = {'Intrepid' : 'Intrepid.mp3', 'Summer Day' : 'SummerDay.mp3'}

def terminate():
    """
    Stop all functions of the program.
    """
    pygame.quit()
    sys.exit()

class button():
    """
    A button class to have a width and coordinates. Also has a pressed state.

    Takes in location, which is the location of the button.
    Takes in button ID, which determines where the button takes you when pressing it.
    Takes in image, the image in which it displays on the screen.
    """
    def __init__(self, location, identity, image):
        self.location = location
        self.identity = identity
        self.image = image
        self.pressed = False
        
    def buttonPressed(self):
        """
        Checks whether or not a button has been clicked.

        Returns a slightly modified list of buttons, modifying whether or not the button has been pressed.
        """
        mouse = pygame.mouse.get_pos()
        print('CONSOLE: Clicked at point '+str(mouse))
        if mouse[0] - self.location[0] <= 200 and mouse[0] - self.location[0] >= 0:
            if mouse[1] - self.location[1] <= 50 and mouse[1] - self.location[1] >= 0:
                self.pressed = True
                print('CONSOLE: Button of ID %s has been pressed.' % self.identity)
    def displayButtons(self, display):
        """
        Displays the button on the screen as self.image. All button images should be 200px X 50px
        to have proper dimensions.

        Takes in the main game display screen.
        """
        display.blit(self.image, self.location)

def checkButtons(buttons, sounds):
    """
    Checks whether the ID of all buttons being pressed checks out with any pre-determined functions
    of specific buttons. If the function goes through and nothing happens, the button becomes un-pressed.

    Takes in the list of all buttons.

    Ex: A 'quit' button will terminate the game when pressed (game state 0).

    Returns the new game state.
    """
    for i in buttons:
        if i.pressed == True:
            if i.identity == 'quit':
                print('CONSOLE: Quit Button pressed.')
                return 0
                print('ERROR: Quit not gone through.')
            if i.identity == 'play':
                print('CONSOLE: Play button pressed.')
                setMusic('Summer Day')
                return 2
        else:
            i.pressed == False
    return 1

def initButtons():
    """
    Initializes the buttons for the main menu.

    Returns a list of all buttons in the main menu.
    """
    buttons = []
    buttons.append(button((150, 210), 'load', pygame.image.load('loadgameButton.png')))
    buttons.append(button((125, 20), None, pygame.image.load('title.png')))
    buttons.append(button((150, 150), 'play', pygame.image.load('newgameButton.png')))
    buttons.append(button((150, 270), 'quit', pygame.image.load('quitButton.png')))
    return buttons

def initSounds():
    """
    Adds a list of sounds to be used in the game.
    """
    sounds = {}
    for sound_name in SOUND_NAMES:
        sounds[sound_name] = pygame.mixer.Sound(SOUND_FILES[sound_name])
    return sounds

def setMusic(song):
    """
    Stops the currently playing song, then sets a new song to be played.
    Takes in the name of the song to be played, a string.
    """
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSIC[song])
    pygame.mixer.music.play(-1)

def initialize():
    """
    Initializes the pygame library, and creates a display window.

    Returns a list of buttons in the main menu, and the starting game state.
    """
    print('CONSOLE: Initializing loop...')
    pygame.init()
    pygame.mixer.init()
    sounds = initSounds()
    display = pygame.display.set_mode((500, 400))
    buttons = initButtons()
    gamestate = 1 #Gamestate 1 is the main menu.
    setMusic('Intrepid')
    print('CONSOLE: Init complete. Starting loop.')
    return buttons, gamestate, display, sounds

def runProgram(buttons, gamestate, display, sounds):
    """
    Run the program main loop

    Takes in a list of buttons in the main menu, and the starting game state.
    """
    while True:
        if gamestate == 1:
            display.fill((65, 35, 55))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in buttons:    
                            i.buttonPressed()
                if event.type == QUIT:
                    terminate()
            gamestate = checkButtons(buttons, sounds)
            for i in buttons:
                i.displayButtons(display)
                
        elif gamestate == 2:
            display.fill((65, 35, 55))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                    
        elif gamestate == 0:
            print('CONSOLE: Quitting game.')
            terminate()

        pygame.display.update()

def main():
    """
    Initialize data, then run the program.
    """
    buttons, gamestate, display, sounds = initialize()
    runProgram(buttons, gamestate, display, sounds)

if __name__ == '__main__':
    main()

