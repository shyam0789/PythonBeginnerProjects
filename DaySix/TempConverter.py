class TempConverter:

    def __init__(self,temp,convert_to):
        self.temp = temp
        self.convert_to = convert_to


    def convert(self):
        if self.convert_to.lower() == "c":
            return (int(self.temp) - 32)/1.8
        elif self.convert_to.lower() == "f":
            return (int(self.temp*1.8))+32
        else:
            return "Invalid input !"

tc = TempConverter(30,"f`1sx`")
print(f"Converted temperature is: {tc.convert()}")


