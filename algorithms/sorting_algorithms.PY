#!/usr/bin/env python3
import time
import os

def selection_sort(a):
    for i in range(len(a) - 1):
        minj = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]

def insertion_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x

def read_numbers(path):
    with open(path, 'r') as f:
        return [int(x) for x in f.read().split()]

def main():
    PASTA = "algorithms/Instances_for_sorting_algorithms"  
    if not os.path.isdir(PASTA):
        print(f"Pasta não encontrada: {PASTA}")
        return

    for nome in sorted(os.listdir(PASTA)):
        if not nome.endswith(".in"):
            continue
        caminho = os.path.join(PASTA, nome)
        nums = read_numbers(caminho)

        t0 = time.time()
        selection_sort(nums.copy())
        t1 = time.time()
        insertion_sort(nums.copy())
        t2 = time.time()

        print(f"\nArquivo: {nome}")
        print(f"  SelectionSort: {t1 - t0:.4f} s")
        print(f"  InsertionSort: {t2 - t1:.4f} s")
        vencedor = "SelectionSort" if (t1 - t0) < (t2 - t1) else "InsertionSort"
        print(f"  → {vencedor} foi mais rápido")

if __name__ == "__main__":
    main()
