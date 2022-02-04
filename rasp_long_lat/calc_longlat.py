from django import db
import serial
import time
import string
import pynmea2
import psycopg2
from psycopg2 import Error

print("Program running\n")

class Database:
    def __init__(self, user, password, host, port, database_name):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database_name = database_name
        ## Database connection cursor --
        self.is_connected = False
        self.connection = None
        self.cursor = None
        
    def connect_to_cloud_db(self):
        try:
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database_name
            )
            self.is_connected = True # set DB if its connected to true
            self.connection = connection
            
            cursor = connection.cursor()
            self.cursor = cursor

        except(Exception, Error) as error:
            print("Error while connection to PostgreSQL", error)
    
    def close_db_connection(self):
        if self.is_connected:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")

# Tracker Class
class Tracker:
    def __init__(self, id, port_gps):
        self.id = id
        self.port_gps = port_gps
        self.lng = 0
        self.lat = 0
        
    def compute_current_location(self, raw_gps_data):
        # gps data received through serial i.e serial.readline()
        newmsg=pynmea2.parse(raw_gps_data)
        lat=newmsg.latitude
        lng=newmsg.longitude
        self.lng = lng
        self.lat = lat
    
    def post_current_location(self, db_cursor, db_connection):
        # send lng lat data to database
        lat = self.lat
        lng = self.lng
        tracker_id = self.id
        gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
        print(gps)
        if (lat + lng) == 0:
            return
        lat = round(lat, 2)
        lng = round(lng, 2)
        # print("lat lng", lat, lng)
        query = f"INSERT INTO tracking_location(lat, lng, tracker_id) VALUES ({lat}, {lng}, {tracker_id});"
        #these two tasks remain
        db_cursor.execute(query)
        db_connection.commit()

# driver code
if __name__ == "__main__":
    db_tracker1 = Database(
        user="postgres",
        password="postgres",
        host="35.200.156.14",
        port="5432",
        database="AssetTracking"
    )
    tracker_1 = Tracker(1, "/dev/ttyAMA0")
    db_tracker1.connect_to_cloud_db()
    
    if db_tracker1.is_connected:
        i = 0
        while True:
            port = tracker_1.port_gps
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout = pynmea2.NMEAStreamReader()
            newdata=ser.readline()
            try:
                newdata = newdata.decode('utf-8')
            except:
                continue
            if newdata[0:6] == "$GPRMC":
                    tracker_1.compute_current_location(newdata)                
                    # post lng and lat to cloud postgreSQL database
                    tracker_1.post_current_location(db_tracker1.cursor, db_tracker1.connection)
                    print("Location Sent", i)
                    if i == 10:
                        i = 0
                    i += 1
                    time.sleep(30)
    else:
        db_tracker1.close_db_connection()
# ---------------------------------- old code
"""
try:
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="35.200.156.14",
        port="5432",
        database="test"
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
                lat = round(lat, 4)
                lng = round(lng, 4)
                print("lat lng", lat, lng)
                '''query = f"UPDATE tracking_location\
                        SET lat={lat}, lng={lng}\
                        WHERE id={i};"'''
                query = f"INSERT INTO tracking_location(lat, lng, tracker_id) VALUES ({lat}, {lng}, 4);"
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

"""
# for git testing
