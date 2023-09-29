#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        # YOUR CODE HERE #
        name = " ".join(sys.argv[2:-1])
        number = sys.argv[-1]
        with open(PHONEBOOK_ENTRIES, 'a') as f:
            f.write("{} {}\n".format(name, number))

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #
            with open(PHONEBOOK_ENTRIES, 'r') as f:
                for line in f.readlines():
                    print(line.strip())
    
    elif sys.argv[1] == "lookup":
        # YOUR CODE HERE #
        name = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            for line in f.readlines():
                if name in line:
                    print(line.strip())

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lines = f.readlines()
        with open(PHONEBOOK_ENTRIES, 'w') as f:
            for line in lines:
                name_in_line = " ".join(line.split()[:-1])
                if name_in_line != name:
                    f.write(line)


    elif sys.argv[1] == "clear":
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'w') as f:
            f.write("")

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            # YOUR CODE HERE #
            if lookup:
                print(lookup.strip())


if __name__ == "__main__":
    main()