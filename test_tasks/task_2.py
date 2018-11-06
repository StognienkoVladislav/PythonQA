
def maskify(mask):
    return mask if len(mask) < 5 else '#'*len(mask[:-4]) + mask[-4:]
