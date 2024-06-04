# MyPet 점프 게임

MyPet 점프 게임에 오신 것을 환영합니다! 이 게임은 여러분의 펫 캐릭터가 장애물을 뛰어넘는 간단하면서도 재미있는 게임입니다. 이 README 파일에서는 게임 실행 방법, 데모 영상, 코드 설명 및 참고 자료를 제공합니다.

## 목차
1. [게임 실행 방법](#게임-실행-방법)
2. [데모 영상](#데모-영상)
3. [코드 설명](#코드-설명)
4. [참고 자료](#참고-자료)

## 게임 실행 방법

### 필요 사항
- Python 3.x
- Pygame 라이브러리
# 지원 Operating Systems 및 실행 방법

## 지원 Operating Systems
|OS| 지원 여부 |
|-----|--------|
|windows | :o:  |
| Linux  | :o: |

## 설치 방법
### Windows

1. python3.12를 설치합니다.

2. 저장소를 클론합니다:
    ```bash
    git clone https://github.com/mppn98/Mypet_jumping_game.git
    cd Mypet_jumping_game
    ```
3. Pygame 라이브러리를 설치합니다:
    ```bash
    pip3 install pygame or pip install pygame
    ```
    
### 게임 실행
1. 프로젝트 디렉토리로 이동합니다.
    ```bash
    cd Mypet_jumping_game
    ```
2. 메인 게임 스크립트를 실행합니다:
    ```bash
    python3 main.py  or  python main.py
    ```

### Linux

1. python3.12를 설치합니다.

2. 저장소를 클론합니다:
    ```bash
    git clone https://github.com/mppn98/Mypet_jumping_game.git
    cd Mypet_jumping_game
    ```
3. Pygame 라이브러리를 설치합니다:
    ```bash
    pip install pygame
    ```
    
### 게임 실행
1. 프로젝트 디렉토리로 이동합니다.
    ```bash
    cd Mypet_jumping_game
    ```
2. 메인 게임 스크립트를 실행합니다:
    ```bash
    python3 main.py
    ```


## 데모 영상
게임이 어떻게 실행되는지 보려면 아래의 데모 영상을 확인하세요.

![demo](https://github.com/mppn98/Mypet_jumping_game/assets/164157381/d58e71e3-67a1-42a3-bf75-012bb189a1f1)

## 코드 설명

### main.py
이 스크립트는 게임을 초기화하고, 게임 루프를 처리하며, 이벤트를 관리합니다.

- **초기화**: `pygame`을 초기화하고 게임 창을 설정합니다. 효과음을 로드하고, 펫과 장애물 이미지를 불러옵니다.
- **난이도 설정**: 난이도에 따라 장애물 속도와 아이템 생성 빈도를 설정합니다.
- **게임 루프**: 
  - **이벤트 처리**: 창 닫기 이벤트와 키 입력을 처리합니다. 스페이스바를 누르면 펫이 점프합니다.
  - **펫 이동**: 펫의 점프와 낙하를 처리합니다. 펫이 특정 높이에 도달하면 방향을 전환합니다.
  - **장애물 이동**: 장애물이 왼쪽으로 이동하며 화면을 벗어나면 새 장애물이 생성됩니다. 점수에 따라 장애물 속도가 증가합니다.
  - **아이템 이동 및 충돌 처리**: 음식과 생명 아이템을 화면에 표시하고, 펫과의 충돌을 감지하여 점수와 체력을 업데이트합니다.
  - **애니메이션**: 펫의 애니메이션을 프레임 단위로 교체합니다.
  - **충돌 감지**: 펫과 장애물의 충돌을 감지하고, 충돌 시 효과음을 재생하며 충돌 횟수를 증가시킵니다.
  - **점수, 체력 및 레벨 표시**: 현재 점수, 체력 및 레벨을 화면에 표시합니다. 체력이 0이 되면 게임 오버 메시지를 표시하고 게임을 종료합니다.
  - **리더보드**: 게임 오버 시 리더보드를 업데이트하고 상위 점수를 표시합니다.
- **화면 업데이트**: 모든 요소를 화면에 그린 후 화면을 업데이트합니다.


### assets
- **picture/**: 게임에 사용되는 모든 이미지가 포함되어 있습니다.
- **sounds/**: 배경 음악 및 효과음을 포함한 모든 소리가 포함되어 있습니다.

### 음향 효과 참고
게임에서 사용된 음향 효과는 [freesound.org](https://freesound.org)에서 확인할 수 있습니다.

## 참고 자료
이 프로젝트는 다음 GitHub 저장소 및 자료를 참고하였습니다:
- [Pygame Documentation](https://www.pygame.org/docs/)
- 음향 효과 출처: [freesound.org](https://freesound.org)
- [Python Dinosaur Game](https://github.com/BlockDMask/Python_dinosaur_game/tree/master)
- 배경,장애물 출처: [kor.pngtree.com](https://kor.pngtree.com/)