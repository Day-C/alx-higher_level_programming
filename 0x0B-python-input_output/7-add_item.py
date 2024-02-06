#!/usr/bin/python3
'''Define function .'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


argv = sys.argv
'''Add items o list adn then save lists to json file.'''

filename = "add_item.json"
container = []
for i in range(len(argv)):
    if i < 1:
        continue
    container.append(argv[i])

save_to_json_file(container, filename)
load_from_json_file(filename)
