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

    while True:
        screen.fill((135, 206, 235))  # 하늘색

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 화면 업데이트
        pygame.display.update()
        fps.tick(33) # fps 설정


if __name__ == '__main__':
    main()