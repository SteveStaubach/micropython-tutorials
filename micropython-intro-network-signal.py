pin1.write_digital(1)  # switch the signal on
pin1.write_digital(0)  # switch the signal off
input = pin2.read_digital()  # read the value of the signal (either 1 or 0)