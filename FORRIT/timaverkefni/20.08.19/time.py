secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
# hours =
hours = secs_int // (60*60)
# minutes =
seconds_after_hours = secs_int % (60*60)
minutes = seconds_after_hours // 60
# seconds =
seconds = seconds_after_hours % 60
print(hours,":",minutes,":",seconds) # do not change this line
