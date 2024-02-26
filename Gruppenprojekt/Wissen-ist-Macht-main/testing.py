import time

def hoch_timer():
    sekunden = 0
    while True:
            minuten, restsekunden = divmod(sekunden, 60)
            zeitformat = "{:02}:{:02}".format(minuten, restsekunden)
            print("Timer: {}".format(zeitformat), end='\r')
            time.sleep(1)
            sekunden += 1


