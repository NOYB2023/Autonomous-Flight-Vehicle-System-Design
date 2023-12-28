from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

# Connect to the Vehicle
connection_string='/dev/serial/by-id/usb-ArduPilot_fmuv2_210036000851393339383036-if00'
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True, baud=115200)

try:
    vehicle.mode = VehicleMode('GUIDED')
    print ('first vehicle.mode: %s' % vehicle.mode)

    currentlat1 = vehicle.location.global_relative_frame.lat
    currentlon1 = vehicle.location.global_relative_frame.lon
    currentlon11 = currentlon1+0.0002
    print("Set default/target airspeed to 1.5")
    vehicle.airspeed = 1.5

    print("Going towards waypoint1")
    waypoint1 = LocationGlobalRelative(currentlat1, currentlon11, 0)
    vehicle.simple_goto(waypoint1, groundspeed=1.5)

    print("Default distance = 2.5")
    distance1 = 2.5
    
    flag = 0
    
    while True:    
        time.sleep(0.1)
        if vehicle.rangefinder.distance <= distance1 and vehicle.rangefinder.distance >= 0.5:
            print('Obstacle is detected')
            vehicle.mode = VehicleMode('HOLD')
            time.sleep(0.1)
            flag = 1
            print ('current vehicle.mode: %s' % vehicle.mode)
            break
        elif flag == 0:
            vehicle.simple_goto(waypoint1, groundspeed=1.5)
            print('Running')
            
    if flag == 1:
        time.sleep(3)    
        vehicle.mode = VehicleMode('GUIDED')
        currentlat2 = vehicle.location.global_relative_frame.lat
        currentlon2 = vehicle.location.global_relative_frame.lon
        currentlat22 = currentlat2+0.00005
        currentlon22 = currentlon2-0.00002
        waypoint2 = LocationGlobalRelative(currentlat22, currentlon22, 0)
        print("Going towards waypoint2")
        vehicle.simple_goto(waypoint2, groundspeed=1.5)
        time.sleep(5)
        print("Going towards waypoint1")
        vehicle.simple_goto(waypoint1, groundspeed=1.5)
        time.sleep(30)
        print("Finish")
        vehicle.mode = VehicleMode("HOLD")
    
# Close vehicle object before exiting script
        
    
except KeyboardInterrupt:
    vehicle.mode = VehicleMode("HOLD")
    print("Close vehicle object")
    vehicle.close()

