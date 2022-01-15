from fritzconnection import FritzConnection
from fritzconnection.lib.fritzcall import FritzCall
from fritzconnection.lib.fritzstatus import FritzStatus


class FritzboxConnect:
    def __init__(self, address: str, username: str, password: str, port: str):
        self.FCONN = FritzConnection(address=address, user=username, password=password, port=port, timeout=2.0)
        self.FSTAT = FritzStatus(address=address, user=username, password=password, port=port, timeout=2.0)
        self.FCALL = FritzCall(address=address, user=username, password=password, port=port, timeout=2.0)

    def connection(self) -> FritzConnection:
        return self.FCONN

    def status(self):
        return self.FSTAT

    def call(self):
        return self.FCALL

    def read_module(self, module: str, action: str):
        try:
            answer = self.connection().call_action(module, action)
        except:
            answer = dict()  # return an empty dict in case of failure
        return answer

    def read_module_indexed(self, module: str, action: str, index: int) -> dict[any, str]:
        try:
            return self.connection().call_action(module, action, NewIndex=index)
        except IndexError as ie:
            raise ie
