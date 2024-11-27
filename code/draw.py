import pygame

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
            if i < 10:
                color = (255, 0, 0)
            elif i < 12:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
            start = (x[i-1], y[i-1])
            end = (x[i], y[i])
            pygame.draw.line(screen, color, start, end, width=5)

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
    rotor_order = [enigma.rotor1.name, enigma.rotor2.name, enigma.rotor3.name]
    plugboard = enigma.plugboard.list
    if not hasattr(draw, "original_key"):
        draw.original_key = key
    original_key = draw.original_key
    settings = ["Chave Original:"+original_key, "Chave Atual:"+key, "Rotores:"+str(rotor_order), "Refletor:"+enigma.reflector.name]
    for i in range(4):
        setting = font.render(settings[i], True, (255, 255, 255))
        text_box = setting.get_rect(center = (200+(i*width/4), 20))
        screen.blit(setting, text_box)
    settings_cont = pygame.font.SysFont("Courier", 20, bold=True).render(str(plugboard), True, (255, 255, 255))
    text_box = settings_cont.get_rect(center = (width/2, 40))
    screen.blit(settings_cont, text_box)