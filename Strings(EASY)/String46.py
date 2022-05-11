def destCity(paths):
    d = dict(paths)
    for i in d.values():
        if i not in d.keys():
            return i
print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))