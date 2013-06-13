from vimpy.plugins import Plugin
from vimpy import variables

variables.globals['vimpy_example_left_message'] = 'Vim left.'

class VimpyExamplePlugin(Plugin):
    def vim_enter(self, data=None):
        print('VimpyExample :: Vim entered.')

    def vim_leave(self, data=None):
        # Try changing this in the vim terminal before quitting.
        # :let g:vimpy_example_left_message="Goodbye."
        left_message = variables.globals['vimpy_example_left_message']

        print('VimpyExample :: {message}'.format(message=left_message))
