import sys

# Check if a part number was provided as a command-line argument
if len(sys.argv) < 2:
  print('Please specify a part number (1 or 2) as a command-line argument')
  sys.exit(1)

# Get the part number from the command-line argument
part_num = int(sys.argv[1])

# Open the assignment map file
with open('assignment-map.txt', 'r') as f:
  # Read the file into a list of strings, one string per line
  assignment_pairs = f.readlines()

# Initialize a counter to keep track of the number of overlapping pairs
overlap_count = 0

# Iterate over each assignment pair
for assignment_pair in assignment_pairs:
  # Split the pair into two assignments
  assignments = assignment_pair.split(',')
  # Split each assignment into a start and end point
  start_1, end_1 = map(int, assignments[0].split('-'))
  start_2, end_2 = map(int, assignments[1].split('-'))

  # Check if the ranges overlap at all
  overlap = start_1 <= end_2 and start_2 <= end_1

  if part_num == 1:
    # If we're solving part 1, only count overlaps where one assignment fully contains the other
    if (start_1 <= start_2 <= end_2 <= end_1) or (start_2 <= start_1 <= end_1 <= end_2):
      overlap_count += 1
  elif part_num == 2:
    # If we're solving part 2, count all overlaps
    if overlap:
      overlap_count += 1

# Print the overlap count
print(overlap_count)
