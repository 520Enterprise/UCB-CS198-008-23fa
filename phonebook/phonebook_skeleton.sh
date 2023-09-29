#!/bin/bash

PHONEBOOK_ENTRIES="bash_phonebook_entries"


if [ "$#" -lt 1 ]; then
    exit 1

elif [ "$1" = "new" ]; then
    # YOUR CODE HERE #
    if [ "$#" -ne 3 ]; then
        echo "Usage: ./phonebook.sh new <name> <number>"
        exit 1
    else
        echo "$2 $3" >> $PHONEBOOK_ENTRIES
    fi

elif [ "$1" = "list" ]; then
    if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
        echo "phonebook is empty"
    else
        # YOUR CODE HERE #
        sed -n 'p' $PHONEBOOK_ENTRIES
    fi

elif [ "$1" = "lookup" ]; then
    # YOUR CODE HERE #
    if [ "$#" -ne 2 ]; then
        echo "Usage: ./phonebook.sh lookup <name>"
        exit 1
    else
        sed -n "/$2 [0-9]/p" $PHONEBOOK_ENTRIES
    fi

elif [ "$1" = "remove" ]; then
    # YOUR CODE HERE #
    sed -i "/$2 [0-9]+/d" $PHONEBOOK_ENTRIES

elif [ "$1" = "clear" ]; then
    # YOUR CODE HERE #
    sed -i 'd' $PHONEBOOK_ENTRIES

else
    # YOUR CODE HERE #
    echo "Usage: ./phonebook.sh <new|list|lookup|remove|clear> <name> <number>"
fi