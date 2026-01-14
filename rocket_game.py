import pygame
import requests
import io
import math
import random
import time
from PIL import Image

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen settings
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Epic Space Adventure - Python Rocket 🚀")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
ORANGE = (255, 165, 0)
MARS_RED = (193, 68, 14)
PURPLE = (148, 0, 211)
YELLOW = (255, 255, 0)
GREEN = (50, 205, 50)
BLUE = (30, 144, 255)

# Fonts
title_font = pygame.font.Font(None, 72)
large_font = pygame.font.Font(None, 48)
medium_font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

def load_image_from_url(url, size=None):
    """Load an image from URL and optionally resize it."""
    try:
        response = requests.get(url, timeout=10)
        image = Image.open(io.BytesIO(response.content))
        image = image.convert("RGBA")
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        mode = image.mode
        data = image.tobytes()
        return pygame.image.fromstring(data, image.size, mode)
    except Exception as e:
        print(f"Could not load image from {url}: {e}")
        return None

def create_gradient_surface(width, height, color1, color2, vertical=True):
    """Create a gradient surface."""
    surface = pygame.Surface((width, height))
    for i in range(height if vertical else width):
        ratio = i / (height if vertical else width)
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        if vertical:
            pygame.draw.line(surface, (r, g, b), (0, i), (width, i))
        else:
            pygame.draw.line(surface, (r, g, b), (i, 0), (i, height))
    return surface

