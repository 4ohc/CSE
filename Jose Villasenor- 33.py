class Items(object):
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name

    def use(self):
        print("you use %s" % self.name)


class Weapon(Items):
    def __init__(self, name, amount, damage, durability, material):
        super(Weapon, self).__init__(amount, name)
        self.name = name
        self.amount = amount
        self.damage = damage
        self.durability = durability
        self.material = material

    def pick_up(self):
        print("you pick up a %s" % self.name)
        print("there is %s of them" % self.amount)


class SteelSword(Weapon):
    def __init__(self, damage, durability, material):
        super(SteelSword, self).__init__("Steel sword", 1, damage, durability, material)
        self.damage = damage
        self.durability = durability
        self.material = material

    def inspect(self):
        print("you inspect your sword it does %s damage" % self.damage)
        print("it has %s hits left until it breaks" % self.durability)
        print("it is made of %s" % self.material)

    def slice(self):
        print("you slash your opponent hitting them for %s they are staggered allowing you to hit again" % self.damage)
        self.durability -= 20
        print("you have %s hits left on this weapon" % self.durability)


s_sword = SteelSword(16, 400, "steel")


class WoodenAxe(Weapon):
    def __init__(self, durability, material):
        super(WoodenAxe, self).__init__("wooden axe", 100, 7, durability, material)

    def axe_rush(self):
        print("you rush your opponent and you use your axe to slash them you smack them for %s, the axe gets stuck in "
              "them...but you at least killed it" % self.damage)
        self.durability -= 30
        print("your weapon is %s hits away from breaking" % self.durability)


w_axe = WoodenAxe(100, "wood")


class SteelAxe(WoodenAxe):
    def __init__(self, durability, material, damage):
        super(SteelAxe, self).__init__(durability, material)
        self.damage = damage

    def inspect(self):
        print("you look at your axe, it has %s hits left" % self.durability)
        print("it is made of %s" % self.material)
        print("it does %s" % self.damage)


s_axe = SteelAxe(400, "steel", 16)


class PlatinumAxe(SteelAxe):
    def __init__(self, durability, damage, material):
        super(PlatinumAxe, self).__init__(durability, damage, material)
        self.damage = damage
        self.material = material
        self.durability = durability

    def inspect(self):
        print("you look at the shiny axe it seems to have %s hits left" % self.durability)
        print("%s, it is the finest material very rare" % self.material)
        print("this amazing weapon deals %s damage" % self.damage)

    def axe_throw(self):
        print("you toss the axe and it hits, the axe takes some massive damage to its durability "
              "but its still usable")
        self.durability -= 300
        self.damage -= 14


p_axe = PlatinumAxe(700, 34, "platinum")


class WoodenSword(SteelSword):
    def __init__(self, damage, material, durability):
        super(WoodenSword, self).__init__(damage, material, durability)
        self.durability = durability
        self.material = material
        self.damage = damage

    def inspect(self):
        print("you inspect your sword it seems sturdy enough to be used %s time(s)" % self.durability)
        print("%s, defiantly not good but it gets the job done" % self.material)
        print("surprisingly it does %s damage" % self.damage)

    def sword_rush(self):
        self.durability -= 25
        self.damage -= 4
        print("you rush your opponent swinging your flimsy sword")
        print("your sword takes some durability damage, it has %s hits left" % self.durability)


w_sword = WoodenSword(7, "wood", 100)


class Platinum_Sword(WoodenSword):
    def __init__(self):
        super(Platinum_Sword, self).__init__(34, "Platinum", 700)

    def ultra_cut(self):
        self.durability -= 600
        self.damage -= 16
        print("you cleave your opponent cutting causing massive damage, the sword becomes flimsy...it has %s hits left"
              % self.durability)

    def inspect(self):
        print("you inspect your sword it seems to be good enough to be used %s time(s)" % self.durability)
        print("%s, best material to get the job done" % self.material)
        print("of course it does %s damage" % self.damage)


p_sword = Platinum_Sword()


class Consumables(Items):
    def __init__(self, amount, name):
        super(Consumables, self).__init__(amount, name)
        self.name = name
        self.amount = amount


class Food(Consumables):
    def __init__(self, amount, name, heal):
        super(Food, self).__init__(amount, name)
        self.heal = heal

    def eat(self):
        print("you eat %s...it seems safe enough" % self.name)
        print("it heals you for %s!" % self.heal)


class Apple(Food):
    def __init__(self):
        super(Apple, self).__init__(2, "green apple", 30)


class Steak(Food):
    def __init__(self):
        super(Steak, self).__init__(1, "Steak", 60)


class poisoned_apple(Food):
    def __init__(self):
        super(poisoned_apple, self).__init__(1, "Red Apple", 44)

    def eat(self):
        print("you eat the %s..you feel sick" % self.name)
        print("the apple was poisoned! you take %s damage from poison..then it goes away" % self.heal)


class rotten_steak(Food):
    def __init__(self):
        super(rotten_steak, self).__init__(1, "Odd looking steak", 50)

    def eat(self):
        print("you eat %s..why? it makes you feel odd" % self.name)
        print("you made a mistake it had gone bad! you vomit and take %s damage" % self.heal)


odd_looking_steak = rotten_steak


class potato(Food):
    def __init__(self):
        super(potato, self).__init__(1, "potato", 200000000000000000000000000000000000000000000000000000000000000000000)


potato = potato


class Monster(object):
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health


