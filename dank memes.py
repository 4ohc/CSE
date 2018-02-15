world_map = {
    'STARTROOM': {
        'NAME': "cave entrance",
        'DESCRIPTION': "the dark cave gives off a mysterious aura",
        'PATHS': {
            'WEST': 'PORTALROOM'
        }
    },
    'PORTALROOM': {
        'NAME': "portal room",
        'DESCRIPTION': "a purple portal, you can hear screams coming from it, a odd looking rug is in the center of the"
                       "room",
        'PATHS': {'DOWN': "DARKROOM",
                  'SOUTH': "FREEZER",
                  'WEST': "EMPTYROOM",
                  'EAST': "STARTROOM"
                  }
    },
    'DARKROOM': {
        'NAME': "dark room",
        'DESCRIPTION': "the room is pich black, you might get eaten by a grue",
        'PATHS': {
            'UP' "PORTALROOM"
        }
    },
    'EMPTYROOM': {
        'NAME': "empty room",
        'DESCRIPTION': "the room seems empty, nothing to see here",
        'PATHS': {
            'EAST': 'PORTALROOM',
            'SOUTH': 'SECRETROOM'
        }
    },
    'FREEZER': {
        'NAME': "freezer",
        'DESCRIPTION' : "a chilling room, its full of meat",
        'PATHS' : {
            'NORTH': 'PORTALROOM',
            'SOUTH': 'KITCHEN'
        }
    },
    'KITCHEN': {
        'NAME' : "kitchen",
        'DESCRIPTION': "an average kitchen...nothing to see here",
        'PATHS' : {
            'NORTH' : 'FREEZER',
            'EAST': 'LIVINGROOM',

        }
    },
    'LIVINGROOM': {
        'NAME': "the livingroom",
        'DESCRIPTION': "The room has a single chest, you could store things there...like that sword",
        'PATHS' : {
            'SOUTH' : "HALL",
            'WEST': "KITCHEN"
        }
    },
    'HALL' : {
        'NAME': "a large hall",
        'DESCRIPTION' : "this hall may be a point of no return",
        'PATHS': {
            'EAST': "DIO ROOM",
            'NORTH' : "LIVING ROOM"
        }

    },
    'DIO ROOM':{
        'NAME': 'a room',
        'DESCRIPTION': 'you feel a dank presence',
        'PATHS' : {
            'WEST': 'HALL',
            'EAST': 'SPIKETRAP',
            'NORTH': 'STARTROOM',
            'SOUTH': 'STARTROOM'
        }
    },
    'SPIKETRAP' : {
        'NAME': 'NO HOPE',
        'DESCRIPTION': 'no point.....youre already dead',
        'PATHS': {
         'NORTH': 'STARTROOM',
        'SOUTH': 'STARTROOM',
        'WEST': 'STARTROOM',
        'EAST': 'STARTROOM',
        'UP': 'STARTROOM',
        'DOWN':'STARTROOM',
        'NANI': 'SECRET'
        }
    },
    'SECRET':{
     'NAME' : 'you see our lord and saviour JoJo',
    'PATHS' : {
     'NORTH':'STARTROOM'
    }
    }
}
current_node = world_map ['STARTROOM']

directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'DOWN', 'UP', 'NANI']

while True :
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node ['PATHS'] [command]
            current_node = world_map [name_of_node]
        except KeyError:
            print("you cannot go this way.")
    else:
        print("direction not recognized")
        print()
