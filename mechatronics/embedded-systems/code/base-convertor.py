def main():
    from_number,from_base,to_base = eval(input("Number, From Base, To Base: "))
    from_number = from_number.upper()

    alphanum = ["0","1","2","3",
                "4","5","6","7",
                "8","9","A","B",
                "C","D","E","F",
                "G","H","I","J",
                "K","L","M","N",
                "O","P","Q","R",
                "S","T","U","V",
                "W","X","Y","Z"]

    pos = len(from_number) - 1
    number = 0

    for c in from_number:
        number += alphanum.index(c) * (from_base ** pos)
        pos -= 1

    to_number = ""
    
    while number != 0:
        digit = number % to_base
        number //= to_base
        to_number = alphanum[digit] + to_number
    
    print(f"To Number: {to_number}")

if __name__ == "__main__":
    main()