class Finalboss(Monster):
    def __init__(self):
        super(Finalboss, self).__init__("wither", 1000000000000, 1000000000000000000000000000000000000000000000000000000
                                        )

    def final_hit(self):
        print("the monster swings ")


class item(object):
    def __init__(self, item):
        self.item = item


class Room(object):
    def __init__(self, name, description, north, east, south, west, up, down, item):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.south = south
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

    def take(self, items):
        global current_item
        current_item = globals()[getattr(self, items)]


STARTROOM = Room("cave entrance", "the dark cave gives off a mysterious aura", None, None, None, "PORTALROOM", None,
                 None, 'nothing')
PORTALROOM = Room("portal room", "a purple portal, you can hear screams coming from it "
                                 "a odd looking rug is in the center of the room", "SECONDCAVE", "STARTROOM", "FREEZER",
                  "EMPTYROOM", None, "DARKROOM", 'nothing')
DARKROOM = Room("dark room", "the room is too dark to see in, you might get eaten by a grue", None, None, None, None,
                "PORTALROOM", None, 'nothing')
EMPTYROOM = Room('"empty room"', "the room seems empty, nothing to see here", None, "PORTALROOM", "SECRETROOM", None,
                 None, None, 'nothing')
FREEZER = Room('freezer', "a chilling room, its full of meat", "PORTALROOM", None, "KITCHEN", None, None, None,
               'odd looking steak')
KITCHEN = Room("kitchen", "an average kitchen...nothing to see here", "FREEZER", "LIVINGROOM", None, None, None, None,
               'potato')
LIVINGROOM = Room("livingroom", "The room has a single chest, you could store things there...like that sword", None,
                  None, "HALL", "KITCHEN", None, None, 'WoodenAxe')
HALL = Room("a large hall", "this hall may be a point of no return, an apple is near the other door", "LIVINGROOM",
            "CURSEDROOM", None, None, None, None, 'red apple')
CURSEDROOM = Room("a room", "a shadowy figure stands at the center of the room", 'STARTROOM', 'SPIKETRAP' 'HALL', None,
                  None, None, None, 'Steak')
SPIKETRAP = Room('trap', 'spikes surround you..you can still turn back...but its no use the shadowy figure blocks your '
                         'exit..all you can to is accept your fate', 'STARTROOM', 'STARTROOM', 'STARTROOM', 'STARTROOM',
                 None, None, 'Apple')
SECONDCAVE = Room('unknown area', "This area seems a bit warm..the path is made with s type of red stone..it "
                                  "seams fragile", 'LAVAPOOL', None, 'PORTALROOM', 'THENETHER', None, None, 'WoodenAxe')
THENETHER = Room('nether', "This place seems to be uninhabitable by man, ..lava is everywhere", None, "SECONDCAVE",
                 'FORTRESS', None, None, None, 'SteelAxe')
FORTRESS = Room("Mysterious Fort", "the fort is made of some odd material, it seems to be open but you'll need to "
                                   "climb it", None, None, None, "THENETHER", 'FORTOPENING', None, None)
FORTOPENING = Room("fort main gate", "this fort has a dark black gate it seemed to be made using the lava.."
                                     "the bars are too wide to keep anyone out", 'FORTROOMONE',
                   None, None, None, None, "Fortress", 'SteelSword')
FORTROOMONE = Room("garden", "a patch of mysterious red mushroom like things grown on haunting sand, "
                             "the sand has faces on it..they all look like they are in pain", "SECONDPORTAL",
                   "SPAWNER", 'FORTOPENING', None, "ROOF", None, 'nothing')
SECONDPORTAL = Room("a portal", "this portal looks similar to the first portal you went into, it may take you home.."
                                " but don't trust it", "STARTROOMV2", None, "FORTROOMONE", None, None, None, 'nothing')
STARTROOMV2 = Room("cave", "hey you made it back..wait the portal closed..there's no exit..you are trapped.."
                           "guess you gotta try again", None, None, None, None, None, None, 'nothing')
SPAWNER = Room("a simple block", "a block sits on top of some stairs..you better just go it seems to make odd noises",
               None, None, None, "FORTROOMONE", None, None, 'Platinum_Sword')
ROOF = Room("roof", "a simple black roof, you could continue to go further into the fort from here",
            "BOSSROOM", None, None, None, "EGG", "FORTROOMONE", 'nothing')
EGG = Room("egg", "the god tier egg only few can harness its power into a nice omelet", None, None, None, None, None,
           "ROOF", 'PlatinumAxe')
BOSSROOM = Room("final", "a giant creature stands at the center, the door behind you shuts closed"
                         "...hope you got everything you need", None, None, None, None, None, None, 'nothing')

SECRETROOM = Room("first easter egg", "good work here's a potato", 'EMPTYROOM', None, None, None, None, None, 'potato')

current_node = STARTROOM
current_item = STARTROOM.item
directions = ['north', 'south', 'east', 'west', 'down', 'up', ]
short_directions = ['n', 's', 'e', 'w', 'd', 'u']
inventory = []
Take = ["take"]
while True:
    print(current_node.name)
    print(current_node.description)
    print("you look around the room and see %s" % current_node.item)
    command = input('>_').lower().strip()

    if command == 'quit':
        quit(0)

    elif command in short_directions:
        # look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]

    if command in Take:
        try:
            current_item.take(command)

        except KeyError and AttributeError:
            print("Nothing to take here")
        else:
            print("command not recognized")

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("you cannot go this way.")
    else:
        print("command not recognized")

