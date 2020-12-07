print(sum([len(set(group.replace('\n', ''))) for group in open('day6.txt').read().split('\n\n')]))
