def main():
    list1 = list(map(int, input().split()))
    list1.sort()
    sum = list1[len(list1)//2] + list1[(len(list1)-1)//2]
    print(sum/2)

if __name__ == "__main__":
    main()

    #email: chase.a.yakaboski@dartmouth