def heap_sort(a):
    def c1(a, n, i):
        m = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[i] < a[l]: m = l
        if r < n and a[m] < a[r]: m = r

        if m != i:
            a[i], a[m] = a[m], a[i]
            c1(a, n, m)

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        c1(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        c1(a, i, 0)
        
    return a