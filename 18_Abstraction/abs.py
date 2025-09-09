# achieve abstraction - we use abc(abstract base class - ABC)
from abc import ABC,abstractmethod

class Laptop(ABC):
        @abstractmethod
        def usb_slot(self):
            pass
        @abstractmethod   
        def hdmi_slot(self):
            pass
        @abstractmethod
        def c_port(self):
            pass
class Lenovo(Laptop):
    def usb_slot(self):
        print("Lenovo usb slot")
    def hdmi_slot(self):
        print("Lenovo hdmi slot")
    def c_port(self):
        print("Lenovo C slot")    

class Dell(Laptop):
    def usb_slot(self):
        print("Dell usb slot")
    def hdmi_slot(self):
        print("Dell hdmi slot")
    def c_port(self):
        print("Dell C slot") 
    def bluetooth(self):
        print("Dell provided bluetooth")       

# user
print("user buying lenovo laptop")
lenovo = Lenovo()
lenovo.usb_slot()
lenovo.hdmi_slot()
lenovo.c_port()


print("user buying dell laptop")
dell = Dell()
dell.usb_slot()
dell.c_port() 
dell.hdmi_slot()
dell.bluetooth()


