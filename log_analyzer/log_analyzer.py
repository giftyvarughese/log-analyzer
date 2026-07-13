filename = input("enter the log file name : ")
success = 0
failed = 0
try:
    with open(filename, "r") as file:
        for line in file:

            if "Login Success" in line:
                success = success + 1

            if "Login Failed" in line:
                failed = failed + 1

    print("\n========== LOG ANALYSIS REPORT ==========")
    print("Total Log Entries :", success + failed)
    print("Successful Logins :", success)
    print("Failed Logins     :", failed)
    total = success + failed
    percentage = (failed / total) * 100

    print(f"Failed Login Percentage : {percentage:.1f}%")
    if failed >= 3:
     print("\n Warning: Multiple failed login attempts detected!")
    else:
     print("\n No suspicious activity detected.")

except FileNotFoundError:
    print("File not found.")