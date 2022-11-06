
def solve(items):
    """
    Sort the given list of items in ascending order
    """
    solved = []
    def merge(left, mid, right):
        #for k in range(left, right):
        #    for i in range(left, right):
        #        if items[i] > items[i+1]:
        #            aux = items[i]
        #            items[i] = items[i+1]
        #            items[i+1] = aux
        
        for i in range(left, mid + 1):
            for j in range(mid, right + 1):
                if items[i] > items[j]:
                    aux = items.pop(j)
                    items.insert(i, aux)
            

    def merge_sort(left, right):
        # solve it here!
        if left < right:
            mid = (int) ((left + right) / 2)
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid + 1, right)
        
    merge_sort (0, len(items)-1)
    return