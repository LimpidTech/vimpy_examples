from vimpy import Command, variables


class VimpyExample(Command):
    def run(self, message=None):

        if message is None:
            if 'vimpy_example_left_message' in variables.globals:
                del variables.globals['vimpy_example_left_message']

            print('No left message set.')

        else:
            variables.globals['vimpy_example_left_message'] = message
            print('New message: ' + message)
