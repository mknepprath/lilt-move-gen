import json
import random

# TO RUN:
# - python room.py > moves_room.json
# - python crescent.py > moves_crescent.json
# Convert to CSV: https://json-csv.com/


def gen_moves(objects, states, position):
    ACTIONS = [
        'close',
        'eat',
        'give',
        'go through',
        'kill',
        'look at',
        'look behind',
        'look under',
        'open',
        'pull',
        'punch',
        'push',
        'take',
        'talk to',
        'think about',
        'use'
    ]

    ERROR_MESSAGES = [
        'Didn\'t work.',
        'You can\'t do that.',
        'That can\'t be done.',
        'Oops, can\'t do that.',
        'Sorry, you can\'t do that.',
        'That didn\'t work.',
        'Try something else.',
        'Sorry, you\'ll have to try something else.',
        'Oops, didn\'t work.',
        'Oops, try something else.',
        'Nice try, but you can\'t do that.',
        'Nice try, but that didn\'t work.',
        'That doesn\'t seem to do anything.',
        'Try something else, that didn\'t seem to work.'
    ]

    SHARED_MOVES = {
        'help',
        'look around',
        'look down',
        'look left',
        'look right',
        'look up',
        'what are my options',
        'what is around me',
        'where am i'
    }

    moves = []

    for move in SHARED_MOVES:
        moves.append({
            'move': move,
            'response': '{error} #gen'.format(
                error=random.choice(ERROR_MESSAGES)
            ),
            'position': position
        })

    for action in ACTIONS:
        for obj in objects:
            moves.append({
                'move': '{action} {obj}'.format(action=action, obj=obj['name']),
                'response': 'You try to {action} the {obj}. {error} #gen'.format(
                    action=action,
                    obj=obj['name'],
                    error=random.choice(ERROR_MESSAGES)
                ),
                'position': position
            })

    # Players can use objects with other objects.
    # Loop through each object.
    for use_obj in objects:
        # Loop through each object for each object.
        for with_obj in objects:
            # Don't use an item with itelf.
            if use_obj['name'] != with_obj['name'] and 'inventory' in use_obj['states']:
                # Add stateless move.
                moves.append({
                    'move': 'use {use_obj} on {with_obj}'.format(
                        use_obj=use_obj['name'],
                        with_obj=with_obj['name']
                    ),
                    'response': 'You try to use the {use_obj} on the {with_obj}. {error} #gen'.format(
                        use_obj=use_obj['name'],
                        with_obj=with_obj['name'],
                        error=random.choice(ERROR_MESSAGES)
                    ),
                    'position': position
                })

                # Loop through every possible state.
                for state_obj in ([use_obj, with_obj] + states):
                    for state in state_obj['states']:
                        # Add the move. There will be a lot of irrelevant moves
                        # generated here - for instance, we don't care if the chest
                        # is open while using scissors with paper.
                        moves.append({
                            'move': 'use {use_obj} on {with_obj}'.format(
                                use_obj=use_obj['name'],
                                with_obj=with_obj['name']
                            ),
                            'response': 'You try to use the {use_obj} on the {with_obj}. {error} #gen'.format(
                                use_obj=use_obj['name'],
                                with_obj=with_obj['name'],
                                error=random.choice(ERROR_MESSAGES)
                            ),
                            'condition': '{{"{state_obj}": "{state}"}}'.format(
                                state_obj=state_obj['name'],
                                state=state
                            ),
                            'position': position
                        })

    # print('// ' + str(len(moves)) + ' moves generated.')

    return json.dumps(moves, indent=2)
