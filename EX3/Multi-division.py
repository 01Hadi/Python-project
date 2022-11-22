def EX3_4 (a, b, c):
  """
(int, int, int) -> string
return True if 2 to the power b to multiply a is divisible by c
  """
    if a * 2**b % c == 0:
        print('True')
    else:
        print('False')
        
