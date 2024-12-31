import pygame

class GameSettings:
    "Game constants"

    SNAKE_WIDTH = 64
    SNAKE_HEIGHT = 64
    BAIT_WIDTH = 64
    BAIT_HEIGHT = 64
    SNAKE_SPEED = 64
    SNAKE_GAME_SPEED = 100
    WIDTH = SNAKE_WIDTH * 20
    HEIGHT = SNAKE_HEIGHT * 15
    MENU_RECT_WIDTH = WIDTH // 5
    MENU_RECT_HEIGHT = HEIGHT // 18
    MENU_SINGLE_PLAYER_BUTTON_X_POS = MENU_RECT_WIDTH
    MENU_SINGLE_PLAYER_BUTTON_Y_POS = 0
    HALL_OF_FAME_FIRST_POS_X = MENU_RECT_WIDTH * 2 + 5
    HALL_OF_FAME_FIRTS_POS_Y = MENU_RECT_HEIGHT * 3
    MENU_MULIT_PLAYER_BUTTON_X_POS = MENU_RECT_WIDTH * 2 + 5
    MENU_MULIT_PLAYER_BUTTON_Y_POS = 0
    MULTI_PLAYER_SCORE_BOX = WIDTH - 90
    MULTI_PLAYER_PLAYER_TWO_WIN = (WIDTH //2, HEIGHT//2)
    MENU_SETTINGS_BUTTON_X_POS = MENU_RECT_WIDTH * 3 + 10
    MENU_SETTINGS_BUTTON_Y_POS = 0
    MENU_EXIT_GAME_BUTTON_X_POS = MENU_MULIT_PLAYER_BUTTON_X_POS
    MENU_EXIT_GAME_BUTTON_Y_POS = HEIGHT - MENU_RECT_HEIGHT
    RIGHT_CLICK = (True, False, False)
    NAME_INPUT_RECT = pygame.Rect(300, 300, 180, 69)
