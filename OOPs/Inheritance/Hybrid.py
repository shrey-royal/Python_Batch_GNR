class Employee:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        return f"Employee Name: {self.name}"
    
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    
    def manage(self):
        return f"{self.name} manages the {self.department} department."
    
class Developer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language

    def code(self):
        return f"{self.name} codes in {self.programming_language}."
    
class TeamLead(Manager, Developer):
    def __init__(self, name, department, programming_language):
        Employee.__init__(self, name)
        self.department = department
        self.programming_language = programming_language

    def lead(self):
        return f"{self.manage()} Also, {self.code()}"
    
def main():
    lead = TeamLead("Kaushal", "IT", 1010)
    print(lead.lead())

if __name__ == "__main__":
    main()
