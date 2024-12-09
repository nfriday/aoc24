input = [int(i) for i in list(open("09.txt", "r").read().strip())]

# part 1

files = list(zip(range(len(input) // 2 + 1),input[::2]))
space = input[1::2]
                 
compressed = []

while files:
    # take file from front
    compressed.append(files.pop(0))

    # take space from front
    free_space = space.pop(0)

    while free_space > 0:
        # take a file from end
        if not files: break
        file = files.pop()
        file_id, file_length = file
        # if it fits, put it in the space
        if file_length <= free_space:
            compressed.append(file)
            free_space -= file_length
        # if not, put what we can in the space, and leave the rest
        else:
            compressed.append((file_id, free_space))
            files.append((file_id, file_length - free_space))
            free_space = 0

checksum = 0
i = 0
for id,length in compressed:
    for _ in range(length):
        checksum += i * id
        i += 1
print(checksum)

# part 2

files = list(zip(range(len(input) // 2 + 1),input[::2]))
space = [(None,i) for i in input[1::2]]

filesystem = []
for file,space in zip(files,space):
    filesystem.append(file)
    filesystem.append(space)
filesystem.append(files[-1])

compressed = []

while filesystem:
    file = filesystem.pop(0)
    id, length = file

    # if it's a file, add it to compressed
    if id != None:
        compressed.append(file)
        continue

    # if it's a space, find the rightmost file that will fit in it
    free_space = length
    for j in range(len(filesystem)-1,-1,-1):
        move_candidate = filesystem[j]
        move_candidate_id, move_candidate_length = move_candidate
        if move_candidate_id == None: continue
        if move_candidate_length <= free_space:
            free_space -= move_candidate_length
            compressed.append(move_candidate)
            filesystem[j] = (None,move_candidate_length)
        if free_space == 0: break

    # if still free space left, add it to compressed
    if free_space > 0:
        compressed.append((None,free_space))

checksum = 0
i = 0
for id,length in compressed:
    for _ in range(length):
        if id != None: checksum += i * id
        i += 1
print(checksum)