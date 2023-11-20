light_status = { 
    "kitchen": "on",
    "living_room": "off",
    "office": "on",
    "hall": "off",
    "Bathroom": "off",
    "Bedroom": "on"
}

def light_press(room):
    if(light_status[room]=='on'):
        light_status[room]='off'

    else:
        light_status[room]='on'   
    return print("Light status of " + room + " is " + light_status[room])      


def check_lights(light_status):
    for room, status in light_status.items():
        if status == 'on':
            print("Turned on the light in " + room + " True")
        else:
            print( room + "----> " + " False")


def turn_off(light_status):
    for room, status in light_status.items():
        if status == 'on':
            light_status[room] = 'off'
            print("Turned off the light in " + room)


room=input("Enter the name of room: ")
light_press(room)
check_lights(light_status)
turn_off(light_status)


        
       

