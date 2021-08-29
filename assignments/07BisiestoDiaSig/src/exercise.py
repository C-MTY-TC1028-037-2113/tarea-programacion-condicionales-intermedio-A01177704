def main():
    #escribe tu código abajo de esta línea
    year = int(input("Año: "))
    month = int(input("Mes: "))
    day = int(input("Día: "))
    # Meses con 31 dias: 1, 3, 5, 7, 8, 10, 12
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day == 31:
            day = 1
            if month == 12:
                month = 1
                year = year + 1
            else:
                month = month + 1
        else:
            day = day + 1
    # Meses con 30 dias: 4, 6, 9, 11
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day == 30:
            day = 1
            month =month + 1
        else:
            day = day + 1
    # Mes 2 puede tener 28 o 29 dias
    else:
        if day == 29 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            day = 1
            month = month + 1
        elif day == 28:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                day = day + 1
            else:
                day = 1
                month = month + 1
        else:
            day = day + 1
    print(year)
    print(month)
    print(day)

if __name__=='__main__':
    main()
