inp = [line.strip() for line in open('input', 'r')]


def parse(line):
    (s, e) = line.split('-')
    return s, e


# smalls - already small caves visited
# dup - flag indicating whether a small cave was already visited twice
# a - accumulate the whole path (just for printing it..)
def search(cave, smalls: list, dup: int, a: list):
    global cnt
    global paths
    if cave.lower() == cave:
        smalls.append(cave)
    if cave == 'end':
        cnt += 1
        return
    starts = [x for x in paths if x[0] == cave or x[1] == cave]
    for si in starts:
        ncave = si[1] if si[0] == cave else si[0]  # next cave
        ndup = dup  # next duplicate flag
        if ncave in smalls:
            if ndup == 0 and ncave not in ['start', 'end']:
                ndup = 1
            else:
                continue
        na = a.copy()
        na.append(ncave)
        search(ncave, smalls.copy(), ndup, na)


lst = list(map(parse, inp))
paths = set(lst)

cnt = 0
search('start', [], 1, ['start'])
print(cnt)  # 3298

cnt = 0
search('start', [], 0, ['start'])
print(cnt)  # 93572
