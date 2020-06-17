import datetime
import os
import sublime
import sublime_plugin

class ShowFileModifiedTimeListener(sublime_plugin.ViewEventListener):

    def on_activated_async(self):
        file = self.view.file_name()

        try:
            mtime = os.path.getmtime(file)
        except:
            mtime = 0

        self.show_file_modified_time(self.view, mtime)

    def show_file_modified_time(self, view, t):
        if t == 0:
            sublime.status_message("")
            return

        mdate = datetime.datetime.fromtimestamp(t)

        view.set_status("mdate", mdate.strftime("%Y/%m/%d %H:%M:%S"))
