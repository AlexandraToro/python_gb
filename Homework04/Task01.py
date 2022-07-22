#    Вычислить число c заданной точностью d
#    Пример:
#   - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

def float_pi(n:float):
    count = 0
    while n < 1:
        n *= 10
        count += 1
    print(count)
    print(round(math.pi,count))    
    
n = float(input('Введите точность числа пи в формате (0.1 0.01 0.001 и тд.): '))

float_pi(n)