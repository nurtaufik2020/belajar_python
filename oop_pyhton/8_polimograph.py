#inherintance,extend,overide,polimograph (memanggil isi class inheritance yang sama)
class Employee :
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    def work(self):
        return f"{self.name} is working"
    
    
#extend
#dia dapet warisan atribut lebih banyak,property method
class Programmer(Employee):
    def __init__(self,name,email,level):
        super().__init__(name,email)
        self.level = level
    
    def debug(self):
        return "debugging"

    #ini yang namanya override atau menulis ulang dan menimpa nilai sebelumnya
    def work(self):
        return f"{self.name} is writing code"

#kelas turunan baru dengan tools
class UIDesigner(Employee):
    def __init__(self,name,email,level,tools):
        super().__init__(name,email)
        self.level = level
        self.tools = tools
    
    #overide yang work.nya
    def work(self):
        return f"{self.name} is designing some new cool product"
    
        
print("")
employee = Employee("Agung","agung@company.com")
programmer = Programmer("Taufik","nurtaufik20220@gmail.com","senior")
ui_designer = UIDesigner("Nur","nurtaufik@gmail.com","senior","Inkscape")

def working(system):
    print(system.work())
    
#parameter itu ngga peduli, yang penting punya method work

working(ui_designer)
working(programmer)
working(employee)
