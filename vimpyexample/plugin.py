from vimpy.plugins import Plugin
from vimpy.conf import settings

settings['g:vimpy_example_left_message'] = 'Vim left.'

class VimpyExamplePlugin(Plugin):
    def vim_enter(self, data=None):
        print('VimpyExample :: Vim entered.')

    def vim_leave(self, data=None):
        left_message = settings['g:vimpy_example_left_message']

        print('VimpyExample :: {message}'.format(message=left_message))

