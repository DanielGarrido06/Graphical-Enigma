import pygame
import math

def draw(enigma, path, screen, width, height, margins, gap, font):

    # Width and height of the components
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # Background
    screen.fill((31, 31, 31))

    # Path coordinates
    y = [margins["top"] + (signal + 1) * h / 27 for signal in path]
    x = [width - margins["right"] - w/2]
    for i in [4, 3, 2, 1, 0]:
        x.append(margins["left"]+i*(w+gap)+w*3/4)
        x.append(margins["left"]+i*(w+gap)+w*1/4)
    x.append(margins["left"] + w*3/4)

    for i in [1, 2, 3, 4]:
        x.append(margins["left"]+i*(w+gap)+w*1/4)
        x.append(margins["left"]+i*(w+gap)+w*3/4)
    x.append(width - margins["right"] - w/2)

    # Draw Path
    if len(path) > 0:
        for i in range(1,21):
            r = 0
            g = int((i / 20) * 255)
            b = 255 - g
            color = (r, g, b)
            start = (x[i-1], y[i-1])
            end = (x[i], y[i])
            pygame.draw.line(screen, color, start, end, width=5)
            # Draw arrow endcaps
            arrow_size = 20
            angle = math.atan2(end[1] - start[1], end[0] - start[0])
            arrow_points = [
                (end[0] - arrow_size * math.cos(angle - math.pi / 6), end[1] - arrow_size * math.sin(angle - math.pi / 6)),
                (end[0] - arrow_size * math.cos(angle + math.pi / 6), end[1] - arrow_size * math.sin(angle + math.pi / 6)),
                end
            ]
            pygame.draw.polygon(screen, color, arrow_points)

    # Base coordinates
    x = margins["left"]
    y = margins["top"]


    # Draw the components
    for component in [enigma.reflector, enigma.rotor1, enigma.rotor2, enigma.rotor3, enigma.plugboard, enigma.keyboard]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    # Write the titles
    titles = ["Refletor", "Rotor Esquerda", "Rotor Meio", "Rotor Direita", "Plugboard", "Teclado"]
    for i in range(6):
        title = font.render(titles[i], True, (255, 255, 255))
        text_box = title.get_rect(center = (margins["left"] + i*(w+gap) + w/2, margins["top"]-20))
        screen.blit(title, text_box)

    # Write the settings
    key = enigma.rotor1.left[0] + enigma.rotor2.left[0] + enigma.rotor3.left[0]
    rotor_order = enigma.rotor1.name + ", " + enigma.rotor2.name + ", " + enigma.rotor3.name
    rings = enigma.rotor1.ring, enigma.rotor2.ring, enigma.rotor3.ring
    plugboard = enigma.plugboard.list
    if not hasattr(draw, "original_key"):
        draw.original_key = key
    original_key = draw.original_key
    settings = ["Chave Original:"+original_key, "Anéis:"+str(rings), "Rotores: "+str(rotor_order), "Refletor:"+enigma.reflector.name]
    for i in range(4):
        setting = font.render(settings[i], True, (255, 255, 255))
        text_box = setting.get_rect(center = (200+(i*width/4), 20))
        screen.blit(setting, text_box)
    settings_cont = pygame.font.SysFont("Courier", 25, bold=True).render(str(plugboard).replace("'","").replace(",",""), True, (255, 255, 255))
    text_box = settings_cont.get_rect(center = (width/2, 40))
    screen.blit(settings_cont, text_box)