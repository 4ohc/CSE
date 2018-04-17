class Room(object):
    def __init__(self, name, description, north, east, south, west, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.south = south

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


STARTROOM = Room("cave entrance", "the dark cave gives off a mysterious aura", None, None, None, "PORTALROOM", None,
                 None)
PORTALROOM = Room("portal room", "a purple portal, you can hear screams coming from it "
                                 "a odd looking rug is in the center of the room", "SECONDCAVE", "STARTROOM", "FREEZER",
                  "EMPTYROOM", None, "DARKROOM")
DARKROOM = Room("dark room", "the room is too dark to see in, you might get eaten by a grue", None, None, None, None,
                "PORTALROOM", None)
EMPTYROOM = Room('"empty room"', "the room seems empty, nothing to see here", None, "PORTALROOM", "SECRETROOM", None,
                 None, None)
FREEZER = Room('freezer', "a chilling room, its full of meat", "PORTALROOM", None, "KITCHEN", None, None, None)
KITCHEN = Room("kitchen", "an average kitchen...nothing to see here", "FREEZER", "LIVINGROOM", None, None, None, None)
LIVINGROOM = Room("livingroom", "The room has a single chest, you could store things there...like that sword", None,
                  None, "HALL", "KITCHEN", None, None)
HALL = Room("a large hall", "this hall may be a point of no return", "LIVINGROOM", "CURSEDROOM", None, None, None, None)
CURSEDROOM = Room("a room", "a shadowy figure stands at the center of the room", 'STARTROOM', 'SPIKETRAP' 'HALL', None,
                  None, None, None)
SPIKETRAP = Room('trap', 'spikes surround you..you can still turn back...but its no use the shadowy figure blocks your '
                         'exit..all you can to is accept your fate', 'STARTROOM', 'STARTROOM', 'STARTROOM', 'STARTROOM'
                 , None, None)
SECONDCAVE = Room('unknown area', "This area seems a bit warm..the path is made with s type of red stone..it "
                                  "seams fragile", 'LAVAPOOL', None, 'PORTALROOM', 'THENETHER', None, None)
THENETHER = Room('nether', "This place seems to be uninhabitable by man, ..lava is everywhere", None, "SECONDCAVE",
                 'FORTRESS', None, None, None)
FORTRESS = Room("Mysterious Fort", "the fort is made of some odd material, it seems to be open but you'll need to "
                                   "climb it", None, None, None, "THENETHER", 'FORTOPENING', None)
FORTOPENING = Room("fort main gate", "this fort has a dark black gate it seemed to be made using the lava.."
                                     "the bars are too wide to keep anyone out", 'FORTROOMONE',
                   None, None, None, None, "Fortress")
FORTROOMONE = Room("garden", "a patch of mystyrious red mushroom like things grown on haunting sand, "
                             "the sand has faces on it..they all look like they are in pain", "SECONDPORTAL"
                   , "SPAWNER", 'FORTOPENING', None, "ROOF", None)
SECONDPORTAL = Room("a portal", "this portal looks similar to the first portal you went into, it may take you home.."
                                " but don't trust it", "STARTROOMV2", None, "FORTROOMONE", None, None, None)
STARTROOMV2 = Room("cave", "hey you made it back..wait the portal closed..there's no exit..you are trapped.."
                           "guess you gotta try again", None, None, None, None, None, None)
SPAWNER = Room("a simple block", "a block sits ontop of some stairs..you better just go it seems to make odd noises"
               , None, None, None, "FORTROOMONE", None, None)
ROOF = Room("roof", "a simple black roof, you could continue to go further into the fort from here",
            "ROOFHOLE", None, None, None, "EGG", "FORTROOMONE")
EGG = Room("egg", "the god tier egg only few can harness its power into a nice omelet", None, None, None, None, None,
           "ROOF")
BOSSROOM = Room("final", "a giant creature stands at the center, the door behind you shuts closed"
                         "...hope you got everything you need", None, None, None, None, None, None)
SECRETROOM = Room("first easter egg", "good work heres a reward...enjoy your potato", )
current_node = STARTROOM
directions = ['north', 'south', 'east', 'west', 'down', 'up', ]
short_directions = ['n', 's', 'e', 'w', 'd', 'u']
while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("you cannot go this way.")
    else:
        print("direction not recognized")
        print()
