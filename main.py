# Homework
# Calculate the sum of 1/n^2 from 1 until it each extra term is not too large.
# 1. SUM = 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + 1/5^2 + etc + …
# 2. SUM = 1 + 0.25 + 0.111 + 0.0625 + 0.04 + etc + …
# Do not need to add ALL terms FOREVER you should only continue WHILE the terms are not too small. For example, maybe you stop add
# when the terms are less than 0.0000000000001

n = 1
sum = 0
Basel = 1

while Basel > 0.0000000000001:
    Basel = (1) / (n ** 2)
    n += 1
    sum += Basel

print("SUM: ",sum)

quit()