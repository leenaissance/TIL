import lotto_functoins

# lotto_functions.get_lotto()
# lotto_functoins.pick_lotto()
# lotto_functoins.amilucky()

result = lotto_functoins.amilucky(
    lotto_functoins.pick_lotto(),
    lotto_functoins.get_lotto(820),
)

print(result)


# 이상적인 함수 체킹
# from lotto_functoins import amilucky, pick_lotto, get_lotto
# result = lotto_functoins.amilucky(
#     lotto_functoins.pick_lotto(),
#      lotto_functoins.get_lotto(837),
# )
# print(result)

# # while True:
#     print(result)
#     if result <=5:
#         print(result)
#         print('나의 로또 번호는 ', lotto_functoins.pick_lotto())
#         print('837회 로또 번호는 ', lotto_functoins.get_lotto(837))

# for i in range(1, 51):ㄹ
#     if resut <=5:
#         print('나의 로또 번호는 ', lotto_functoins.pick_lotto())
#         print('837회 로또 번호는 ', lotto_functoins.get_lotto(837))
#         print(result) 