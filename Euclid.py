
def euclidus_algorithmus(numb1, numb2):
    if numb2 == 0:
        return numb1
    else:
        return euclidus_algorithmus(numb2, numb1 % numb2)
    
def main():
    numb1 = int(input("Введите первое число:"))
    numb2 = int(input("Введите второе число:"))
    print(euclidus_algorithmus(numb1, numb2))

if __name__ == '__main__':
    main()