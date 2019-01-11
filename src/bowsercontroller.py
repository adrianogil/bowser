import webbrowser
import utils

import json
import os


class BowserController():
    """BowserController is responsible for managing commands"""
    def __init__(self):
        self.search_engine_data_path = os.environ["BOWSER_DIRS"] + "/data/search_engine.bowser"

    def open(self, args, extra_args):
        url = args[0]

        if 'http' not in url:
            url = 'http://' + url

        utils.dprint(url)
        webbrowser.open(url, autoraise=True)
        # webbrowser.open_new_tab(url)

    def search_engine(self, args, extra_args):
        if not os.path.exists(self.search_engine_data_path):
            return

        keyword = args[0]
        keyword = keyword.replace(" ", "%20")

        with open(self.search_engine_data_path, 'r') as f:
            search_engine_data = json.load(f)

        if keyword not in search_engine_data:
            return

        search_engine_str = search_engine_data[keyword]

        for i in range(1, len(args)):
            search_engine_str = search_engine_str.replace("%s" + str(i - 1), args[i])

        self.open([search_engine_str], [])

    def save_search_engine(self, args, extra_args):
        search_engine_keyword = args[0]
        search_engine_str = args[1]

        search_engine_data = {}

        if os.path.exists(self.search_engine_data_path):
            with open(self.search_engine_data_path, 'r') as f:
                search_engine_data = json.load(f)

        search_engine_data[search_engine_keyword] = search_engine_str

        with open(self.search_engine_data_path, 'w') as f:
            json.dump(search_engine_data, f)

    def get_commands(self):
        commands_parse = {
            '-o'              : self.open,
            '-e'              : self.search_engine,
            '-s'              : self.save_search_engine,
            '--open'          : self.open,
            '--engine'        : self.search_engine,
            '--save'          : self.save_search_engine,
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