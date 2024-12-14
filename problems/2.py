result = 0 

f_n = 0
f_n_minus_2 = 1
f_n_minus_1 = 2
while f_n < 4_000_000:
    f_n = f_n_minus_1 + f_n_minus_2
    f_n_minus_2 = f_n_minus_1
    f_n_minus_1 = f_n

    if f_n % 2 == 0:
        result += f_n

print(result + 2)