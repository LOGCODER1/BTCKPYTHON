# BTCKPYTHON
bài tập khóa python cơ bản
# Bouncing Ball Game - Hướng dẫn chi tiết

## **1. Giới thiệu**
Trò chơi **Bouncing Ball** là một trong những dự án game cơ bản nhưng rất thú vị, giúp bạn hiểu rõ hơn về cách lập trình game 2D, xử lý va chạm, và hoạt hình. Dự án này sẽ sử dụng thư viện **Pygame** để tạo một cửa sổ game, quản lý đối tượng di chuyển và phản xạ bóng khi va chạm vào các cạnh màn hình.

### **Mục tiêu dự án:**
- Tạo một cửa sổ game với Pygame.
- Di chuyển bóng tự do trong màn hình.
- Phản xạ bóng khi va chạm vào các cạnh.
- Thêm âm thanh và hiệu ứng để tăng trải nghiệm.

---

## **2. Các bước thực hiện**

### **Bước 1: Cài đặt môi trường**
- Cài đặt **Pygame**:
```bash
pip install pygame
```

### **Bước 2: Khởi tạo cửa sổ game**
- Tạo một file **`bouncing_ball.py`** và khởi tạo cửa sổ game:
```python
import pygame

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Màu nền
BG_COLOR = (30, 30, 30)

# Vòng lặp game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tô màu nền
    screen.fill(BG_COLOR)
    pygame.display.flip()

pygame.quit()
```

### **Bước 3: Tạo đối tượng bóng**
- Thêm logic tạo bóng và thiết lập vị trí ban đầu:
```python
import random

BALL_RADIUS = 20
BALL_COLOR = (255, 165, 0)
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
```

### **Bước 4: Cập nhật vị trí bóng**
- Di chuyển bóng trong vòng lặp game:
```python
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật vị trí bóng
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Phản xạ khi va chạm với cạnh màn hình
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_speed[1] = -ball_speed[1]

    # Vẽ bóng
    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, BALL_RADIUS)
    pygame.display.flip()

pygame.quit()
```

### **Bước 5: Thêm âm thanh phản xạ**
- Thêm âm thanh mỗi khi bóng va chạm vào tường:
```python
# Thêm đoạn này sau khi khởi tạo Pygame
bounce_sound = pygame.mixer.Sound("bounce.wav")

# Thêm vào logic phản xạ
if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
    ball_speed[0] = -ball_speed[0]
    bounce_sound.play()
if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
    ball_speed[1] = -ball_speed[1]
    bounce_sound.play()
```

### **Bước 6: Tối ưu hóa và cải tiến**
- Thêm nhiều bóng.
- Thay đổi kích thước và tốc độ bóng.
- Thêm tính năng ghi điểm hoặc mạng sống.

### **Bước 7: Chạy và thử nghiệm**
- Chạy game và kiểm tra mọi chức năng.
```bash
python bouncing_ball.py
```

---

## **3. Tổng kết**
- Đã tạo được trò chơi Bouncing Ball cơ bản.
- Đã áp dụng các thuật toán xử lý va chạm.
- Đã thêm âm thanh và hiệu ứng để tăng trải nghiệm game.

Hãy tiếp tục mở rộng trò chơi với nhiều thử thách và tính năng thú vị hơn!
