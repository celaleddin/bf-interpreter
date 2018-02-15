import re

from syntax import Syntax
from utils import OPERATIONS, LOOP_CHARS
from utils import UnbalancedLoopChars


class Interpreter:
    """ Basic brainfuck interpreter """
    def __init__(self, code=""):
        self.syntax = Syntax()
        self.code = re.sub('\s+', '', code)
        self.position = 0

    @property
    def current_char(self):
        """ Return current character of source code """
        return self.code[self.position]

    def next_char(self):
        """ Move to next character """
        self.position += 1

    def is_operation(self, char):
        """ Is 'char' a valid operation """
        return char in OPERATIONS.keys()

    def is_loop_operation(self, char):
        """ Is 'char' a loop character ('loop_in' or 'loop_out') """
        return char in LOOP_CHARS.values()

    def make_operation(self, operation, *args, **kwargs):
        """ Make an operation on syntax """
        return getattr(self.syntax, operation)(*args, **kwargs)

    def dispatch(self, char):
        """ Decide what to do with character 'char' """
        result = self.make_operation(OPERATIONS[char])
        if result == "pass" and char == LOOP_CHARS['loop_in']:
            self.goto_closing_loop_char()
        elif result == "enter" and char == LOOP_CHARS['loop_in']:
            self.into_the_loop()
        elif result == "continue" and char == LOOP_CHARS['loop_out']:
            self.goto_opening_loop_char()
        elif result == "exit" and char == LOOP_CHARS['loop_out']:
            pass

    def into_the_loop(self):
        """ We are about to enter a loop! """
        self.loop_in_position = self.position

    def goto_opening_loop_char(self):
        """ C'mon, let us do it again! """
        self.position = self.loop_in_position

    def goto_closing_loop_char(self):
        """ We won't enter, just directly pass by """
        loop_in_count = 0
        for index, char in enumerate(self.code[self.position:]):
            if char == LOOP_CHARS['loop_in']:
                loop_in_count += 1
            elif char == LOOP_CHARS['loop_out']:
                loop_in_count -= 1
                if loop_in_count == 0:
                    self.position = self.position + index
                    return
        raise UnbalancedLoopChars("hey")

    def parse_code(self):
        """ Parse the source code """
        code_length = len(self.code)
        while self.position < code_length:
            if self.is_operation(self.current_char):
                self.dispatch(self.current_char)
            self.next_char()


if __name__ == "__main__":
    while True:
        i = Interpreter(input("bf@python> "))
        i.parse_code()
        print()
