import webbrowser
import utils

class BowserController():
    """BowserController is responsible for managing commands"""
    def __init__(self):
        pass
        
    def open(self, args, extra_args):
        url = args[0]

        if 'http' not in url:
            url = 'http://' + url

        utils.dprint(url)
        webbrowser.open(url, autoraise=True)
        # webbrowser.open_new_tab(url)

    def get_commands(self):
        commands_parse = {
            '-o'           : self.open,
            '--open'       : self.open,
            # '-s'           : self.save,
            # '-r'           : self.remove,
            # '-u'           : self.update,
            # '-l'           : self.list,
            # '-p'           : self.path,
            # '-c'           : self.clean,
            # '-f'           : self.find,
            # '-q'           : self.current,
            # '-bk'          : self.go_back,
            # '-bh'          : self.show_history,
            # '--stats'      : self.show_stats,
            # '--back'       : self.go_back,
            # '--clean'      : self.clean,
            # '--save'       : self.save,
            # '--open'       : self.open,
            # '--list'       : self.list,
            # '--find'       : self.find,
            # '--path'       : self.path,
            # '--remove'     : self.remove,
            # '--update'     : self.update,
            # '--current'    : self.current,
            # '--history'    : self.show_history,
            # '--list-args'  : self.list_args,
            # '--auto-list'  : self.auto_list,
            # 'no-args'      : self.handle_no_args,
        }
        return commands_parse

    def finish(self):
        pass