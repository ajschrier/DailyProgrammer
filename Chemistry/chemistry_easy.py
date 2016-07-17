def checkValidity(name, symbol):

    #Condition 1
    if len(symbol) != 2:
        return False

    #Condition 4 quick check
    if symbol[0].lower()==symbol[1].lower():
        count = 0
        for letter in name:
            if letter == symbol[0].lower():
                count += 1
        if count >= 2:
            return True

    #Condition 2
    for letter in symbol:
        if letter.lower() not in name.lower():
            return False

    # Condition 3
    idx=0
    for letter in name.lower():
        if letter == symbol[0].lower():
            substring = name[idx+1:]
            if symbol[1] in substring:
                return True
        else:
            idx += 1