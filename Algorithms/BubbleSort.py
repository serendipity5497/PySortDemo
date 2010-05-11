from SortAlgorithm import SortAlgorithm

class BubbleSort(SortAlgorithm):
    def sort(self): 
        yield
        changed = True
        i = len(self.items.items)
        while changed:
            changed = False
            for j in range(1, i):
                if self.cmp.gtI(j-1, j):
                    self.items.swap(j-1, j)
                    changed = True
                    yield
            i -= 1
