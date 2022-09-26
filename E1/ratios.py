import fractions
def main():

    n = int(input())
    x = list(map(int, input().split()))

    # print n-1 lines
    # each line contains A/B in reduced form
    # format: "1/2"
    ratio = [0]
    for i in range(n - 1):
        if(ratio[0] == 0):
            ratio[0] = x[i] / x[i + 1]
        else:
            ratio.append(ratio[i-1] * x[i] / x[i + 1])
    for r in ratio:
        print(str(fractions.Fraction(r).limit_denominator(10).numerator) + "/" + str(fractions.Fraction(r).limit_denominator(10).denominator))

if __name__ == "__main__":
    main()
