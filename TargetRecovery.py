# -*- coding:

from Tkinter import *
import tkFileDialog
import tkMessageBox
import os
import time
import zlib
import platform

################
################


################
list_files = [] # list contains all files name including both local and remote that displayed.
dict_local = [] # dict contains file's info for local. filename as key, and CRC as value
dict_remote = [] # dict contains file's info for remote.

g_ShDirFileName = "TargetRecovery_dir.txt"
g_ShMatchFileName = "TargetRecovery_match.txt"
g_ShDeleteFileName = "TargetRecovery_delete.txt"
g_ShUploadFileName = "TargetRecovery_upload.txt"
g_ShModuleFileName = "TargetRecovery_module.txt"
g_ConfigFileName = "TargetRecovery.ini"
g_targetCRCFileName = "TargetRecovery_crc.txt"

g_title = "TargetRecovery Tool"
g_lastValidIp = ""
g_lastValidDir = ""

#
# a compound widget that gangs multiple Tk Listboxes o a single scrollbar to achieve a simple multi-column
# scrolled listbox
#

class MultiListbox(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l, w in lists:
            frame = Frame(self);frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=1, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=1, selectborderwidth=0,
                         activestyle='none' highlightthickness=0, takefocus=0,
                         relief=FLAT, exportselection=FALSE, selectmode=EXTENDED)
            lb.pack(expand=YES, file=BOTH)
            self.lists.append(lb)
            lb.

