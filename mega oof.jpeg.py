#OofSwcsdc
world_map = {
    'WESTHOUSE' :{
         'NAME': "west of house",
        'DESCRIPTION': "you are west of a white house",
        'PATHS' : {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTH HOUSE'
        }

    },
    'NORTHHOUSE' : {
        'NAME': 'north of house',
        'DESCRIPTION': 'dank memes',
        'PATHS': {
            'SOUTH' : 'WESTHOUSE'
        }
    },
    'SOUTHHOUSE' : {
        'NAME': 'south of house',
        'DESCRIPTION': 'dank memes',
        'PATHS': {
            'NORTH' : 'WESTHOUSE'
        }
    },
}
input()