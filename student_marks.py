name = input("Enter your name: ")

marks = []
for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Please enter marks between 0 and 100.")
else:
    total = sum(marks)
    average = total / len(marks)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Average:", round(average, 2))

    if all(mark >= 35 for mark in marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")
