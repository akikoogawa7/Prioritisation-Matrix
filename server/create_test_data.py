import json

user_inputs = {
    'DE1': {
        'user_id': 'DE1',
        'name': 'Akiko Ogawa',
        'role': 'Data Engineer',
        'tasks': {
            'work on A': (9, 2)
        }
    },
    'MO1': {
        'user_id': 'MO1',
        'name': 'James Fox',
        'role': 'Management Operator',
        'tasks': {
            'work on A': (8, 7)
        }
    },
    'PD1': {
        'user_id': 'PD1',
        'name': 'Joe Chan',
        'role': 'Product Design',
        'tasks': {
            'work on A': (2, 9)
        }
    }
}

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(user_inputs, f, ensure_ascii=False, indent=4)