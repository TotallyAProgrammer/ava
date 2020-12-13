"""
The verbal programmer module for AVA
"""

import json

# TODO Faster lookup. Maybe use a table of IDs? Distribute 

async def write_verbal_command(t_phrase, orig_cmd): # Test, async should make this faster (AVA shouldnt have to wait for file write operations)
    """
    Asynchronous function to write new verbal commands to a DB 
    """
    data = {}
    data['verbal'].append({
        'id': None,
        'trigger': str(t_phrase),
        'original': str(orig_cmd)
    })
    with open('c_v_cmds_db.json', 'w') as output:
        json.dump(data, output)

def read_verbal_command(t_phrase): # Make async?
    with open('c_v_cmds_db.json', 'r') as input:
        data = json.load(input)
        for trigger in data['trigger']:
            if str(t_phrase) == str(trigger):
                return data['original']
            else:
                return False
