#import ava_cmds
#import ava_core

#ava_cmds.speak("Test")

#import v_programmer

#v_programmer.write_verbal_command("Hello AVA", "AVA")

#print(v_programmer.read_verbal_command("Hello AVAs"))

# import json
# t_phrase = "Hello AVA"
# orig_cmd = "AVA"

# dataDict = {
#     'id': None,
#     'trigger': str(t_phrase.lower()),
#     'original': str(orig_cmd.lower())
# }

# dataJson = json.dumps(dataDict)

# print(dataJson)
# with open('c_v_cmds_db.json', 'w') as output:
#     json.dump(dataJson, output)
