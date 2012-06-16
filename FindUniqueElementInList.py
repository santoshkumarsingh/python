'''
1.Sort the scores.
2.Add items to the result list only when the item changes.
'''
def uniq(aList):

  aList.sort()

  result = []
  lastItem = None

  for item in aList:
    if item != lastItem:
      result.append(item)
      lastItem = item

  return result


print uniq([1,2,4,2,3,5,2,1,3])
