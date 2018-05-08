# encoding: utf-8
import gzip
import os
import sys

"""
    EXAMPLE:
        python some/very/long/path/directory_with_chunks
    RETURNS:
        directory_with_chunks.json.gz
"""

dir_name = sys.argv[1]
item_counter = 0
destination = './' + dir_name.split('/')[-1] + '.json.gz'

with gzip.open(destination, 'w') as f:
    f.write('{ "tweets": [')

    for fname in os.listdir(sys.argv[1]):
        line_counter = 0

        if fname == '.DS_Store':
            item_counter += 1
        else:
            print 'Formatting item ' + str(item_counter) + ', file: ' + fname

            cfile = gzip.open(sys.argv[1] + '/' + fname, 'rb')
            lines = cfile.readlines()

            for line in lines:
                if item_counter < len(os.listdir(sys.argv[1])) - 1:
                    f.write(line.replace('}\n', '},\n'))
                else:
                    if line_counter < len(lines) - 1:
                        f.write(line.replace('}\n', '},\n'))
                        line_counter += 1
                    else:
                        f.write(line)

            item_counter += 1

    f.write(']}')
