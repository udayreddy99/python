def is_even(num):
  reminder = num%2
  if reminder==0:
    print"the num{0} is even".format(num)
    return True
  else:
    print"the num{0} is odd".format(num)
    return False
    
is_even(5)
