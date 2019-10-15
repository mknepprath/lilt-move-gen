from gen_moves import gen_moves

POSITION = 'room'

OBJECTS = [
    {
        'name': 'ant',
        'states': ['inventory']
    },
    {
        'name': 'back wall',
        'states': []
    },
    {
        'name': 'banana',
        'states': ['inventory']
    },
    {
        'name': 'bars',
        'states': []
    },
    {
        'name': 'bed',
        'states': []
    },
    {
        'name': 'bent coin',
        'states': ['inventory']
    },
    {
        'name': 'bird',
        'states': []
    },
    {
        'name': 'blanket',
        'states': ['inventory']
    },
    {
        'name': 'bowl',
        'states': []
    },
    {
        'name': 'bucket',
        'states': []
    },
    {
        'name': 'ceiling',
        'states': []
    },
    {
        'name': 'chest',
        'states': ['open', 'closed']
    },
    {
        'name': 'coin',
        'states': ['inventory']
    },
    {
        'name': 'door',
        'states': ['open', 'closed']
    },
    {
        'name': 'drain',
        'states': []
    },
    {
        'name': 'floor',
        'states': []
    },
    {
        'name': 'flower',
        'states': ['inventory']
    },
    {
        'name': 'forest',
        'states': []
    },
    {
        'name': 'front wall',
        'states': []
    },
    {
        'name': 'key',
        'states': ['pasted', 'inventory']
    },
    {
        'name': 'left wall',
        'states': []
    },
    {
        'name': 'paste',
        'states': ['inventory']
    },
    {
        'name': 'pillow',
        'states': []
    },
    {
        'name': 'right wall',
        'states': []
    },
    {
        'name': 'room',
        'states': []
    },
    {
        'name': 'window',
        'states': []
    }
]

STATES = [
    # {
    #     'name': 'ants',
    #     'states': ['training', 'trained']
    # },
    # {
    #     'name': 'tilt',
    #     'states': ['left', 'right']
    # }
]

print(gen_moves(OBJECTS, STATES, POSITION))
