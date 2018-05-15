# 6 5
# 1 2 2 3 4 5

# 5 6 4 1 2


from sys import stdin
from collections import deque

n, x = (map (int, stdin.readline ().strip ().split (' ')))
a = (list (map (int, stdin.readline ().strip ().split (' '))))

# a_indexed=np.array(deque())
# a_dequeued=np.array(deque())
a_indexed = deque ()

for i, j in enumerate (a):
    # a_indexed=np.append(a_indexed,[j,i+1])
    a_indexed.append ([j, i + 1])
print ('a_indexed={}'.format (a_indexed))

for i in range (0, x, +1):
    a_dequeued = deque ()
    print ('============{}==========='.format (i))
    print ('initial a_indexed={}'.format (a_indexed))
    print ('initial a_dequeued={}'.format (a_dequeued))

    for j in range (0, min (x, len (a_indexed))):
        a_dequeued.append (a_indexed.popleft ())

    print ('a_dequeued=', a_dequeued)
    max_this_time = max (a_dequeued, key=lambda x: x[0])
    print ('max this time={}'.format (max_this_time))
    max_index = max_this_time[1]

    print ('Index={}'.format (max_index))

    del (a_dequeued[a_dequeued.index(max_this_time)])

    for k in range (0, len (a_dequeued), +1):
        a_dequeued[k][0] = max(a_dequeued[k][0] - 1, 0)
        a_indexed.append (a_dequeued[k])
