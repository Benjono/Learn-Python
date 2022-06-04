class MyClass:
    variable = "deez"

    def function(self):
        print("%s" % self.variable)

myObject = MyClass()
myObject.function()

myObject.variable="nuts"
myObject.function()
