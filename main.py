import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
window_width = 800
window_height = 600

# Размеры игрового поля
field_width = 600
field_height = 400

# Размеры блока
block_size = 20

# Расчет позиции верхнего левого угла игрового поля
field_x = (window_width - field_width) // 2
field_y = (window_height - field_height) // 2

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)
yellow = (255, 255, 0)

# Создание окна
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 50)

# Кастомизация змейки
snake_head_img = pygame.Surface((block_size, block_size))
snake_head_img.fill(green)
snake_body_img = pygame.Surface((block_size, block_size))
snake_body_img.fill(green)

# Кастомизация фруктов
fruit_img = pygame.Surface((block_size, block_size))
fruit_img.fill(red)
bonus_fruit_img = pygame.Surface((block_size, block_size))
bonus_fruit_img.fill(yellow)

# Кастомизация игрового окна
background_img = pygame.Surface((window_width, window_height))
background_img.fill(black)

def our_snake(snake_list):
    for segment in snake_list:
        game_display.blit(snake_body_img, segment)

def message(msg, color, y_displacement=0, x_displacement=0, font_size=25):
    font_style = pygame.font.SysFont(None, font_size)
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [window_width / 6 + x_displacement, window_height / 3 + y_displacement])



def show_score(score):
    score_text = score_font.render("Счет: " + str(score), True, white)
    game_display.blit(score_text, [10, 10])

def draw_field():
    pygame.draw.rect(game_display, gray, (field_x - block_size, field_y - block_size, field_width + 2 * block_size, field_height + 2 * block_size), block_size)

def start_screen():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    difficulty = choose_difficulty()
                    game_loop(difficulty)
                if event.key == pygame.K_i:
                    show_instructions()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        game_display.blit(background_img, (0, 0))
        message("ЗМЕЙКА", white, x_displacement=220, y_displacement=0, )
        message("Для того чтобы начать игру нажмите «SPACE»", white,x_displacement=70, y_displacement=100)
        message("Для выхода из игры нажмите «Esc»", white,x_displacement=95, y_displacement=300)
        message("Для отображения правил игры нажмите «i»", white,x_displacement=70, y_displacement=320)

        pygame.display.update()
        clock.tick(15)

def choose_difficulty():
    choose = True
    difficulty = 1

    while choose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choose = False
                    difficulty = 1
                elif event.key == pygame.K_2:
                    choose = False
                    difficulty = 2
                elif event.key == pygame.K_3:
                    choose = False
                    difficulty = 3
                elif event.key == pygame.K_ESCAPE:
                    start_screen()
                    return

        game_display.blit(background_img, (0, 0))
        message("Выберите уровень сложности", white, x_displacement=145, y_displacement=-70)
        message("1 - Легкий (без препятствий)", white, y_displacement=0)
        message("2 - Средний (с препятствиями)", white, y_displacement=50)
        message("3 - Сложный (с препятствиями и увеличением скорости)", white, y_displacement=100)
        message("- Для выбора уровня нажмите соответствующую цифру", white,x_displacement=20, y_displacement=200)
        message("- Чтобы взять паузу во время игры нажмите кнопку «P» ", white,x_displacement=20, y_displacement=230)
        message("Для выхода в главное меню нажмите «Esc»", white, x_displacement=75, y_displacement=300)

        pygame.display.update()
        clock.tick(15)

    return difficulty


def show_instructions():
    instructions = True

    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions = False

        game_display.blit(background_img, (0, 0))
        message("Правила игры", white, x_displacement=200, y_displacement=-50)
        message("- Управление змейкой осуществляется с помощью стрелок на клавиатуре", white, x_displacement=-50, y_displacement=50)
        message("- Собирайте фрукты, чтобы увеличивать длину змейки и набирать очки", white, x_displacement=-50, y_displacement=80)
        message("- Избегайте столкновений со стенами и самим собой", white, x_displacement=-50, y_displacement=110)
        message("- Бонусные фрукты увеличивают в 2 блока змейку и дают больше очков", white, x_displacement=-50, y_displacement=140)
        message("Для выхода из правил в главное меню нажмите «Esc»", white, x_displacement=40, y_displacement=250)


        pygame.display.update()
        clock.tick(15)

