NORMAL_LOW = 97 # normal human body temp lower end
NORMAL_HIGH = 99 # normal human body temp higher end

def sort_temperatures(measurements):
    low = []
    normal = []
    high = []

    for temperature in measurements:
        if temperature < NORMAL_LOW:
            low.append(temperature)
        elif temperature > NORMAL_HIGH:
            high.append(temperature)
        else:
            normal.append(temperature)

    return low, normal, high