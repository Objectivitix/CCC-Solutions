# https://www.aioicode.com/post/ccc-2020-s2
#
# Gets 15/15 points. And they have the overhead
# of the class. What in the world guys.
#
# TODO: Decode this and rewrite it.

class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


N = int(input())
M = int(input())
P = N*M
N += 1
M += 1

list1 = []
visited = []
#rlist = [0]*1000000
curlist = []
vcur = []
stacklist=[]
for i in range(M):
    curlist.append(0)
    vcur.append(True)
list1.append(curlist)
visited.append(vcur)

for i in range(N-1):
    curlist1 = [0]
    vcur1 = [True]
    S = input().split()
    for j in range(M-1):
        curlist1.append(int(S[j]))
        vcur1.append(False)
    list1.append(curlist1)
    visited.append(vcur1)

def handlexy(x1, y1):
    if x1 < N and y1 < M:
        if not visited[x1][y1]:
            if P == list1[x1][y1]:
                return True
            visited[x1][y1] = True
            stacklist.append(cell(x1, y1))
    if x1 < M and y1 < N:
        if not visited[y1][x1]:
            visited[y1][x1] = True
            if P == list1[y1][x1]:
                return True
            stacklist.append(cell(y1, x1))
    return False

def dfs2():
    if N-1 == 1 and M-1 == 1:
        return True
    if P == list1[1][1]:
        return True
    fn = cell(1,1)

    stacklist.append(fn)
    visited[1][1] = True
    while len(stacklist) > 0:
        cur = stacklist[-1]
        stacklist.pop()
        x = cur.x
        y = cur.y
        n = list1[x][y]

        start = int(n/(M-1))
        if start == 0:
            start = 1
        if start > 1:
            start -= 1
        end = N
        if end > n:
            end = n + 1
        i = start
        j = end
        while i <= j:
            if i < N:
                if n % i == 0:
                    x1 = i
                    y1 = int(n / i)
                    if handlexy(x1, y1):
                        return True
                    j = y1
            i += 1

    return False

if dfs2():
    print("yes")
else:
    print("no")
