import pygame
import random
import time
import math
pygame.init()
window_w = 1280
window_h = 720
size = (window_w,window_h)
screen = pygame.display.set_mode(size)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
done = False
target_clicked = False
clicked_counter = 0
accuracy_counter = 0
target_location_x = random.randrange(0, window_w)
target_location_y = random.randrange(0, window_h)
score = 0
start_button = pygame.Rect(490,400,300,80)
targets_5 = pygame.Rect(275, 325,110,100)
targets_10 = pygame.Rect(555, 325,150,100)
targets_15 = pygame.Rect(855, 325,150,100)
targets_20 = pygame.Rect(255, 475,150,100)
targets_25 = pygame.Rect(555, 475,150,100)
targets_30 = pygame.Rect(855, 475,150,100)
difficulty_easy_button = pygame.Rect(75, 400, 250, 100)
difficulty_medium_button = pygame.Rect(425, 400, 425, 100)
difficulty_hard_button = pygame.Rect(925, 400, 270, 100)
mode_timed_button = pygame.Rect(280, 440, 310, 120)
mode_fast_button = pygame.Rect(760, 440, 230, 120)
time_play_5 = pygame.Rect(275, 325, 110, 100)
time_play_10 = pygame.Rect(555, 325, 150, 100)
time_play_15 = pygame.Rect(855, 325, 150, 100)
time_play_20 = pygame.Rect(255, 475, 150, 100)
time_play_25 = pygame.Rect(555, 475, 150, 100)
time_play_30 = pygame.Rect(855, 475, 150, 100)

game_started = False
font = pygame.font.SysFont("Calibri", 60, False, False)
score_font = pygame.font.SysFont("Calibri", 40, False, False)
font_50 = pygame.font.SysFont("Calibri", 50, False, False)
font_60 = pygame.font.SysFont("Calibri", 60, False, False)
font_70 = pygame.font.SysFont("Calibri", 70, False, False)
font_80 = pygame.font.SysFont("Calibri", 80, False, False)
menu_font = pygame.font.SysFont("Calibri", 110, False, False)
start_text = font.render("Press the button to start", True, WHITE)
score_format = "{:.2f}"
accuracy_format = "{:.0f}%"
score_print_location = 233
score_location_check = 0
targets_chosen = 0
num_target_image = font.render("Please choose the amount of targets", True, WHITE)
text_targets_5 = menu_font.render("5", True, WHITE)
text_targets_10 = menu_font.render("10", True, WHITE)
text_targets_15 = menu_font.render("15", True, WHITE)
text_targets_20 = menu_font.render("20", True, WHITE)
text_targets_25 = menu_font.render("25", True, WHITE)
text_targets_30 = menu_font.render("30", True, WHITE)

text_time_play_5 = menu_font.render("5", True, WHITE)
text_time_play_10 = menu_font.render("10", True, WHITE)
text_time_play_15 = menu_font.render("15", True, WHITE)
text_time_play_20 = menu_font.render("20", True, WHITE)
text_time_play_25 = menu_font.render("25", True, WHITE)
text_time_play_30 = menu_font.render("30", True, WHITE)

targets_chosen_text_x_pos = 910
targets_chosen = 0
targets_hit_text = font.render("Targets Hit", True, WHITE)
time_spent_text = font.render("Score (seconds)", True, WHITE)
seconds_spent_text = font.render("Seconds", True, WHITE)
accuracy_display_text = font.render("Accuracy", True, WHITE)
difficulty_chosen = 0
difficulty_easy_text = menu_font.render("Easy", True, WHITE)
difficulty_medium_text = menu_font.render("Medium", True, WHITE)
difficulty_hard_text = menu_font.render("Hard", True, WHITE)
difficulty_choose_text = font.render("Select the difficulty", True, WHITE)
accuracy_text_pos = 530
target_space_between = 50
mode_choose_text = font.render("Choose the mode", True, WHITE)
mode_chosen = 0
mode_timed_text = menu_font.render("Timed", True, WHITE)
mode_fast_text = menu_font.render("Fast", True, WHITE)
fast_play_time = 0
run_time_image = font.render("Choose the amount of time to play", True, WHITE)
score_play_time = 0
time_taken_text_x_pos = 300

