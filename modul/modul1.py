def topla(*arg):
    toplam = 0
    for i in arg:
        toplam += i
    return toplam


def cikar(sayi1, sayi2):
    return sayi1 - sayi2


def bol(sayi1, sayi2):
    return sayi1 / sayi2


def carp(sayi1, sayi2):
    return sayi1 * sayi2


def us_al(sayi1, sayi2):
    return sayi1 ** sayi2


def kokten_cikar(sayi):
    return sayi ** 0.5


def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi):
        sonuc *= i
    return sonuc
