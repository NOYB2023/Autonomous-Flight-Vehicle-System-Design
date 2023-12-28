import dronekit
import time
import os

connection_string = (
    "/dev/serial/by-id/usb-ArduPilot_fmuv2_210036000851393339383036-if00"
)
try:
    vehicle = dronekit.connect(connection_string, wait_ready=True, baud=115200)
    vehicle.mode = dronekit.VehicleMode("GUIDED")  # change flight mode
    time.sleep(1)
    print("First vehicle.mode: %s" % vehicle.mode)

    distance = int(input("Enter your desired recognition distance : "))
    flag = False  # for
    st = 1
    while True:
        try:
            print("Rangefinder distance: %s" % vehicle.rangefinder.distance)
            time.sleep(1)

            if vehicle.rangefinder.distance <= distance:
                vehicle.mode = dronekit.VehicleMode("HOLD")
                print("vehicle.mode: %s" % vehicle.mode)
                print("Obstacle is detected")
                if flag == False:
                    terminal_command = f"libcamera-jpeg -o test{st}.jpg -t 1000"
                    os.system(terminal_command)
                    flag = True
                    st += 1
            else:
                vehicle.mode = dronekit.VehicleMode("GUIDED")
                print("vehicle.mode: %s" % vehicle.mode)
                print("Resume the movement")
                flag = False
                continue

        except KeyboardInterrupt:
            print("Emergency stop")
            break

    vehicle.mode = dronekit.VehicleMode("HOLD")
    print(" vehicle.mode: %s" % vehicle.mode)
    vehicle.close()

except Exception as err:
    print(str(err))
