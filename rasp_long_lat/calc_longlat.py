import serial
import time
import string
import pynmea2
import psycopg2
from psycopg2 import Error

print("Program running\n")

try:
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="35.200.156.14",
        port="5432",
        database="AssetTracking"
    )
    cursor = connection.cursor()

    i = 0
    while True:    
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        try:
            newdata = newdata.decode('utf-8')
        except:
            continue

        if newdata[0:6] == "$GPRMC":
                newmsg=pynmea2.parse(newdata)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
                print(gps)
                if (lat + lng) == 0:
                    continue
                lat = round(lat, 2)
                lng = round(lng, 2)
                print("lat lng", lat, lng)
                '''query = f"UPDATE tracking_location\
                        SET lat={lat}, lng={lng}\
                        WHERE id={i};"'''
                query = f"INSERT INTO tracking_location(lat, lng, tracker_id) VALUES ({lat}, {lng}, 1);"
                cursor.execute(query)
                connection.commit()

                print("Location Sent", i)
                if i == 10:
                    i = 0
                i += 1
                time.sleep(30)

except(Exception, Error) as error:
    print("Error while connectiong to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


<<<<<<< HEAD
# for git testing
=======
# for git push testing
>>>>>>> c4cfebf0835ffd7bff47ef38759d205b437ac4f7
