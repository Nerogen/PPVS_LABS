import sqlite3
import sys

import pygame.display

from Lab3.entity.enemy_class import *
from Lab3.entity.player_class import *

pygame.init()
vec = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH // COLS
        self.cell_height = MAZE_HEIGHT // ROWS
        self.walls = []
        self.coins = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        self.enemys = [
            r'D:\PPVS_LABS\Lab3\additional files\first.png',
            r'D:\PPVS_LABS\Lab3\additional files\second.png',
            r'D:\PPVS_LABS\Lab3\additional files\third.png',
            r'D:\PPVS_LABS\Lab3\additional files\fourth.png'
        ]
        self.player = Player(self, vec(self.p_pos))
        self.make_enemies()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'game over':
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('./additional files/maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

        with open("./additional files/walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xidx * self.cell_width, yidx * self.cell_height,
                                                                  self.cell_width, self.cell_height))

    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx, self.enemys[idx]))

    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, GREY, (x * self.cell_width, 0),
                             (x * self.cell_width, HEIGHT))
        for x in range(HEIGHT // self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height),
                             (WIDTH, x * self.cell_height))

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0

        self.coins = []
        with open("./additional files/walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
        self.state = "playing"

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, [
            WIDTH // 2, HEIGHT // 2 - 50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [
            WIDTH // 2, HEIGHT // 2 + 50], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('HIGH SCORE', self.screen, [4, 0],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        db = sqlite3.connect('serialization/user.db')
        sql = db.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS user (
                                   id INT,
                                   name TEXT,
                                   score INT)""")
        db.commit()

        top = []

        longest = 0
        name = ''

        for value in sql.execute("""SELECT * FROM user"""):
            if value[2] > longest:
                longest = value[2]
                name = value[1]
        top.append(longest)

        self.draw_text(f'{top[0]} {name}', self.screen, [5, 20],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)

        pygame.display.update()

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_KP6:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_KP8:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_KP2:
                    self.player.move(vec(0, 1))

    def playing_update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
            if enemy.grid_pos == self.player.grid_pos:
                self.remove_life()

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER // 2, TOP_BOTTOM_BUFFER // 2))
        self.draw_coins()

        self.draw_text('CURRENT SCORE: {}'.format(self.player.current_score),
                       self.screen, [60, 0], 18, WHITE, START_FONT)

        db = sqlite3.connect('serialization/user.db')
        sql = db.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS user (
                                           id INT,
                                           name TEXT,
                                           score INT)""")
        db.commit()

        longest = 0

        for value in sql.execute("""SELECT * FROM user"""):
            if value[2] > longest:
                longest = value[2]

        self.draw_text(f'HIGH SCORE: {longest}', self.screen, [WIDTH // 2 + 60, 0], 18, WHITE, START_FONT)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.update()

    def remove_life(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            pygame.mixer.music.load("./additional files/Death.mp3"),
            pygame.mixer.music.play(1)
            self.state = "game over"
        else:
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (124, 123, 7),
                               (int(coin.x * self.cell_width) + self.cell_width // 2 + TOP_BOTTOM_BUFFER // 2,
                                int(coin.y * self.cell_height) + self.cell_height // 2 + TOP_BOTTOM_BUFFER // 2), 5)

    def game_over_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                name = input("Input name: ")
                db = sqlite3.connect('serialization/user.db')
                sql = db.cursor()

                sql.execute("""CREATE TABLE IF NOT EXISTS user (
                    id INT,
                    name TEXT,
                    score INT)""")
                db.commit()

                count = 0

                for _ in sql.execute("""SELECT * FROM user"""):
                    count += 1

                sql.execute("""INSERT INTO user VALUES (?,?,?)""", (count, name, self.player.current_score))
                db.commit()

                for value in sql.execute("""SELECT * FROM user"""):
                    print(value)

    def game_over_update(self):
        pass

    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press the escape button to QUIT"
        again_text = "Press SPACE bar to PLAY AGAIN"
        new_score = "Press enter button to make new score record"
        self.draw_text("GAME OVER", self.screen, [WIDTH // 2, 100], 52, RED, "arial", centered=True)
        self.draw_text(again_text, self.screen, [
            WIDTH // 2, HEIGHT // 2], 36, (190, 190, 190), "arial", centered=True)
        self.draw_text(quit_text, self.screen, [
            WIDTH // 2, HEIGHT // 1.5], 36, (190, 190, 190), "arial", centered=True)
        self.draw_text(new_score, self.screen, [
            WIDTH // 2, HEIGHT // 1.25], 36, (190, 190, 190), "arial", centered=True)

        pygame.display.update()
