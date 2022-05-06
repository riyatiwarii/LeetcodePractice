'''Count Items Matching a Rule'''
def countMatches(items, ruleKey, ruleValue):
    ruleIndex = ['type', 'color', 'name'].index(ruleKey)
    return len([item for item in items if item[ruleIndex] == ruleValue])
print(countMatches([["phone","blue","pixel"],["computer","silver","phone"],
                    ["phone","gold","iphone"]], ruleKey = "type",
                   ruleValue = "phone"))