x = input("Please enter the length of the vector in kb for the initial restriction enzyme: ")
y = input("Please enter the length of the insert in kb[Enter 0 if there is none]: ")
z = input("How many more enzymes are there?: ")
h = []
j = 1
while j <= z:
    k = input("Enter the size in kb of each fragment, denote a ',' for each one: ")
    j += 1
    g = []
    g.append(k)
    h.append(g)
c = []
d = []
w = h[0]
try: 
  i = h[1]
except:
  print "calculating"
for b in h[0]:
  for a in h[0]:
      if a + b == x:
        c.append(a)
        c.append(b)
for l in h[0]:
    for q in h[0]:
        if l + q == y:
          d.append(l)
          d.append(q)
c.append(k[2:])
try:
  for r in i[1]:
    for e in i[1]:
        if r + e == max(w[0]):
            c.append(r)
            c.append(e)
except:
  print "no other enzyme used"
def First_Map_Slice():
    f = x - max(w[0])
    s = max(w[0])
    m = []
    m.append(f)
    m.append(s)
    return str(m)
def First_Map_Finish():
    if y == 0:
       return str(k[1:])
def Second_Map_Slice():
    return str(c)
def Plasmid_Generator():
 with open("Plasmid.html","w",) as web_page:
     web_page.write("<!doctype html>\n<html>\n<head>\n")
     web_page.write("<link rel='stylesheet' type='text/css' href='stylesheet.css' />")
     web_page.write("</head>\n<body>\n<p>\n")
     web_page.write("<div></div>")
     web_page.write("First, slice it into\n")
     web_page.write(First_Map_Slice())
     web_page.write("Then on one side, slice it into: \n")
     web_page.write(First_Map_Finish())
     if z > 1:
         web_page.write("Then on the other: \n")
         web_page.write(Second_Map_Slice())
     web_page.write("</p>\n</body>\n</html>\n")
     
Plasmid_Generator()
