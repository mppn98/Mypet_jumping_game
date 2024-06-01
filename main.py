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
    imgpet = pygame.image.load('pet.jpg')
    imgpet = pygame.transform.scale(imgpet, (imgpet.get_width() // 7, imgpet.get_height() // 7))
    pet_height = imgpet.get_size()[1]
    pet_bottom = MAX_HEIGHT - pet_height
    pet_x = 50
    pet_y = pet_bottom
    jump_top = 300
    is_bottom = True
    is_go_up = False

    #장애물 설정
    imgobstacle = pygame.transform.scale(pygame.image.load('tree.png'), (100, 100))  # 크기를 200x200으로 변경

    obstacle_height = imgobstacle.get_size()[1]
    obstacle_x = MAX_WIDTH
    obstacle_y = MAX_HEIGHT - obstacle_height



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
            screen.blit(imgpet, (pet_x, pet_y))

        # 장애물 이동
        obstacle_x -= 17.0
        if obstacle_x <= -200:
            obstacle_x = MAX_WIDTH

        # 장애물 그리기
        screen.blit(imgobstacle, (obstacle_x, obstacle_y))

        # pet 그리기
        screen.blit(imgpet, (pet_x, pet_y))

        # 화면 업데이트
        pygame.display.update()
        fps.tick(33) # fps 설정


if __name__ == '__main__':
    main()