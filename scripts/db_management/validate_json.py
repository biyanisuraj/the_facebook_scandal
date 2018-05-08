import gzip
import json
import os
import subprocess
import sys


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


dir_name = sys.argv[1]
corrupted_files = list()

for fname in os.listdir(sys.argv[1]):
    line_counter = 0

    if fname == '.DS_Store':
        continue
    else:
        tmp_json = open('./tmp_json.json', 'w')
        tmp_json.write('{ "tweets": [')

        cfile = gzip.open(sys.argv[1] + '/' + fname, 'r')
        lines = cfile.readlines()

        for line in lines:
            if line_counter < len(lines) - 1:
                tmp_json.write(line.replace('}\n', '},\n'))
                line_counter += 1
            else:
                tmp_json.write(line)
        tmp_json.write(']}')
        tmp_json.close()

        try:
            f = open('./tmp_json.json')
            json.load(f)
        except ValueError:
            corrupted_files.append(fname)

        subprocess.call(['rm', './tmp_json.json'])

print 'FOUNDED ' + str(len(corrupted_files)) + ' CORRUPTED FILES'

for f in corrupted_files:
    print 'REMOVING CORRUPTED FILE ' + f
    subprocess.call(['rm', sys.argv[1] + '/' + f])
