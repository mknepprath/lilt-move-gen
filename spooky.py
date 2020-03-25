from gen_moves import gen_moves

POSITION = 'spookytown'

OBJECTS = [
    {
        'name': 'hut',
        'states': ['smashed']
    },
    {
        'name': 'medallion',
        'states': ['inventory']
    },
    {
        'name': 'spookytown',
        'states': []
    },
    {
        'name': 'totem',
        'states': ['inventory']
    }
]

# State unassociated with objects.
STATES = []

print(gen_moves(OBJECTS, STATES, POSITION))
