array = [];tree = [int(0)]*100001


def built(node,beg,end):
    if beg == end:
        tree[node] = array[beg]
        return
    left = node*2
    right = left+1
    mid = (beg+end)//2
    built(left, beg, mid)
    built(right, mid+1, end)
    tree[node] = tree[left]+tree[right]


def query(node, beg, end, rang1, rang2):
    if end < rang1 or rang2 < beg :
        return 0
    if beg >= rang1 and end <= rang2:
        return tree[node]
    left = node * 2
    right = left + 1
    mid = (beg+end) // 2
    x = query(left, beg, mid, rang1, rang2)
    y = query(right, mid+1, end, rang1, rang2)
    return x+y


array = list(map(int,input().split()))
n = len(array)
built(1, 0, n-1)

querynumber = int(input())

for i in range(querynumber):
        rang1, rang2 = map(int, input().split())
        print(query(1, 0, n - 1, rang1 - 1, rang2 - 1))

