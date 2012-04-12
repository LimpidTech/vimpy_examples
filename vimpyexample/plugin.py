from vimpy.plugins import Plugin

class VimpyExamplePlugin(Plugin):
    def vim_enter(self, data=None):
        print('VimpyExample :: Vim entered.')

    def vim_leave(self, data=None):
        print('VimpyExample :: Vim left.')

