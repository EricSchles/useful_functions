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
    for i in characters:
        between_all.append(' ')
        between_all.append(i)
    return between_all
