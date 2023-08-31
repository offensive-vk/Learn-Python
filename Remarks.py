def main():
    subject_marks = []  # List to store subject marks

    for i in range(5):
        subject_mark = int(input(f"Enter marks for subject {i+1}: "))
        subject_marks.append(subject_mark)

    total_marks = sum(subject_marks)
    print(f"Total Marks: {total_marks}")

    if total_marks <= 250:
        print("Remarks: Poor")
    elif total_marks >= 450:
        print("Remarks: Keep it up<Excellent>")
    elif total_marks >= 400:
        print("Remarks: Excellent")
    elif total_marks >= 350:
        print("Remarks: Very Good")
    elif total_marks >= 300:
        print("Remarks: Good")
    else:
        print("Remarks: Outstanding")

if __name__ == "__main__":
    main()
