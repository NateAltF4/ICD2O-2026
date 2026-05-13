import pygame
import sys
import random
import numpy as np

pygame.init()
pygame.font.init()
pygame.mixer.init()

LOGICAL_WIDTH, LOGICAL_HEIGHT = 480, 240

logical = pygame.Surface((LOGICAL_WIDTH, LOGICAL_HEIGHT))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()
pygame.display.set_caption("Forgotten Bug Knight")

lvl_name = "tile1.tile"

TILE_SIZE = 24

GRAVITY = 0.4
MAX_FALL_SPEED = 8

JUMP_FORCE = -9  
DOUBLE_JUMP_FORCE = -6

DASH_SPEED = 8
DASH_DURATION = 150
DASH_CD = 1500
MELEE_CD = 400
MELEE_RANGE = 30
MELEE_DAMAGE = 20

# Boss constants
BOSS_SCORE_REQUIREMENT = 300
BOSS_MAX_HP = 800
BOSS_SPEED_P1 = 0.9
BOSS_SPEED_P2 = 1.4
BOSS_FIREBALL_CD_P1 = 3000       
BOSS_FIREBALL_CD_P2 = 3000       
BOSS_RAIN_INTERVAL = 350         
BOSS_RAIN_DURATION = 15000       
BOSS_RISE_TARGET_Y = 35.0        
FIREBALL_SPEED = 3.0
FIREBALL_RAIN_SPEED = 4.0
FIREBALL_DAMAGE = 1

enemy_spawn_interval = 2000

FADE_DURATION = 800  
ENTRANCE_PROMPT_RADIUS = 3  

transition_active = False
transition_start = 0
transition_target = None
transition_phase = "out"
fade_surface = pygame.Surface((LOGICAL_WIDTH, LOGICAL_HEIGHT))
fade_surface.fill((0, 0, 0))

footstep_channel = None
dash_channel = None
charging_channel = None
atk_channel = None
bg_music_channel = None

last_enemy_spawn = 0

# Global boss and fireball lists
boss = None
fireballs = []


# ─── SPRITES ────────────────────────────────────────────────────────────────

SPRITES = {
    "idle": {
        "sheet": pygame.image.load("player-idle-anim.png").convert_alpha(),
        "frames": 4,
    },
    "run": {
        "sheet": pygame.image.load("player-running-anim.png").convert_alpha(),
        "frames": 6,
    },
    "jump": {
        "sheet": pygame.image.load("player-jump-anim.png").convert_alpha(),
        "frames": 4,
    },
    "fall": {
        "sheet": pygame.image.load("player-fall-anim.png").convert_alpha(),
        "frames": 2,
    },
    "arm-idle": {
        "sheet": pygame.image.load("arm-idle-anim.png").convert_alpha(),
        "frames": 4,
    },
    "arm-atk": {
        "sheet": pygame.image.load("arm-atk-anim.png").convert_alpha(),
        "frames": 3,
    },
    "arm-jump": {
        "sheet": pygame.image.load("arm-jump-anim.png").convert_alpha(),
        "frames": 4,
    },
    "arm-run": {
        "sheet": pygame.image.load("arm-jump-anim.png").convert_alpha(),
        "frames": 4,
    },
    "heart": {
        "sheet": pygame.image.load("heart.png").convert_alpha(),
        "frames": 1,
    },
    "heart-outline": {
        "sheet": pygame.image.load("heart-outline.png").convert_alpha(),
        "frames": 1,
    }
}

BOSS_SPRITES = {
    "walk": {
        "sheet": pygame.image.load("boss-walk.png").convert_alpha(),
        "frames": 7,
    },
    "fly": {
        "sheet": pygame.image.load("boss-walk.png").convert_alpha(),
        "frames": 7,
    },
}

_fb_raw = pygame.image.load("fireball.png").convert_alpha()
FIREBALL_IMG = pygame.transform.scale(_fb_raw, (48, 48))


