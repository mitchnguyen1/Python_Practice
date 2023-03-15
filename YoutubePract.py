weight = int(input("Weight: "))
type = input("(K)g or (L)bs: ")
ans = ""
cal = 0
if type == 'l' or type == 'L':
    ans = "Kg"
    cal = round(weight * 0.45, 2)
elif type == 'k' or type == "K":
    ans = "Lbs"
    cal = round(weight / 0.45, 2)
else:
    print("Enter a valid weight type. K or L ")

print(f"Weight in {ans}: {cal}")