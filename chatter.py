import network
import sys
import time

task_num = 0


def do_work(data):  # "x y"
    global task_num
    task_num += 1
    print(f"doing work: |{task_num} {mode}| {data}")
    time.sleep(3)  # pretend to do work
    network.say("newx newy")


# First argument is the IP address of the other RPi
# Second argument is the starting mode
if (len(sys.argv) >= 2):
    ip_of_other_rpi = sys.argv[1]
    mode = sys.argv[2]
else:
    sys.exit("Bad arguments")

if mode == "first":
    network.call(ip_of_other_rpi, whenHearCall=do_work)
    do_work("0 0")
else:
    network.wait(whenHearCall=do_work)

while network.isConnected():
    time.sleep(20)
