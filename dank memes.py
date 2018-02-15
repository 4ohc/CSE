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
            'NORTH': 'PORTALROOM'
        }
    }
}

current_node = world_map ['STARTROOM']

directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'DOWN', 'UP']

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
