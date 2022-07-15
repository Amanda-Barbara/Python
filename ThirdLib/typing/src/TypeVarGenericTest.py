from typing import Sequence, TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name #把字符串类型封装到了LoggedVar类中
        self.logger = logger #把日志模块Logger类型封装到了LoggedVar类中
        self.value = value #把泛型类型T封装到了LoggedVar类中

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)


from collections.abc import Iterable

def zero_all_vars(vars: Sequence[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(10)

if __name__ == '__main__':
    logobj = Logger('logging')
    log = LoggedVar(bool, 'zjw', logobj)
    logList = [log] * 10
    zero_all_vars(logList)
    for log in logList:
        print(log.get)