"""
AVA Cloud 'top-level' commands
"""


def ser_ver():
    """
    Retreive server version
    """
    try:
        with open('/home/carl/ava/ava_cloud/server_version', 'r') as version:
            ava_c_v = version.readline(1)
            return str(ava_c_v)
    except Exception as err:
        print("Error in ser_ver function: " + str(err))
        return "0"


def parse_questions(question):
    """
    Parse and handle requests and questions
    """
    question = str(question).lower()
    if question == "ava cloud version":
        return ser_ver()
    elif question == "ava cloud host":
        return "foobar"