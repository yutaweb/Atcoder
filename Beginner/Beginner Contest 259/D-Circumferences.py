N = int(input())
Sx, Sy, Tx, Ty = map(int, input().split())
points = [list(map(int, input().split())) for val in range(N)]


class UnionFind:
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)


def dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2


ti = 0
si = 0

for i in range(N):
    """
    s, tが与えられた円の何番目に属しているかを判定する為に使用する。
    """
    if dist(Sx, Sy, points[i][0], points[i][1]) == (points[i][2])**2:
        si = i
    if dist(Tx, Ty, points[i][0], points[i][1]) == (points[i][2])**2:
        ti = i

uf = UnionFind(N)

for i in range(N):
    for j in range(i):
        d = dist(points[i][0], points[i][1], points[j][0], points[j][1])
        r1 = points[i][2]
        r2 = points[j][2]

        if d > (r1 + r2)**2:
            continue
        if d < (r1 - r2)**2:
            continue

        uf.unite(i, j)


if uf.same(si, ti):
    print("Yes")
else:
    print("No")
