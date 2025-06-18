import pygame
import random
import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initial setup
pygame.init()

# Load sounds
win_sound = pygame.mixer.Sound(resource_path("assets/win.mp3"))
error_sound = pygame.mixer.Sound(resource_path("assets/error.mp3"))

# Set up display
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guesser")

# Set up font
FONT = pygame.font.SysFont("arial", 32)
SMALL_FONT = pygame.font.SysFont("arial", 24)

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
target_number = random.randint(1, 100)
guess = ''
feedback = ''
attempts = 0
running = True
won = False

while running:
    win.fill(WHITE)

    # Title and Instructions
    title = FONT.render("Guess the number (1-100)", True, BLACK)
    win.blit(title, (100, 50))

    input_text = FONT. render("Your Guess: " + guess, True, BLACK)
    win.blit(input_text, (1000, 120))

    result_text = SMALL_FONT.render(feedback, True, BLACK)
    win.blit(result_text, (100, 170))

    attempts_text = SMALL_FONT.render(f"Attempts: {attempts}", True, BLACK)
    win.blit(attempts_text, (100, 200))
    if won:
        victory_text = FONT.render("You Win! Press 'R' to play again", True, BLACK)
        win.blit(victory_text, (50, 250))

    pygame.display.update()

    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not won:
                if guess.isdigit():
                    player_guess = int(guess)
                    attempts += 1
                    if player_guess < target_number:
                        feedback = "Too low! Try again."
                    elif player_guess > target_number:
                        feedback = "Too high! Try again."
                    else:
                        win_sound.play()
                        feedback = f"Correct! The number was {target_number}"
                        won = True
                else:
                    error_sound.play()
                    feedback = "Please enter numbers only."
                guess = ''
            elif event.key == pygame.K_BACKSPACE and not won:
                guess = guess[:-1]
            elif event.unicode.isdigit() and not won:
                guess += event.unicode
            elif event.key == pygame.K_r and won:
                # Restart the game
                target_number = random.randint(1, 100)
                guess = ''
                feedback = ''
                attempts = 0
                won = False

pygame.quit()
sys.exit()
            