ENEMY_SPRITES = {
    "enemy-fox": {
        "sheet": pygame.image.load("enemy-fox.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 60,
        "speed": 0.5,
        "dmg": 1,
        "scale": 1,
    },
    "enemy-green-orb": {
        "sheet": pygame.image.load("enemy-green-orb.png").convert_alpha(),
        "frames": 10,
        "type": "fly",
        "hp": 40,
        "speed": 0.7,
        "dmg": 1,
        "scale": 1,
    },
    "enemy-soul-wisp": {
        "sheet": pygame.image.load("enemy-soul-wisp.png").convert_alpha(),
        "frames": 5,
        "type": "fly",
        "hp": 40,
        "speed": 0.8,
        "dmg": 1,
        "scale": 1.5,
    },
    "enemy-night-crawler": {
        "sheet": pygame.image.load("enemy-night-crawler.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 60,
        "speed": 0.6,
        "dmg": 1,
        "scale": 1.5,
    },
    "enemy-sand-stalker": {
        "sheet": pygame.image.load("enemy-sand-stalker.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 80,
        "speed": 0.6,
        "dmg": 1,
        "scale": 0.85,
    },
    "enemy-skin-crawler": {
        "sheet": pygame.image.load("enemy-skin-crawler.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 60,
        "speed": 0.7,
        "dmg": 1,
        "scale": 0.8,
    },
    "enemy-magma-shark": {
        "sheet": pygame.image.load("enemy-magma-shark.png").convert_alpha(),
        "frames": 5,
        "type": "fly",
        "hp": 80,
        "speed": 0.7,
        "dmg": 1,
        "scale": 1.5,
    },
    "enemy-magma-dog": {
        "sheet": pygame.image.load("enemy-magma-dog.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 60,
        "speed": 0.6,
        "dmg": 1,
        "scale": 1.5,
    },
    "enemy-ice-worm": {
        "sheet": pygame.image.load("enemy-ice-worm.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 40,
        "speed": 0.4,
        "dmg": 1,
        "scale": 1.5,
    },
    "enemy-ice-golem": {
        "sheet": pygame.image.load("enemy-ice-golem.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 100,
        "speed": 0.3,
        "dmg": 1,
        "scale": 1.5,
    },
    "enemy-rock-turtle": {
        "sheet": pygame.image.load("enemy-rock-turtle.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 80,
        "speed": 0.3,
        "dmg": 1,
        "scale": 1.5,
    },
    "enemy-ruin-lion": {
        "sheet": pygame.image.load("enemy-ruin-lion.png").convert_alpha(),
        "frames": 5,
        "type": "ground",
        "hp": 100,
        "speed": 0.3,
        "dmg": 1,
        "scale": 0.9,
    },
}

ROOM_ENEMIES = {
    "tile1.tile": ["enemy-green-orb", "enemy-fox"],
    "tile2.tile": ["enemy-soul-wisp", "enemy-night-crawler"],
    "tile3.tile": ["enemy-sand-stalker", "enemy-skin-crawler"],
    "tile4.tile": ["enemy-magma-shark", "enemy-magma-dog"],
    "tile5.tile": ["enemy-ice-worm", "enemy-ice-golem"],
    "tile6.tile": ["enemy-ruin-lion", "enemy-rock-turtle"],
}

BACKGROUNDS = {
    "tile1.tile": pygame.image.load("background-grass.webp").convert(),
    "tile2.tile": pygame.image.load("background-cave.webp").convert(),
    "tile3.tile": pygame.image.load("background-wasteland.webp").convert(),
    "tile4.tile": pygame.image.load("background-magma.webp").convert(),
    "tile5.tile": pygame.image.load("background-ice.png").convert(),
    "tile6.tile": pygame.image.load("background-ruin.webp").convert(),
    "tile7.tile": pygame.image.load("background-final.webp").convert()
}

TILES = {
    "grass": pygame.image.load("block-grass.png"),
    "cave": pygame.image.load("block-cave.png"),
    "wasteland": pygame.image.load("block-wasteland.png"),
    "magma": pygame.image.load("block-magma.png"),
    "ice": pygame.image.load("block-ice.png"),
    "ruin": pygame.image.load("block-ruin.png"),
    "final": pygame.image.load("block-final.png")
}

SOUNDS = {
    "hurt-1": pygame.mixer.Sound("hurt-1.mp3"),
    "hurt-2": pygame.mixer.Sound("hurt-2.mp3"),
    "footsteps": pygame.mixer.Sound("footsteps.mp3"),
    "jump": pygame.mixer.Sound("jump.mp3"),
    "background": pygame.mixer.Sound("background-music.mp3"),
    "attack": pygame.mixer.Sound("slash.mp3"),
    "dash": pygame.mixer.Sound("dash.mp3"),
    "charging": pygame.mixer.Sound("charging.mp3")
}

SOLID_TILES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

PLAYER_STATES = ("idle", "run", "jump", "fall")


# ─── CLASSES ────────────────────────────────────────────────────────────────

class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.LEFT_EDGE = 100
        self.RIGHT_EDGE = 260
        self.TOP_EDGE = 60
        self.BOTTOM_EDGE = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 3
        self.moving = False
        self.x = 0
        self.player_screen_x = self.x
        self.y = 0
        self.current_lives = 5
        self.max_lives = 5
        self.score = 0

        self.max_soul = 100
        self.soul = 0

        self.is_healing = False
        self.heal_timer = 0
        self.heal_duration = 1500

        self.invulnerable = False
        self.invulnerability_duration = 2000
        self.last_hit_time = 0

        self.vel_y = 0.0
        self.on_ground = True
        self.double_jumped = False
        self.just_jumped = False

        self.direction = "right"
        self.state = "idle"
        self.prev_state = self.state

        self.frame_index = 0
        self.anim_speed = 100
        self.last_update = pygame.time.get_ticks() 
        self.last_arm_update = pygame.time.get_ticks()

        self.attacking = False
        self.attack_type = None      
        self.attack_start = 0
        self.last_attack = 0
                    
        self.last_melee = 0
        self.attack_finished_time = 0

        self.dashing = False
        self.dash_start = 0
        self.last_dash = 0

        self.last_melee_attack = 0
        self.melee_rect = None

        self.animations = {
            "run": self.load_frames(SPRITES["run"]["sheet"], SPRITES["run"]["frames"]),
            "idle": self.load_frames(SPRITES["idle"]["sheet"], SPRITES["idle"]["frames"]),
            "jump": self.load_frames(SPRITES["jump"]["sheet"], SPRITES["jump"]["frames"]),
            "fall": self.load_frames(SPRITES["fall"]["sheet"], SPRITES["fall"]["frames"])
        }

        self.animations_right = {
            state: [pygame.transform.flip(f, True, False) for f in frames]
            for state, frames in self.animations.items()
        }

        self.arm_animations = {
            "idle": self.load_frames(SPRITES["arm-idle"]["sheet"], SPRITES["arm-idle"]["frames"]),
            "run": self.load_frames(SPRITES["arm-run"]["sheet"], SPRITES["arm-run"]["frames"]),
            "jump": self.load_frames(SPRITES["arm-jump"]["sheet"], SPRITES["arm-jump"]["frames"]),
            "atk": self.load_frames(SPRITES["arm-atk"]["sheet"], SPRITES["arm-atk"]["frames"]),
        }

        self.arm_animations_right = {
            state: [pygame.transform.flip(f, True, False) for f in frames]
            for state, frames in self.arm_animations.items()
        }

        self.arm_frame_index = 0
        self.arm_image = self.arm_animations["idle"][0]

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect(topleft=(int(self.x), int(self.y)))

        self.hitbox = pygame.Rect(0, 0, 20, self.rect.height - 4) 
        self.hitbox.midbottom = self.rect.midbottom

        self.hit_flash_duration = 200

    def load_frames(self, sheet, num_frames):
        frames = []
        cell_w = sheet.get_width() // num_frames
        cell_h = sheet.get_height()
        bg_key = sheet.get_at((0, 0))[:3]

        for i in range(num_frames):
            rect = pygame.Rect(i * cell_w, 0, cell_w, cell_h)
            frame = sheet.subsurface(rect).copy()

            threshold = 30
            pixels = pygame.surfarray.pixels3d(frame)
            mask = (
                (pixels[:,:,0].astype(int) - bg_key[0])**2 +
                (pixels[:,:,1].astype(int) - bg_key[1])**2 +
                (pixels[:,:,2].astype(int) - bg_key[2])**2
            ) < threshold**2
            pixels[mask] = bg_key
            del pixels

            frame.set_colorkey(bg_key)
            frame = pygame.transform.scale(frame, (int(cell_w * 2), int(cell_h * 2)))
            frames.append(frame)

        return frames

    def move(self, collision_rects, camera: Camera):
        keys = pygame.key.get_pressed()
        self.moving = False

        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "left"
            self.moving = True
            if self.on_ground: 
                play_sound("step")

        if keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "right"
            self.moving = True
            if self.on_ground:
                play_sound("step")

        self.hitbox.x = int(self.x)

        self.player_screen_x = self.x - camera.x
        if self.player_screen_x > camera.RIGHT_EDGE:
            camera.x += self.player_screen_x - camera.RIGHT_EDGE
        elif self.player_screen_x < camera.LEFT_EDGE:
            camera.x += self.player_screen_x - camera.LEFT_EDGE
        camera.x = max(0, min(camera.x, world_w - LOGICAL_WIDTH))

        for tile in collision_rects:
            if self.hitbox.colliderect(tile):
                if keys[pygame.K_d]:
                    self.hitbox.right = tile.left
                elif keys[pygame.K_a]:
                    self.hitbox.left = tile.right
                self.x = float(self.hitbox.x)

        self.vel_y += GRAVITY
        if self.vel_y > MAX_FALL_SPEED:
            self.vel_y = MAX_FALL_SPEED

        if keys[pygame.K_SPACE] and self.on_ground and not self.just_jumped:
            self.vel_y = JUMP_FORCE
            self.on_ground = False
            self.double_jumped = False
            self.just_jumped = True
            play_sound("jump")
        else:
            self.just_jumped = False        

        self.y += self.vel_y
        self.hitbox.y = int(self.y)

        for tile in collision_rects:
            if self.hitbox.colliderect(tile):
                if self.vel_y > 0:
                    self.hitbox.bottom = tile.top
                    self.on_ground = True
                    self.double_jumped = False
                elif self.vel_y < 0:
                    self.hitbox.top = tile.bottom
                self.vel_y = 0
                self.y = float(self.hitbox.y)

        self.rect.midbottom = self.hitbox.midbottom
        self.x = float(self.hitbox.x)
        self.y = float(self.hitbox.y)

        if not self.on_ground:
            if self.vel_y > 1:
                self.state = "fall"
            elif self.vel_y < -1:
                self.state = "jump"
        elif self.moving:
            self.state = "run"
        else:
            self.state = "idle"

        if self.state != self.prev_state:
            self.frame_index = 0
            self.prev_state = self.state

        player_screen_y = self.y - camera.y
        if player_screen_y < camera.TOP_EDGE:
            camera.y += player_screen_y - camera.TOP_EDGE
        elif player_screen_y > camera.BOTTOM_EDGE:
            camera.y += player_screen_y - camera.BOTTOM_EDGE
        
        camera.y = max(0, min(camera.y, world_h - LOGICAL_HEIGHT))

        self.x = max(0, min(self.x, world_w - self.hitbox.width))
        self.x = float(self.hitbox.x)
        self.y = float(self.hitbox.y)
        self.x = max(0, min(self.x, world_w - self.hitbox.width))
        self.y = max(24, min(self.y, world_h - self.hitbox.height))

    def attack(self, events):
        now = pygame.time.get_ticks()

        if self.dashing:
            elapsed = now - self.dash_start
            play_sound("dash")
            if elapsed < DASH_DURATION:
                dash_dir = 1 if self.direction == "right" else -1
                self.x += DASH_SPEED * dash_dir
                self.x = max(0, min(self.x, world_w - self.hitbox.width))
                self.hitbox.x = int(self.x)
                self.rect.midbottom = self.hitbox.midbottom
            else:
                self.dashing = False

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    if now - self.last_dash >= DASH_CD:
                        self.dashing = True
                        self.dash_start = now
                        self.last_dash = now
                if event.key == pygame.K_SPACE:
                    if not self.on_ground and not self.double_jumped and not self.just_jumped:
                        self.vel_y = DOUBLE_JUMP_FORCE
                        self.double_jumped = True
                        play_sound("jump")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if now - self.last_melee_attack >= MELEE_CD and not self.dashing:
                        self.attacking = True
                        self.attack_type = "melee"
                        self.attack_start = now
                        self.frame_index = 0
                        self.arm_frame_index = 0
                        self.last_melee_attack = now
                        play_sound("attack")
                        if self.direction == "right":
                            self.melee_rect = pygame.Rect(self.hitbox.right, self.hitbox.top, MELEE_RANGE, self.hitbox.height)
                        else:
                            self.melee_rect = pygame.Rect(self.hitbox.left - MELEE_RANGE, self.hitbox.top, MELEE_RANGE, self.hitbox.height)

    def handle_healing(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

        if keys[pygame.K_f] and self.soul >= 33 and self.current_lives < self.max_lives and self.on_ground:
            if not self.is_healing:
                self.is_healing = True
                self.heal_timer = now
            
            if now - self.heal_timer >= self.heal_duration:
                self.current_lives += 1
                self.soul -= 33
                self.is_healing = False
        else:
            self.is_healing = False

    def take_damage(self, amount):
        now = pygame.time.get_ticks()
        if not self.invulnerable and self.current_lives > 0:
            self.current_lives -= amount
            if amount > 1:
                play_sound("hurt2")
            else:
                play_sound("hurt1")

            self.score -= 15
            self.soul += 7

            if self.current_lives < 0:
                self.current_lives = 0
            
            self.invulnerable = True
            self.last_hit_time = now
        
        if self.current_lives <= 0:
            self.current_lives = 0

    def update_timers(self):
        now = pygame.time.get_ticks()
        if self.invulnerable and (now - self.last_hit_time > self.invulnerability_duration):
            self.invulnerable = False        

    def get_draw_image(self):
        now = pygame.time.get_ticks()
        if self.invulnerable and (now - self.last_hit_time) < self.hit_flash_duration:
            white = self.image.copy()
            white.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MAX)
            return white
        return self.image

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.anim_speed:
            self.last_update = now

            display_state = self.state
            if self.attacking and self.attack_type in self.animations:
                display_state = self.attack_type

            frames = (
                self.animations_right[display_state]
                if self.direction == "right"
                else self.animations[display_state]
            )

            self.frame_index = self.frame_index % len(frames)
            self.image = frames[self.frame_index]
            self.frame_index = (self.frame_index + 1) % len(frames)

    def animate_arm(self):
        now = pygame.time.get_ticks()
        if now - self.last_arm_update > self.anim_speed:
            self.last_arm_update = now

            arm_state = self.state
            if arm_state not in self.arm_animations:
                arm_state = "jump"

            if self.attacking:
                arm_state = "atk"

            frames = (
                self.arm_animations_right[arm_state]
                if self.direction == "right"
                else self.arm_animations[arm_state]
            )

            if self.attacking:
                self.arm_frame_index = min(self.arm_frame_index, len(frames) - 1) 
                self.arm_image = frames[self.arm_frame_index]
                if self.arm_frame_index < len(frames) - 1:
                    self.arm_frame_index += 1
                else:
                    self.attacking = False  
                    self.arm_frame_index = 0
            else:
                self.arm_frame_index = self.arm_frame_index % len(frames)
                self.arm_image = frames[self.arm_frame_index]
                self.arm_frame_index = (self.arm_frame_index + 1) % len(frames)


class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y, damage=FIREBALL_DAMAGE):
        super().__init__()
        self.x = float(x)
        self.y = float(y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.damage = damage
        self.image = FIREBALL_IMG.copy()
        self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.center = (int(self.x), int(self.y))

    def is_off_screen(self):
        return (
            self.x < -60 or self.x > world_w + 60 or
            self.y < -60 or self.y > world_h + 60
        )


class Boss(pygame.sprite.Sprite):
    # Two-phase boss: Shadow Dragon.

    # Phase 1 — Ground:
    #     Walks toward the player using gravity + tile collision, identical to
    #     how a ground enemy moves. Fires an aimed fireball every 3 seconds.
    #     Transitions to phase 2 when HP drops to 50 %.

    # Phase 2 — Air, three substates driven by self.p2_substate:
    #     "rising"  — floats straight upward until y <= BOSS_RISE_TARGET_Y.
    #                 Invulnerable during this substate.
    #     "raining" — stays at height, rains many fireballs toward the player
    #                 for BOSS_RAIN_DURATION ms. Still invulnerable.
    #     "flying"  — becomes vulnerable again, flies freely toward the player,
    #                 fires aimed shots every 3 seconds.

    def __init__(self):
        super().__init__()

        self.max_hp = BOSS_MAX_HP
        self.hp = self.max_hp
        self.phase = 1
        self.invulnerable = False   # becomes True when phase 2 starts
        self.dead = False

        # World position (float for sub-pixel movement)
        self.x = float(world_w // 2)
        self.y = 50.0
        self.vel_y = 0.0
        self.on_ground = False
        self.direction = "right"

        # Phase 2 state machine
        self.p2_substate = None          # "rising", "raining", "flying"
        self.p2_start = 0               # time when current substate began

        # Shooting timers
        self.last_fireball = 0
        self.last_rain_fireball = 0

        # Hit-flash
        self.last_hit_time = 0
        self.hit_flash_duration = 150

        # Animation
        self.current_anim = "walk"
        self.frame_index = 0
        self.anim_speed = 150
        self.last_update = pygame.time.get_ticks()

        self.animations = {
            "walk": self._load_frames(
                BOSS_SPRITES["walk"]["sheet"],
                BOSS_SPRITES["walk"]["frames"]
            ),
            "fly": self._load_frames(
                BOSS_SPRITES["fly"]["sheet"],
                BOSS_SPRITES["fly"]["frames"]
            ),
        }
        # Pre-bake horizontally flipped copies so we don't flip every frame
        self.animations_flip = {
            anim: [pygame.transform.flip(f, True, False) for f in frames]
            for anim, frames in self.animations.items()
        }

        self.image = self.animations["walk"][0]
        self.rect = self.image.get_rect(topleft=(int(self.x), int(self.y)))
        self.hitbox = pygame.Rect(0, 0, self.rect.width - 8, self.rect.height - 20)
        self.hitbox.midbottom = self.rect.midbottom

    def _load_frames(self, sheet, num_frames):
        frames = []
        cell_w = sheet.get_width() // num_frames
        cell_h = sheet.get_height()
        bg_key = sheet.get_at((0, 0))[:3]

        for i in range(num_frames):
            rect = pygame.Rect(i * cell_w, 0, cell_w, cell_h)
            frame = sheet.subsurface(rect).copy()

            threshold = 30
            pixels = pygame.surfarray.pixels3d(frame)
            mask = (
                (pixels[:, :, 0].astype(int) - bg_key[0]) ** 2 +
                (pixels[:, :, 1].astype(int) - bg_key[1]) ** 2 +
                (pixels[:, :, 2].astype(int) - bg_key[2]) ** 2
            ) < threshold ** 2
            pixels[mask] = bg_key
            del pixels

            frame.set_colorkey(bg_key)
            frame = pygame.transform.scale(frame, (cell_w, cell_h))
            frames.append(frame)

        return frames

    def update(self, collision_rects, player, fireballs):
        now = pygame.time.get_ticks()

        if self.phase == 1 and self.hp <= self.max_hp // 2:
            self.phase = 2
            self.invulnerable = True          # immune until "flying" substate
            self.p2_substate = "rising"
            self.p2_start = now
            self.current_anim = "fly"
            self.frame_index = 0


        if player.hitbox.centerx < self.rect.centerx:
            self.direction = "left"
        else:
            self.direction = "right"

        if self.phase == 1:
            self._phase1(collision_rects, player, fireballs, now)
        else:
            self._phase2(player, fireballs, now)

        self.rect.topleft = (int(self.x), int(self.y))
        self.hitbox.midbottom = self.rect.midbottom

        self.animate()

    def _phase1(self, collision_rects, player, fireballs, now):
        self.current_anim = "walk"

        # Horizontal movement
        if self.rect.centerx > player.hitbox.centerx:
            self.x -= BOSS_SPEED_P1
        else:
            self.x += BOSS_SPEED_P1

        self.rect.x = int(self.x)

        # Horizontal tile collision
        for tile in collision_rects:
            if self.rect.colliderect(tile):
                if self.x > tile.centerx:
                    self.rect.left = tile.right
                else:
                    self.rect.right = tile.left
                self.x = float(self.rect.x)

        # Gravity
        self.vel_y = min(self.vel_y + GRAVITY, MAX_FALL_SPEED)
        self.y += self.vel_y
        self.rect.y = int(self.y)

        # Vertical tile collision
        self.on_ground = False
        for tile in collision_rects:
            if self.rect.colliderect(tile):
                if self.vel_y > 0:
                    self.rect.bottom = tile.top
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = tile.bottom
                self.vel_y = 0
                self.y = float(self.rect.y)

        # Shoot aimed fireball every 3 seconds
        if now - self.last_fireball >= BOSS_FIREBALL_CD_P1:
            self._shoot_at(player, fireballs)
            self.last_fireball = now

    # ── Phase 2 ─────────────────────────────────────────────────────────────

    def _phase2(self, player, fireballs, now):
        self.current_anim = "fly"

        if self.p2_substate == "rising":
            self._substate_rising(now)

        elif self.p2_substate == "raining":
            self._substate_raining(player, fireballs, now)

        elif self.p2_substate == "flying":
            self._substate_flying(player, fireballs, now)

    def _substate_rising(self, now):
        if self.y > BOSS_RISE_TARGET_Y:
            self.y -= 2.0
            self.rect.y = int(self.y)
        else:
            # Arrived at height — start the rain
            self.y = BOSS_RISE_TARGET_Y
            self.p2_substate = "raining"
            self.p2_start = now
            self.last_rain_fireball = now

    def _substate_raining(self, player, fireballs, now):
        # Drift slowly left/right to stay centred above the player
        if self.rect.centerx > player.hitbox.centerx + 4:
            self.x -= 0.5
        elif self.rect.centerx < player.hitbox.centerx - 4:
            self.x += 0.5
        self.rect.x = int(self.x)

        # Spawn rain fireballs on an interval
        if now - self.last_rain_fireball >= BOSS_RAIN_INTERVAL:
            offset = random.randint(-70, 70)
            spawn_x = player.hitbox.centerx + offset
            spawn_y = 0
            fireballs.append(Fireball(spawn_x, spawn_y, 0.0, FIREBALL_RAIN_SPEED))
            self.last_rain_fireball = now

        # Transition to flying after the rain window ends
        if now - self.p2_start >= BOSS_RAIN_DURATION:
            self.p2_substate = "flying"
            self.invulnerable = False        # vulnerable again
            self.p2_start = now
            self.last_fireball = now

    def _substate_flying(self, player, fireballs, now):
        # Horizontal chase
        if self.rect.centerx > player.hitbox.centerx:
            self.x -= BOSS_SPEED_P2
        else:
            self.x += BOSS_SPEED_P2

        if self.rect.centery > player.hitbox.centery:
            self.y -= BOSS_SPEED_P2 * 0.7
        else:
            self.y += BOSS_SPEED_P2 * 0.7
        
        self.y = min(175, self.y)

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if now - self.last_fireball >= BOSS_FIREBALL_CD_P2:
            self._shoot_at(player, fireballs)
            self.last_fireball = now

    def _shoot_at(self, player, fireballs):
        dx = player.hitbox.centerx - self.rect.centerx
        dy = player.hitbox.centery - self.rect.centery
        dist = max((dx * dx + dy * dy) ** 0.5, 1.0)
        vel_x = (dx / dist) * FIREBALL_SPEED
        vel_y = (dy / dist) * FIREBALL_SPEED
        fireball = Fireball(self.rect.centerx, self.rect.centery, vel_x, vel_y)
        if self.direction == "left":
            fireball.image = pygame.transform.flip(fireball.image, True, True)
        fireballs.append(fireball)

    def take_damage(self, amount):
        if not self.invulnerable:
            self.hp = max(0, self.hp - amount)
            self.last_hit_time = pygame.time.get_ticks()

    def get_draw_image(self):
        now = pygame.time.get_ticks()
        if not self.invulnerable and (now - self.last_hit_time) < self.hit_flash_duration:
            white = self.image.copy()
            white.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MAX)
            return white
        return self.image

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.anim_speed:
            self.last_update = now
            frames = (
                self.animations_flip[self.current_anim]
                if self.direction == "right"
                else self.animations[self.current_anim]
            )
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.image = frames[self.frame_index]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite_name=None):
        super().__init__()

        self.x = 100
        self.screen_x = self.x
        self.y = 100

        self.frame_index = 0
        self.anim_speed = 120
        self.last_update = pygame.time.get_ticks()

        self.vel_y = 0.0
        self.on_ground = False

        self.last_hit_time = 0

        self.enemy_sprite = sprite_name if sprite_name else random.choice(list(ENEMY_SPRITES))
        self.animations = {
            "anim": self.load_frames(ENEMY_SPRITES[self.enemy_sprite]["sheet"], ENEMY_SPRITES[self.enemy_sprite]["frames"], ENEMY_SPRITES[self.enemy_sprite]["scale"])
        }

        self.animations_left = {
            state: [pygame.transform.flip(f, True, False) for f in frames]
            for state, frames in self.animations.items()
        }

        self.type = ENEMY_SPRITES[self.enemy_sprite]["type"]
        self.hp = ENEMY_SPRITES[self.enemy_sprite]["hp"]
        self.speed = ENEMY_SPRITES[self.enemy_sprite]["speed"]
        self.dmg = ENEMY_SPRITES[self.enemy_sprite]["dmg"]
        self.image = self.animations["anim"][0]

        self.rect = self.image.get_rect()
        self.rect.topleft = (int(self.x), int(self.y))

        self.hitbox = pygame.Rect(0, 0, self.rect.width, self.rect.height - 5)
        self.hitbox.midbottom = self.rect.midbottom

        self.hit_flash_duration = 200
    
    def load_frames(self, sheet, num_frames, scale):
        content_rect = sheet.get_bounding_rect()
        sheet = sheet.subsurface(content_rect).copy()

        frames = []
        cell_w = sheet.get_width() // num_frames
        cell_h = sheet.get_height()
        bg_key = sheet.get_at((0, 0))[:3]

        for i in range(num_frames):
            rect = pygame.Rect(i * cell_w, 0, cell_w, cell_h)
            frame = sheet.subsurface(rect).copy()

            threshold = 30
            pixels = pygame.surfarray.pixels3d(frame)
            mask = (
                (pixels[:,:,0].astype(int) - bg_key[0])**2 +
                (pixels[:,:,1].astype(int) - bg_key[1])**2 +
                (pixels[:,:,2].astype(int) - bg_key[2])**2
            ) < threshold**2
            pixels[mask] = bg_key
            del pixels

            frame.set_colorkey(bg_key)
            frame = pygame.transform.scale(frame, (cell_w * scale, cell_h * scale))
            frames.append(frame)

        return frames

    def move(self, collision_rects, player: Player):
        if self.rect.centerx > player.hitbox.centerx:
            self.x -= self.speed
        elif self.rect.centerx < player.hitbox.centerx:
            self.x += self.speed

        self.rect.x = int(self.x)

        for tile in collision_rects:
            if self.rect.colliderect(tile):
                overlap_left = self.rect.right - tile.left
                overlap_right = tile.right - self.rect.left
                if overlap_left < overlap_right:
                    self.rect.right = tile.left
                    self.rect.y = int(self.y)
                else:
                    self.rect.left = tile.right
                    self.rect.y = int(self.y)
                    
                self.x = float(self.rect.x)
                self.rect.y -= TILE_SIZE
                self.y = float(self.rect.y)

        if self.type == "fly":
            if self.rect.centery > player.hitbox.centery:
                self.y -= self.speed
            elif self.rect.centery < player.hitbox.centery:
                self.y += self.speed

            self.rect.y = int(self.y)

            for tile in collision_rects:
                if self.rect.colliderect(tile):
                    overlap_top = self.rect.bottom - tile.top
                    overlap_bottom = tile.bottom - self.rect.top
                    if overlap_top < overlap_bottom:
                        self.rect.bottom = tile.top
                    else:
                        self.rect.top = tile.bottom
                    self.y = float(self.rect.y)
        else:
            self.vel_y += GRAVITY
            if self.vel_y > MAX_FALL_SPEED:
                self.vel_y = MAX_FALL_SPEED

            self.y += self.vel_y
            self.rect.y = int(self.y)

            self.on_ground = False
            for tile in collision_rects:
                if self.rect.colliderect(tile):
                    if self.vel_y > 0:
                        self.rect.bottom = tile.top
                        self.on_ground = True
                    elif self.vel_y < 0:
                        self.rect.top = tile.bottom
                    self.vel_y = 0
                    self.y = float(self.rect.y)

        self.hitbox.midbottom = self.rect.midbottom

    def get_draw_image(self):
        now = pygame.time.get_ticks()
        if (now - self.last_hit_time) < self.hit_flash_duration:
            white = self.image.copy()
            white.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MAX)
            return white
        return self.image

    def death(self, enemies: list):
        if self.hp <= 0:
            self.hp = 0
            enemies.remove(self)

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.anim_speed:
            self.last_update = now
            frames = self.animations["anim"]
            if self.rect.centerx < player.hitbox.centerx:
                frames = self.animations_left["anim"]
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.image = frames[self.frame_index]


def build_collision_rects(grid):
    rects = []
    for row_i, row in enumerate(grid):
        for col_i, value in enumerate(row):
            if value in SOLID_TILES:
                rects.append(pygame.Rect(
                    col_i * TILE_SIZE,
                    row_i * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                ))
    return rects

def draw_background(surface, camera):
    bg = BACKGROUNDS.get(lvl_name)
    if not bg:
        surface.fill((0, 200, 255))
        return

    offset_x = int(camera.x)
    offset_x = max(0, min(offset_x, world_w - LOGICAL_WIDTH))
    offset_y = int(camera.y)
    offset_y = max(0, min(offset_y, world_h - LOGICAL_HEIGHT))

    surface.blit(bg, (0, 0), area=pygame.Rect(offset_x, offset_y - 48, LOGICAL_WIDTH, LOGICAL_HEIGHT))

def update(player: Player, collision_rects, events, camera: Camera, enemies: list, entrances: dict):
    global boss, fireballs

    player.update_timers()
    player.handle_healing()

    player.max_lives = 5 + player.score // 200 if player.score >= 0 else 5

    if not player.is_healing:
        player.move(collision_rects, camera)
    player.attack(events)
    player.animate()
    player.animate_arm()

    # ── Regular enemies ────────────────────────────────────────────────────
    for enemy in enemies[:]:
        enemy.move(collision_rects, player)

        if player.hitbox.colliderect(enemy.rect):
            player.take_damage(enemy.dmg)

        if player.melee_rect and enemy.rect.colliderect(player.melee_rect):
            enemy.hp -= MELEE_DAMAGE
            player.soul += 2
            if player.soul > player.max_soul:
                player.soul = player.max_soul
            enemy.x -= 10 if player.direction == "left" else -10
            enemy.last_hit_time = pygame.time.get_ticks()

        if enemy.hp <= 0:
            player.score += 15
            enemies.remove(enemy)
            continue

        enemy.animate()

    # ── Boss ───────────────────────────────────────────────────────────────
    if boss is not None and not boss.dead:
        boss.update(collision_rects, player, fireballs)

        if player.melee_rect and boss.hitbox.colliderect(player.melee_rect):
            boss.take_damage(MELEE_DAMAGE)
            player.soul = min(player.soul + 2, player.max_soul)

        # Boss body collision with player
        if player.hitbox.colliderect(boss.hitbox):
            player.take_damage(1)

        if boss.hp <= 0:
            boss.dead = True

    player.melee_rect = None

    # ── Fireballs ─────────────────────────────────────────────────────────
    for fb in fireballs[:]:
        fb.update()

        # Damage player on contact
        if player.hitbox.colliderect(fb.rect):
            player.take_damage(fb.damage)
            fireballs.remove(fb)
            continue

        # Remove if off-screen or hit a solid tile
        if fb.is_off_screen():
            fireballs.remove(fb)
            continue

        hit_wall = False
        for tile in collision_rects:
            if fb.rect.colliderect(tile):
                hit_wall = True
                break
        if hit_wall:
            fireballs.remove(fb)

    # ── Entrance / room transitions ────────────────────────────────────────
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            current_entrances = entrances.get(lvl_name, [])
            for (ent_rect, dest_file, dest_col, dest_row) in current_entrances:
                if player.hitbox.colliderect(ent_rect):
                    # Gate the boss room behind the score requirement
                    if dest_file == "tile7.tile" and player.score < BOSS_SCORE_REQUIREMENT:
                        break  # silently deny — the prompt already shows the requirement
                    start_transition(dest_file, dest_col, dest_row)
                    break

def get_letterbox_rect(surface_size, target_size):
    sw, sh = surface_size
    tw, th = target_size
    scale = min(tw / sw, th / sh)
    w = int(sw * scale)
    h = int(sh * scale)
    x = (tw - w) // 2
    y = (th - h) // 2
    return pygame.Rect(x, y, w, h)

def draw_ui(surface, player, camera):
    mask_spacing = 30
    start_x = 10
    start_y = 10
    heart_sprite = SPRITES["heart"]["sheet"]
    heart_outline_sprite = SPRITES["heart-outline"]["sheet"]

    for i in range(player.max_lives):
        x = start_x + (i * mask_spacing)
        y = start_y
        if i < player.current_lives:
            logical.blit(heart_sprite, (x, y))
        else:
            logical.blit(heart_outline_sprite, (x, y))
    
    bar_x = 10
    bar_y = 40
    bar_width = 80
    bar_height = 8
    
    pygame.draw.rect(surface, (40, 40, 40), (bar_x, bar_y, bar_width, bar_height))
    
    fill_percentage = max(0, min(player.soul / player.max_soul, 1.0))
    fill_width = int(bar_width * fill_percentage)
    
    if fill_width > 0:
        pygame.draw.rect(surface, (135, 206, 255), (bar_x, bar_y, fill_width, bar_height))
        
    pygame.draw.rect(surface, (80, 80, 80), (bar_x, bar_y, bar_width, bar_height), 1)

    if player.is_healing:
        now = pygame.time.get_ticks()
        progress = min((now - player.heal_timer) / player.heal_duration, 1.0)
        
        float_bar_w = 24
        float_bar_h = 4
        px = (player.hitbox.centerx - camera.x) - (float_bar_w // 2)
        py = (player.hitbox.top - camera.y) - 12
        
        pygame.draw.rect(surface, (0, 0, 0), (px - 1, py - 1, float_bar_w + 2, float_bar_h + 2))
        pygame.draw.rect(surface, (255, 255, 255), (px, py, float_bar_w * progress, float_bar_h))

def draw_boss_bar(surface, boss):
    if boss is None or boss.dead:
        return

    bar_w   = 220
    bar_h   = 10
    bx      = LOGICAL_WIDTH  // 2 - bar_w // 2
    by      = LOGICAL_HEIGHT - 28

    # ── Background track ──────────────────────────────────────────────────
    pygame.draw.rect(surface, (20, 20, 20), (bx - 2, by - 2, bar_w + 4, bar_h + 4))

    # ── Filled portion ────────────────────────────────────────────────────
    fill = max(0, int(bar_w * (boss.hp / boss.max_hp)))
    if fill > 0:
        # Colour shows phase and invulnerability state at a glance
        if boss.invulnerable:
            bar_colour = (120, 0, 180)   # purple — untouchable
        elif boss.phase == 2:
            bar_colour = (180, 60, 200)  # lighter purple — phase 2
        else:
            bar_colour = (180, 20, 20)   # dark red — phase 1
        pygame.draw.rect(surface, bar_colour, (bx, by, fill, bar_h))

    # ── Border ────────────────────────────────────────────────────────────
    pygame.draw.rect(surface, (100, 100, 100), (bx - 2, by - 2, bar_w + 4, bar_h + 4), 1)

    # ── Boss name ─────────────────────────────────────────────────────────
    font = pygame.font.SysFont("Calibri", 11, bold=True)
    name_surf = font.render("Shadow Dragon", True, (230, 200, 255))
    surface.blit(name_surf, (LOGICAL_WIDTH // 2 - name_surf.get_width() // 2, by - 14))

def spawn_enemies(enemies, player, now):
    global last_enemy_spawn, enemy_spawn_interval

    # Never spawn regular enemies in the boss room
    if lvl_name == "tile7.tile":
        return

    if now - last_enemy_spawn < enemy_spawn_interval:
        return
    
    allowed = ROOM_ENEMIES.get(lvl_name, [])
    if not allowed:
        return

    can_go_right = player.hitbox.centerx + LOGICAL_WIDTH < world_w
    can_go_left  = player.hitbox.centerx - LOGICAL_WIDTH > 0

    if not can_go_right and not can_go_left:
        return  

    side = random.choice(["left", "right"]) if (can_go_right and can_go_left) else ("right" if can_go_right else "left")

    last_enemy_spawn = now

    spawn_x = (
        player.hitbox.centerx - LOGICAL_WIDTH
        if side == "right"
        else player.hitbox.centerx + LOGICAL_WIDTH
    )

    spawn_y = player.y

    chosen_sprite = random.choice(allowed)
    enemy = Enemy(sprite_name=chosen_sprite)
    enemy.x = float(spawn_x)
    enemy.y = float(spawn_y)
    enemy.rect.topleft = (int(enemy.x), int(enemy.y))
    enemy.hitbox.midbottom = enemy.rect.midbottom
    enemies.append(enemy)

    enemy_spawn_interval = random.randint(1500, 3500)

def play_sound(sound):
    global playing, footstep_channel, bg_music_channel, dash_channel, charging_channel
    if sound == "hurt1":
        SOUNDS.get("hurt-1").play()
    if sound == "hurt2":
        SOUNDS.get("hurt-2").play()
    if sound == "dash" and not playing:
        if dash_channel is None or not dash_channel.get_busy():
            dash_channel = SOUNDS.get("dash").play()
            playing = True
    if sound == "step" and not playing:
        if footstep_channel is None or not footstep_channel.get_busy():
            footstep_channel = SOUNDS.get("footsteps").play()
    if sound == "jump":
        SOUNDS.get("jump").play()
    if sound == "background":
        bg_music_channel = SOUNDS.get("background").play(-1).set_volume(0.5)
    if sound == "attack":
        SOUNDS.get("attack").play()
    if sound == "charging" and not playing:
        if charging_channel is None or not charging_channel.get_busy():
            footstep_channel = SOUNDS.get("charging").play()
    
    playing = False

def load_entrances(config_file):
    entrances = {}
    with open(config_file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            src_file, col, row, dest_file, dest_col, dest_row = (
                parts[0], int(parts[1]), int(parts[2]),
                parts[3], int(parts[4]), int(parts[5])
            )
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE * 2, TILE_SIZE * 2)
            if src_file not in entrances:
                entrances[src_file] = []
            entrances[src_file].append((rect, dest_file, dest_col, dest_row))
    return entrances

def load_level(tile_file, spawn_col, spawn_row, player):
    global grid, world_w, world_h, collision_rects, enemies, lvl_name, boss, fireballs

    lvl_name = tile_file
    grid = []
    with open(tile_file) as f:
        for line in f:
            row = [int(ch) for ch in line.strip()]
            grid.append(row)

    world_w = len(grid[0]) * TILE_SIZE
    world_h = len(grid) * TILE_SIZE
    collision_rects = build_collision_rects(grid)
    enemies = []
    fireballs = []          # clear any leftover projectiles from the previous room

    player.x = float(spawn_col * TILE_SIZE)
    player.y = float(spawn_row * TILE_SIZE)
    player.vel_y = 0
    player.on_ground = False
    player.attacking = False
    player.attack_type = None
    player.melee_rect = None
    player.hitbox.topleft = (int(player.x), int(player.y))
    player.rect.midbottom = player.hitbox.midbottom

    bg = BACKGROUNDS.get(lvl_name)
    if bg:
        BACKGROUNDS[lvl_name] = pygame.transform.scale(bg, (world_w, world_h))

    # ── Boss room ─────────────────────────────────────────────────────────
    if tile_file == "tile7.tile":
        boss = Boss()
        # Place the boss horizontally centred and a few tiles down from the top
        boss.x = float(world_w // 2)
        boss.y = float(player.y)
        boss.rect.topleft = (int(boss.x), int(boss.y))
        boss.hitbox.midbottom = boss.rect.midbottom
    else:
        boss = None

def start_transition(dest_file, dest_col, dest_row):
    global transition_active, transition_start, transition_target, transition_phase
    transition_active = True
    transition_start = pygame.time.get_ticks()
    transition_target = (dest_file, dest_col, dest_row)
    transition_phase = "out"

def update_transition(player):
    global transition_active, transition_start, transition_phase

    half = FADE_DURATION // 2
    elapsed = pygame.time.get_ticks() - transition_start

    if transition_phase == "out":
        alpha = min(255, int((elapsed / half) * 255))
        if elapsed >= half:
            dest_file, dest_col, dest_row = transition_target
            load_level(dest_file, dest_col, dest_row, player)
            transition_phase = "in"
            transition_start = pygame.time.get_ticks()
        return alpha
    else:
        alpha = max(0, 255 - int((elapsed / half) * 255))
        if elapsed >= half:
            transition_active = False
        return alpha

def draw_entrance_prompts(surface, player, lvl_name, entrances, camera):
    font        = pygame.font.SysFont("Calibri", 10)
    font_locked = pygame.font.SysFont("Calibri", 9)
    radius_px   = ENTRANCE_PROMPT_RADIUS * TILE_SIZE

    current_entrances = entrances.get(lvl_name, [])
    for (ent_rect, dest_file, dest_col, dest_row) in current_entrances:
        dx   = player.hitbox.centerx - ent_rect.centerx
        dy   = player.hitbox.centery - ent_rect.centery
        dist = (dx * dx + dy * dy) ** 0.5

        if dist <= radius_px:
            locked = dest_file == "tile7.tile" and player.score < BOSS_SCORE_REQUIREMENT

            label    = "NEED 300\nSCORE TO\nENTER" if locked else "PRESS E\nTO MOVE"
            colour   = (255, 80, 80) if locked else (255, 255, 255)
            f        = font_locked if locked else font

            lines = label.split('\n')
            
            rendered_lines = [f.render(line, True, colour) for line in lines]
            
            max_width = max([line_surf.get_width() for line_surf in rendered_lines])
            line_height = f.get_linesize()  # Gets the standard height of a line for this font
            total_height = line_height * len(rendered_lines)

            draw_tx  = ent_rect.centerx - camera.x - max_width // 2
            draw_ty  = ent_rect.top - camera.y - total_height - 4

            bg_rect  = pygame.Rect(draw_tx - 3, draw_ty - 2, max_width + 6, total_height + 4)
            bg_surf  = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
            bg_surf.fill((0, 0, 0, 140))
            surface.blit(bg_surf, bg_rect)

            current_y = draw_ty
            for line_surf in rendered_lines:
                line_x = ent_rect.centerx - camera.x - line_surf.get_width() // 2
                surface.blit(line_surf, (line_x, current_y))
                current_y += line_height # Move down for the next line

def pause():
    global in_game, paused
    in_game = False
    paused = not paused
    in_game = not in_game

def reset_game(player, camera):
    global boss, fireballs
    player.current_lives = player.max_lives
    player.score = 0
    player.soul = 0
    player.invulnerable = False
    boss = None
    fireballs = []
    
    spawn_col = spawn_x // TILE_SIZE
    load_level("tile1.tile", spawn_col, spawn_row, player)
    
    camera.x = 0
    camera.y = 0

def tile_map(surface, grid, cam_x, cam_y):
    y = -cam_y  
    for row in grid:
        x = -cam_x
        for value in row:
            tile = None
            if value == 2: tile = TILES["grass"]
            elif value == 3: tile = TILES["cave"]
            elif value == 4: tile = TILES["wasteland"]
            elif value == 5: tile = TILES["magma"]
            elif value == 6: tile = TILES["ice"]
            elif value == 7: tile = TILES["ruin"]
            elif value == 8: tile = TILES["final"]
            if tile:
                w, h = tile.get_size()
                tile = pygame.transform.scale(tile, (w * 0.5, h * 0.5))
                surface.blit(tile, (x, y))
            x += TILE_SIZE
        y += TILE_SIZE

entrances = load_entrances("entries.txt")

grid = []
with open(lvl_name) as f:
    for line in f:
        row = [int(ch) for ch in line.strip()]
        grid.append(row) 

world_w = len(grid[0]) * TILE_SIZE
world_h = len(grid) * TILE_SIZE

bg = BACKGROUNDS.get(lvl_name)
if bg:
    BACKGROUNDS[lvl_name] = pygame.transform.scale(bg, (world_w, world_h))

collision_rects = build_collision_rects(grid)

spawn_row = 8
spawn_x   = 24
spawn_y   = (spawn_row * TILE_SIZE) - TILE_SIZE

player = Player()
player.x = spawn_x
player.y = spawn_y

camera = Camera()

enemies    = []
fireballs  = []

playing    = False
paused     = False
in_game    = True
running    = True

game_state = "menu"   # "menu" | "playing" | "paused" | "game_over" | "win"

play_sound("background")


while running:
    clock.tick(60)
    now    = pygame.time.get_ticks()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
        if game_state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game(player, camera)
                    game_state = "playing"
                elif event.key == pygame.K_q:
                    running = False
                
        elif game_state == "playing":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = "paused"
                
        elif game_state == "paused":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = "playing"
                elif event.key == pygame.K_q:
                    running = False
                    
        elif game_state == "game_over":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = "menu"

        elif game_state == "win":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = "menu"

    logical.fill((0, 0, 0))

    if game_state == "playing":
        update(player, collision_rects, events, camera, enemies, entrances)
        spawn_enemies(enemies, player, now)

        if player.current_lives <= 0:
            game_state = "game_over"

        # Win condition: boss is dead
        if boss is not None and boss.dead:
            game_state = "menu"

        draw_background(logical, camera)
        tile_map(logical, grid, camera.x, camera.y)

        # ── Fireballs (drawn behind entities) ─────────────────────────────
        for fb in fireballs:
            fb_rect = fb.rect.move(-int(camera.x), -int(camera.y))
            logical.blit(fb.image, fb_rect)

        # ── Player ────────────────────────────────────────────────────────
        screen_rect = player.rect.move(-int(camera.x), -int(camera.y))
        if not player.invulnerable or (now // 100) % 2 == 0:
            logical.blit(player.get_draw_image(), screen_rect)
            logical.blit(player.arm_image, screen_rect)

        # ── Regular enemies ───────────────────────────────────────────────
        for enemy in enemies:
            enemy_draw_rect = enemy.rect.move(-int(camera.x), -int(camera.y))
            logical.blit(enemy.get_draw_image(), enemy_draw_rect)

        # ── Boss ──────────────────────────────────────────────────────────
        if boss is not None and not boss.dead:
            boss_draw_rect = boss.rect.move(-int(camera.x), -int(camera.y))
            logical.blit(boss.get_draw_image(), boss_draw_rect)
        
        if boss is not None and boss.dead:
            game_state = "win"


        # ── HUD ───────────────────────────────────────────────────────────
        draw_ui(logical, player, camera)
        draw_entrance_prompts(logical, player, lvl_name, entrances, camera)

        # Boss bar — only visible in the boss room
        if lvl_name == "tile7.tile":
            draw_boss_bar(logical, boss)

        font = pygame.font.SysFont("Calibri", 15)
        text = font.render(f"Score: {int(player.score)}", True, (0, 0, 0))
        logical.blit(text, (250, 0))

        if transition_active:
            alpha = update_transition(player)
            fade_surface.set_alpha(alpha)
            logical.blit(fade_surface, (0, 0))

    elif game_state == "menu":
        draw_background(logical, camera)
        overlay = pygame.Surface((LOGICAL_WIDTH, LOGICAL_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        logical.blit(overlay, (0, 0))

        font_title  = pygame.font.SysFont("Calibri", 30, bold=True)
        font_prompt = pygame.font.SysFont("Calibri", 15)
        
        title_text  = font_title.render("FORGOTTEN BUG KNIGHT",    True, (255, 255, 255))
        prompt_text = font_prompt.render("Press ENTER to Start",   True, (200, 200, 200))
        quit_text   = font_prompt.render("Press Q to Quit",        True, (200, 200, 200))
        
        cx, cy = LOGICAL_WIDTH // 2, LOGICAL_HEIGHT // 2
        logical.blit(title_text,  title_text.get_rect(center=(cx, cy - 20)))
        logical.blit(prompt_text, prompt_text.get_rect(center=(cx, cy + 20)))
        logical.blit(quit_text,   prompt_text.get_rect(center=(cx, cy + 60)))

    elif game_state == "game_over":
        logical.fill((50, 0, 0))

        font_title  = pygame.font.SysFont("Calibri", 30, bold=True)
        font_prompt = pygame.font.SysFont("Calibri", 15)
        
        title_text  = font_title.render("GAME OVER",                          True, (255, 100, 100))
        score_text  = font_prompt.render(f"Final Score: {int(player.score)}", True, (255, 255, 255))
        prompt_text = font_prompt.render("Press ENTER to Return to Menu",     True, (200, 200, 200))
        
        cx, cy = LOGICAL_WIDTH // 2, LOGICAL_HEIGHT // 2
        logical.blit(title_text,  title_text.get_rect(center=(cx, cy - 30)))
        logical.blit(score_text,  score_text.get_rect(center=(cx, cy)))
        logical.blit(prompt_text, prompt_text.get_rect(center=(cx, cy + 30)))

    elif game_state == "paused":
        draw_background(logical, camera)
        overlay = pygame.Surface((LOGICAL_WIDTH, LOGICAL_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        logical.blit(overlay, (0, 0))

        font_big   = pygame.font.SysFont("Calibri", 20)
        font_small = pygame.font.SysFont("Calibri", 13)

        pause_text  = font_big.render("PAUSED",  True, (255, 255, 255))
        resume_text = font_small.render("R  -  Resume", True, (200, 200, 200))
        quit_text   = font_small.render("Q  -  Quit",   True, (200, 200, 200))

        cx, cy = LOGICAL_WIDTH // 2, LOGICAL_HEIGHT // 2
        logical.blit(pause_text,  pause_text.get_rect(center=(cx, cy - 20)))
        logical.blit(resume_text, resume_text.get_rect(center=(cx, cy + 10)))
        logical.blit(quit_text,   quit_text.get_rect(center=(cx, cy + 30)))
    
    elif game_state == "win":
        draw_background(logical, camera)
        overlay = pygame.Surface((LOGICAL_WIDTH, LOGICAL_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        logical.blit(overlay, (0, 0))

        font_big   = pygame.font.SysFont("Calibri", 20)
        font_small = pygame.font.SysFont("Calibri", 13)

        win_text = font_big.render("YOU WIN!", True, (255, 255, 255))
        play_again = font_small.render("Press enter to play again", True, (200, 200, 200))
        score_text = font_small.render(f"Final score: {int(player.score)}", True, (200, 200, 200))

        cx, cy = LOGICAL_WIDTH // 2, LOGICAL_HEIGHT // 2
        logical.blit(win_text, win_text.get_rect(center=(cx, cy - 20)))
        logical.blit(score_text, score_text.get_rect(center=(cx, cy + 10)))
        logical.blit(play_again, play_again.get_rect(center=(cx, cy + 40)))

    screen.fill((0, 0, 0))
    dest   = get_letterbox_rect(logical.get_size(), screen.get_size())
    scaled = pygame.transform.scale(logical, (dest.width, dest.height))
    screen.blit(scaled, dest)
    pygame.display.flip()

pygame.quit()
sys.exit()