def generate_obstacles():
    obstacles = []
    num_obstacles = random.randint(6, 8)
    for _ in range(num_obstacles):
        obstacle_x = round(random.randrange(field_x, field_x + field_width - block_size) / block_size) * block_size
        obstacle_y = round(random.randrange(field_y, field_y + field_height - block_size) / block_size) * block_size
        obstacles.append((obstacle_x, obstacle_y))
    return obstacles


def pause_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return

        game_display.blit(background_img, (0, 0))
        message("Пауза", white, x_displacement=240, y_displacement=60)
        message("Нажмите «P» для продолжения", white, x_displacement=130, y_displacement=100)

        pygame.display.update()
        clock.tick(15)

def game_loop(difficulty):
    game_over = False
    game_close = False
    paused = False
    key_pressed = False

    # Начальные координаты змейки
    x1 = field_width / 2
    y1 = field_height / 2

    # Изменение координат змейки
    x1_change = 0
    y1_change = 0

    # Создание змейки
    snake_list = []
    length_of_snake = 1

    # Создание фруктов
    fruit_x = round(random.randrange(field_x, field_x + field_width - block_size) / block_size) * block_size
    fruit_y = round(random.randrange(field_y, field_y + field_height - block_size) / block_size) * block_size

    # Создание бонусного фрукта
    bonus_fruit_x = -block_size
    bonus_fruit_y = -block_size
    bonus_fruit_active = False

    score = 0

    if difficulty == 3:
        snake_speed = 15
    else:
        snake_speed = 10

    obstacles = generate_obstacles() if difficulty >= 2 else []

    while not game_over:

        while game_close:
            game_display.blit(background_img, (0, 0))
            message("Game Over! Набранные очки: " + str(score), red,x_displacement=125, y_displacement=70)
            message("Нажмите «C»-Играть снова или «Q»-Выход", white,x_displacement=85, y_displacement=100)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop(difficulty)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change == block_size:
                        continue
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == -block_size:
                        continue
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == block_size:
                        continue
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change == -block_size:
                        continue
                    y1_change = block_size
                    x1_change = 0
                elif event.key == pygame.K_p:
                    paused = not paused
                    key_pressed = True

        if not paused:
            # Обновление координат змейки
            x1 += x1_change
            y1 += y1_change

            game_display.blit(background_img, (0, 0))

            draw_field()

            # Отрисовка фруктов
            game_display.blit(fruit_img, (fruit_x, fruit_y))

            if bonus_fruit_active:
                # Отрисовка бонусного фрукта
                game_display.blit(bonus_fruit_img, (bonus_fruit_x, bonus_fruit_y))

            if difficulty >= 2:
                # Отрисовка препятствий
                for obstacle in obstacles:
                    pygame.draw.rect(game_display, gray, (obstacle[0], obstacle[1], block_size, block_size))

                # Проверка столкновения со стенами
                if x1 >= field_x + field_width or x1 < field_x or y1 >= field_y + field_height or y1 < field_y:
                    game_close = True

                # Проверка столкновения с препятствиями
                if (x1, y1) in obstacles:
                    game_close = True

            # Проверка столкновения с фруктом
            if x1 == fruit_x and y1 == fruit_y:
                fruit_x = round(random.randrange(field_x, field_x + field_width - block_size) / block_size) * block_size
                fruit_y = round(random.randrange(field_y, field_y + field_height - block_size) / block_size) * block_size
                length_of_snake += 1
                score += 1
                obstacles = generate_obstacles() if difficulty >= 2 else []

                # Активация бонусного фрукта
                if not bonus_fruit_active and random.random() < 0.3:
                    bonus_fruit_x = round(random.randrange(field_x, field_x + field_width - block_size) / block_size) * block_size
                    bonus_fruit_y = round(random.randrange(field_y, field_y + field_height - block_size) / block_size) * block_size
                    bonus_fruit_active = True

            # Проверка столкновения с бонусным фруктом
            if bonus_fruit_active and x1 == bonus_fruit_x and y1 == bonus_fruit_y:
                bonus_fruit_active = False
                score += 3
                length_of_snake += 2
                obstacles = generate_obstacles() if difficulty >= 2 else []

            # Проверка выхода за границы игрового поля
            if x1 >= field_x + field_width or x1 < field_x or y1 >= field_y + field_height or y1 < field_y:
                game_close = True

            # Проверка столкновения с самим собой
            for segment in snake_list[:-1]:
                if segment == [x1, y1]:
                    game_close = True

            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            our_snake(snake_list)
            show_score(score)

        else:
            pause_game()
            paused = False

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


start_screen()
