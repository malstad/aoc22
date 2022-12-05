wkd, fname = str(__file__).rsplit('/', 1) 

def main():
    puzzle_input = open(wkd + '/puzzle_input.txt', 'r')
    elf_count, result = problem1()
    print(result)

    result = problem2(elf_count)
    print(result)
    
    return

# A rucksack is a string of characters (case-sensitive) where each letter represents an item in the bag
# Each one has two equally sized partitions, and each one should contain one - and only 1 (?) - shared item
# the shared item determines the type of rucksack, which in turn determines its priority, see get_priority()
def problem1():
    sum_of_type_priority = elf_count = 0
    puzzle_input = open(wkd + '/puzzle_input.txt', 'r')
    
    for line in puzzle_input:
        contents = line.strip()
        sum_of_type_priority += get_priority(get_type(contents))
        elf_count += 1      # when you reduce people to numbers, it makes them easier to manipulate.
    return elf_count, sum_of_type_priority

# This time we don't care about partitions of each individual rucksack, 
# but instead we should look at 3 rucksacks at a time to find the uniquely common letter between them (badge)
# what is the total of every group of elves' badges' values?
def problem2(elf_count):
    puzzle_input = open(wkd + '/puzzle_input.txt', 'r')
    sum_of_badge_values = 0
    sack_count = 0
    rucksacks = puzzle_input.readlines()
    
    while sack_count < len(rucksacks):
        group_size = 3
        elf_index = 0
        elf_group = rucksacks[sack_count:sack_count+group_size] # a slice of
        
        badge = get_badge(elf_group)
        sum_of_badge_values += get_priority(badge)
        
        sack_count += group_size # next set of elves, ready for processing


    return sum_of_badge_values

# With a collection of rucksacks to rummage through, which item is uniquely shared between them all? (e.g. they all have 'j', or 'N')
def get_badge(collection):
    badge_type = 'z'

    # this loop definitely assumes valid input...
    for item in collection[0]:                  # for every item in the *first* rucksack
        found_matches = 0 
        for other in collection[1:]:            # look at every item in the collection of rucksacks (excluding the first one)
            if item in other.strip():           # and check to see if it's in each of the others, one at a time
                found_matches += 1              # if it's found in one, we increase the counter by 1
                badge_type = item               # just in case this *is* the right one, assign it
        if found_matches == len(collection)-1:  # in the case of collections of 3, there should be two matches for it to be legit
            break

    return badge_type   


# determines the type of rucksack
# according to the rules, the type is the uniquely shared letter (case sensitive) between each half
def get_type(rucksack):
    mid = int(len(rucksack)/2)
    bag_type = 'Z'                          # start at a high value, again so we fail loudly

    part0 = rucksack[0:mid] 
    part1 = rucksack[mid:mid*2] 

    for item in part0:          # in the first partition, go letter by letter 
        if item in part1:       # and see if that letter is in the other part
            bag_type = item     # if so, we now know the bag type
            break               # no need to continue looping
              
    return bag_type

 # this was originally just a quick bounds check with if/elif and >= and <= conditionals using ascii hardcoded values,
 # but this seemed more fun... crash course with lists, and ranges, and dictionaries
def get_priority(item_type):
    item_type_ascii = ord(item_type)
    lcase = list(range(ord('a'), ord('z')+1))           # range of ascii values for lowercase (97 - 122)
    ucase = list(range(ord('A'), ord('Z')+1))           # range of ascii values for uppercase (65 - 90)
    
    length = len(lcase + ucase)                         # total number of unique letters, upper and lower case ofc
    point_vals = list(range(1, length+1))               # list meant to be parallel to the combined list of ascii values, to represent their game value (1, 2, 3, ... 52, 53)

    game_values = dict(zip(lcase + ucase, point_vals))  # now we can use the ascii value as a key to find its assigned value {(97:1), (98:2), ... (41:27), (42:28)}
    return game_values[item_type_ascii]

if __name__ == "__main__":
    main()