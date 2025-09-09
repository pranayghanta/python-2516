# without abstraction - we used regular/contract classes
class Laptop:
    def usb_slot(self):
        pass
    def hdmi_slot(self):
        pass
    def c_port(self):
        pass

class Lenovo(Laptop):
    def usb_slot(self):
        print("Lenovo usb slot")
    def hdmi_slot(self):
        print("Lenovo hdmi slot")
class Dell(Laptop):
    def usb_slot(self):
        print("Lenovo usb slot")
    def c_port(self):
        print("Lenovo C slot")    

# user
print("user buying lenovo laptop")
lenovo = Lenovo()
lenovo.usb_slot()
lenovo.hdmi_slot()

print("user buying dell laptop")
dell = Dell()
dell.usb_slot()
dell.c_port()