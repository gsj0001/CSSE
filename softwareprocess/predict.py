__CURRENT_YEAR__ = 2017
__LEAP_YEARS_SINCE_2001__ = [2004, 2008, 2012, 2016]

from datetime import date, time, datetime

def predict(values=None):
    starNames = ['Alpheratz', 'Ankaa', 'Schedar', 'Diphda', 'Achernar', 'Hamal', 'Polaris', 'Akamar', 'Menkar', 'Mirfak', 'Aldebaran', 'Rigel', 'Capella', 'Bellatrix', 'Elnath', 'Alnilam', 'Betelgeuse', 'Canopus', 'Sirius', 'Adara', 'Procyon', 'Pollux', 'Avior', 'Suhail', 'Miaplacidus', 'Alphard', 'Regulus', 'Dubhe', 'Denebola', 'Gienah', 'Acrux', 'Gacrux', 'Alioth', 'Spica', 'Alcaid', 'Hadar', 'Menkent', 'Arcturus', 'Rigil', 'Kent', 'Zubenelg', 'Kochab', 'Alphecca', 'Antares', 'Atria', 'Sabik', 'Shaula', 'Rasalhague', 'Etamin', 'Kaus', 'Aust.', 'Vega', 'Nunki', 'Altair', 'Peacock', 'Deneb', 'Enif', 'Alnair', 'Fomalhaut', 'Scheat', 'Markab']
    siderealHourAngles = ['357d41.7', '353d14.1', '349d38.4', '348d54.1', '335d25.5', '327d58.7', '316d41.3', '315d16.8', '314d13.0', '308d37.4', '290d47.1', '281d10.1', '280d31.4', '278d29.8', '278d10.1', '275d44.3', '270d59.1', '263d54.8', '258d31.7', '255d10.8', '244d57.5', '243d25.2', '234d16.6', '222d50.7', '221d38.4', '217d54.1', '207d41.4', '193d49.4', '182d31.8', '175d50.4', '173d07.2', '171d58.8', '166d19.4', '158d29.5', '152d57.8', '148d45.5', '148d05.6', '145d54.2', '139d49.6', '137d03.7', '137d21.0', '126d09.9', '112d24.4', '107d25.2', '102d10.9', '96d20.0', '96d05.2', '90d45.9', '83d41.9', '80d38.2', '75d56.6', '62 d06.9', '53 d17.2', '49d30.7', '33d45.7', '27d42.0', '15d22.4', '13d51.8', '13d36.7']
    declinations = ['29d10.9', '-42d13.4', '56d37.7', '-17d54.1', '-57d09.7', '23d32.3', '89d20.1', '-40d14.8', '4d09.0', '49d55.1', '16d32.3', '-8d11.3', '46d00.7', '6d21.6', '28d37.1', '-1d11.8', '7d24.3', '-52d42.5', '-16d44.3', '-28d59.9', '5d10.9', '27d59.0', '-59d33.7', '-43d29.8', '-69d46.9', '-8d43.8', '11d53.2', '61d39.5', '14d28.9', '-17d37.7', '-63d10.9', '-57d11.9', '55d52.1', '-11d14.5', '49d13.8', '-60d26.6', '-36d26.6', '19d06.2', '-60d53.6', '-16d06.3', '74d05.2', '26d39.7', '-26d27.8', '-69d03.0', '-15d44.4', '-37d06.6', '12d33.1', '51d29.3', '-34d22.4', '38d48.1', '-26d16.4', '8d54.8', '-56d41.0', '45d20.5', '9d57.0', '-46d53.1', '-29d32.3', '28d10.3', '15d17.6']


    if(values == None or not 'body' in values):
        return {'error':'mandatory information is missing', 'op':'predict'}
    if(not values['body'] in starNames):
        values['error'] = 'star not in catalog'
        return values

    #Give default date
    if(not 'date' in values):
        values['date'] = '2001-01-01'

    #Give default time
    if(not 'time' in values):
        values['time'] = '00:00:00'

    #Check values within date
    dateValues = values['date'].split('-')
    if(int(dateValues[0]) > __CURRENT_YEAR__ or int(dateValues[1]) > 12 or int(dateValues[2]) > 31):
        values['error'] = 'invalid date'
        return values

    #Check values within time
    timeValues = values['time'].split(':')
    if(int(timeValues[0]) > 23 or int(timeValues[1]) > 59 or int(timeValues[2]) > 59):
        values['error'] = 'invalid time'
        return values

#################################################################################################

    #Since bad/invalid values have been accounted for, calculation begins here
    __GREENWICHHOURANGLEARIES__ = '100d42.6'
    referenceAngle = __GREENWICHHOURANGLEARIES__.split('d')
    referenceAngleMinutes = int(referenceAngle[0])
    referenceAngleSeconds = float(referenceAngle[1])
    referenceAngleDecimal = float(referenceAngleMinutes) + float(referenceAngleSeconds/60)

    starTableIndex = starNames.index(values['body'])
    sideHourAngle = siderealHourAngles[starTableIndex]
    declination = declinations[starTableIndex]
    values['latitude'] = declinations[starTableIndex]

    currentDate = datetime(int(dateValues[0]), int(dateValues[1]), int(dateValues[2]), int(timeValues[0]), int(timeValues[1]), int(timeValues[2]))
    referenceDate = datetime(2001, 1, 1, 0,0,0)

    timedelta = currentDate - referenceDate

    totalRotation = 360 / 86164.1 * timedelta.seconds

    greenwichhourariesCurrent = referenceAngleDecimal - totalRotation

    sideHourAngleSplit = sideHourAngle.split('d')

    sideHourAngleDecimal = float(sideHourAngle[0]) + float(sideHourAngle[1])

    greenwichhourstar = str(sideHourAngleDecimal + greenwichhourariesCurrent)

    greenwichhourstarSplit = greenwichhourstar.split('.')

    greenwichhourstarMinutes = greenwichhourstarSplit[0]
    greenwichhourstarSecondsDecimal = '.' + greenwichhourstarSplit[1]

    greenwichhourstarSeconds = str(float(greenwichhourstarSecondsDecimal) * 100/60)[:4]

    values['longitude'] = greenwichhourstarMinutes + 'd' + greenwichhourstarSeconds

    return values

def convertStringToDegrees(angle):
    splitStrings = angle.split('d')
    minutes = int(splitStrings[0])
    seconds = float(splitStrings[1])

    ##List; int and float
    return [minutes, seconds]

def simplifyAngle(angle):
    angleAsAList = convertStringToDegrees(angle)
    angleMinutes = int(angleAsAList[0])
    while angleMinutes > 360:
        angleMinutes -= 360
    while angleMinutes < 0:
        angleMinutes +=360
    newAngleString = str(angleMinutes) + 'd' + angleAsAList[1]

    return newAngleString

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


