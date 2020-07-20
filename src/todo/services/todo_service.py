from typing import List, Dict

from datetime import datetime


def get_todos() -> List[Dict[str, any]]:
    return [
        {'description': 'Cleaning kitchen', 'planned_for': datetime(2020, 3, 2), 'done': True},
        {'description': 'shopping', 'planned_for': datetime(2020, 4, 16), 'done': False},
        {'description': 'Calling pizza service', 'planned_for': datetime.now(), 'done': True}
    ]
