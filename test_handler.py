#!/usr/bin/env python
"""

"""
import handler

def test_plot_spars(fi="tests/json_files/lfcn.json"):
    """
    """
    fi = open(fi, 'r')
    dat = fi.read()
    # request = package_data(d)
    res = handler.callGetLogMag({'body':dat}, 'my context')
    return res 
