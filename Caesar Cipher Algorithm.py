# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:43:44 2021

@author: Admin
"""

def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))
def main_loop():
    lis = input("Enter Text: ")
    print("".join(map(rotate_chr,lis)))
if __name__ == '__main__':
    main_loop()