# python game with pygame : jumping pet game
# by. mppn98
import pygame
import sys
import random
import os


# step1 : 창 제목 설정, 화면 설정

pygame.init()
pygame.display.set_caption('Jumping Pet Game')
MAX_WIDTH = 1280
MAX_HEIGHT = 720

# 난이도 설정
difficulty_settings = {
    "easy": {"obstacle_speed": 10, "item_frequency": 3000},
    "medium": {"obstacle_speed": 15, "item_frequency": 2000},
    "hard": {"obstacle_speed": 20, "item_frequency": 1000},
}


def main():
    # 창 설정, fps 설정
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # 난이도 선택 화면 표시
    difficulty = select_difficulty(screen, fps)
    settings = difficulty_settings[difficulty]


    # 효과음 초기화
    pygame.mixer.init()
    jump_sound = pygame.mixer.Sound('sounds/jump.wav')
    collision_sound = pygame.mixer.Sound('sounds/collision.wav')
    pygame.mixer.music.load('sounds/background_music.mp3')
    pygame.mixer.music.play(-1)  # 무한 반복 재생

    # pet 설정
    pet_images = [pygame.image.load(f'picture/pet{i}.png') for i in range(1, 3)]
    pet_images = [pygame.transform.scale(img, (img.get_width() // 3, img.get_height() // 3)) for img in pet_images]
    pet_height = pet_images[0].get_size()[1]
    pet_bottom = MAX_HEIGHT - pet_height
    pet_x = 50
    pet_y = pet_bottom
    jump_top = 300
    is_bottom = True
    is_go_up = False

    # 애니메이션을 위한 변수
    pet_index = 0
    animation_delay = 5
    animation_counter = 0

    #장애물 설정
    obstacle_images = [
        pygame.transform.scale(pygame.image.load('picture/tree.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('picture/rock.png'), (80, 80)),
        pygame.transform.scale(pygame.image.load('picture/bird.png'), (120, 60))
]
    
    # 장애물 초기화 부분 수정   
    current_obstacle = random.choice(obstacle_images)
    obstacle_height = current_obstacle.get_size()[1]
    if current_obstacle == obstacle_images[2]:  # bird
        obstacle_y = random.randint(100, 300)  # 하늘에 위치하도록
    else:
        obstacle_y = MAX_HEIGHT - obstacle_height
    obstacle_x = MAX_WIDTH


    # 장애물 속도 변수 추가
    obstacle_speed = 17.0

    # 충돌 횟수
    collision_count = 0

    # 점수
    score = 0

    # 레벨을 나타내는 변수 추가
    level=1

    #체력변수 추가
    health = 3

    # 점수판 글꼴 설정
    font = pygame.font.Font(None, 74)

    # 아이템 이미지와 초기 위치 설정
    food_image = pygame.transform.scale(pygame.image.load('picture/food.png'), (50, 50))
    life_image = pygame.transform.scale(pygame.image.load('picture/life.png'), (50, 50))
    food_x = random.randint(MAX_WIDTH, MAX_WIDTH + 500)
    food_y = random.randint(jump_top, pet_bottom)
    life_x = random.randint(MAX_WIDTH, MAX_WIDTH + 500)
    life_y = random.randint(jump_top, pet_bottom)



    while True:
        screen.fill((135, 206, 235))  # 하늘색

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False
                    # 점프 효과음 재생
                    jump_sound.play()
        
        # pet 이동
        if is_go_up:
            pet_y -= 15.0
        elif not is_go_up and not is_bottom:
            pet_y += 15.0

        # pet top, bottom 체크
        if is_go_up and pet_y <= jump_top:  # end up
            is_go_up = False

        if not is_bottom and pet_y >= pet_bottom:
            is_bottom = True
            pet_y = pet_bottom
        
        

        # 장애물 이동
        obstacle_x -= obstacle_speed
        # 점수 처리 부분 수정
        if obstacle_x <= -100:
            if not pet_rect.colliderect(obstacle_rect):
                score += 1
                if score % 5 == 0:
                    obstacle_speed += 3
                    level += 1  # 레벨 증가
            obstacle_x = MAX_WIDTH
            current_obstacle = random.choice(obstacle_images)
            obstacle_height = current_obstacle.get_size()[1]
            if current_obstacle == obstacle_images[2]:  # bird
                obstacle_y = random.randint(100, 300)  # 하늘에 위치하도록
            else:
                obstacle_y = MAX_HEIGHT - obstacle_height


        # 장애물 그리기
        screen.blit(current_obstacle, (obstacle_x, obstacle_y))

        # 애니메이션 프레임 교체
        animation_counter += 1
        if animation_counter >= animation_delay:
            pet_index = (pet_index + 1) % len(pet_images)
            animation_counter = 0

        # pet 그리기
        screen.blit(pet_images[pet_index], (pet_x, pet_y))
        

        # 충돌 감지
        pet_rect = pet_images[pet_index].get_rect(topleft=(pet_x, pet_y))
        obstacle_rect = current_obstacle.get_rect(topleft=(obstacle_x, obstacle_y))

        
        if pet_rect.colliderect(obstacle_rect):
            health -= 1
            collision_count += 1
            obstacle_x = MAX_WIDTH  # 충돌 시 장애물을 화면 밖으로 재배치
            # 충돌 효과음 재생
            collision_sound.play()

        # 체력 화면에 표시
        health_text = font.render(f"Life: {health}", True, (0, 0, 0))
        screen.blit(health_text, (10, 10))

        # 점수를 화면에 표시
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 80))

        # 레벨을 화면에 표시
        level_text = font.render(f"Level: {level}", True, (0, 0, 0))
        screen.blit(level_text, (MAX_WIDTH - level_text.get_width() - 10, 10))

        # 체력이 0이 되면 게임 오버 처리
        if health <= 0:
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, (MAX_WIDTH // 2 - 150, MAX_HEIGHT // 2 - 50))
            pygame.display.update()
            pygame.time.wait(2000)  # 2초 대기
            # 게임 재시작 여부를 묻는 메시지 추가
            restart_text = font.render("Press R to Restart", True, (0, 0, 0))
            screen.blit(restart_text, (MAX_WIDTH // 2 - 200, MAX_HEIGHT // 2))
            pygame.display.update()
            wait_for_restart = True
            while wait_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        wait_for_restart = False
                        main()  # 재시작을 위해 main 함수를 다시 호출
            pygame.quit()
            sys.exit()

        # 아이템 그리기
        screen.blit(food_image, (food_x, food_y))
        screen.blit(life_image, (life_x, life_y))

        # 아이템 이동
        food_x -= obstacle_speed
        life_x -= obstacle_speed

        # 아이템이 화면을 벗어나면 새 위치로 재배치
        if food_x < -50:
            food_x = random.randint(MAX_WIDTH, MAX_WIDTH + 500)
            food_y = random.randint(jump_top, pet_bottom)

        if life_x < -50:
            life_x = random.randint(MAX_WIDTH, MAX_WIDTH + 500)
            life_y = random.randint(jump_top, pet_bottom)

        # 아이템 충돌 처리
        food_rect = food_image.get_rect(topleft=(food_x, food_y))
        life_rect = life_image.get_rect(topleft=(life_x, life_y))
        

        if pet_rect.colliderect(food_rect):
            score += 1  # food 획득 시 점수 증가
            food_x = random.randint(MAX_WIDTH, MAX_WIDTH + 500)
            food_y = random.randint(jump_top, pet_bottom)
        
        if pet_rect.colliderect(life_rect):
            health = min(health + 1, 3)  # life 획득 시 체력 증가, 최대 체력은 3
            life_x = random.randint(MAX_WIDTH, MAX_WIDTH + 500)
            life_y = random.randint(jump_top, pet_bottom)

        # 화면 업데이트
        pygame.display.update()
        fps.tick(33) # fps 설정

def select_difficulty(screen, fps):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)
    title_text = font.render("Select Difficulty", True, (0, 0, 0))
    easy_text = small_font.render("1. Easy", True, (0, 0, 0))
    medium_text = small_font.render("2. Medium", True, (0, 0, 0))
    hard_text = small_font.render("3. Hard", True, (0, 0, 0))

    while True:
        screen.fill((135, 206, 235))
        screen.blit(title_text, (MAX_WIDTH // 2 - title_text.get_width() // 2, MAX_HEIGHT // 4))
        screen.blit(easy_text, (MAX_WIDTH // 2 - easy_text.get_width() // 2, MAX_HEIGHT // 2 - 50))
        screen.blit(medium_text, (MAX_WIDTH // 2 - medium_text.get_width() // 2, MAX_HEIGHT // 2))
        screen.blit(hard_text, (MAX_WIDTH // 2 - hard_text.get_width() // 2, MAX_HEIGHT // 2 + 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "easy"
                elif event.key == pygame.K_2:
                    return "medium"
                elif event.key == pygame.K_3:
                    return "hard"
        fps.tick(30)
        
if __name__ == '__main__':
    main()