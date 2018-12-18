scores = [45, 60, 52, 75, 90]

high_score = max(scores)
lowest_score = min(scores)
pass


first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# full  에 first와 second를 합쳐서 저장
# full_sorted 에 full을 오름차순으로 정렬해서 저장 
# *reverse_sorted 에 full을 내림차순으로 정렬해서 저장 

full = first + second
full_sorted = sorted(full)
reverse_sorted = sorted(full, reverse = True)

