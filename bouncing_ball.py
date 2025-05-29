import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Màu sắc
BG_COLOR = (30, 30, 30)

# Load âm thanh phản xạ
bounce_sound = pygame.mixer.Sound("bounce.wav")

# FPS và Clock
FPS = 60
clock = pygame.time.Clock()

# Lớp Ball
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = [speed_x, speed_y]

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

        # Va chạm cạnh trái/phải
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.speed[0] = -self.speed[0]
            bounce_sound.play()

        # Va chạm cạnh trên/dưới
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.speed[1] = -self.speed[1]
            bounce_sound.play()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Tạo danh sách bóng
balls = []
for _ in range(5):  # Thêm 5 quả bóng
    radius = random.randint(15, 30)
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    color = [random.randint(100, 255) for _ in range(3)]
    speed_x = random.choice([-4, -3, 3, 4])
    speed_y = random.choice([-4, -3, 3, 4])
    balls.append(Ball(x, y, radius, color, speed_x, speed_y))

# Vòng lặp game
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật và vẽ bóng
    screen.fill(BG_COLOR)
    for ball in balls:
        ball.move()
        ball.draw(screen)

    pygame.display.flip()

pygame.quit()
