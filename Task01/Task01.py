#Задача №1.
#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
#километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

speedCar = int(input('Введите какое расстояние в км проезжает машина за день:'))

routeCar = int(input('Введите маршрут для машины: '))

daysRouteCar = round(routeCar / speedCar + 0.5)

print(daysRouteCar)




#Второе решение:

#daysRouteCar = (speedCar + routeCar - 1) // speedCar


#Round(число, до скольки нулей округлить) Если не писать до скольки округлять, то функция Round будет округлять математически - например:
#															7.5 - 8
#															73. - 7


