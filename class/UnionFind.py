# https://algo-method.com/descriptions/136
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
    
    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]
        
    # x と y が同じグループに属するか
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]