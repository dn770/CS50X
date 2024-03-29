import csv
import sys


def main():

    # TODO: Check for command-line usage
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python tournament.py FILENAME")

    names = []
    # TODO: Read into memory from file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        # TODO: Read database file into a variable
        for row in reader:
            names.append(row)

    # TODO: Read DNA sequence file into a variable
    sequence = open(sys.argv[2], 'r')
    chars = sequence.read()

    dict_longest = dict()
    # TODO: Find longest match of each STR in DNA sequence
    for sub in names[0].keys():
        if sub == 'name':
            continue
        dict_longest[sub] = longest_match(chars, sub)


    # TODO: Check database for matching profiles
    for person in names:
        match = True
        for sub in person.keys():
            if sub == "name":
                continue
            if int(person[sub]) !=  dict_longest[sub]:
                match = False
                break
        if match:
            print(person['name'])
            return

    print("No match")
    return



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
