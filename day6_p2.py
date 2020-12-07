print(sum([len(set.intersection(*[set(i) for i in group.split('\n')])) for group in open('day6.txt').read().split('\n\n')]))
