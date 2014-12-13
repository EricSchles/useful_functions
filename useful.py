def remove_all(listing,x):
    while x in listing:
        listing.remove(x)
    return listing

def impose_ordering(ordering,listing):
    new_listing = []
    for elem in ordering:
        if elem in listing:
            new_listing.append(elem)
    if len(ordering) < len(listing):
        new_listing += listing[len(ordering)-1:]
    return new_listing


def fuzz_by_whitespace(text):
    """
    algorithm:
    start with the original string
    add spaces between each letter
    start at the last space and remove them one by one
    then decrease the number of spaces by one from the front and repeat previous step
    remove any duplicates along the way
    """
    characters = [x for x in text]
    original_num_spaces = characters.count(' ')
    total_num_spaces = len(characters) 
    full_spaces = []
    records = []
    records.append([x for x in text])
    for ind,elem in enumerate(characters):
        if ind != 0:
            full_spaces.append(' ')
        full_spaces.append(elem)
    records.append(full_spaces)
    text = full_spaces[:]
    while text.count(' ') > original_num_spaces:
        tmp = text
        while tmp.count(' ') > original_num_spaces:
            records.append(tmp)
            tmp = remove_last_space(tmp)
            if not tmp in records:
                records.append(tmp)

        text = remove_first_space(text)
    final = []

    for ind,record in enumerate(records):
        records_tmp = records[ind:]
        if records_tmp.count(record) > 1:
            continue
        else:
            final.append(record)
    final_text = []
    for i in final:
        final_text.append(''.join(i))
    return final_text
#The issue is that the actual spaces in the string are being removed as well.
def remove_first_space(text):
    text = ''.join(text)
    kth = text.find(" ")
    if text[kth+1] == ' ':
        if text[kth+2] == ' ':
            new_text = text[:kth] + " " + text[kth+3:]
        else:
            new_text = text[:kth] + " " + text[kth+2:] 
    else:
        new_text = text[:kth] + text[kth+1:]
    return [x for x in new_text]
     
def remove_last_space(text):
    text = ''.join(text)
    kth = text.rfind(" ")
    new_text = text[:kth] + text[kth+1:]
    return [x for x in new_text]


def file_len(fname):
    with open(fname,"r") as f:
        i = 0
        for i,l in enumerate(f):
            pass
    if i == 0:
        return i
    else:
        return i +1
