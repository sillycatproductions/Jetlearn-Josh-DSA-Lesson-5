wq = [543,29589857,456564564,1,18274897587459872958723,1987245]
print('Unsorted =', wq)

for i in range(0, len(wq)):
    for a in range(i, len(wq)):
        if wq[i] > wq[a]:
            wq[i], wq[a] = wq[a], wq[i]
            

print(' \n Sorted =', wq)



