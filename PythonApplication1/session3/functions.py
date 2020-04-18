#function with default values

def philippsfunction(planet="Earth"):
    print("Hello {}".format(planet))

def functionvariousVar(*planets):
    for planet in planets:
        print("Hello {}".format(planet))

def functionvariousVarDictionary(**planets):
    # print(planets)
    # loop through keys
    # for key in planets:
    #     print("Hello {}".format(   planets[key]   ))

    # # loop thourgh values
    # for planet in planets.values():
    #     print("Hello {}".format(    planet   ))
    # loop thourgh key value pairs
    for key, value in planets.items():
        print("Key: {}, Value: {}".format(    key, value   ))


def richFunction(name, planet, *planets, **kplanets):
    pass

    

def readMeasurements(filePath, customdelimiter = ';', debugging = False):
    """Read the measurement from filePath and return a useful list"""
    import csv

    measurements = [] # finally should look like:
    # [{'measurementid': '1140', "material": 'helional', 'density':1.166},...]

    with open(filePath, 'r') as fcsv:
        dcsv = csv.DictReader(fcsv, delimiter=customdelimiter)

        for row in dcsv:
            keys = list(row.keys()) # row is a dictonary

            measurementID = row[keys[0]] # using the keys, we get the values
            materialName = row[keys[1]]
            density = row[keys[2]]

            # if debugging: print("Measurement ID: {}, Material Name: {}, Density Value: {:.4f}".format(measurementID, materialName.upper(), float(density)))

            # then we populate our list as we desire it:
            measurements.append({'measurementid': measurementID, 'material': materialName, 'density': float(density)})

    if debugging: printDictionary(measurements, valueType="Measurements")
    return measurements



def calculateDeviation(measurements, debugging=False):
    """Calculate the deviations of materials compared to measurements"""
    # original density values are hardcoded
    # since they won't change...
    densities = {"lilial":0.946, 'helional':1.162, 'citral':0.89}

    deviations = [] # finally should look like:
    # [{'measurementid': '1140', "material": 'helional', 'density':0.004},...]

    for measurement in measurements:
        measurementID = measurement['measurementid']
        materialName = measurement['material']
        density = measurement['density']

        deviation = abs(density - densities[materialName])
        deviation = float('{:.4f}'.format(deviation)) # floating point precision to 4 digits

        # if debugging: print("Deviation ID: {}, Material Name: {}, Density Value: {:.4f}".format(measurement_ID, material_name.upper(), deviation))

        
        deviations.append({'measurementid': measurementID, 'material': materialName, 'density': float(deviation)})

    if debugging: printDictionary(deviations, valueType="Deviation")
    return deviations



def printDictionary(values, valueType="Measurement"):
    """Prints 'values'. 'values' is a list as defined in previous functions. i.e:  [{'measurementid': '1140', "material": 'helional', 'density':1.166},...] 
    valueType specifies list type. Default: 'Measurements'. Other possibility is: 'Deviations'. """

    for measurement in values:
        measurementID = measurement['measurementid']
        materialName = measurement['material']
        density = measurement['density']

        print("{} ID {}, Material Name: {}, Density {:.4f}".format(valueType, measurementID, materialName.upper(), density))



def writeValuesToFile(values, filePath):
    """Write down the values (a standard dictionary defined by us) into filePath. The (folder) directories in the filePath must exist."""
    import csv

    csv_columns = values[0].keys()
    try:
        with open(filePath, 'w') as fwrite:
            writer = csv.DictWriter(fwrite, fieldnames=csv_columns, delimiter=';')
            writer.writeheader()

            for row in values:
                writer.writerow(row)
        print("File write succesful.")
    except Exception as e:
        print("There was an error during file write: {}".format(str(e)))




if __name__ == '__main__':
    #measurements = readMeasurements('PythonApplication1/session3/measurements.csv', debugging=True)
    #deviations = calculateDeviation(measurements, debugging=True)
    #print(deviations)
    #writeValuesToFile(deviations, 'PythonApplication1/session3/newDeviations.csv')
    #pi=philippsfunction
    #pi("Mercury")
    # functionvariousVar("Earth", "Mercury", "Venus", "Jupiter")
    functionvariousVarDictionary(p1="Earth", p2="Mercury", p3="Venus", p4="Jupiter")