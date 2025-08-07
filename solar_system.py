# Solar System with Parallax, Mini-Map, 2D/3D Toggle, Trails, GUI Button, Sound
import pygame
import pygame_gui
import math
import os
import random

pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System GUI Edition")

font = pygame.font.SysFont("Comic Sans MS", 14, bold=True)
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Sound
sound_on = True
try:
    pygame.mixer.music.load(os.path.join("sounds", "space_ambient.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
except:
    print("No sound file found in 'sounds/space_ambient.mp3'")
    sound_on = False

# GUI Buttons
pause_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((20, HEIGHT - 62), (80, 25)),
    text='Pause', manager=manager)
toggle_3d_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((110, HEIGHT - 62), (100, 25)),
    text='Toggle 3D', manager=manager)
mute_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((220, HEIGHT - 62), (100, 25)),
    text='Mute' if sound_on else 'Unmute', manager=manager)

# Star background
def generate_stars(count, layer_speed):
    return [{
        "x": random.randint(0, WIDTH * 2),
        "y": random.randint(0, HEIGHT * 2),
        "speed": layer_speed,
        "size": random.randint(1, 3)
    } for _ in range(count)]

far_stars = generate_stars(80, 0.2)
mid_stars = generate_stars(50, 0.5)
near_stars = generate_stars(30, 0.8)

# Planet images
planet_images = {
    "Sun": pygame.transform.scale(pygame.image.load(os.path.join("planets", "sun.png")), (90, 90)),
    "Mercury": pygame.transform.scale(pygame.image.load(os.path.join("planets", "mercury.png")), (15, 15)),
    "Venus": pygame.transform.scale(pygame.image.load(os.path.join("planets", "venus.png")), (25, 25)),
    "Earth": pygame.transform.scale(pygame.image.load(os.path.join("planets", "earth.png")), (30, 30)),
    "Mars": pygame.transform.scale(pygame.image.load(os.path.join("planets", "mars.png")), (20, 20)),
    "Jupiter": pygame.transform.scale(pygame.image.load(os.path.join("planets", "jupiter.png")), (50, 50)),
    "Saturn": pygame.transform.scale(pygame.image.load(os.path.join("planets", "saturn_ring.png")), (100, 40)),
    "Uranus": pygame.transform.scale(pygame.image.load(os.path.join("planets", "uranus.png")), (35, 35)),
    "Neptune": pygame.transform.scale(pygame.image.load(os.path.join("planets", "neptune.png")), (40, 40)),
}

# Planet data
planet_data = [
    {"name": "Sun", "real_dist": 0, "sim_dist": 0, "period": 0},
    {"name": "Mercury", "real_dist": 58, "sim_dist": 70, "period": 0.24},
    {"name": "Venus", "real_dist": 108, "sim_dist": 110, "period": 0.62},
    {"name": "Earth", "real_dist": 150, "sim_dist": 160, "period": 1.0},
    {"name": "Mars", "real_dist": 228, "sim_dist": 200, "period": 1.88},
    {"name": "Jupiter", "real_dist": 778, "sim_dist": 250, "period": 11.86},
    {"name": "Saturn", "real_dist": 1429, "sim_dist": 320, "period": 29.5},
    {"name": "Uranus", "real_dist": 2871, "sim_dist": 390, "period": 84},
    {"name": "Neptune", "real_dist": 4495, "sim_dist": 450, "period": 164.8},
]

for planet in planet_data:
    planet["image"] = planet_images[planet["name"]]
    planet["angle"] = 0
    planet["orbits"] = 0
    planet["trail"] = []

# Controls
zoom = 1.0
speed_multiplier = 1.0
offset_x, offset_y = WIDTH // 2, HEIGHT // 2
dragging = False
mouse_prev = (0, 0)
paused = False
show_3d = False
clock = pygame.time.Clock()

def draw_stars(stars, color):
    for s in stars:
        sx = s["x"] * zoom + offset_x * s["speed"]
        sy = s["y"] * zoom + offset_y * s["speed"]
        pygame.draw.circle(screen, color, (int(sx % WIDTH), int(sy % HEIGHT)), s["size"])

def draw_minimap():
    mini_size = 200
    map_surf = pygame.Surface((mini_size, mini_size))
    map_surf.fill((10, 10, 20))
    center = mini_size // 2
    pygame.draw.circle(map_surf, (255, 255, 0), (center, center), 3)
    for p in planet_data[1:]:
        px = int(center + math.cos(p["angle"]) * (p["sim_dist"] / 3))
        py = int(center + math.sin(p["angle"]) * (p["sim_dist"] / 3))
        pygame.draw.circle(map_surf, (255, 255, 255), (px, py), 2)
    screen.blit(map_surf, (WIDTH - mini_size - 10, 10))

# Main loop
running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    screen.fill((0, 0, 0))
    draw_stars(far_stars, (50, 50, 80))
    draw_stars(mid_stars, (100, 100, 150))
    draw_stars(near_stars, (180, 180, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                dragging = True
                mouse_prev = pygame.mouse.get_pos()
            elif event.button == 4:
                zoom *= 1.1
            elif event.button == 5:
                zoom /= 1.1
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            mx, my = pygame.mouse.get_pos()
            dx, dy = mx - mouse_prev[0], my - mouse_prev[1]
            offset_x += dx
            offset_y += dy
            mouse_prev = (mx, my)

        manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == pause_button:
                paused = not paused
                pause_button.set_text("Play" if paused else "Pause")
            elif event.ui_element == toggle_3d_button:
                show_3d = not show_3d
            elif event.ui_element == mute_button:
                sound_on = not sound_on
                if sound_on:
                    pygame.mixer.music.set_volume(0.3)
                    mute_button.set_text("Mute")
                else:
                    pygame.mixer.music.set_volume(0.0)
                    mute_button.set_text("Unmute")

    # Draw planets
    for planet in planet_data:
        if not paused:
            prev_angle = planet["angle"]
            planet["angle"] += 0.05 * (1 / planet["period"]) * speed_multiplier if planet["period"] != 0 else 0
            if prev_angle % (2 * math.pi) > planet["angle"] % (2 * math.pi):
                planet["orbits"] += 1

        x = math.cos(planet["angle"]) * planet["sim_dist"]
        y = math.sin(planet["angle"]) * planet["sim_dist"] * (0.5 if show_3d else 1)
        scale = max(0.3, 1 - (y / 800)) if show_3d else 1
        img = pygame.transform.rotozoom(planet["image"], 0, scale * zoom)
        px = x * zoom + offset_x
        py = y * zoom + offset_y
        planet["trail"].append((int(px), int(py)))
        if len(planet["trail"]) > 100:
            planet["trail"].pop(0)
        for i in range(1, len(planet["trail"])):
            pygame.draw.line(screen, (100, 100, 0), planet["trail"][i-1], planet["trail"][i], 1)
        screen.blit(img, img.get_rect(center=(int(px), int(py))))

    draw_minimap()
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()
