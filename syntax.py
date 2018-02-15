from utils import register_operation, register_loop_symbol


class Syntax:
    """ Synactic rules of brainfuck """
    def __init__(self, num_of_cells=30000):
        self.cells = [0] * num_of_cells
        self.position = 0

    @property
    def current_cell(self):
        """ Return current cell """
        return self.cells[self.position]

    @current_cell.setter
    def current_cell(self, value):
        """ Set a value to current cell """
        self.cells[self.position] = value

    @register_operation('+')
    def increment(self):
        """ Increment the value of current cell """
        self.current_cell += 1

    @register_operation('-')
    def decrement(self):
        """ Decrement the value of current cell """
        self.current_cell -= 1

    @register_operation('>')
    def next_cell(self):
        """ Move position pointer to next cell """
        self.position += 1

    @register_operation('<')
    def prev_cell(self):
        """ Move position pointer to previous cell """
        self.position -= 1

    @register_operation('.')
    def print_cell(self):
        """ Print the ASCII character corresponding to current cell value """
        cell_value = self.current_cell
        print(chr(cell_value), end='')

    @register_operation(',')
    def read_to_cell(self):
        """ Read a input to current cell """
        self.current_cell = ord(input(">>> "))

    @register_loop_symbol('loop_in', '[')
    @register_operation('[')
    def loop_in(self):
        if self.current_cell == 0:
            return "pass"
        else:
            return "enter"

    @register_loop_symbol('loop_out', ']')
    @register_operation(']')
    def loop_out(self):
        if self.current_cell == 0:
            return "exit"
        else:
            return "continue"
