#İleri seviye sayı veri tipleri ve metodları
liste = [-4.3,-4,1,2,3,4,5]
print(min(liste))
print(max(liste))
print(sum(liste))
liste1 = [2,2]
print(pow(2,2))

#İleri Seviye Stringler  ve metodları
print(("PYThon").lower())
a = "kemal"
print(a.upper())


b = "Aa"
c="a"
d="kkk"
print(b.replace(c,d))
print(a.startswith("ke"))
print("python".endswith("on"))

liste3 = "c-python-php-js"
print(liste3.split("-"))

liste4 = ["Kemal","Ayhan"]
a = "/".join(liste4)
print(a)


python = "<<<<<python<<<<<"
print(python.rstrip("<"))
print(python.lstrip("<"))

print("Python Programlama".count("m"))

print("Python Programlama".find("hon"))
print("Python Programlama".rfind("a"))

print("Mercedes".count("e",2 ))
print("------------------------")

# İleri Seviye Kümeler ve metodları
l = ["python","php","python","java"]
l = set(l)
print(l)
x = {1,2,3}
x.add(4)
x.add(-1)
print(x)

#difference
y = {1,2,3,5,6}
print(y)
print(x.difference(y))
print(y.difference(x))
y.difference_update(x)
print(y)

#intersection
y = {1,2,3,5,6}

print(x.intersection(y))

k = {1,2,3,4}
d = {5,6,7}
print(k.intersection(d))
print(k.union(d))
print(k.isdisjoint(d))
print(k.issubset(d))

k.update(d)
print(k)

#ileri seviye listeler ve metodları




