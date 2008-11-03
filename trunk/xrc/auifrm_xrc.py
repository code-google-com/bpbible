# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res






# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    __res.Load('auifrm.xrc')

# ----------------------- Gettext strings ---------------------

def __gettext_strings():
    # This is a dummy function that lists all the strings that are used in
    # the XRC file in the _("a string") format to be recognized by GNU
    # gettext utilities (specificaly the xgettext utility) and the
    # mki18n.py script.  For more information see:
    # http://wiki.wxpython.org/index.cgi/Internationalization 
    
    def _(str): pass
    
    _("&Set Sword Paths...")
    _("Install books...")
    _("Manage books...")
    _("Set fonts...")
    _("&Language")
    _("&Exit")
    _("&File")
    _("&Display")
    _("Default Layout")
    _("Toolbars")
    _("&Windows")
    _("Debug")
    _("Html Ide")
    _("WI")
    _("gather")
    _("diff")
    _("confirm")
    _("compile")
    _("Restart")
    _("Locale")
    _("&Help")
    _("BPBible Website")
    _("Documentation...")
    _("Report a problem...")
    _("Download books...")
    _("&About...")
    _("Bible")

