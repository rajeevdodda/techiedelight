def power(m, n):
    if n > 0:
        return m * power(m, n - 1)
    else:
        return 1


print(power(2, 5))


def power_best(m, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return power_best(m * m, n // 2)
        else:
            return power_best(m * m, (n - 1) / 2) * m


print(power_best(3, 12))
