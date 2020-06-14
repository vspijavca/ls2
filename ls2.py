# lesson 2 homework

#variables assign:

a, b, c, d, e = 1, -3, 4.567, True, False
k = ['a', 'b', 'c', 'd', 'e']
j = 0

# lest's check types of variabiles

for i in a, b, c, d, e:
    print("\nvar", k[j], "=", i, "is type of:", type(i))
    i += 1
    j += 1

# some logic here

if d and e:
    print("d and e are True")
else:
    print("\none is False and else is True, we don't know who is who")
if d != e:
    print("\nd and e variables are completly differnet")
else:
    pritn("They are equal")
if d or e:
    print("\nOne of them is True")

if a > 0 and b < 0:
    sum = a + b
print("\nsum=", sum)

print("\nThis (a + b == 0) is ", a + b == 0)

if a + b > 0:
    print("its True")
else:
    print('\na + b > 0 this is False')

print("\nEND of checking")