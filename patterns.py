# --------
# Patterns for the Command Palette
# Author: marcol
# Description: Get patterns 
# --------

import sublime, sublime_plugin, os, re, threading
from os.path import basename

class SublimingPatternCommand(sublime_plugin.TextCommand):

        def run(self, edit):
                print(self);
                print(edit);

        def get_javascript_files(self, dir_name, *args):
                fileList = []
                for file in os.listdir(dir_name):
                        dirfile = os.path.join(dir_name, file)
                        if os.path.isfile(dirfile):
                                fileName, fileExtension = os.path.splitext(dirfile)
                                if fileExtension == ".js" and ".min." not in fileName:
                                        fileList.append(dirfile)
                        elif os.path.isdir(dirfile):
                                fileList += self.get_javascript_files(dirfile, *args)
                return fileList
