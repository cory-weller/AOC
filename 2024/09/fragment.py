#!/usr/bin/env python3

# infilename = 'tiny.txt'
infilename = 'input.txt'

with open(infilename, 'r', encoding='UTF-8') as infile:
    rawdisk = infile.read().strip()

print(rawdisk)

def get_n_blocks(rawdisk):
    total_blocks = sum([int(x) for x in rawdisk[::2]])
    return(total_blocks)


def backfill_fileid(rawdisk):
    fileid = round(len(rawdisk)/2)
    for i in rawdisk[::-2]:
        fileid -= 1
        for j in range(int(i)):
            yield fileid


def expand_rawdisk(rawdisk, backfill):
    fileid = -1
    is_space = True
    for i in rawdisk:
        is_space = not is_space
        if is_space:
            for i in range(int(i)):
                yield next(backfill)
        else:
            fileid += 1
            for j in range(int(i)):
                yield fileid


total_blocks = get_n_blocks(rawdisk)
backfill = backfill_fileid(rawdisk)
a = expand_rawdisk(rawdisk, backfill)

checksum = 0
block_pos = -1
for i in a:
    block_pos += 1
    if block_pos >= total_blocks:
        break
    else:
        checksum += block_pos * i



print(checksum)

