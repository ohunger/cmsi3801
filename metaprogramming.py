class CustInheritor:
    def __init__(self, base_class):
        self.new_class = type("CustomClass", (base_class,), {})
    def print_inheritance(self):
        print(f"CustomClass inherits from: {self.new_class.__bases__}")



class Base:
    pass

custom_instance = CustInheritor(Base)
custom_instance.print_inheritance()