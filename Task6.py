#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no

b = input("Введите билет с шестизначным номером: ");
if int(b[0])+int(b[1])+int(b[2]) == int(b[3])+int(b[4])+int(b[5]):
    print("Это счастливый билет")
else:
    print("Обычный билет")
