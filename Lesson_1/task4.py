import math
meaning_a = int(input("Value ax²: a= "))
meaning_b = int(input("Value bx: b= "))
meaning_c = int(input("Value c: c= "))

print(f'{meaning_a}x²+{meaning_b}x+{meaning_c}') # discriminant formula


discriminant_decision  = meaning_b**2-4*meaning_c*meaning_a
print(f'D {discriminant_decision}')

if discriminant_decision > 0:
    print(f'x1  {-meaning_b+math.sqrt(discriminant_decision)/(2*meaning_a)}')
    print(f'x2  {-meaning_b-math.sqrt(discriminant_decision)/(2*meaning_a)}')
    
if discriminant_decision == 0:
    print(f'x  {-meaning_b/(2*meaning_a)}')
    
if discriminant_decision < 0:
    print("Has no roots: 'D=0 and D>0'")
