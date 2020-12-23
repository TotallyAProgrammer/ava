import configparser
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
            }
        }
    }
    try:
        #print(question_arr[0])
        return (q_dict.get(str(question_arr[0])).get(str(question_arr[1])).get(str(question_arr[2])))
    except Exception as exp:
        print(str(exp))
        return None


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
        return 
    elif question in {"exit", "quit", "disconnect", "dc"}:
        return "!!!DISCONNECT_CLIENT!!!"
