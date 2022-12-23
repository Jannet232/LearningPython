tuple_1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
start = 2 #start position of slice
stop = 7 #end position of slice
step = 2
slice_object = slice(start, stop, step)
result = tuple_1[slice_object]
print(result)


