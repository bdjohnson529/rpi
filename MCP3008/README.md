# MCP3008
This method uses an SPI method called 'bit-banging' to communicate between the Raspberry Pi and MCP3008.

The MCP3008 is a successive approximation register (SAR) analog to digital converter (ADC). The circuit store the results of a series of comparisons between the input voltage and a known voltage. Each comparison is succesively more accurate than the last. The ADC first compares the input voltage to 2.5 volts using a comparator. If the input voltage is greater than 2.5 Volts, the ADC will record a 1, else the ADC will record a 0. Depending on the result, the second approximation will either be 3.75 or 1.25 Volts. The MCP3008 makes a total of 10 approximations.

The Python script works backwards from the 10 approximations to calculate the input voltage. The user only needs to connect the proper GPIO pins of the RPi with the proper pins on the MCP3008.
