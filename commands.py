from vimpy import Command, variables


class VimpyExample(Command):
    """ A command for changing variables related vimpy_example's Plugin. """

    def run(self, message=None):
        """ This function gets called with :VimpyExample.

        This function gets called when executing the :VimpyExample command
        from Vim. It can be used in the following ways:

        :VimpyExample
        :VimpyExample "A new message."
        :VimpyExample message=hi

        """

        if message is None:
            if 'vimpy_example_left_message' in variables.globals:
                del variables.globals['vimpy_example_left_message']

            print('No left message set.')

        else:
            variables.globals['vimpy_example_left_message'] = message
            print('New message: ' + message)
