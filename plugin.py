from vimpy import Plugin, variables

variables.globals['vimpy_example_left_message'] = 'Vim left.'


class VimpyExamplePlugin(Plugin):
    def vim_leave(self, data=None):
        print(data)

        # Try changing this in the vim terminal before quitting.
        # :VimpyExample Goodbye.

        if 'vimpy_example_left_message' in variables.globals:
            left_message = variables.globals['vimpy_example_left_message']
            print('VimpyExample :: {message}'.format(message=left_message))
