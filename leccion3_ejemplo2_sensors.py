import random
class Sensor:
    """The sensor base class.
    Defines the base class utilized by all sensors.
    """

    def __init__(self, name):
        """The Sensor base class initializer.
        
        :param name: The name of the sensor.
        :return: An instance of the Sensor class initialized with the specified name.
        """

        self.name = name
        """The name of the sensor."""
        self.value = random.randint(0, 50)
        """The value of the sensor."""

    def __str__(self):
        """Retrieves the sensor's description.
        
        :return: A description of the sensor.
        """

        return f"The {self.name} sensor has a value of {self.value}."


class TempSensor(Sensor):
    """The temperature sensor class.
    Provides access to the connected temperature sensor.
    Supported units are "F" (Fahrenheit), "C" (Celsius), and "K" (Kelvin)
    with "F" being the default unit.
    """

    def __init__(self, name, unit="F"):
        """The TempSensor class initializer.
        
        :param name: The name of the temperature sensor.
        :param unit: The unit of the temperature sensor, defaults to "F".
        :return: An instance of the TempSensor class initialized with the specified name and unit.
        """

        super().__init__(name)
        self.unit = unit
        """The temperature unit."""

    def __str__(self):
        """Retrieves the temperature sensor's description.
        
        :return: A description of the temperature sensor.
        """

        return (
            f"The {self.name} temperature sensor has a value of "
            f"{self.value} degrees {self.unit}."
        )

    def set_unit(self, unit):
        """Sets the temperature unit.
        
        :param unit: The temperature unit ("F", "C", or "K"),
        defaults to "F" if a valid unit is not provided.
        """

        if unit in ("C", "K"):
            self.unit = unit
        else:
            self.unit = "F"