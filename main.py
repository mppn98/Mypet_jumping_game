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
    imgpet = pygame.image.load('pet.png')  
    pet_height = imgpet.get_size()[1]
    pet_bottom = MAX_HEIGHT - pet_height
    pet_x = 50
    pet_y = pet_bottom
    jump_top = 200
    is_bottom = True
    is_go_up = False


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

        # 화면 업데이트
        pygame.display.update()
        fps.tick(33) # fps 설정


if __name__ == '__main__':
    main()