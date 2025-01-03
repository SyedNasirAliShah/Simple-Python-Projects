names = []
rolls = []
fees = []
paids = []
char = 'y'
roll = 0
name = ''
fee = 0
paid = ''
print('\tWELCOME TO THIS PROGRAM.')
while True:
    print('\n\t1. Adding students')
    print('\t2. Removing students')
    print('\t3. Updating Records')
    print('\t4. All Record')
    choice = int(input('\n\tEnter your choice from menu:'))
    match choice:
        case 1:
            while True:
                name = input("\tEnter Student's Name:")
                names.append(name)
                roll = int(input("\tEnter Student's Roll No:"))
                rolls.append(roll)
                fee = int(input("\tEnter Student's Fee:"))
                fees.append(fee)
                paid = input('\tFee is paid or not (Y/N):')
                paids.append(paid)
                with open("studentsFile.txt", "a") as f:
                    # f.write("NAME \t ROLL_NO \t FEE \t PAID(Y/N)\n")
                    f.write(f"{name}  \t  {roll}   \t     {fee}  \t   {paid}\n")
                ch = input('\tWould you want to add another student: (Y/N):')
                if ch != 'Y' and ch != 'y':
                    break
        case 2:
            l = len(names)
            l2 = len(rolls)
            if l == 0:
                print('\tEmpty students record.')
            else:
                roll = int(input('\tEnter the roll no of student you want to remove:'))
                i = 0
                while i < l:
                    if roll == rolls[i]:
                        rolls.remove(rolls[i])
                        names.remove(names[i])
                        fees.remove(fees[i])
                        paids.remove(paids[i])
                        # with open("studentsFile.txt", "a") as f:
                        #     f.
                        print('\tRecord Removed Successfully...')
                        break
                    else:
                        i += 1
                else:
                    print(f"\t{roll} Roll No not exist in students record!")
        case 3:
            l = len(names)
            l2 = len(rolls)
            if l == 0:
                print('\tEmpty students record.')
            else:
                roll = int(input('\tEnter the roll no of student you want to update:'))
                i = 0
                while i < l:
                    if roll == rolls[i]:
                        rolls.remove(rolls[i])
                        names.remove(names[i])
                        fees.remove(fees[i])
                        paids.remove(paids[i])
                        name = input('\tEnter new name:')
                        names.append(name)
                        roll = int(input('\tEnter new Roll No:'))
                        rolls.append(roll)
                        fee = int(input('\tEnter Fee:'))
                        fees.append(fee)
                        paid = input('\tFee is paid or not (Y/N):')
                        paids.append(paid)
                        print('\tRecord Updated Successfully...')
                        break
                    else:
                        i += 1
                else:
                    print(f"\t{roll} Roll No not exist in students record!")
        case 4:
            l = len(names)
            l2 = len(rolls)
            i = 0
            if l == 0:
                print('\tEmpty students record...')
            else:
                print(f"\tNAME \t ROLL NO \t FEE \t PAID(Y/N)")
                while i < l:
                    print(f"\t{names[i]} \t {rolls[i]} \t\t {fees[i]} \t\t {paids[i]}")
                    i += 1
            break
        case _:
            print('\tINVALID CHOICE!')
    char = input('\tWould you like to go to main menu(Y/N):')
    if char != 'y' and char != 'Y':
        break