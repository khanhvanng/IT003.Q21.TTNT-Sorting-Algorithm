def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        l = a[:m]
        r = a[m:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while (i < len(l)) and (j < len(r)):
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        
        while (i < len(l)):
            a[k] = a[i]
            i += 1
            k += 1

        while (j < len(r)):
            a[k] = a[j]
            j += 1
            k += 1

    return a