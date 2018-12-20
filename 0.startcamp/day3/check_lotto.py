import lotto_functoins

lotto_function.get_lotto()
lotto_functoins.pick_lotto()
lotto_functoins.amilucky()

result = lotto_functoins.amilucky(
    lotto_functoins.pick_lotto(),
    lotto_functoins.get_lotto(),
)

print(result)


# 이상적인 함수 체킹
from lotto_functoins import amilucky, pick_lotto, get_lotto
result = lotto_functoins.amilucky(
    lotto_functoins.pick_lotto(),
    lotto_functoins.get_lotto(837),
)
print(result)
