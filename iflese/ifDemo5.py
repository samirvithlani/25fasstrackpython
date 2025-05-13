#multipule cond : logical operators:
#and or not
'''
    mult line comment
    and
    cond1  and cond2  result
      T          T     True
      T          F      False
      F         -       False
      
      every cond must satified...
      
      cond1  or cond2  result
        T        -       T
        F        T       T
        F        F       F
      
      atleast one cond sat...
      
'''
personAge = 59
isAlive = True

if personAge>=60 and isAlive == True:
    print("relese pension...")
else:
    print("dont relese...")    