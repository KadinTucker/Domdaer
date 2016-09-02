import objects
from pygame import Surface

class area():
    """
    An area is a plot of area on screen, with entities, sceneries, NPCs, and others.
    It also has 4 warps areas that go to different areas of the world.
    The warps are [Left, Up, Right, Down]
    """
    def __init__(self, items):
        self.enemies = items[0]
        self.sceneries = items[1]
        self.bgcolor = items[4]
        self.quests = items[2]
        self.warps = items[3]
        self.scene = None

    def buildSurface(self, resolution):
        self.scene = Surface(resolution)
        self.scene.fill(self.bgcolor)
        for i in self.sceneries:
            self.scene.blit(i.image, i.coords)
        

world = {}

world['janonia1'] = ([objects.enemy(objects.soldier[0], objects.soldier[1], (200, 730))], [], [], [None, None, None, 'janonia3'], (50, 150, 50))

world['janonia2'] = ([objects.enemy(objects.soldier[0], objects.soldier[1], (225, 780)), objects.enemy(objects.soldier[0], objects.soldier[1],
(689, 625))], [], [], [None, None, 'janonia3', 'janonia6'], (50, 150, 50))

world['janonia3'] = ([objects.enemy(objects.soldier[0], objects.soldier[1], (781, 846)), objects.enemy(objects.soldier[0], objects.soldier[1],
(1482, 452))], [], [], ['janonia2', 'janonia1', 'janonia4', 'janonia7'], (50, 150, 50))

world['janonia4'] = ([objects.enemy(objects.soldier[0], objects.soldier[1], (1121, 802)), objects.enemy(objects.soldier[0], objects.soldier[1],
(482, 298))], [], [], ['janonia3', 'janon1', 'janonia5', 'janonia8'], (50, 150, 50))

world['janonia5'] = ([objects.enemy(objects.soldier[0], objects.soldier[1], (1121, 802)), objects.enemy(objects.soldier[0], objects.soldier[1],
(482, 298))], [objects.scenery(objects.tree[0], objects.tree[1],
True, (980, 678))], [], ['janonia4', None, None, 'janonia9'], (50, 150, 50))

world['janon1'] = ([objects.enemy(objects.soldier[0], objects.soldier[1], (727, 730)), objects.enemy(objects.soldier[0], objects.soldier[1],
(827, 730))], [objects.scenery(objects.citywall[0], objects.citywall[1], True, (0, 678)), objects.scenery(objects.citywall[0], objects.citywall[1],
True, (980, 678))], [], [None, None, 'janon2', 'janonia4'], (150, 150, 150))

world['janon2'] = ([], [objects.scenery(objects.citywall[0], objects.citywall[1], True, (0, 678)), objects.scenery(objects.citywall[0], objects.citywall[1],
True, (720, 678)), objects.scenery(objects.citywall[0], objects.citywall[1], True, (1440, 678))], [], ['janon1', None, None, None], (150, 150, 150))
