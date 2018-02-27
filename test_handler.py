#!/usr/bin/env python
"""

"""
import handler

def test_get_logmag(fi="tests/json_files/lfcn.json"):
    """
    """
    fi = open(fi, 'r')
    dat = fi.read()
    # file_data = 'lfcn-800.s2p'
    # file_name = fi.read()
    # d = {
    #     'filedata': file_data,
    #     'filename': file_name
    #      }
    # fi.close()
    # request = package_data(d)
    res = handler.callGetLogMag({'body':dat}, 'my context')
    return res 
