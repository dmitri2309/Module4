from fake_math import divide as dvd_fake
from true_math import divide as dvd_true

result1 = dvd_fake(69, 3)
result2 = dvd_fake(3, 0)
result3 = dvd_true(49, 7)
result4 = dvd_true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
