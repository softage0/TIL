class PrimeFactors:
    def __init__(self, prime_factors=None):
        self.prime_factors = prime_factors or {}

    def get_prime_factors(self, n):
        if n < 2:
            return

        if n in self.prime_factors:
            return self.prime_factors[n]

        init = n
        factors = []

        while True:
            division = 0
            divider = 2

            while divider != n:
                division, reminder = divmod(n, divider)
                if reminder == 0:
                    break
                divider = divider + 1

            if divider == n:
                factors.append(divider)
                break

            factors.append(divider)
            n = division

            if n in self.prime_factors:
                factors = factors + self.prime_factors[n]
                break

        self.prime_factors[init] = factors
        return factors


pf = PrimeFactors()

for i in [6, 21, 12, 24, 8, 21 * 21]:
    print(pf.get_prime_factors(i))
