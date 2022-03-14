from Tema1_LaboratSD import *

sorts =[counting_sort, merge_sort, radix_sort_orice_baza, quick_sort, counting_sort,shellsort]
# atentie: radixul are 2 parametrii... si baza


# functia pentru testare corectitudine sortare
def test_sortare(lista):
    if (all(lista[i] <= lista[i+1] for i in range(len(lista) - 1))):
        print("Sortare corecta.")
    else:
            print("Sortare_incorecta.")


names = ['radix_sort_orice_baza_16','radix_sort_orice_baza_10,', 'merge_sort', 'timsort', 'shellsort', 'quick_sort', 'counting_sort']

for max_nr, n in [(1000, 1000), (1000, 10000),(1000, 100000), (1000, 1000000), (1000, 10000000),(10000, 1000), (10000, 10000), (10000, 100000), (10000, 1000000), (10000, 10000000), (100000, 1000), (100000, 10000), (100000, 100000), (100000, 1000000), (100000, 10000000) ]:
  
    print(f"max_nr={max_nr}, n={n}")
    
    x = [random.randint(0, max_nr) for _ in range(n)]
  
# x = [23, 56, 0, 23, 85, 100, 200, 12, 32, 78, 90, 102] 
    for sort in sorts:
        timp = T(lambda:  sort(x))
        numar_iteratii = 1
        timp_per_nr_iteratii= round(timp.timeit(number= numar_iteratii),4)
        for i in range(7):
            print(f'{names[0]} per nr={numar_iteratii} de iteratii,{timp_per_nr_iteratii} sec')   

# OBS:
# partea de corectitudine a sortarii a fost rulata per fiecare sortare
# nu am rulat centralizat si partea aceasta fiindca dura mai mult sa reapeleze din nou functia
        # lista_output = sort(x, 16)
        # test_sortare(lista_output)
        
 