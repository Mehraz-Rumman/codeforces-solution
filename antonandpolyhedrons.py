n=int(input())
p=[]

d={
    "Cube":6,
    "Tetrahedron":4,
    "Octahedron":8,
    "Dodecahedron":12,
    "Icosahedron":20
}
count=0
j=0
while j<n:
    p.append(input())
    count+=d[p[j]]
    j += 1
print(count)


