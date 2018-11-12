# 201358937 Tonge_Brandon-CA03.py
# October 2018
# This program uses a menu system to navigate the user to a nutrition adviser.
# This will accept the users inputs and then outputs the colour rating as per
# the Food Standards Agency.

# Main Function
def main():
    print("---Main Menu---")
    print("A - Selection")
    print("B - Iteration")
    print("C - Games")
    print("E - Extend")
    print("X - Exit Program")
    print("")
    choice = str.upper(input("Please select an option from the menu: "))

    # TEST
    # print(choice)

    # Function Selection
    if(choice == "A"):
        selection()

    elif(choice == "B" or choice == "C"):
        development()

    elif(choice == "E"):
        extended()

    elif(choice == "X"):
        exit()

    else:
        print("\nPlease enter a valid choice!\n")
        main()


#Selection Function
def selection():
    # User inputs
    print("\nPlease enter the values per 100g:")
    fat = float(input("Fat: "))
    saturates = float(input("Saturates: "))
    sugar = float(input("Sugar: "))
    salt = float(input("Salt: "))
    portion = float(input("Portion size in grams: "))

    # Fat Test
    if(fat <= 3):
        fat_class = "Green"

    elif(fat>3 and fat<=20):
        fat_class = "Amber"

    else:
        fat_class = "Red"

    # Saturates Test
    if(saturates <= 1.5):
        saturates_class = "Green"

    elif(saturates>1.5 and saturates<=5):
        saturates_class = "Amber"

    else:
        saturates_class = "Red"

    # Sugar Test
    if(sugar <= 5):
        sugar_class = "Green"

    elif(sugar>5 and sugar<=12.5):
        sugar_class = "Amber"

    else:
        sugar_class = "Red"

    # Salt Test
    if(salt <= 0.3):
        salt_class = "Green"

    elif(salt>0.3 and salt<=1.5):
        salt_class = "Amber"

    else:
        salt_class = "Red"

    # Fat Portion
    if(fat * (portion/100)>21):
        fat_class = "Red (Portion)"

    # Saturates Portion
    if(saturates * (portion/100)>6):
        saturates_class = "Red (Portion)"

    # Sugar Portion
    if(sugar *(portion/100)>15):
        sugar_class = "Red (Portion)"

    # Salt Portion
    if(salt *(portion/100)>2.4):
        salt_class = "Red (Portion)"

    # Outputs
    print(f"\nPortion size = {portion}g")
    print(f"{fat_class}: Fat {fat}g per 100g")
    print(f"{saturates_class}: Fat {saturates}g per 100g")
    print(f"{sugar_class}: Fat {sugar}g per 100g")
    print(f"{salt_class}: Fat {salt}g per 100g")
    print()



    '''TEST
    print(fat_class)
    print(saturates_class)
    print(sugar_class)
    print(salt_class)
    print(fat,saturates,sugar, salt, portion)'''

    main()

# Development Function
def development():
    print("\nFunction under development\n")
    main()

# Extended Function
def extended():
    print("\nExtended Requirements\n")
    main()

main()


