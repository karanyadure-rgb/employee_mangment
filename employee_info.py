# Employee Information: id,name,department,salary,position
# Store in a list of dictionaries for easy access and manipulation
# store data in json file
#display data from json file

import json

class Employee:

    FILE_NAME = "employee_data.json"

    def __init__(self):
        self.emp_info=[]

    def AcceptInfo(self):
        while True:

            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            try :
                salary = float(input("Enter Salary: "))
            except ValueError:
                print("Invalid input for salary. Please enter a numeric value.")
                
            position = input("Enter Position: ")

            self.emp_info.append({
                "id": emp_id,
                "name": name,
                "department": department,
                "salary": salary,
                "position": position
            })
        
            cont = input("Do you want to add another employee? (y/n): ")
            if cont.lower() != 'y':
                self.store_to_json()
                break
        
    def store_to_json(self):
        # checking file is empty or not
        try :
            existing_data = []

            with open(self.FILE_NAME ,"r") as f :
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data=[]

        Merage_data = existing_data + self.emp_info      

        with open(self.FILE_NAME, "w") as f:
            json.dump(Merage_data, f,indent=4) 
            print(f"Employee data stored in {self.FILE_NAME}")


    def display_a_data(self):

        find=input("Enter the employee no. ")

        try :
            with open (self.FILE_NAME , "r") as f:
                data = json.load(f)
                for emp in data:
                    if emp['id']==find:
                        print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Salary: {emp['salary']}, Position: {emp['position']}")
        except Exception as e:
            print("No employee data found.",e)

    def display_data(self):

        try :
            with open (self.FILE_NAME , "r") as f:
                data = json.load(f)
                for emp in data:
                    print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Salary: {emp['salary']}, Position: {emp['position']}")
        except Exception as e:
                print("No employee data found.",e)


def main():
    emp = Employee()
    while True:
        print("1.ADD NEW EMPLOYEE")
        print("2.DISPLAY DATA OF EMPLOYEE")
        print("3.DISPLAY DATA OF ALL EMPLOYEES")
        print("4.EXIT")
        user_choice=int(input("ENTER THE CHOICE NO : ").strip())

        if 1 == user_choice: emp.AcceptInfo()
        elif 2 == user_choice: emp.display_a_data()
        elif 3 == user_choice: emp.display_data()
        elif 4 == user_choice: break
        else : print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
