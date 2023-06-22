#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and saves them to a file"""


import sys
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from('add_item.json')
    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to(my_list, 'add_item.json')

except Exception:
    save_to(sys.argv[1:], 'add_item.json')
