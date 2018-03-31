#encoding: utf-8
import gzip
import os
import sys

# COME USARE LO SCRIPT:
#   DARE IN INPUT ALLO SCRIPT IL PATH DELLA DIRECTORY DOVE SONO CONTENUTI I
#   CHUNKS. LO SCRIPT SALVERÀ TUTTO IN UNICO FILE FORMATTATO NELLA POSIZIONE
#   DA DOVE È STATO CHIAMATO.

dir_name = sys.argv[1]
item_counter, line_counter = 0, 0

with gzip.open('./' + dir_name.split('/')[1] + '.json.gz', 'w') as f:
    f.write('{ "tweets": [')

    for fname in os.listdir(dir_name):
        if fname == '.DS_Store':
            item_counter += 1
        else:
            print 'Formatting item ' + str(item_counter) + ', file: ' + fname

            cfile = gzip.open(dir_name + '/' + fname, 'rb')

            for line in cfile.readlines():
                if item_counter < len(os.listdir(dir_name)) - 1:
                    f.write(line.replace('}\n', '},\n'))
                else:
                    if line_counter < 499:
                        f.write(line.replace('}\n', '},\n'))
                        line_counter += 1
                    else:
                        f.write(line)

            item_counter += 1

    f.write(']}')
