import math 
from timeit import Timer as T
import random

# '''
# Implementați următorii 3 algoritmi de sortare:
# 1: RadixSort (ideal in mai multe baze inclusiv 2^16)
# 2: MergeSort○
# 3: ShellSort
# 4: Inca 2 la algere dintre care unul in O(n logn) sau bazat pe numarare
#     --> Eu am ales Counting sort (prin numarare) si Quick sort (O(n logn))
# '''
#____________________________________________________________________________
# #SORTAREA BUILT-IN, din Python
def timsort(x):
    return sorted(x);

# #_____________________________________________________________________________
# #RADIX SORT (aplicabil in orice baza- var 1)--> are in spate un ocounting sort
def counting_sort1(lista_input, digit, baza):
#e un vector de frecventa pentru cifrele numerelor din input
    frecv = [0]*int(baza) 
    
    lista_output = [0]*len(lista_input) #initializare lista de output
 
    # fac un counting la nivel de cifre per numere din input
    for elem in range(0, len(lista_input)):
        # extrag cifra din element, in functie de baza acelor elemente
        digit_elem = (lista_input[elem]// baza**digit) % baza
    # deci la valoarea lui frecv[digit_elem] am frecventa lui digit_elem 
        frecv[digit_elem] = frecv[digit_elem] + 1 
    

    # imi suprascriu tabela de frecvente cu o frecventa cumulativa adica:
    # in acest mod o sa vad cate numere contin cifre mai mici decat indexul din frecv=elem
    # frecventa cumulativa va fi index pentru tabela de output, la final si ma va ajuta
    for elem in range(1,baza):
        frecv[elem] = frecv[elem] + frecv[elem-1]
        
    # apoi parcurg lista de input in sens invers si imi completez tabela de output
    for j in range(len(lista_input)-1, 0-1, -1): #to count down (go through A backwards)
        digit_elem = (lista_input[j]//baza**digit) % baza  
        # extrag cifra care im trebuie ca sa conectez mai departe tabela de frecvente  cumulative
        
        #pe masura ce competez outputul, scad tabela de frecvente
        frecv[digit_elem] = frecv[digit_elem] -1 
        lista_output[frecv[digit_elem]] = lista_input[j]

    return lista_output


def radix_sort_orice_baza(lista_input, baza):
    #radix- cu sensul de baza :) 
    
#trebuie sa stabilesc in functie de baza, 
# care sunt cifrele ce vor fi folosite drept index in counting-ul mai sus
# iau caa reper cel mai mare numar din input pentru a vedea lungimea numarului
    maxim = max(lista_input)
   
    lista_output = lista_input
    
    # trebuie sa vad nr de cifre posibile in functie de baza
    cifre = int(math.floor(math.log(maxim, baza)+1))
    
    for cifra in range(cifre):
        lista_output = counting_sort1(lista_output,cifra,baza)

    return lista_output


# ___________________________________________________________________________________
# #RADIX SORT- binar cu shiftare de biti
# #fac parcurgerea bit cu bit din numarul meu, cu ajutorul unei masti si a lui AND pe biti
# #imi returneaza valoarea bit-ului de pe pozitie_bit din numarul respectiv
# def bitul_urmarit(number, pozitie_bit):
#     mask = 1 << pozitie_bit  # am 1 shiftat stanga cu pozitia bitului pe care il urmaresc la counting
#     if number & mask != 0:
#         return 1
#     return 0
# '''
# Asadar functia de mai sus ma ajuta sa obtin succesiv:
# 1 << 0  →  0000 0001   # pt bitul de pe poz 0
# 1 << 1  →  0000 0010   # pt bitul de pe poz 1
# 1 << 2  →  0000 0100   # pt bitul de pe poz 2
# ...
# 1 << 7  →  1000 0000   # pt bitul de pe poz 7
# '''

# def counting_sort2(lista_input, pozitie_bit):
# # imi grupez elementele din lista de input in functie de pozitia bit-ului urmarit
# # nu-mi sorteaza final lista de input dar imi sorteaza totusi in functie de un bit specific 
# # si pot folosi asta mai departe la radix (am grupurile pe 0 si 1 construite in acest mod)


# # totul se leaga de pozitia specifica a unui bit si in list frecv:vect de frecv voi avea:
#     # cate elem cu 0 pe bitul respectiv am: frecv[0]
#     # cate elem cu 1 pe bitul respectiv am: frecv[1]
#     frecv = [0, 0]
#     for elem in lista_input:
#         frecv[ bitul_urmarit(elem, pozitie_bit) ] += 1
       
# #indici[0], tabela indici imi retine unde ar trebui sa pun urmatorul elem cu 0 pe pozitia bitului pe care il urmaresc
# #imi ia toate elem  cu 0 pe acel bit (la inceput--> index 0) dupa care aseaza elem cu 1 pe acel bit position

#     indici = [0, frecv[0]]

#     sort_list = [0] * len(lista_input)

#     for elem in lista_input:
#         valoare_bit_elem = bitul_urmarit(elem, pozitie_bit)
# # pun elem in lista finala a fi sortata in functie de val bit-ului
#         sort_list[indici[valoare_bit_elem] ] = elem
        
# # Am grija ca urmatorul elem care are aceeasi valoare de bit 
# # sa vina dupa primul elem deja adaugat cu aceeasi val de bit, deci ma duc pe urmat index
#         indici[valoare_bit_elem] += 1
#     return sort_list

# def radix_sort_binar(lista_output):
#     maximul = max(lista_output)
#     # max = 0
#     # for elem in lista:
#     #     if elem.bit_length() > max:
#     #         max= elem.bit_length()
#     #     max= max
#     bits_lungime = int(maximul.bit_length())
    
# # Folosesc counting sort pt a aranja nuemerele de la LSB la MSB
#     for pozitie_bit in range(bits_lungime): # am considerat numerele pe atatia biti in functie de context
#         lista_output = counting_sort2(lista_output, pozitie_bit)
#     return lista_output

# #________________________________________________________________________________________________________
# #MERGE SORT
def merge_sort(lista_input):
    if(len(lista_input)>1):
        mediana = len(lista_input)//2
        left = lista_input[:mediana]
        right = lista_input[mediana:]
        
    # avem apelare recursiva pt ca vom continua sa divizam 
    # pana cand ajungem la elem individual de la care incepem sortarea si apoi facem acel merge sortat
        
        merge_sort(left)
        merge_sort(right)   
       
    #avem 2 iteratori pentru listele de left si right    
        l = 0 
        r = 0
         
    # poz este contorul principal pentru lista finala
        poz = 0
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                lista_input[poz] = left[l]
                l +=1
            else:
                lista_input[poz] = right[r]
                r +=1
            poz +=1
            
            
        while l < len(left):
            lista_input[poz] = left[l]
            l +=1
            poz +=1
        
        while r < len(right):
            lista_input[poz] = right[r]  
            r +=1
            poz +=1
    return(lista_input)

# #_________________________________________________________________________________________________

# # SHELL SORT
# Am folosit, Shell’s original sequence: N/2, N/4, …,  pe parte de distante intre elemente
def shellsort(lista_input): 
    n = len(lista_input)
    distanta = n >> 1  # impartirea la 2 ca parte ubtreaga luata
    while distanta > 0:  #distanta poate ajunge la min 1 elem conform secventei Shell considerate
        for i in range(distanta,n):  # ma uit de la o anumita distanta incolo
            temp = lista_input[i]  # si memorez val pe acel index
            j = i 
            while  j >= distanta and lista_input[j-distanta] > temp: 
                lista_input[j] = lista_input[j-distanta] 
                # prin  lista_input[j-distanta], ma duc i stanb=nga  pt comparatie si fac swap-ul aici
                j = j - distanta 
            lista_input[j] = temp 
        distanta = distanta >> 1

    return lista_input

# #__________________________________________________________________________________________________________
# #COUNTING SORT
def counting_sort(lista_input):
    # Are in spate tabela de frecventa
    # counting[0] are nr de zerouri din input
    # counts[3] contine frecventa pe 3 din input

    maxim_nr= max(lista_input)
    counting = [0] * (maxim_nr + 1)
    
    for elem in lista_input:
        counting[elem] += 1

    # Voi suprascrie tabela de frecventa stfel incat:
    # de pilda counting[2] sa imi arate indexul pentru urmatorul elem de 2 si nu cati de 2 inputul meu are
    
    num_item = 0
    for i, count in enumerate(counting):
        counting[i] = num_item
        num_item += count

    lista_output = [None] * len(lista_input)

    for elem in lista_input:
        lista_output[ counting[elem] ] = elem

        # ma asigur ca un elem cu aceeasi valoare este pus imediat dupa alem anterior identic lui pozitionat 
        counting[elem] += 1

    return lista_output

# #_____________________________________________________________________________________________

# #QUICK SORT
def quick_sort(lista_input):
    if len(lista_input) <= 1:
        return lista_input
    else:
        less = []
        more = []
        # last_elem = len(lista_input) - 1
        # first_elem = lista_input[0]
        mediana = len(lista_input)//2
        pivot = lista_input[mediana] #pot alege diferit aici pivotul (first, last sau median), eu am testat pe mediana
        for i in lista_input:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        
        return less + [pivot] * lista_input.count(pivot) + more 
    #assamblez bucatile, am grija in situatia in care am pivotul repetat de mai mutle ori
    
    
    

