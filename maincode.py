import math
import random
hoopxcoord1 = random.randint(5,15)
hoopWidth = round(random.uniform(1,6),5)
hoopxcoord2 = hoopxcoord1 + hoopWidth
hoopycoord1 = round(random.uniform(-15,15),5)
hoopycoord2 = hoopycoord1
yIntercept = random.randint(0,10)
print "The Y intercept is:", yIntercept
print "Left endpoint of horizontal hoop: (", hoopxcoord1, ",",  hoopycoord1, ")"
print "Right endpoint of horizontal hoop: (", hoopxcoord2, ",",  hoopycoord2, ")"
print
iteration = 0
for count in range(3):
  score = 0 
  form = random.randint(1,3)
  if form == 1:
    print ("Enter the equation in standard form:")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    if yIntercept == c:
      score += 1
    c = c - hoopycoord1
    x1 = round((-b - (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
    x2 = round((-b + (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
    if hoopxcoord1 < x1 and hoopxcoord2 > x1:
      score += 1
    if hoopxcoord1 < x2 and hoopxcoord2 > x2:
      score += 1
  elif form == 2:
    print ("Enter the equation in vertex form:")
    a = float(input("a:"))
    h = float(input("h:"))
    k = float(input("k:")) 
    b = -2*a*h
    c = a*h**2 + k
    if yIntercept == c:
      score += 1
    c = c - hoopycoord1
    x1 = round((-b - (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
    x2 = round((-b + (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
    if hoopxcoord1 < x1 and hoopxcoord2 > x1:
      score += 1
    if hoopxcoord1 < x2 and hoopxcoord2 > x2:
      score += 1
  elif form == 3:
    print ("Enter the equation in factored form:")
    a = float(input("a:"))
    m = float(input("m:"))
    n = float(input("n:"))
    b = - a*m - a*n
    c = a*m*n
    if yIntercept == c:
      score += 1
    c = c - hoopycoord1
    x1 = round((-b - (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
    x2 = round((-b + (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
    if hoopxcoord1 < x1 and hoopxcoord2 > x1:
      score += 1
    if hoopxcoord1 < x2 and hoopxcoord2 > x2:
      score += 1
  iteration += 1
  print
  if score >= 2:
    print ("You won!")
    break
  else:
    if iteration < 3:
      print("NOPE! Try again!")
    else: 
      print("You lost!")
