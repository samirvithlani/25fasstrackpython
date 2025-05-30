even_or_odd = lambda x : "even" if x %2 ==0 else "odd"
print(even_or_odd(101))

maximum = lambda a, b : a if a> b else b
print(maximum(90,78))

pass_or_fail = lambda marks : "pass" if marks>=35 else "fail"
print(pass_or_fail(34))

check_number = lambda x: "Pos" if x>0 else("Zero" if x ==0 else "Neg")
print(check_number(1))


grade = lambda pers : "A" if pers>80 else ("B" if pers >70 else "C")
print(grade(87))