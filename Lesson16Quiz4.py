# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

def split_string(source,splitlist):
    # go through source until any of the split list characters
    words = []
    starting_position = 0
    for item in source:
    # for each character in a string
    # remember that you can loop through strings as well
        if item in splitlist:
            #if the character is in the splitlist
            hold = item
            hold_position = source.find(hold,starting_position)
            if hold_position == starting_position:
                pass
            append_this = source[starting_position:hold_position]
            words.append(append_this)
            starting_position = hold_position + 1
    return words

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']