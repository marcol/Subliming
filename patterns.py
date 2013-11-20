# --------
# Patterns for the Command Palette
# Author: marcol
# Description: Get patterns 
# --------

import sublime, sublime_plugin, os, re, threading
from os.path import basename

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

class WritePatternCommand(sublime_plugin.TextCommand):
        def run (self, edit, content, syntax_file):
                self.view.insert(edit, self.view.size(), content)
                self.view.set_syntax_file(syntax_file)


class GetPatternCommand(sublime_plugin.WindowCommand):

        def run(self, pattern, syntax, isNew):

                ext = '.js'
                syntax_file = 'Packages/JavaScript/JavaScript.tmLanguage'

                if (syntax == 'HTML') :
                        ext = '.html'
                        syntax_file = 'Packages/HTML/HTML.tmLanguage'
                elif (syntax == 'CSS') :
                        ext = '.css'
                        syntax_file = 'Packages/CSS/CSS.tmLanguage'

                patternFile = 'Packages/Subliming/' + syntax + '/patterns/' + pattern + ext
                content = self.get_file(patternFile)

                if (content and isNew):      
                        self.window.new_file()

                self.window.run_command('write_pattern', {'content': content, 'syntax_file': syntax_file});                        


        def get_file(self, patternFile):
                if hasattr(sublime, 'load_resource'):
                        return sublime.load_resource(patternFile)
                else:
                        with open(os.path.join(sublime.packages_path(), patternFile[9:])) as f: return f.read()

