def distance(strand_a, strand_b):
    c=0
    if len(strand_a) == len(strand_b):
        for x in range(len(strand_a)):
            if strand_a[x] != strand_b[x]:
                c = c +1
    else:
        raise ValueError("ValueError")
    return c
