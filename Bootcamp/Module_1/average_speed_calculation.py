# Taking input
s1 = float(input())
t1 = float(input())
s2 = float(input())
t2 = float(input())

d1 = s1 * t1
d2 = s2 * t2

total_distance = d1 + d2
total_time = t1 + t2

avg_speed = int(total_distance / total_time)

# Print the result
print(avg_speed)
