import pygame

from Lab3.constants.settings import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, app, pos):
        pygame.sprite.Sprite.__init__(self)
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 3
        self.prev_x = 0
        self.prev_y = 0
        self.count = 0

    def update(self):
        if self.able_to_move:
            self.pix_pos += self.direction * self.speed
        if self.time_to_move():
            if self.stored_direction is not None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()

        self.grid_pos[0] = (self.pix_pos[0] - TOP_BOTTOM_BUFFER +
                            self.app.cell_width // 2) // self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - TOP_BOTTOM_BUFFER +
                            self.app.cell_height // 2) // self.app.cell_height + 1
        if self.on_coin():
            if self.current_score % 2:
                pygame.mixer.music.load("./additional files/chomp.mp3")
                pygame.mixer.music.play(1)
            self.eat_coin()

    def draw(self):

        if self.prev_x > self.pix_pos.x and self.prev_y == self.pix_pos.y and 10 < self.count < 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac2.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(pygame.transform.flip(image, True, True), rect)
            self.count += 1

        elif self.prev_x > self.pix_pos.x and self.prev_y == self.pix_pos.y and self.count >= 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac3.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(pygame.transform.flip(image, True, True), rect)
            self.count = 0

        elif self.prev_x < self.pix_pos.x and self.prev_y == self.pix_pos.y and 10 < self.count < 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac2.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(image, rect)
            self.count += 1

        elif self.prev_x < self.pix_pos.x and self.prev_y == self.pix_pos.y and self.count >= 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac3.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(image, rect)
            self.count = 0

        elif self.prev_x == self.pix_pos.x and self.prev_y >= self.pix_pos.y and 10 < self.count < 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac_up1.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(image, rect)
            self.count += 1

        elif self.prev_x == self.pix_pos.x and self.prev_y >= self.pix_pos.y and self.count >= 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac_up2.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(image, rect)
            self.count = 0

        elif self.prev_x == self.pix_pos.x and self.prev_y < self.pix_pos.y and 10 < self.count < 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac_down1.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(image, rect)
            self.count += 1

        elif self.prev_x == self.pix_pos.x and self.prev_y < self.pix_pos.y and self.count >= 25:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac_down2.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(image, rect)
            self.count = 0

        else:
            image = pygame.image.load(r'D:\PPVS_LABS\Lab3\additional files\pac1.png').convert_alpha()
            rect = image.get_rect(center=(int(self.pix_pos.x), int(self.pix_pos.y)))
            self.app.screen.blit(image, rect)
            self.count += 1

        self.prev_x = self.pix_pos.x
        self.prev_y = self.pix_pos.y

        # Drawing player lives
        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (30 + 20 * x, HEIGHT - 15), 7)

    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x + TOP_BOTTOM_BUFFER // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + TOP_BOTTOM_BUFFER // 2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1

    def move(self, direction):
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos[0] * self.app.cell_width) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_width // 2,
                   (self.grid_pos[1] * self.app.cell_height) +
                   TOP_BOTTOM_BUFFER // 2 + self.app.cell_height // 2)

    def time_to_move(self):
        if int(self.pix_pos.x + TOP_BOTTOM_BUFFER // 2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y + TOP_BOTTOM_BUFFER // 2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos + self.direction) == wall:
                return False
        return True
