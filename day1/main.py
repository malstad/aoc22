elves = []
ration_sums = []
elf_index = 0
rations_info = open('/workspace/advent-of-code/day1/rations.txt', 'r')

# iterate over the file to create a list of lists (list of elves, each with a list of their own rations)
for ration in rations_info:
    if ration != "\n":
        if len(elves) == elf_index: # check if we need to init the inner list
            elves.append([])
        elves[elf_index].append(int(ration.strip()))
    else:
        elf_index += 1

rations_info.close()

for elf in elves:
    ration_sums.append(sum(elf))

print( sum(sorted(ration_sums, reverse=True)[:3]))