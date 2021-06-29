import json

import os


def merge(source1, source2, dest, lines1=[], lines2=[]):
    with open(source1, 'r') as file1:
        read_lines1 = file1.readlines()
    with open(source2, 'r') as file2:
        read_lines2 = file2.readlines()
    count = 0
    dict1 = {}
    if not lines1:
        lines1 = [i for i in range(len(read_lines1))]
    if not lines2:
        lines2 = [i for i in range(len(read_lines2))]
    with open(dest, 'w') as dest_file:
        try:
            for i in range(min(len(lines1), len(lines2))):
                count += 1
                dict1["Line {}".format(count)] = [read_lines1[lines1[i]].strip(), read_lines2[lines2[i]].strip()]
            for i in range(max(len(lines1), len(lines2)) - min(len(lines1), len(lines2))):
                count += 1
                if i + min(len(read_lines1), len(read_lines2)) < len(lines1):
                    dict1["Line {}".format(count)] = [read_lines1[lines1[i + min(len(lines1), len(lines2))]].strip()]
                else:
                    dict1["Line {}".format(count)] = [
                        read_lines2[lines2[i + min(len(read_lines1), len(read_lines2))]].strip()]
        except IndexError as index_error:
            print(index_error)
        dest_file.write(json.dumps(dict1, indent=4, sort_keys=True))
