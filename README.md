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

### 설치 방법
1. 저장소를 클론합니다:
    ```bash
    git clone https://github.com/mppn98/Mypet_jumping_game.git
    cd Mypet_jumping_game
    ```
2. Pygame 라이브러리를 설치합니다:
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

## Docker를 사용한 실행 방법

### 필요 사항
- Docker
- 먼저 Docker가 설치되어 있어야 합니다. 설치되어 있지 않은 경우 [Docker 공식 웹사이트](https://www.docker.com/)에서 다운로드하여 설치하세요.
### 실행 방법
1. 이 저장소를 클론합니다:
    ```bash
    git clone https://github.com/mppn98/Mypet_jumping_game.git
    ```
2. 저장소 디렉토리로 이동합니다:
    ```bash
    cd Mypet_jumping_game
    ```
3. 필요한 Python 패키지들을 설치하기 위해 Docker 컨테이너를 빌드합니다:
    ```bash
    docker build -t mypet_jumping_game .
    ```
4. 앱을 실행하기 위해 다음 명령어를 사용합니다:
    ```bash
    docker run -it --rm mypet_jumping_game
    ```

## Docker를 사용한 실행 방법

### 필요 사항
- Docker
- 먼저 Docker가 설치되어 있어야 합니다. 설치되어 있지 않은 경우 [Docker 공식 웹사이트](https://www.docker.com/)에서 다운로드하여 설치하세요.
### 실행 방법
1. 이 저장소를 클론합니다:
    ```bash
    git clone https://github.com/mppn98/Mypet_jumping_game.git
    ```
2. 저장소 디렉토리로 이동합니다:
    ```bash
    cd Mypet_jumping_game
    ```
3. 필요한 Python 패키지들을 설치하기 위해 Docker 컨테이너를 빌드합니다:
    ```bash
    docker build -t mypet_jumping_game .
    ```
4. 앱을 실행하기 위해 다음 명령어를 사용합니다:
    ```bash
    docker run -it --rm mypet_jumping_game
    ```


## 데모 영상
게임이 어떻게 실행되는지 보려면 아래의 데모 영상을 확인하세요.

![demo](https://github.com/mppn98/Mypet_jumping_game/assets/164157381/d58e71e3-67a1-42a3-bf75-012bb189a1f1)

## 코드 설명

### main.py
이 스크립트는 게임을 초기화하고, 게임 루프를 처리하며, 이벤트를 관리합니다.

- **초기화**: `pygame`을 초기화하고 게임 창을 설정합니다. 효과음을 로드하고, 펫과 장애물 이미지를 불러옵니다.
- **게임 루프**: 
  - **이벤트 처리**: 창 닫기 이벤트와 키 입력을 처리합니다. 스페이스바를 누르면 펫이 점프합니다.
  - **펫 이동**: 펫의 점프와 낙하를 처리합니다. 펫이 특정 높이에 도달하면 방향을 전환합니다.
  - **장애물 이동**: 장애물이 왼쪽으로 이동하며 화면을 벗어나면 새 장애물이 생성됩니다. 점수에 따라 장애물 속도가 증가합니다.
  - **애니메이션**: 펫의 애니메이션을 프레임 단위로 교체합니다.
  - **충돌 감지**: 펫과 장애물의 충돌을 감지하고, 충돌 시 효과음을 재생하며 충돌 횟수를 증가시킵니다.
  - **점수 및 충돌 횟수 표시**: 현재 점수와 충돌 횟수를 화면에 표시합니다. 충돌 횟수가 4회 이상이면 게임 오버 메시지를 표시하고 게임을 종료합니다.
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
