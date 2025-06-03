from modules.colors import RED, RESET, BLUE
import csv, os

def recordingEmail(email:str, name:str, company:str, count:int, base_name:str):
    base = f"{count}_{base_name}"
    if not os.path.exists(base):
        with open(base, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Email', 'Name', 'Company'])

    with open(base, 'a+') as file:
        write = csv.writer(file)
        write.writerow([email, name, company])

def DivideBase(base:str, count_base:int):
    with open(base, 'r') as file:
        number_email = 0
        count = 0
        for row in csv.DictReader(file):
            try:
                number_email+=1
                count+=1
                email = row["Email"]
                name = row["Name"]
                company = row["Company"]

                recordingEmail(
                        email=email, 
                        name=name, 
                        company=company, 
                        count=count,
                        base_name=base
                        )
                print(f"[{number_email}] [{count}] {email}")
                
                if count == count_base:count = 0

            except Exception as err:
                print(
                        f"{RED}При обработке базы произошла ошибка: "
                        f"{err}{RESET}")
                break
