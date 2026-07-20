# ==========================================
# SMART DEVICE MANAGEMENT SYSTEM
# EL 162 / EL 234 OOP MINI PROJECT
# ==========================================

# Parent Class
class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id
        self.__power_status = False

    # Getter for device_id
    @property
    def device_id(self):
        return self.__device_id

    # Setter for device_id
    @device_id.setter
    def device_id(self, value):
        if value.strip() == "":
            print("Device ID cannot be empty.")
        else:
            self.__device_id = value

    # Getter for power_status
    @property
    def power_status(self):
        return self.__power_status

    def turn_on(self):
        self.__power_status = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.__power_status = False
        print(f"{self.name} is now OFF.")

    def display_info(self):
        print("\n========== DEVICE INFORMATION ==========")
        print(f"Device Name : {self.name}")
        print(f"Device ID   : {self.device_id}")
        print(f"Power Status: {'ON' if self.power_status else 'OFF'}")


# Child Class 1
class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.recording_status = False

    def start_recording(self):
        if self.power_status:
            self.recording_status = True
            print("Recording Started.")
        else:
            print("Turn on the camera first.")

    def stop_recording(self):
        self.recording_status = False
        print("Recording Stopped.")

    def display_info(self):
        super().display_info()
        print(f"Recording: {'YES' if self.recording_status else 'NO'}")


# Child Class 2
class SmartLight(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.__brightness = 50

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Brightness must be between 0 and 100.")

    def increase_brightness(self):
        if self.brightness < 100:
            self.brightness += 10
        print(f"Brightness: {self.brightness}%")

    def decrease_brightness(self):
        if self.brightness > 0:
            self.brightness -= 10
        print(f"Brightness: {self.brightness}%")

    def display_info(self):
        super().display_info()
        print(f"Brightness : {self.brightness}%")


# Child Class 3
class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature):
        super().__init__(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        print(f"Current Temperature: {self.temperature}°C")

    def display_info(self):
        super().display_info()
        print(f"Temperature: {self.temperature}°C")


# Objects
camera = SecurityCamera("Front Door Camera", "CAM001")
light = SmartLight("Living Room Light", "LGT001")
sensor = TemperatureSensor("Bedroom Sensor", "TMP001", 26)


# Menu
while True:

    print("\n===================================")
    print(" SMART DEVICE MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Display Device Information")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start Recording")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        camera.display_info()
        light.display_info()
        sensor.display_info()

    elif choice == "2":
        camera.turn_on()
        light.turn_on()
        sensor.turn_on()

    elif choice == "3":
        camera.turn_off()
        light.turn_off()
        sensor.turn_off()

    elif choice == "4":
        sensor.read_temperature()

    elif choice == "5":
        print("1. Increase Brightness")
        print("2. Decrease Brightness")
        option = input("Choose: ")

        if option == "1":
            light.increase_brightness()
        elif option == "2":
            light.decrease_brightness()

    elif choice == "6":
        camera.start_recording()

    elif choice == "7":
        print("Thank you for using Smart Device Management System.")
        break

    else:
        print("Invalid choice.")
