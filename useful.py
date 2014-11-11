def remove_all(listing,x):
    while x in listing:
        listing.remove(x)
    return listing

def impose_ordering(ordering,listing):
    tmp = [x for x in listing if x in ordering]
    new_listing = []
    for elem in ordering:
        
