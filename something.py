import matplotlib.pyplot as plt
import math

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)

data = [0, 0.5, 1, 1.5, 2, 2.5,
        3, 3.5, 4, 4.5, 5, 5.5,
        6, 6.5, 7, 7.5, 8, 8.5,
        9, 9.5, 10, 10.5, 11,
        11.5, 12, 12.5, 13,
        13.5, 14, 14.5, 15]
temp1 = [6.48773984052241, 5.50310960547532, 4.19047508431161,
         17.480265650133, 38.156783622165, 37.1697020341714,
         40.0051495866111, 41.3885159919645, 64.5386848731954,
         81.3788118954882, 122.554168607724, 203.622134166765,
         264.516840109667, 377.207341853305, 530.27411941004,
         723.738467853529, 1047.60068001725, 1456.37114954243,
         2014.2907567928, 2805.83889544656, 3941.38897855703,
         5480.51641232266, 7657.94478592193, 10695.4883721303,
         14897.7373687716, 20786.8613399812, 29047.8310624743,
         40505.7636146707, 56528.4572682974, 78906.6426107198,
         110146.063624971]
a = 0.5
temp2 = []
temp2.append(temp1[0])
for i in range(1, len(temp1)):
    temp2.append(a * temp1[i] + (1 - a) * temp2[i - 1])


n = len(data)
# log_x = list(map(lambda x: math.log(x, 10), data))
log_y = list(map(lambda x: math.log(x, math.e), temp1))

sum_xy = 0
for i in range(len(data)):
    sum_xy += data[i] * log_y[i]
kv_sum_x = 0
for i in range(len(data)):
    kv_sum_x += data[i] ** 2

A = (n * sum_xy - sum(data) * sum(log_y) )/(n * kv_sum_x - sum(data) ** 2)
B = (sum(log_y) - A * sum(data) ) / (n)



temp3 = []
for el in data:
    temp3.append(math.e ** B * math.e ** (A * el))
print("a - {}. b - {}".format(A, math.e ** B))

k = a
plt.plot(data, temp1, "--", data, temp2, data, temp3)
plt.xlabel('Зелёная - аппроксимирующая прямая. Оранжевая - сглаживающая', fontsize=15, color='blue')
plt.ylabel('X', fontsize=15, color='blue')
plt.title('Y', fontsize=17)
plt.show()
print(temp3)