def draw_stars(surface, num_stars=100, offset=0):
    """Draw twinkling stars."""
    random.seed(42)  # Consistent star positions
    for i in range(num_stars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        brightness = 150 + int(50 * math.sin((offset + i) * 0.1))
        size = random.choice([1, 1, 1, 2, 2, 3])
        pygame.draw.circle(surface, (brightness, brightness, brightness), (x, y), size)

def draw_rocket(surface, x, y, scale=1.0, with_flame=True):
    """Draw a detailed rocket."""
    # Rocket body
    body_width = int(60 * scale)
    body_height = int(150 * scale)
    
    # Main body (silver/white gradient effect)
    body_rect = pygame.Rect(x - body_width//2, y - body_height//2, body_width, body_height)
    pygame.draw.rect(surface, (200, 200, 210), body_rect, border_radius=10)
    pygame.draw.rect(surface, (150, 150, 160), body_rect, 3, border_radius=10)
    
    # Nose cone (red)
    nose_points = [
        (x, y - body_height//2 - int(50 * scale)),
        (x - body_width//2, y - body_height//2),
        (x + body_width//2, y - body_height//2)
    ]
    pygame.draw.polygon(surface, (200, 30, 30), nose_points)
    pygame.draw.polygon(surface, (150, 20, 20), nose_points, 3)
    
    # Window
    window_y = y - body_height//4
    pygame.draw.circle(surface, (100, 150, 255), (x, window_y), int(15 * scale))
    pygame.draw.circle(surface, (50, 100, 200), (x, window_y), int(15 * scale), 2)
    
    # Fins
    fin_width = int(30 * scale)
    fin_height = int(40 * scale)
    # Left fin
    left_fin = [
        (x - body_width//2, y + body_height//2 - fin_height),
        (x - body_width//2 - fin_width, y + body_height//2),
        (x - body_width//2, y + body_height//2)
    ]
    pygame.draw.polygon(surface, (200, 30, 30), left_fin)
    # Right fin
    right_fin = [
        (x + body_width//2, y + body_height//2 - fin_height),
        (x + body_width//2 + fin_width, y + body_height//2),
        (x + body_width//2, y + body_height//2)
    ]
    pygame.draw.polygon(surface, (200, 30, 30), right_fin)
    
    # Flame
    if with_flame:
        flame_offset = random.randint(-5, 5)
        flame_height = int(80 * scale) + random.randint(-10, 20)
        flame_points = [
            (x - int(25 * scale), y + body_height//2),
            (x + int(25 * scale), y + body_height//2),
            (x + flame_offset, y + body_height//2 + flame_height)
        ]
        # Outer flame (orange)
        pygame.draw.polygon(surface, ORANGE, flame_points)
        # Inner flame (yellow)
        inner_points = [
            (x - int(15 * scale), y + body_height//2),
            (x + int(15 * scale), y + body_height//2),
            (x + flame_offset//2, y + body_height//2 + flame_height * 0.7)
        ]
        pygame.draw.polygon(surface, YELLOW, inner_points)

def draw_earth(surface, x, y, radius):
    """Draw Earth."""
    pygame.draw.circle(surface, (30, 100, 200), (x, y), radius)
    # Continents (simplified)
    pygame.draw.ellipse(surface, (50, 150, 50), (x - radius//2, y - radius//3, radius, radius//2))
    pygame.draw.circle(surface, (50, 150, 50), (x + radius//3, y + radius//3), radius//4)
    # Atmosphere glow
    pygame.draw.circle(surface, (100, 150, 255), (x, y), radius + 5, 3)

def draw_mars(surface, y_offset=0):
    """Draw Mars surface."""
    # Mars sky gradient
    sky = create_gradient_surface(WIDTH, HEIGHT//2, (80, 30, 10), (150, 60, 20))
    surface.blit(sky, (0, 0))
    
    # Mars ground
    pygame.draw.rect(surface, MARS_RED, (0, HEIGHT//2 + y_offset, WIDTH, HEIGHT//2))
    
    # Craters
    for i in range(8):
        cx = 100 + i * 150
        cy = HEIGHT//2 + 100 + y_offset + (i % 3) * 50
        crater_size = 30 + (i % 4) * 20
        pygame.draw.ellipse(surface, (160, 50, 10), (cx, cy, crater_size, crater_size//2))
        pygame.draw.ellipse(surface, (130, 40, 8), (cx + 5, cy + 5, crater_size - 10, crater_size//2 - 5))
    
    # Mountains
    mountain_points = [(0, HEIGHT//2 + y_offset)]
    for i in range(12):
        peak = HEIGHT//2 + y_offset - random.randint(30, 100)
        mountain_points.append((i * 100 + 50, peak))
        mountain_points.append((i * 100 + 100, HEIGHT//2 + y_offset))
    mountain_points.append((WIDTH, HEIGHT//2 + y_offset))
    pygame.draw.polygon(surface, (170, 55, 12), mountain_points)

def draw_alien(surface, x, y, scale=1.0, alive=True):
    """Draw an alien."""
    if not alive:
        return
    
    # Body (green)
    body_color = (100, 200, 100)
    head_size = int(40 * scale)
    
    # Head
    pygame.draw.ellipse(surface, body_color, (x - head_size, y - head_size, head_size * 2, int(head_size * 1.5)))
    
    # Big eyes
    eye_size = int(15 * scale)
    pygame.draw.ellipse(surface, BLACK, (x - head_size//2 - eye_size//2, y - head_size//3, eye_size, int(eye_size * 1.3)))
    pygame.draw.ellipse(surface, BLACK, (x + head_size//2 - eye_size//2, y - head_size//3, eye_size, int(eye_size * 1.3)))
    # Eye shine
    pygame.draw.circle(surface, WHITE, (x - head_size//2, y - head_size//4), int(4 * scale))
    pygame.draw.circle(surface, WHITE, (x + head_size//2, y - head_size//4), int(4 * scale))
    
    # Body
    pygame.draw.ellipse(surface, body_color, (x - int(25 * scale), y + int(20 * scale), int(50 * scale), int(60 * scale)))
    
    # Arms
    pygame.draw.line(surface, body_color, (x - int(25 * scale), y + int(40 * scale)), 
                     (x - int(50 * scale), y + int(30 * scale)), int(8 * scale))
    pygame.draw.line(surface, body_color, (x + int(25 * scale), y + int(40 * scale)), 
                     (x + int(50 * scale), y + int(30 * scale)), int(8 * scale))
    
    # Antenna
    pygame.draw.line(surface, body_color, (x, y - head_size), (x, y - head_size - int(20 * scale)), 3)
    pygame.draw.circle(surface, (255, 100, 100), (x, y - head_size - int(20 * scale)), int(6 * scale))

def draw_astronaut(surface, x, y, scale=1.0, facing_right=True):
    """Draw an astronaut."""
    # Helmet
    helmet_size = int(35 * scale)
    pygame.draw.circle(surface, WHITE, (x, y - int(20 * scale)), helmet_size)
    pygame.draw.circle(surface, (50, 50, 50), (x, y - int(20 * scale)), helmet_size, 3)
    
    # Visor
    visor_offset = int(5 * scale) if facing_right else int(-5 * scale)
    pygame.draw.ellipse(surface, (100, 150, 200), 
                        (x - int(15 * scale) + visor_offset, y - int(30 * scale), int(25 * scale), int(20 * scale)))
    
    # Body (spacesuit)
    pygame.draw.ellipse(surface, WHITE, (x - int(25 * scale), y + int(15 * scale), int(50 * scale), int(60 * scale)))
    pygame.draw.ellipse(surface, (200, 200, 200), (x - int(25 * scale), y + int(15 * scale), int(50 * scale), int(60 * scale)), 3)
    
    # Backpack
    pack_x = x + int(25 * scale) if facing_right else x - int(40 * scale)
    pygame.draw.rect(surface, (150, 150, 150), (pack_x, y + int(10 * scale), int(15 * scale), int(40 * scale)))
    
    # Arms
    arm_end_x = x + int(60 * scale) if facing_right else x - int(60 * scale)
    pygame.draw.line(surface, WHITE, (x, y + int(30 * scale)), (arm_end_x, y + int(20 * scale)), int(12 * scale))
    
    # Legs
    pygame.draw.line(surface, WHITE, (x - int(10 * scale), y + int(70 * scale)), 
                     (x - int(15 * scale), y + int(100 * scale)), int(12 * scale))
    pygame.draw.line(surface, WHITE, (x + int(10 * scale), y + int(70 * scale)), 
                     (x + int(15 * scale), y + int(100 * scale)), int(12 * scale))

def draw_laser(surface, start_x, end_x, y):
    """Draw a laser beam."""
    pygame.draw.line(surface, RED, (start_x, y), (end_x, y), 6)
    pygame.draw.line(surface, YELLOW, (start_x, y), (end_x, y), 2)
    # Glow effect
    for i in range(3):
        alpha = 100 - i * 30
        s = pygame.Surface((end_x - start_x, 20), pygame.SRCALPHA)
        pygame.draw.line(s, (*RED, alpha), (0, 10), (end_x - start_x, 10), 10 + i * 4)
        surface.blit(s, (start_x, y - 10))

def draw_wormhole(surface, x, y, radius, rotation):
    """Draw a swirling wormhole."""
    for i in range(8):
        r = radius - i * 15
        if r > 0:
            color_shift = (i * 20) % 255
            color = ((128 + color_shift) % 255, 0, (200 + color_shift) % 255)
            angle = rotation + i * 0.5
            points = []
            for j in range(36):
                a = j * 10 * math.pi / 180 + angle
                wobble = math.sin(a * 3 + rotation) * 10
                px = x + (r + wobble) * math.cos(a)
                py = y + (r + wobble) * 0.4 * math.sin(a)  # Elliptical
                points.append((px, py))
            if len(points) > 2:
                pygame.draw.polygon(surface, color, points, 3)
    
    # Center glow
    pygame.draw.circle(surface, (200, 100, 255), (x, y), 30)
    pygame.draw.circle(surface, WHITE, (x, y), 15)

def draw_school(surface):
    """Draw Vianney High School."""
    # Sky
    sky = create_gradient_surface(WIDTH, HEIGHT, (135, 206, 235), (70, 130, 180))
    surface.blit(sky, (0, 0))
    
    # Sun
    pygame.draw.circle(surface, YELLOW, (100, 100), 50)
    
    # Clouds
    for cx, cy in [(200, 80), (400, 120), (700, 90), (900, 130)]:
        pygame.draw.ellipse(surface, WHITE, (cx, cy, 100, 40))
        pygame.draw.ellipse(surface, WHITE, (cx + 30, cy - 20, 80, 50))
        pygame.draw.ellipse(surface, WHITE, (cx + 60, cy, 90, 40))
    
    # Ground
    pygame.draw.rect(surface, (50, 150, 50), (0, HEIGHT - 150, WIDTH, 150))
    
    # School building
    building_x = WIDTH//2 - 250
    building_y = HEIGHT - 400
    building_width = 500
    building_height = 250
    
    # Main building
    pygame.draw.rect(surface, (180, 120, 80), (building_x, building_y, building_width, building_height))
    pygame.draw.rect(surface, (140, 90, 60), (building_x, building_y, building_width, building_height), 4)
    
    # Roof
    roof_points = [
        (building_x - 20, building_y),
        (building_x + building_width//2, building_y - 80),
        (building_x + building_width + 20, building_y)
    ]
    pygame.draw.polygon(surface, (100, 60, 40), roof_points)
    
    # Windows
    for row in range(2):
        for col in range(5):
            wx = building_x + 40 + col * 90
            wy = building_y + 40 + row * 80
            pygame.draw.rect(surface, (150, 200, 255), (wx, wy, 50, 60))
            pygame.draw.rect(surface, (80, 60, 40), (wx, wy, 50, 60), 3)
            pygame.draw.line(surface, (80, 60, 40), (wx + 25, wy), (wx + 25, wy + 60), 2)
            pygame.draw.line(surface, (80, 60, 40), (wx, wy + 30), (wx + 50, wy + 30), 2)
    
    # Door
    door_x = building_x + building_width//2 - 40
    door_y = building_y + building_height - 100
    pygame.draw.rect(surface, (60, 40, 20), (door_x, door_y, 80, 100))
    pygame.draw.rect(surface, (40, 25, 10), (door_x, door_y, 80, 100), 3)
    pygame.draw.circle(surface, YELLOW, (door_x + 65, door_y + 50), 5)
    
    # Sign
    sign_rect = pygame.Rect(building_x + 100, building_y - 60, 300, 50)
    pygame.draw.rect(surface, (50, 50, 100), sign_rect)
    pygame.draw.rect(surface, YELLOW, sign_rect, 3)
    sign_text = large_font.render("VIANNEY HIGH SCHOOL", True, WHITE)
    surface.blit(sign_text, (building_x + 110, building_y - 55))
    
    # Flag pole
    pygame.draw.line(surface, (100, 100, 100), (building_x - 60, building_y - 80), (building_x - 60, HEIGHT - 150), 5)
    # Flag
    flag_points = [(building_x - 60, building_y - 80), (building_x - 60, building_y - 40), (building_x - 20, building_y - 60)]
    pygame.draw.polygon(surface, (200, 50, 50), flag_points)
    
    # Trees
    for tx in [50, 150, WIDTH - 150, WIDTH - 50]:
        pygame.draw.rect(surface, (100, 70, 40), (tx - 10, HEIGHT - 200, 20, 60))
        pygame.draw.circle(surface, (30, 100, 30), (tx, HEIGHT - 220), 40)
        pygame.draw.circle(surface, (40, 120, 40), (tx - 20, HEIGHT - 200), 30)
        pygame.draw.circle(surface, (40, 120, 40), (tx + 20, HEIGHT - 200), 30)

def draw_explosion(surface, x, y, frame):
    """Draw an explosion."""
    colors = [YELLOW, ORANGE, RED, (200, 100, 50)]
    for i in range(4):
        radius = (frame + 1) * 15 - i * 10
        if radius > 0:
            pygame.draw.circle(surface, colors[i], (x, y), radius)
    
    # Particles
    for i in range(12):
        angle = i * 30 * math.pi / 180
        dist = frame * 20
        px = x + dist * math.cos(angle)
        py = y + dist * math.sin(angle)
        pygame.draw.circle(surface, ORANGE, (int(px), int(py)), 5)

def show_text(surface, text, y, font=large_font, color=WHITE, center=True):
    """Display text on screen."""
    rendered = font.render(text, True, color)
    if center:
        x = WIDTH//2 - rendered.get_width()//2
    else:
        x = 50
    surface.blit(rendered, (x, y))

def wait_or_skip(duration):
    """Wait for duration but allow skipping with any key."""
    start = time.time()
    while time.time() - start < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                return True
        clock.tick(60)
    return True

def stage_launch():
    """Stage 1: Launch from Earth."""
    rocket_y = HEIGHT - 200
    
    for frame in range(180):  # 3 seconds at 60fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        screen.fill(BLACK)
        draw_stars(screen, 150, frame)
        
        # Earth at bottom
        draw_earth(screen, WIDTH//2, HEIGHT + 300, 400)
        
        # Rocket rising
        if frame > 30:
            rocket_y -= (frame - 30) * 0.15
        
        draw_rocket(screen, WIDTH//2, rocket_y, 1.0, frame > 30)
        
        # Text
        if frame < 60:
            show_text(screen, "LAUNCHING FROM EARTH", 50, title_font, GREEN)
        elif frame > 120:
            show_text(screen, "LEAVING ATMOSPHERE...", 50, large_font, YELLOW)
        
        pygame.display.flip()
        clock.tick(60)
    
    return True

def stage_space_travel():
    """Stage 2: Travel through space to Mars."""
    for frame in range(240):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        screen.fill(BLACK)
        draw_stars(screen, 200, frame * 2)
        
        # Rocket moving across screen
        rocket_x = 100 + frame * 4
        rocket_y = HEIGHT//2 + math.sin(frame * 0.05) * 30
        
        # Draw rocket (rotated to face right - simplified)
        pygame.draw.polygon(screen, (200, 200, 210), [
            (rocket_x + 60, rocket_y),
            (rocket_x - 40, rocket_y - 25),
            (rocket_x - 40, rocket_y + 25)
        ])
        pygame.draw.polygon(screen, (200, 30, 30), [
            (rocket_x + 60, rocket_y),
            (rocket_x + 80, rocket_y),
            (rocket_x + 60, rocket_y - 15),
            (rocket_x + 60, rocket_y + 15)
        ])
        # Flame trail
        for i in range(5):
            fx = rocket_x - 50 - i * 20
            pygame.draw.circle(screen, ORANGE if i % 2 == 0 else YELLOW, 
                             (fx + random.randint(-5, 5), rocket_y + random.randint(-5, 5)), 10 - i)
        
        # Mars appearing
        mars_size = min(frame // 2, 80)
        if mars_size > 0:
            pygame.draw.circle(screen, MARS_RED, (WIDTH - 100, HEIGHT//2), mars_size)
        
        # Distance counter
        distance = max(0, 225 - frame)
        show_text(screen, f"DISTANCE TO MARS: {distance} MILLION KM", 50, medium_font)
        show_text(screen, "INTERPLANETARY TRAVEL", HEIGHT - 80, large_font, BLUE)
        
        pygame.display.flip()
        clock.tick(60)
    
    return True

def stage_mars_landing():
    """Stage 3: Landing on Mars."""
    rocket_y = -100
    
    for frame in range(180):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        screen.fill(BLACK)
        draw_mars(screen)
        
        # Rocket descending
        rocket_y = -100 + frame * 4
        if rocket_y > HEIGHT//2 - 100:
            rocket_y = HEIGHT//2 - 100
        
        draw_rocket(screen, WIDTH//2, rocket_y, 0.8, frame < 150)
        
        show_text(screen, "MARS APPROACH", 50, title_font, RED)
        
        if frame > 150:
            show_text(screen, "TOUCHDOWN!", HEIGHT - 100, title_font, GREEN)
        
        pygame.display.flip()
        clock.tick(60)
    
    return wait_or_skip(1.5)

def stage_alien_encounter():
    """Stage 4: Meet the alien."""
    for frame in range(180):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        screen.fill(BLACK)
        draw_mars(screen)
        
        # Landed rocket
        draw_rocket(screen, 200, HEIGHT//2 - 80, 0.6, False)
        
        # Astronaut walking out
        astro_x = min(350, 200 + frame * 2)
        draw_astronaut(screen, astro_x, HEIGHT//2 + 50, 1.0, True)
        
        # Alien appearing
        if frame > 60:
            alien_x = WIDTH - 200
            draw_alien(screen, alien_x, HEIGHT//2 + 30, 1.2)
            
            if frame > 90:
                show_text(screen, '"GREETINGS EARTHLING..."', HEIGHT - 150, medium_font, GREEN)
            if frame > 130:
                show_text(screen, '"PREPARE TO BE PROBED!"', HEIGHT - 100, medium_font, GREEN)
        
        show_text(screen, "FIRST CONTACT", 50, title_font, YELLOW)
        
        pygame.display.flip()
        clock.tick(60)
    
    return wait_or_skip(1.0)

def stage_alien_fight():
    """Stage 5: Shoot the alien!"""
    laser_x = 400
    explosion_frame = 0
    alien_alive = True
    
    for frame in range(180):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        screen.fill(BLACK)
        draw_mars(screen)
        
        # Landed rocket
        draw_rocket(screen, 200, HEIGHT//2 - 80, 0.6, False)
        
        # Astronaut
        draw_astronaut(screen, 350, HEIGHT//2 + 50, 1.0, True)
        
        alien_x = WIDTH - 200
        
        # Laser firing
        if frame > 30 and frame < 90:
            laser_end = min(400 + (frame - 30) * 20, alien_x)
            draw_laser(screen, 400, laser_end, HEIGHT//2 + 30)
            
            if laser_end >= alien_x - 50:
                alien_alive = False
                explosion_frame = frame - 60
        
        # Alien or explosion
        if alien_alive:
            draw_alien(screen, alien_x, HEIGHT//2 + 30, 1.2)
        elif explosion_frame < 20:
            draw_explosion(screen, alien_x, HEIGHT//2 + 30, explosion_frame)
            explosion_frame += 1
        
        # Text
        if frame < 30:
            show_text(screen, "NOT TODAY, ALIEN!", 50, title_font, RED)
        elif frame > 30 and frame < 90:
            show_text(screen, "PEW PEW PEW!", 50, title_font, YELLOW)
            show_text(screen, '"SAY HELLO TO MY LITTLE FRIEND!"', HEIGHT - 80, medium_font)
        else:
            show_text(screen, "ALIEN ELIMINATED", 50, title_font, GREEN)
            show_text(screen, '"GET REKT LMAOOO"', HEIGHT - 80, medium_font, YELLOW)
        
        pygame.display.flip()
        clock.tick(60)
    
    return wait_or_skip(1.0)

def stage_wormhole():
    """Stage 6: Enter the wormhole."""
    wormhole_size = 0
    astro_x = 350
    
    for frame in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        # Purple space background
        screen.fill((20, 0, 40))
        draw_stars(screen, 100, frame)
        
        # Wormhole growing
        wormhole_size = min(frame * 2, 200)
        draw_wormhole(screen, WIDTH//2, HEIGHT//2, wormhole_size, frame * 0.1)
        
        # Astronaut moving toward wormhole
        if frame > 60:
            astro_x = min(350 + (frame - 60) * 3, WIDTH//2 - 50)
            if frame < 200:
                draw_astronaut(screen, astro_x, HEIGHT//2 + 50, 1.0 - (frame - 60) * 0.003)
        else:
            draw_astronaut(screen, astro_x, HEIGHT//2 + 50, 1.0)
        
        # Trippy effects when entering
        if frame > 150:
            for i in range(10):
                color = ((frame * 10 + i * 25) % 255, 0, (frame * 5 + i * 50) % 255)
                pygame.draw.circle(screen, color, 
                                 (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 
                                 random.randint(5, 20))
        
        # Text
        if frame < 60:
            show_text(screen, "ANOMALY DETECTED", 50, title_font, PURPLE)
        elif frame < 150:
            show_text(screen, "WORMHOLE OPENING!", 50, title_font, PURPLE)
            show_text(screen, '"YOOO WHAT IS THAT?!"', HEIGHT - 80, medium_font)
        else:
            show_text(screen, "ENTERING WORMHOLE", 50, title_font, WHITE)
            show_text(screen, "AAAAAAHHHHH!!!", HEIGHT - 80, large_font, YELLOW)
        
        pygame.display.flip()
        clock.tick(60)
    
    return True

def stage_vianney():
    """Stage 7: Land at Vianney High School."""
    astro_y = -100
    
    for frame in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        draw_school(screen)
        
        # Astronaut falling from sky
        if frame < 120:
            astro_y = -100 + frame * 5
        else:
            astro_y = min(500, astro_y + 2)
        
        if astro_y < 500:
            draw_astronaut(screen, WIDTH//2, astro_y, 1.0)
            # Parachute when falling
            if frame < 100:
                pygame.draw.polygon(screen, (255, 100, 100), [
                    (WIDTH//2, astro_y - 80),
                    (WIDTH//2 - 60, astro_y - 150),
                    (WIDTH//2 + 60, astro_y - 150)
                ])
                pygame.draw.line(screen, BLACK, (WIDTH//2, astro_y - 40), (WIDTH//2 - 60, astro_y - 150), 2)
                pygame.draw.line(screen, BLACK, (WIDTH//2, astro_y - 40), (WIDTH//2 + 60, astro_y - 150), 2)
        else:
            draw_astronaut(screen, WIDTH//2, HEIGHT - 220, 1.0)
        
        # Text
        if frame < 60:
            show_text(screen, "EXITING WORMHOLE", 50, title_font, PURPLE)
        elif frame < 150:
            show_text(screen, "WHERE AM I?!", 50, title_font, YELLOW)
        else:
            if (frame // 30) % 2 == 0:
                show_text(screen, "RING RING! Time for class!", HEIGHT - 50, large_font, YELLOW)
        
        if frame > 180:
            dialog = [
                '"Yo... is this... VIANNEY?!"',
                '"I just shot an alien on Mars..."',
                '"Went through a WORMHOLE..."',
                '"And ended up at HIGH SCHOOL?!"'
            ]
            dialog_idx = min((frame - 180) // 30, len(dialog) - 1)
            show_text(screen, dialog[dialog_idx], 100, medium_font, WHITE)
        
        pygame.display.flip()
        clock.tick(60)
    
    return wait_or_skip(2.0)

def stage_victory():
    """Final victory screen."""
    for frame in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                return True
        
        # Animated background
        screen.fill((0, 20, 0))
        draw_stars(screen, 50, frame)
        
        # Victory box
        box_rect = pygame.Rect(WIDTH//2 - 300, HEIGHT//2 - 200, 600, 400)
        pygame.draw.rect(screen, (0, 50, 0), box_rect)
        pygame.draw.rect(screen, GREEN, box_rect, 4)
        
        # Title
        show_text(screen, "MISSION COMPLETE", HEIGHT//2 - 170, title_font, GREEN)
        
        # Checklist
        items = [
            "Launched from Earth",
            "Landed on Mars", 
            "Eliminated hostile alien",
            "Traversed wormhole",
            "Arrived at Vianney High School"
        ]
        
        for i, item in enumerate(items):
            y = HEIGHT//2 - 80 + i * 45
            if frame > i * 20:
                pygame.draw.circle(screen, GREEN, (WIDTH//2 - 250, y + 10), 12)
                show_text(screen, item, y, medium_font, WHITE)
        
        # Final message
        if frame > 150:
            pulse = abs(math.sin(frame * 0.1)) * 0.3 + 0.7
            color = (int(255 * pulse), int(255 * pulse), 0)
            show_text(screen, "YOU ARE A LEGEND", HEIGHT//2 + 160, title_font, color)
        
        pygame.display.flip()
        clock.tick(60)
    
    return True

def main():
    """Run the epic space adventure!"""
    print("Starting Epic Space Adventure...")
    print("Press any key to skip animations, or just enjoy the show!")
    
    # Run all stages
    stages = [
        ("Launching...", stage_launch),
        ("Space Travel...", stage_space_travel),
        ("Mars Landing...", stage_mars_landing),
        ("First Contact...", stage_alien_encounter),
        ("Combat...", stage_alien_fight),
        ("Wormhole...", stage_wormhole),
        ("Arrival...", stage_vianney),
        ("Victory!", stage_victory)
    ]
    
    for name, stage_func in stages:
        print(f"Stage: {name}")
        if not stage_func():
            break
    
    pygame.quit()
    print("\nThanks for playing Python Rocket!")

if __name__ == "__main__":
    main()
