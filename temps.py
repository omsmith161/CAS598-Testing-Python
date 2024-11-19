NORMAL_LOW = 97  # normal human body temp lower end
NORMAL_HIGH = 99  # normal human body temp higher end


def sort_temperatures(measurements):
    """Sort temperatures into three categories in comparison to normal human body temperature. 
    
    Input is a list of temperatures to sort, outputs are three lists containing low, normal, and high temperatures. 
    """
    low = []
    normal = []
    high = []

    for temperature in measurements:
        if temperature < NORMAL_LOW:
            low.append(temperature)        # list.append() adds the result into the respective list
        elif temperature > NORMAL_HIGH:
            high.append(temperature)
        else:
            normal.append(temperature)

    return low, normal, high


def convert_from_fahrenheit(temps):
    """Convert temperatures from fahrenheit to celsius. 

    Input is a list of temperatures, output is a list of converted celsius results. 
    """
    results = []
    for temp in temps:
        results.append((temp-32)/1.8)

    return results

def convert_to_fahrenheit(temps):
    """Convert temperatures from celsius to fahrenheit. 

    Input is a list of temperatures, output is a list of converted fahrenheit results. 
    """
    results = []
    for temp in temps:
        results.append(temp*1.8+32)

    return results
