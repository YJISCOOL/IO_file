review = []
with open('IO_file-reviews_analytics.txt', 'r') as f1:
	for line in f1:
		review.append(line)
print (len(review))

#每一千筆就印出來
for x in range(0, len(review)):
	if (x+1) % 1000 == 0:
		print (x+1, review[x])
		print ("------")

#算留言的平均長度
sum_len = 0
for y in review:
	sum_len += len(y)
print ("留言平均長度為", sum_len/(len(review)))

'''
import statistics as stat
length_each_review = []
for y in range(0, len(review)):
	length_each_review.append(len(review[y]))
print (stat.mean(length_each_review))
'''

#篩選出長度<100的留言有幾筆
less_than_100 = []
#less_than_100 = [z for z in review if len(z) < 100] -> list comprehension
#z for z in review...第一個z是指我們要append(z)在清單裡面
for z in review:
	if len(z) < 100:
		less_than_100.append(z)
print ('一共有', len(less_than_100), '筆留言長度小於100。')

#篩選有good的留言
include_good = [] #include_good = [a for a in review if "very good" in a]
for a in review:
	if "very good" in a:
		include_good.append(a)
print ('一共有', len(include_good), '筆留言提到very good。')