from pathlib import Path
import json
import pygame
from SnakeAndBait import SnakeII
from ImageHandler import ImageHandlerII
from Button import Button
from GameSettings import GameSettings



class Score:
    def __init__(self, snake: SnakeII, screen: pygame.Surface) -> None:
        self.name: str = ""
        self.snake: SnakeII = snake
        self.name_input_rect: pygame.Rect = GameSettings.NAME_INPUT_RECT
        self.color: pygame.Color = pygame.Color("Red")
        self.font: pygame.font.Font = pygame.font.Font(None, 32)
        self.high_score_database_path: Path = Path(__file__).resolve().parent / 'Docs' / 'snake_High_Score.json'
        self.screen: pygame.Surface = screen
        self.image_handler: ImageHandlerII = ImageHandlerII()
        self.instructions: str = "Type your name in the box. Hit 'Escape' to save highscore and continue."
        self.name_input_instruction_rect: pygame.Rect = pygame.Rect(300, 200, 180, 69)

    def get_name(self):
        "Gets name from the user"
        name_typing = True
        while name_typing is True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.name = self.name[0:-1]
                    elif event.key == pygame.K_ESCAPE:
                        return
                    else:
                        self.name += event.unicode
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.dynamic_name_input_rect()
            self.instruction_for_name_input()
            pygame.display.flip()

    def read_json(self):
        "reads the score from json.file"
        with open(self.high_score_database_path, "+r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def write_json(self):
        "writes the score to json.file"
        all_dict = self.read_json()
        self.get_name()
        new_d: dict[str, int] = {self.name: self.snake.score}
        all_dict.update(new_d)
        sorted_dict_to_write: dict[str, int] = dict(
            sorted(all_dict.items(), key=lambda value: value[1], reverse=True)
        )

        if len(sorted_dict_to_write) > 5:
            sorted_dict_to_write.popitem()
            with open(self.high_score_database_path, "w", encoding="utf-8") as f:
                json.dump(sorted_dict_to_write, f)
        else:
            with open(self.high_score_database_path, "w", encoding="utf-8") as f:
                json.dump(sorted_dict_to_write, f)

    def display(self):
        "Single player score displayer"
        score_text: Button = Button(0, 0, "Highscore: " + str(self.snake.score))
        score_text.narrow_buttons(self.screen)

    def display_second_snake_score(self):
        "Single player score displayer"
        score_text: Button = Button(
            GameSettings.MULTI_PLAYER_SCORE_BOX, 0, "Highscore: " + str(self.snake.score)
        )
        score_text.narrow_buttons(self.screen)

    def instruction_for_name_input(self):
        "Instructions for name input"
        instruction: Button = Button(
            self.name_input_instruction_rect.x,
            self.name_input_instruction_rect.y,
            self.instructions,
        )
        instruction.narrow_buttons(self.screen)

    def dynamic_name_input_rect(self):
        "creates a dynamically growing rect on the screen for name input"
        self.screen.blit(self.image_handler.single_player_background_path, (0, 0))
        pygame.draw.rect(self.screen, self.color, self.name_input_rect, 5)
        text_surface = self.font.render(self.name, True, (255, 255, 255))
        self.screen.blit(
            text_surface, (self.name_input_rect.x + 5, self.name_input_rect.y + 5)
        )
        self.name_input_rect.w = max(20, text_surface.get_width() + 10)
