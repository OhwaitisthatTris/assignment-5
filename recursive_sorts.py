# recursive_sorts.py
# merge sort, quicksort, hybrid sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: Tristan Crawford
from random import randint
 
 

def merge(left, right):
    merged = [None] * (len(left) + len(right))
    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged[merged_index] = left[left_index]
            left_index += 1
        else:
            merged[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1
   
    while left_index < len(left):
        merged[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1
   
    while right_index < len(right):
        merged[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1
    return merged
 
 

def merge_sort(lst):
    if len(lst) <= 1:
        return
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
 
    merge_sort(left)
    merge_sort(right)
 
    lst[:] = merge(left, right)
 
 

def quicksort_in_place(lst, start, end):
    if start >= end:
        return
   
    pivot_index = randint(start, end)
    lst[pivot_index], lst[end] = lst[end], lst[pivot_index]
 
    pivot = lst[end]
    boundary = start
   
    for i in range(start, end):
        if lst[i] < pivot:
            lst[i], lst[boundary] = lst[boundary], lst[i]
            boundary += 1
            
    lst[boundary], lst[end] = lst[end], lst[boundary]
 
    quicksort_in_place(lst, start, boundary - 1)
    quicksort_in_place(lst, boundary + 1, end)
   
 
def quicksort(lst):
    quicksort_in_place(lst, 0, len(lst) - 1)
 
 
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
 

def hybrid_sort(lst, threshold=10):
    if len(lst) <= threshold:
        insertion_sort(lst)
        return
 
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
 
    hybrid_sort(left, threshold)
    hybrid_sort(right, threshold)
 
    lst[:] = merge(left, right)
