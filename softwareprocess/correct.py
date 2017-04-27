import math

def correct(values=None):

    if(values == None or not 'lat' in values or not 'long' in values or not 'altitude' in values or not 'assumedLat' in values or not 'assumedLong' in values):
        values = {'error': 'mandatory information is missing', 'op':'correct'}
        return values
    if(not 'd' in values['lat']):
        values['error'] = 'invalid input for lat'
        return values
    if (not 'd' in values['long']):
        values['error'] = 'invalid input for long'
        return values
    if (not 'd' in values['altitude']):
        values['error'] = 'invalid input for altitude'
        return values
    if (not 'd' in values['assumedLat']):
        values['error'] = 'invalid input for assumedLat'
        return values
    if (not 'd' in values['assumedLong']):
        values['error'] = 'invalid input for assumedLong'
        return values

    latitude = values['lat'].split('d')
    try:
        latitudeMinutes = int(latitude[0])
    except ValueError:
        values['error'] = 'invalid lat'
        return values
    latitudeSeconds = float(latitude[1])
    latitudeRadians = convertDegreesToRadians(convertDegreeMinutesIntoDegreeDecimal(latitudeMinutes, latitudeSeconds))

    longitude = values['long'].split('d')
    try:
        longitudeMinutes = int(longitude[0])
    except ValueError:
        values['error'] = 'invalid long'
        return values
    longitudeSeconds = float(longitude[1])


    altitude = values['altitude'].split('d')
    try:
        altitudeMinutes = int(altitude[0])
    except ValueError:
        values['error'] = 'invalid altitude'
        return values
    altitudeSeconds = float(altitude[1])
    altitudeRadians = convertDegreesToRadians(convertDegreeMinutesIntoDegreeDecimal(altitudeMinutes, altitudeSeconds))

    assumedLatitude = values['assumedLat'].split('d')
    try:
        assumedLatitudeMinutes = int(assumedLatitude[0])
    except ValueError:
        values['error'] = 'invalid assumedLat'
        return values
    assumedLatitudeSeconds = float(assumedLatitude[1])
    assumedLatitudeRadians = convertDegreesToRadians(convertDegreeMinutesIntoDegreeDecimal(assumedLatitudeMinutes, assumedLatitudeSeconds))

    assumedLongitude = values['assumedLong'].split('d')
    try:
        assumedLongitudeMinutes = int(assumedLongitude[0])
    except ValueError:
        values['error'] = 'invalid assumedLong'
        return values
    assumedLongitude[1] = float(assumedLongitude[1])

    localHourAngle = addAngle(longitude, assumedLongitude)
    localHourAngleRadians = convertDegreesToRadians(convertDegreeMinutesIntoDegreeDecimal(convertStringToDegrees(localHourAngle)))

    intermediateDistanceRadians = (math.sin(latitudeRadians) * math.sin(assumedLatitudeRadians)) + (math.cos(latitudeRadians) * math.cos(assumedLatitudeRadians) * math.cos(localHourAngleRadians))

    correctedAltitudeRadians = math.asin(intermediateDistanceRadians)

    correctedDistanceRadians = altitudeRadians - correctedAltitudeRadians

    correctedDistanceArcMinutes = correctedDistanceRadians * 10800 / math.pi

    correctedAzimuth = math.acos( math.sin(latitudeRadians - intermediateDistanceRadians) / (math.cos(assumedLatitudeRadians) * math.cos(math.arcsin(correctedDistanceRadians) )))

    values['correctedDistance'] = str(correctedDistanceArcMinutes)

    values['correctedAzimuth'] = convertDegreesToString(convertRadiansToDegrees(correctedAzimuth))

    return values

#in DMS format
def convertStringToDegrees(angle):
    if()
    splitStrings = angle.split('d')
    minutes = int(splitStrings[0])
    seconds = float(splitStrings[1])

    ##List; int and float
    return [minutes, seconds]

#angleAsAList is assumed to have only two elements in it, minutes and seconds
#returns a string for the purposes of values
def convertDegreesToString(angleAsAList):
    return str(angleAsAList[0] + 'd' + angleAsAList[1])

def convertRadiansToDegrees(radians):
    degrees = radians * 180 / math.pi

    degreesInt = int(degrees)

    degreesList = [degreesInt, (degrees - degreesInt)]

    degreesList[1]*= 60

    return degreesList

def simplifyAngle(angle):
    angleAsAList = convertStringToDegrees(angle)
    angleMinutes = int(angleAsAList[0])
    while angleMinutes > 360:
        angleMinutes -= 360
    while angleMinutes < 0:
        angleMinutes +=360
    newAngleString = str(angleMinutes) + 'd' + angleAsAList[1]

    return newAngleString

def simplifyLatitude(angle):
    if(type(angle) is str):
        angleList = convertStringToDegrees(angle)
        simplifyLatitude(angleList)
    elif(type(angle) is list):
        while(angle[0] <= -90):
            angle[0]+= 90
        while(angle[0] > 90):
            angle[0]-= 90
    elif(type(angle) is float):
        {

        }

def addAngle(angle1, angle2):
    angle1AsAList = convertStringToDegrees(angle1)
    angle2AsAList = convertStringToDegrees(angle2)
    addedMinutes = angle1AsAList[0] + angle2AsAList[0]
    addedSeconds = angle1AsAList[1] + angle2AsAList[1]
    while addedSeconds > 60:
        addedSeconds-=60
        addedMinutes+=1
    newAngleString = str(addedMinutes) + 'd' + str(addedSeconds)
    newAngleString = simplifyAngle(newAngleString)

    return newAngleString

def convertDegreeMinutesIntoDegreeDecimal(degrees, minutes):
    return float(degrees + minutes/60)

#In Decimal format
def convertDegreesToRadians(degrees):
    return float(degrees * math.pi / 180.0)

#To Decimal format (degrees)
def convertRadiansToDegrees(radians):
    return float(radians * 180.0 / math.pi)