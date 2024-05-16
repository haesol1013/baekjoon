while True:
    n = int(input())

    if n != -1:
        factor: list = [i for i in range(1, n) if n % i == 0]

        if n == sum(factor):
            factor = list(map(str, factor))
            print(n, '=', ' + '.join(factor))
        else:
            print(f"{n} is NOT perfect.")
    else:
        break
