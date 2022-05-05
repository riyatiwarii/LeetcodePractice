'''Final Value of Variable After Performing Operations'''
def finalValueAfterOperations(operations):
    operdict = {'++X': 1, 'X++': 1, '--X': -1, 'X--':-1}
    return sum(operdict[op] for op in operations)
print(finalValueAfterOperations(["--X","X++","X++","X--"]))

