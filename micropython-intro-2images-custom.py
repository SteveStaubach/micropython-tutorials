from microbit import *

a    = Image("03903:"
             "04944:"
             "65956:"
             "99999:"
             "00900")

b    = Image("30930:"
             "45934:"
             "46965:"
             "99999:"
             "00900")

c    = Image("03933:"
             "45945:"
             "56956:"
             "99999:"
             "00900")

satan = [a, b, c]
display.show(satan, loop=True, delay=100)