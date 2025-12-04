
def pascal(rows):  #Функция создания рядов для треугольника Паскаля
    if rows == 0: #Если число рядов 0, то в выводе ничего не будет
        return [1]
    else:
        row = [1] #Задаем первый ряд, состоящий из единицы, просчитываем его значения, и добавляем в конце единицу
        previous_row = pascal(rows - 1) 
        for i in range(len(previous_row) - 1): 
            row.append(previous_row[i] + previous_row[i + 1])    
        row.append(1)
        return row

def main(): #основная функция, ввод числа рядов, вывод
    rows = int(input("Из скольких рядов построить треугольник Паскаля?:"))
    for i in range(rows):
        print(pascal(i)) 

if __name__ == "__main__": #Файл выполнится в случае если он самостоятельный файл
    main()  


#https://it.kgsu.ru/Python_Recursion/pythonRecursion073.html