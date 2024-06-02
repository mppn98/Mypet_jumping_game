# python game with pygame : jumping pet game
# by. mppn98
import pygame
import sys

# step1 : 창 제목 설정, 화면 설정

pygame.init()
pygame.display.set_caption('Jumping Pet Game')
MAX_WIDTH = 1280
MAX_HEIGHT = 720


def main():
    # 창 설정, fps 설정
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # pet 설정
    pet_images = [pygame.image.load(f'pet{i}.png') for i in range(1, 3)]
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
    imgobstacle = pygame.transform.scale(pygame.image.load('tree.png'), (100, 100))  # 크기를 200x200으로 변경
    obstacle_height = imgobstacle.get_size()[1]
    obstacle_x = MAX_WIDTH
    obstacle_y = MAX_HEIGHT - obstacle_height

    # 충돌 횟수
    collision_count = 0

    # 점수
    score = 0

    # 점수판 글꼴 설정
    font = pygame.font.Font(None, 74)


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
        obstacle_x -= 17.0
        if obstacle_x <= -100:  # 장애물이 화면을 완전히 지나쳤을 때
            if not pet_rect.colliderect(obstacle_rect):  # 펫이 장애물과 충돌하지 않았을 때
                score += 1  # 점수 증가
            obstacle_x = MAX_WIDTH

        # 장애물 그리기
        screen.blit(imgobstacle, (obstacle_x, obstacle_y))

        # 애니메이션 프레임 교체
        animation_counter += 1
        if animation_counter >= animation_delay:
            pet_index = (pet_index + 1) % len(pet_images)
            animation_counter = 0

        # pet 그리기
        screen.blit(pet_images[pet_index], (pet_x, pet_y))
        

        # 충돌 감지
        pet_rect = pet_images[pet_index].get_rect(topleft=(pet_x, pet_y))
        obstacle_rect = imgobstacle.get_rect(topleft=(obstacle_x, obstacle_y))

        
        if pet_rect.colliderect(obstacle_rect):
            collision_count += 1
            obstacle_x = MAX_WIDTH  # 충돌 시 장애물을 화면 밖으로 재배치

        # 충돌횟수 화면에 표시
        collision_text = font.render(f"collisions: {collision_count}", True, (0, 0, 0))
        screen.blit(collision_text, (10, 10))

        # 점수를 화면에 표시
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 80))

        if collision_count >= 4:
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, (MAX_WIDTH // 2 - 150, MAX_HEIGHT // 2 - 50))
            pygame.display.update()
            pygame.time.wait(2000)  # 2초 대기
            pygame.quit()
            sys.exit()


        # 화면 업데이트
        pygame.display.update()
        fps.tick(33) # fps 설정


if __name__ == '__main__':
    main()