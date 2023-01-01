with open("crate_instructions.txt", "r", encoding="utf-8") as f:
    stack_len = 9                                       # tried to manually look at the first line, but python won't let me
    crates_examined = False                             # assume file layout first contains crate layout
    stacks = {i: "" for i in range(1, stack_len+1)}     # get each stack ready with its ID (1-9) and empty string
    print(stacks)

    for i, line in enumerate(f, start=1):

        # begin by examining the crate structure, line by line, totaling up each stack in reverse
        if not crates_examined:
            for j, ch in enumerate(line, start=1):
                if j % 4 == 2 and (ch.isalpha()):       # we only need to check certain characters on each line
                    stack_index = int(((j-2)/4)+1)      # position 10 > 3, 14 > 4, etc
                    #print("stack_index is: " + str(stack_index) + " and the character found is: " + ch + " and j is: " + str(j))
                    stacks[stack_index] = ch + stacks[stack_index]
            #print(stacks)
            if line.strip() == '':
                # empty line means we've reached the end, now onto the movement
                crates_examined = True
                print(stacks)
        else:
            # after the diagram of the crates and the newline, every subsequent line is a move command like:
            # move 6 from 6 to 5
            # so let's just split it up by the spaces and take what we need
            command = line.split(' ')
            amount = int(command[1])
            remove_from = int(command[3])
            move_to = int(command[5])

            # Take the last <amount> of characters of <remove_from>, reverse it, and append it to <move_to>, per the puzzle's instructions
            prefix, suffix = stacks[remove_from][:amount*-1], stacks[remove_from][amount*-1:]   
            stacks[move_to] = stacks[move_to] + "".join(reversed(suffix)) # for problem #2, simply don't reverse the suffix
            stacks[remove_from] = prefix


            print(stacks)