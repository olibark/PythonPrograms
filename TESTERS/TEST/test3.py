check = False
while check == False:
    square = ""
    while len(square) != 2:
        square = input("Enter grid reference (eg C2): ")
        square = square.upper()
        #end of paper
        allowed_columns = ["A", "B", "C"]
        allowed_rows = ["1", "2", "3"]
        if len(square) == 2:
            column = square[0]
            row = square[1]
            print ("Valid length")
        else:
            print ("Invalid length")
            break
        #if column != int(1, 3):
        #    print("invalid column")
        for i in range (len(allowed_columns)):
            if column == allowed_columns[i]:
                print ("Valid column")
                break
        else:
            print ("Invalid column")
            break
        for i in range (0, 3):
            if row == allowed_rows[i]:
                print ("Valid row number ")
                break
        else:
            print("Invalid row number")
            break