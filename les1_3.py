name,lastname=input("Имя Фамилия: ").split()
weight = int(input("Вес: "))
age = int(input("Возраст: "))

print(f"{lastname} {name} ваш вердикт - ")
if (50<weight<120) and (age<30):
    print ("хорошее состояние")
elif (50>weight or weight>120):
    if (30 < age <=40):
        print("следует заняться собой")
    elif (age>40):
        print("требуется врачебный осмотр")
    else:
        print("мы подумаем")
else:
    print("мы подумаем")




