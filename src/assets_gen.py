import pygame

def create_sprite(data, size=(16, 16), color=(15, 56, 15)):
    surface = pygame.Surface(size, pygame.SRCALPHA)
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == '#':
                surface.set_at((x, y), color)
    return surface

def get_egg_sprites():
    frame1 = [
        "      ####      ",
        "    ##    ##    ",
        "   #        #   ",
        "  #          #  ",
        "  #   ##     #  ",
        " #   #  #     # ",
        " #   #  #     # ",
        " #    ##      # ",
        " #            # ",
        " #            # ",
        "  #          #  ",
        "  #          #  ",
        "   #        #   ",
        "    ##    ##    ",
        "      ####      ",
        "                "
    ]
    return [create_sprite(frame1)]

def get_thorn_sprites():
    # A spiky variant of sprout
    frame1 = [
        "      #         ",
        "     ###        ",
        "    # # #       ",
        "      #         ",
        "    #####       ",
        "   # # # #      ",
        "  #  # #  #     ",
        "  #  # #  #     ",
        "  #       #     ",
        "  #  #### #     ",
        "   #     #      ",
        "    #####       ",
        "     # #        ",
        "    ## ##       ",
        "                ",
        "                "
    ]
    return [create_sprite(frame1)]

def get_wither_sprites():
    # A drooping variant of arbor
    frame1 = [
        "                ",
        "     ######     ",
        "   ##      ##   ",
        "  #  X    X  #  ",
        " #    ####    # ",
        " #            # ",
        "  #   ####   #  ",
        "   ##      ##   ",
        "     #    #     ",
        "    #      #    ",
        "   #        #   ",
        "  #          #  ",
        "  #          #  ",
        "   #  #  #  #   ",
        "                ",
        "                "
    ]
    return [create_sprite(frame1)]

def get_baby_sprites():
    # A small blob with eyes
    frame1 = [
        "                ",
        "                ",
        "      ####      ",
        "    ##    ##    ",
        "   #        #   ",
        "  #  #    #  #  ",
        "  #  #    #  #  ",
        "  #          #  ",
        "  #   ####   #  ",
        "   #        #   ",
        "    ########    ",
        "                ",
        "                ",
        "                ",
        "                ",
        "                "
    ]
    frame2 = [
        "                ",
        "                ",
        "                ",
        "      ####      ",
        "    ##    ##    ",
        "   #  #  #  #   ",
        "   #  #  #  #   ",
        "   #        #   ",
        "   #  ####  #   ",
        "    ########    ",
        "                ",
        "                ",
        "                ",
        "                ",
        "                ",
        "                "
    ]
    return [create_sprite(frame1), create_sprite(frame2)]

def get_child_sprites():
    # A small sprout creature
    frame1 = [
        "      ##        ",
        "     #  #       ",
        "      ##        ",
        "      #         ",
        "    ######      ",
        "   #      #     ",
        "  #  #  #  #    ",
        "  #  #  #  #    ",
        "  #        #    ",
        "  #  ####  #    ",
        "   #      #     ",
        "    ######      ",
        "     #  #       ",
        "    ##  ##      ",
        "                ",
        "                "
    ]
    return [create_sprite(frame1)]

def get_adult_sprites():
    # A larger tree-like creature
    frame1 = [
        "     ######     ",
        "   ##      ##   ",
        "  #  #    #  #  ",
        " #    ####    # ",
        " #   #    #   # ",
        " #   #    #   # ",
        "  #   ####   #  ",
        "   ##      ##   ",
        "     #    #     ",
        "    #      #    ",
        "   #        #   ",
        "  #          #  ",
        "  ############  ",
        "   #  #  #  #   ",
        "   #  #  #  #   ",
        "                "
    ]
    return [create_sprite(frame1)]

def get_food_sprite():
    data = [
        "     ####       ",
        "    #    #      ",
        "    #    #      ",
        "     ####       ",
        "      ##        ",
        "    ######      ",
        "   ########     ",
        "   ########     "
    ]
    return create_sprite(data, size=(8, 8))

def get_poop_sprite():
    data = [
        "      ##      ",
        "     #  #     ",
        "    #    #    ",
        "   #      #   ",
        "  #        #  ",
        "   ########   "
    ]
    return create_sprite(data, size=(16, 16))
