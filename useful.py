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
    characters = [x for x in text]
    total_num_spaces = len(characters)-2 #it's -2 because we leave off the ends
    records = []
    for iteration in xrange(total_num_spaces):
        for num_whitespace in xrange(total_num_spaces):
            record = []
            for ind,elem in enumerate(characters):
                if iteration == 0:
                    if not ind == 0:
                        record.append(' ')
                    record.append(elem)
                    
                else:
                    if ind < num_whitespace:
                        if not ind == 0:
                            record.append(' ')
                    record.append(elem)
        records.append(record)
    return records

def fuzzer_by_whitespace(text):
    characters = [x for x in text]
    total_num_spaces = len(characters) #it's -2 because we leave off the ends
    records = []
    for iteration in xrange(total_num_spaces):
        for num_whitespace in xrange(total_num_spaces):
            greater_record = []
            lesser_record = []
            for ind,elem in enumerate(characters):
                if iteration == 0:
                    if not ind == 0:
                        greater_record.append(' ')
                    greater_record.append(elem)
                    
                else:
                    if ind > num_whitespace:
                        if ind != 0:
                            greater_record.append(' ')
                    greater_record.append(elem)
                    if ind < num_whitespace:
                        if ind != 0:
                            lesser_record.append(' ')
                    lesser_record.append(elem)
            if greater_record != []:
                records.append(greater_record)
            if lesser_record != []:
                records.append(lesser_record)
    
    final = []
    for i in records:
        if not i in final:
            final.append(i)
    return final

def fuzzer3_by_whitespace(text):
    """
    algorithm:
    start with the original string
    add spaces between each letter
    start at the last space and remove them one by one
    then decrease the number of spaces by one from the front and repeat previous step
    remove any duplicates along the way
    """
    characters = [x for x in text]
    total_num_spaces = len(characters) #it's -2 because we leave off the ends
    full_spaces = []
    for ind,elem in enumerate(characters):
        if ind != 0:
            full_spaces.append(' ')
        full_spaces.append(elem)


for i in fuzz_by_whitespace("Hello"):
    print i
