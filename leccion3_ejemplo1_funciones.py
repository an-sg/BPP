"""Defines the sensor classes.
Description
-----------
Defines the base and end user classes for various sensors.
- Sensor (base class)
- TempSensor

Libraries/Modules
-----------------
- random standard library (https://docs.python.org/3/library/random.html)
- Access to randint function.
    
Notes
-----
- Comments are Sphinx (reStructuredText) compatible.

Título 2
~~~~~~~~

Título 3
^^^^^^^^

* Elemento 1

* Elemento 2

  * Elemento 2.1

* Elemento 3

Author(s)
---------
- Created by John Woolsey on 05/27/2020.
- Modified by John Woolsey on 07/02/2020.
- Copyright (c) 2020 Woolsey Workshop.  All rights reserved.

"""
class operaciones:
    """Esta es una primera descripción de la clase
    """
    
    def __init__(self,op1,op2):
        """Contructor de la clase bla bla
        
        :param op1: Valor 1.
        :type op1: :class:`float`
        :param op2: Valor 2.
        :type op2: :class:`float`
        :return: An instance of the Sensor class initialized with the specified name.
        """
        self.op1=op1
        self.op2=op2
    
    def suma(self):
        """Esta función realiza una suma
        
        :return: An instance of the Sensor class initialized with the specified name.
        """
        return self.op1+self.op2
    
    def resta(self):
        """Esta función realiza una resta
        
        :return: An instance of the Sensor class initialized with the specified name.
        """
        return self.op1-self.op2
        