while not done:
    if game_started == False:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, start_button)
        screen.blit(start_text, [345, 200])
        pygame.display.flip()
    elif mode_chosen == 0:
        screen.fill(BLACK)
        screen.blit(mode_choose_text, [425, 200])
        pygame.draw.rect(screen, BLACK, mode_timed_button) 
        pygame.draw.rect(screen, BLACK, mode_fast_button)
        screen.blit(mode_timed_text, [300, 450])
        screen.blit(mode_fast_text, [780, 450])
        pygame.display.flip()

    if mode_chosen == 1:
        if fast_play_time == 0:
            screen.fill(BLACK)
            pygame.draw.rect(screen, BLACK, time_play_5)
            pygame.draw.rect(screen, BLACK, time_play_10)
            pygame.draw.rect(screen, BLACK, time_play_15)
            pygame.draw.rect(screen, BLACK, time_play_20)
            pygame.draw.rect(screen, BLACK, time_play_25)
            pygame.draw.rect(screen, BLACK, time_play_30)
            screen.blit(text_time_play_5, [295, 325])
            screen.blit(text_time_play_10, [565, 325])
            screen.blit(text_time_play_15, [865, 325])
            screen.blit(text_time_play_20, [265, 475])
            screen.blit(text_time_play_25, [565, 475])
            screen.blit(text_time_play_30, [865, 475])
            screen.blit(run_time_image, [215, 170])
            pygame.display.flip()
        elif difficulty_chosen == 0:
            screen.fill(BLACK)
            screen.blit(difficulty_choose_text, [400, 200])
            pygame.draw.rect(screen, BLACK, difficulty_easy_button)
            pygame.draw.rect(screen, BLACK, difficulty_medium_button)
            pygame.draw.rect(screen, BLACK, difficulty_hard_button)
            screen.blit(difficulty_easy_text, [100, 400])
            screen.blit(difficulty_medium_text, [450, 400])
            screen.blit(difficulty_hard_text, [950, 400])
            pygame.display.flip()
        else:
            score += 1
            
            score_play_time = fast_play_time * 60
            if score == score_play_time:
                score_seconds = score / 60

                accuracy_100 = (accuracy_counter + clicked_counter)
                
                final_accuracy = accuracy_format.format((clicked_counter / accuracy_100) * 100)
                
                accuracy_text = font_80.render(final_accuracy, True, WHITE)            
                
                time_taken_text = font_80.render(str(int(score_seconds)), True, WHITE)

                targets_chosen_text = font_80.render(str(clicked_counter), True, WHITE)

                if clicked_counter < 10:
                    targets_chosen_text_x_pos = 940

                if score_seconds > 5:
                    time_taken_text_x_pos = 275
    
                if accuracy_100 > clicked_counter:
                    accuracy_text_pos = 545
                
                screen.fill(BLACK)
                screen.blit(accuracy_text, [accuracy_text_pos, 550])
                screen.blit(time_taken_text, [time_taken_text_x_pos, 225])
                screen.blit(targets_chosen_text, [targets_chosen_text_x_pos, 225])
                screen.blit(accuracy_display_text, [510, 465])
                screen.blit(seconds_spent_text, [210, 150])
                screen.blit(targets_hit_text, [825, 150])
                pygame.display.flip()
                time.sleep(3)
                done = True

            elif target_clicked == True:
                target_location_x = random.randrange(0, window_w)
                target_location_y = random.randrange(0, window_h)
                while last_target_location_x + target_space_between > target_location_x and last_target_location_x - target_space_between < target_location_x:
                    target_location_x = random.randrange(0, window_w)
                while last_target_location_y + target_space_between > target_location_y and last_target_location_y - target_space_between < target_location_y:
                    target_location_y = random.randrange(0, window_h)
                target_clicked = False

            else:
                if difficulty_chosen == 1:
                    target_size = 90
                elif difficulty_chosen == 2:
                    target_size = 70
                elif difficulty_chosen == 3:
                    target_size = 50

                if target_location_x < target_size:
                    target_location_x += target_size + 25

                if target_location_x > window_w - target_size:
                    target_location_x -= target_size + 25
                
                if target_location_y < target_size:
                    target_location_y += target_size + 25

                if target_location_y > window_h - target_size:
                    target_location_y -= target_size + 25

                last_target_location_x = target_location_x
                last_target_location_y = target_location_y

                screen.fill(BLACK)
                pygame.draw.circle(screen, RED, [target_location_x, target_location_y], target_size)

                mouse_pos_x = pygame.mouse.get_pos()[0]
                mouse_pos_y = pygame.mouse.get_pos()[1]
                sqx = (mouse_pos_x - target_location_x)**2
                sqy = (mouse_pos_y - target_location_y)**2
                pygame.display.flip()    

    elif mode_chosen == 2:        
        if difficulty_chosen == 0 or targets_chosen == 0:

            if difficulty_chosen == 0:
                screen.fill(BLACK)
                screen.blit(difficulty_choose_text, [400, 200])
                pygame.draw.rect(screen, BLACK, difficulty_easy_button)
                pygame.draw.rect(screen, BLACK, difficulty_medium_button)
                pygame.draw.rect(screen, BLACK, difficulty_hard_button)
                screen.blit(difficulty_easy_text, [100, 400])
                screen.blit(difficulty_medium_text, [450, 400])
                screen.blit(difficulty_hard_text, [950, 400])
                pygame.display.flip()
            elif targets_chosen == 0:
                screen.fill(BLACK)
                pygame.draw.rect(screen, BLACK, targets_5)
                pygame.draw.rect(screen, BLACK, targets_10)
                pygame.draw.rect(screen, BLACK, targets_15)
                pygame.draw.rect(screen, BLACK, targets_20)
                pygame.draw.rect(screen, BLACK, targets_25)
                pygame.draw.rect(screen, BLACK, targets_30)
                screen.blit(text_targets_5, [295, 325])
                screen.blit(text_targets_10, [565, 325])
                screen.blit(text_targets_15, [865, 325])
                screen.blit(text_targets_20, [265, 475])
                screen.blit(text_targets_25, [565, 475])
                screen.blit(text_targets_30, [865, 475])
                screen.blit(num_target_image, [195, 170])
                pygame.display.flip()

        
        else:    
            score += 1

            if clicked_counter == targets_chosen:
                score_seconds = score / 60

                accuracy_100 = (accuracy_counter + clicked_counter)
                
                final_accuracy = accuracy_format.format((clicked_counter / accuracy_100) * 100)
                
                accuracy_text = font_80.render(final_accuracy, True, WHITE)            
                
                time_taken = (score_format.format(score_seconds))
                time_taken_text = font_80.render(time_taken, True, WHITE)

                targets_chosen_text = font_80.render(str(targets_chosen), True, WHITE)

                if targets_chosen < 10:
                    targets_chosen_text_x_pos = 940

                if accuracy_100 > clicked_counter:
                    accuracy_text_pos = 545
                
                screen.fill(BLACK)
                screen.blit(accuracy_text, [accuracy_text_pos, 550])
                screen.blit(time_taken_text, [250, 225])
                screen.blit(targets_chosen_text, [targets_chosen_text_x_pos, 225])
                screen.blit(accuracy_display_text, [510, 465])
                screen.blit(time_spent_text, [150, 150])
                screen.blit(targets_hit_text, [825, 150])
                pygame.display.flip()
                time.sleep(3)
                done = True

            elif target_clicked == True:
                target_location_x = random.randrange(0, window_w)
                target_location_y = random.randrange(0, window_h)
                while last_target_location_x + target_space_between > target_location_x and last_target_location_x - target_space_between < target_location_x:
                    target_location_x = random.randrange(0, window_w)
                while last_target_location_y + target_space_between > target_location_y and last_target_location_y - target_space_between < target_location_y:
                    target_location_y = random.randrange(0, window_h)
                target_clicked = False

            else:
                if difficulty_chosen == 1:
                    target_size = 90
                elif difficulty_chosen == 2:
                    target_size = 70
                elif difficulty_chosen == 3:
                    target_size = 50

                if target_location_x < target_size:
                    target_location_x += target_size + 25

                if target_location_x > window_w - target_size:
                    target_location_x -= target_size + 25
                
                if target_location_y < target_size:
                    target_location_y += target_size + 25

                if target_location_y > window_h - target_size:
                    target_location_y -= target_size + 25

                last_target_location_x = target_location_x
                last_target_location_y = target_location_y

                screen.fill(BLACK)
                pygame.draw.circle(screen, RED, [target_location_x, target_location_y], target_size)

                mouse_pos_x = pygame.mouse.get_pos()[0]
                mouse_pos_y = pygame.mouse.get_pos()[1]
                sqx = (mouse_pos_x - target_location_x)**2
                sqy = (mouse_pos_y - target_location_y)**2
                pygame.display.flip()    
        
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and game_started == False:
            game_start_click = start_button.collidepoint(pygame.mouse.get_pos())
            if game_start_click == 1:
                game_started = True
        elif event.type == pygame.MOUSEBUTTONDOWN and mode_chosen == 0:
            mode_choose_timed_click = mode_timed_button.collidepoint(pygame.mouse.get_pos())
            if mode_choose_timed_click == 1:
                mode_chosen = 1

            mode_choose_fast_click = mode_fast_button.collidepoint(pygame.mouse.get_pos())
            if mode_choose_fast_click == 1:
                mode_chosen = 2
            
        elif event.type == pygame.MOUSEBUTTONDOWN and fast_play_time == 0 and mode_chosen == 1:

            time_play_choose_click_5 = time_play_5.collidepoint(pygame.mouse.get_pos())
            if time_play_choose_click_5 == 1:
                fast_play_time = 5

            time_play_choose_click_10 = time_play_10.collidepoint(pygame.mouse.get_pos())
            if time_play_choose_click_10 == 1:
                fast_play_time = 10

            time_play_choose_click_15 = time_play_15.collidepoint(pygame.mouse.get_pos())
            if time_play_choose_click_15 == 1:
                fast_play_time = 15

            time_play_choose_click_20 = time_play_20.collidepoint(pygame.mouse.get_pos())
            if time_play_choose_click_20 == 1:
                fast_play_time = 20

            time_play_choose_click_25 = time_play_25.collidepoint(pygame.mouse.get_pos())
            if time_play_choose_click_25 == 1:
                fast_play_time = 25

            time_play_choose_click_30 = time_play_30.collidepoint(pygame.mouse.get_pos())
            if time_play_choose_click_30 == 1:
                fast_play_time = 30

        elif event.type == pygame.MOUSEBUTTONDOWN and difficulty_chosen == 0:

            difficulty_choose_easy_click = difficulty_easy_button.collidepoint(pygame.mouse.get_pos())
            if difficulty_choose_easy_click == 1:
                difficulty_chosen = 1

            difficulty_choose_medium_click = difficulty_medium_button.collidepoint(pygame.mouse.get_pos())
            if difficulty_choose_medium_click == 1:
                difficulty_chosen = 2

            difficulty_choose_hard_click = difficulty_hard_button.collidepoint(pygame.mouse.get_pos())
            if difficulty_choose_hard_click == 1:
                difficulty_chosen = 3

        elif event.type == pygame.MOUSEBUTTONDOWN and targets_chosen == 0 and mode_chosen == 2:
            targets_choose_click_5 = targets_5.collidepoint(pygame.mouse.get_pos())
            if targets_choose_click_5 == 1:
                targets_chosen = 5
            targets_choose_click_10 = targets_10.collidepoint(pygame.mouse.get_pos())
            if targets_choose_click_10 == 1:
                targets_chosen = 10
            targets_choose_click_15 = targets_15.collidepoint(pygame.mouse.get_pos())
            if targets_choose_click_15 == 1:
                targets_chosen = 15
            targets_choose_click_20 = targets_20.collidepoint(pygame.mouse.get_pos())
            if targets_choose_click_20 == 1:
                targets_chosen = 20
            targets_choose_click_25 = targets_25.collidepoint(pygame.mouse.get_pos())
            if targets_choose_click_25 == 1:
                targets_chosen = 25
            targets_choose_click_30 = targets_30.collidepoint(pygame.mouse.get_pos())
            if targets_choose_click_30 == 1:
                targets_chosen = 30
        elif event.type == pygame.MOUSEBUTTONDOWN and game_started == True and mode_chosen > 0 and difficulty_chosen > 0 and (math.sqrt(sqx + sqy) < target_size):
            target_clicked = True
            clicked_counter += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and game_started == True and mode_chosen > 0 and difficulty_chosen > 0 and (math.sqrt(sqx + sqy) > target_size):
            accuracy_counter += 1
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

