"""
The verbal programmer module for AVA
"""

import json

# TODO Faster lookup. Maybe use a table of IDs? Distribute

def write_verbal_command(t_phrase, orig_cmd): # Test, async should make this faster (AVA shouldnt have to wait for file write operations)
    """
    Function to write new verbal commands to a DB
    t_phrase: The trigger phrase
    orig_cmd: The original command
    """
    dataDict = {
        'id': None,
        'trigger': str(t_phrase.lower()),
        'original': str(orig_cmd.lower())
    }
    dataJson = json.dumps(dataDict)
    try:
        with open('c_v_cmds_db.json', 'a') as output:
            # json.dump(dataJson, output)
            output.write(dataJson + "\n")
    except Exception as exp:
        print("Exception: " + str(exp))
        return False

def read_verbal_command(t_phrase): # Make async?
    """
    Function to read verbal commands from the DB
    t_phrase: Trigger phrase to check
    """
    try:
        with open('c_v_cmds_db.json', 'r') as f_input:
            for line in f_input:
                # data = json.load(f_input)
                dataDict = json.loads(line)
                for (key, val) in dataDict.items():
                    if str(key) == "trigger":
                        if str(t_phrase).lower() == str(val).lower():
                            return dataDict['original']
            return False
    except Exception as exp:
        print("Exception: " + str(exp))
        return False
