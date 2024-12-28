import json
from pathlib import Path
import pygame
from Button import Button
from GameSettings import GameSettings
from ImageHandler import ImageHandlerII


class HallOfFame:
    "Starts highscores in game"

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.high_score_database_path = (
            Path(__file__).resolve().parent / "Docs" / "snake_High_Score.json"
        )
        self.font = pygame.font.Font(None, 32)
        self.image_handler = ImageHandlerII()

    def start(self):
        "Hall Of Fame for the Best player scores"
        self.screen.fill("black")
        self.screen.blit(self.image_handler.hall_of_fame_background_path, (0, 100))
        data = self.reading_json()
        i = 0
        for key, value in data.items():
            self.fame_creation(
                GameSettings.HALL_OF_FAME_FIRST_POS_X,
                GameSettings.HALL_OF_FAME_FIRTS_POS_Y + i,
                key,
                value,
                10,
            )
            i += 100
        pygame.display.flip()

    def reading_json(self):
        "Reads from the database"
        with open(self.high_score_database_path, "+r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def fame_creation(self, x_pos: int, y_pos: int, name: str, score: str, dis: int):
        "displays the highscore"
        score = str(score)
        scored_name = name + ": " + score + " Points"
        fame_name_plate = Button(x_pos, y_pos + dis, scored_name)
        fame_name_plate.narrow_buttons(self.screen)
