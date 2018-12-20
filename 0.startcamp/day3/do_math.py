print('!', __name__)
# import math_functions
# 
# math_functions.cube(5)
# math_functions.average([10,20,30])

import math_functions
print('import finished!')

print(math_functions.cube(5))
print(math_functions.average([10,20,30]))


# 가져올 모듈의 크기가 너무 클 경우(내용이 너무 많을 경우) from ~ import 를 쓰고, 메소드로 쓰지 않고 함수로 쓴다
from math_functions import cube, average
print(cube(5))
print(average([10,20,30]))
