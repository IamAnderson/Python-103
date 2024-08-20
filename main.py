age = int(input("How old are you tho?? :"))

if age >= 18:
    print("Ohh, you are off age, nice")
    ans = input("Do you like white chocolate ?? :")
    if ans == "Yes":
        print("Uhmm, subarashi,, hehe")
    elif ans == "No":
        print("Hmm, okay, what do you like then")
    else:
        print("Answer Yes or No")
else:
    print("You don't belong here kid")