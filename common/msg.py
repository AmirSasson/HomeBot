""" Models"""


# pylint: disable=too-few-public-methods
class Msg(object):
    """ A Msg to send upon action"""

    def __init__(self, ref_id: str, time: int, msgType: str, user_id: str):
        self.ref_id = ref_id
        self.time = time
        self.type = msgType
        self.user_id = user_id
