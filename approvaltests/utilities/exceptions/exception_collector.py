from typing import Callable

from approvaltests.utilities.exceptions.multiple_exceptions import MultipleExceptions


class ExceptionCollector:
    def __init__(self):
        self._exceptions = []

    def gather(self, callable: Callable):
        try:
            callable()
        except Exception as exception:
            self._exceptions.append(exception)

    def release(self):
        if len(self._exceptions) == 0:
            return
        if len(self._exceptions) == 1:
            raise self._exceptions[0]

        raise MultipleExceptions(self._exceptions)