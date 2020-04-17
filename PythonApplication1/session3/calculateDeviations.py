import functions as f



readFilePath = 'PythonApplication1/testdata/measurements.csv'
writeFilePath = 'PythonApplication1/session3/newDeviations.csv'


measurements = f.readMeasurements(readFilePath, debugging=True)
deviations = f.calculateDeviation(measurements, debugging=True)

print(deviations)
f.writeValuesToFile(deviations, writeFilePath)