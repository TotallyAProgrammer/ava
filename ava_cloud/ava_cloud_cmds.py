import configparser
import re
import requests
"""
AVA Cloud 'top-level' commands
"""

# Read AVA's Configuration
config = configparser.ConfigParser()
config.readfp(open(r'/home/carl/ava/ava_cloud/ava-cloud-config.conf'))

def read_socket_info(info="ip"):
    """
    Read the socket info for either the port or IP binding
    info = "port" or "ip"
    """
    if str(info).lower() == "port":
        return int(config.get('AVA_CLOUD', 'bind_port'))
    elif str(info).lower() == "ip":
        return str(config.get('AVA_CLOUD', 'bind_addr'))

def commitCount(uname, repo):
	return re.search('\d+$', requests.get('https://api.github.com/repos/{}/{}/commits?per_page=1'.format(uname, repo)).links['last']['url']).group()

def update_version(new_version):
    try:
        with open("./server_version", "w") as f:
            f.write(str(new_version))
            f.close
            return True
    except Exception as exp:
        print("Error updating version: " + str(exp))
        return False

def ser_ver():
    """
    Retreive server version
    """
    try:
        if str(config.get('AVA_CLOUD', 'ser_ver_reporting_location')).lower() == "file":
            with open('/home/carl/ava/ava_cloud/server_version', 'r') as version:
                ava_c_v = version.readline(1)
        elif str(config.get('AVA_CLOUD', 'ser_ver_reporting_location')).lower() == "config":
            ava_c_v = str(config.get('AVA_CLOUD', 'server_version'))
        else:
            return "0"
        return str(ava_c_v)
    except Exception as err:
        print("Error in ser_ver function: " + str(err))
        return "0"

def cmd_help(question):
    """
    The function to output help data when requested
    """
    question_arr = question.split()
    del question_arr[0]
    del question_arr[0]
    print(question_arr)
    q_dict = {
        "ava": {
            "cloud": {
                "help": "AVA Cloud specific commands.",
                "version": "Retreive the AVA Cloud version.",
                "host": "Retrieve the AVA Cloud host\'s name."
            },
            "local": {
                "help": "AVA Local specific commands.",
                "speak": "Tell\'s AVA to speak what is passed."
            },
            "help": "AVA's command base."
        }
    }
    def ret(val):
        if val is not None or "":
            return val
        else:
            return "No help available."
    try:
        if len(question_arr) == 4:
            #print(len(question_arr))
            val = ( q_dict.get(str(question_arr[1])).get(str(question_arr[2])).get(str(question_arr[3])) )
            return ret(val)
        elif len(question_arr) == 3:
            val = ( q_dict.get(str(question_arr[1])).get(str(question_arr[2])).get("help") )
            return ret(val)
        elif len(question_arr) == 2:
            val = ( q_dict.get(str(question_arr[1])).get("help") )
            return ret(val)
        elif len(question_arr) > 4:
            return "No help available."
        elif question_arr == "help".split():
            return "AVA Cloud help command."

    except Exception as exp:
        #print(str(exp))
        return "No help available."


def parse_questions(question):
    """
    Parse and handle requests and questions
    """
    
    question = str(question).lower()
    if question == "ava cloud version":
        return ser_ver()
    elif question == "ava cloud host":
        return "foobar"
    elif "help" in question.split():
        return cmd_help(question)
    elif question in {"exit", "quit", "disconnect", "dc"}:
        return "!!!DISCONNECT_CLIENT!!!"
