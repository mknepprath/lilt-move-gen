from gen_moves import gen_moves

POSITION = 'crescent'

OBJECTS = [
    {
        'name': 'bird',
        'states': []
    },
    {
        'name': 'bucket',
        'states': []
    },
    {
        'name': 'crescent plaza',
        'states': []
    },
    {
        'name': 'merchant',
        'states': []
    },
    {
        'name': 'sign',
        'states': []
    },
    {
        'name': 'shop',
        'states': []
    },
    {
        'name': 'sky',
        'states': []
    },
    {
        'name': 'well',
        'states': []
    }
]

# State unassociated with objects.
STATES = []

print(gen_moves(OBJECTS, STATES, POSITION))
