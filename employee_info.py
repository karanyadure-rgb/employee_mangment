# Employee Information: id,name,department,salary,position
# Store in a list of dictionaries for easy access and manipulation
# store data in json file
#display data from json file

import json

class Employee:
    emp_info = []
    FILE_NAME = "employee_data.json"

    def AcceptInfo(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        try :
            salary = float(input("Enter Salary: "))
        except ValueError:
            print("Invalid input for salary. Please enter a numeric value.")
            return
            
        position = input("Enter Position: ")

        self.emp_info.append({
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary,
            "position": position
        })
        
    def store_to_json(self):

        try :
            existing_data = []

            with open(self.FILE_NAME ,"r") as f :
                existing_data = json.load(f)
        except FileNotFoundError, json.JSONDecodeError:
            existing_data=[]

        Merage_data = existing_data + self.emp_info      

        with open(self.FILE_NAME, "w") as f:
            json.dump(Merage_data, f,indent=4) 

    def display_data(self):

        try :
            with open (self.FILE_NAME , "r") as f:
                data = json.load(f)
                for emp in data:

                    print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Salary: {emp['salary']}, Position: {emp['position']}")
        except :
            print("No employee data found.")


def main():
     emp = Employee()
     while True:
        emp.AcceptInfo()
        cont = input("Do you want to add another employee? (y/n): ")
        if cont.lower() != 'y':
            break
     emp.store_to_json()
     print(f"Employee data stored in {emp.FILE_NAME}")
     emp.display_data()


if __name__ == "__main__":
    main()