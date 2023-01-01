with open("crate_instructions.txt", "r", encoding="utf-8") as f:
    stack_len = 9                                       # tried to manually look at the first line, but python won't let me
    methods = 2                                         # CrateMover 9000 & 9001
    crates_examined = False                             # assume file layout first contains crate layout
    stacks = {i: "" for i in range(1, stack_len+1)}     # get each stack ready with its ID (1-9) and empty string
    restacked= []                                       # for keeping track of multiples stacking methods
    print(stacks)

    for i, line in enumerate(f, start=1):
        # begin by examining the crate structure, line by line, totaling up each stack in reverse:
        # In my case, J is the first letter detected (which makes for some confusing debug output given my iterator),
        # in Stack 3, but when the crates have been parsed, it will still be the top crate in that stack
        if not crates_examined:
            for j, ch in enumerate(line, start=1):
                if j % 4 == 2 and (ch.isalpha()):       # crates can only be found on the 2nd, 6th, 10th, 14, ... 34th characters
                    stack_index = int(((j-2)/4)+1)      # 2nd char is for Stack 1, 6th ch is Stack 2, 10th: 3, etc
                    stacks[stack_index] = ch + stacks[stack_index]  # add each new crate to the beginning of the string
                    #print("stack_index is: " + str(stack_index) + " and the char found is: " + ch + " and j is: " + str(j))
            #print(stacks)
            if line.strip() == '':
                # empty line means we've reached the end, now onto the movement
                crates_examined = True
                print(stacks)
                for i in range(0, methods): # now that we're finished, make two clones of the stacks to solve both methods at once
                    restacked.append(dict(stacks))
        else:
            # after the diagram of the crates and the newline, every subsequent line is a move command like:
            # move(0) 6(1) from(2) 6(3) to(4) 5(5)
            # so let's just split it up by the spaces and take what we need
            command = line.split(' ')
            amount = int(command[1])
            remove_from = int(command[3])
            move_to = int(command[5])

            # Heck it, let's just do both answers at once.
            for i, restack in enumerate(restacked):
                prefix, suffix = restack[remove_from][:amount*-1], restack[remove_from][amount*-1:]
                if i == 0:      # in the 1st prob we have to move the crates one a time, reversing achieves the same thing
                    restack[move_to] = restack[move_to] + "".join(reversed(suffix))
                elif i == 1:    # in the 2nd prob we move the entire requested amount at once, so you can just slap it right on
                    restack[move_to] = restack[move_to] + suffix
                restack[remove_from] = prefix   # in either case, the original stack no longer has those
    print(restacked[0])
    print(restacked[1])

    # Find the secret message (each stack's top crate's letter in order from Stacks 1 through stacks_len)
    secret_messages = ['', '']
    
    for i, stacks_dict in enumerate(restacked):
        for stack in stacks_dict.values():
            secret_messages[i] += stack[-1]
    
    print(secret_messages)