class Room(object):
    def __int__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

STARTROOM = Room ("cave entrance", "the dark cave gives off a mysterious aura", None, None, "PORTALROOM", None, None )