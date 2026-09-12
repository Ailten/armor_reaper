
class ErrorView:

    def __init__(self, msg: str, input_name: str|None = None):
        self.msg = msg
        self.input_name = input_name