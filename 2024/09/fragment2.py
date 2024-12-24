#!/usr/bin/env python3

infilename = 'tiny.txt'
#infilename = 'input.txt'

with open(infilename, 'r', encoding='UTF-8') as infile:
    rawdisk = infile.read().strip()

print(rawdisk)

def get_n_blocks(rawdisk):
    total_blocks = sum([int(x) for x in rawdisk[::2]])
    return(total_blocks)

def get_n_files(rawdisk):
    total_files = len([int(x) for x in rawdisk[::2]])
    return(total_files)

def expand_rawdisk(rawdisk, infill.pop):
    fileid = -1
    is_space = True
    for size in rawdisk:
        is_space = not is_space
        if is_space:
            return next(infill[i])
        else:
            fileid += 1
            for j in range(int(i)):
                yield fileid


infill = {str(x):[] for x in range(10)}


fileid = round(len(rawdisk)/2)
for size in rawdisk[::-2]:
    fileid -= 1
    infill[size].append(fileid)






total_files = get_n_files(rawdisk)

a = expand_rawdisk(rawdisk, infill)

for i in a:
    print(i)



checksum = 0
files_handled = 0
for i in a:
    if block_pos >= total_blocks:
        break
    else:
        checksum += block_pos * i



print(checksum)


