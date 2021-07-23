# Lists as a Data Structure, basically an array from javaScript
# ---------------------------------------------------------------

# >> > fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

list.append(x)  # Add an item to the end of the list
# >> > fruits.append('grape')
# >> > fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

# extend the list by appending all the items from the iterable
list.extent(iterable)
# fruits.extend('avocado')
# >> > fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'avocado']


# insert an item at index i, such that a.insert(0,x) inserts at the beginning and a.insert(len(a),x) is equivalent to a.append(x)
list.insert(i, x)

# remove the first item from the list whose value is equal to x.
list.remove(x)

# remove the item at the given position in the list, and return it. if no index is specified,
list.pop([i])
# a.pop() removes and returns the last item in the list
# >> > fruits.pop()
# 'pear'

list.clear()  # remove all items from the list

# return zer-based index in the list of the first item whose value is equal to x. The optional arguements start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. the returned index is computed relative to the beginning of the full sequence rather than the start argument.
list.index(x[, start[, end]])
# >> > fruits.index('banana')
# 3
# >> > fruits.index('banana', 4)  # Find next banana starting a position 4
# 6

list.count(x)  # return the nuimber of times x appears in the list
# >> > fruits.count('apple')
# 2
# >> > fruits.count('tangerine')
# 0

# Sort the items of the list in place (the arguments can be used for sort customization, see 'sorted()' for their explanation)
list.sort(*, key=None, reverse=False)
# >> > fruits.sort()
# >> > fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

list.reverse()  # reverse the elements of the list in place
# >> > fruits.reverse()
# >> > fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

list.copy()  # returns a shallow copy of the list

