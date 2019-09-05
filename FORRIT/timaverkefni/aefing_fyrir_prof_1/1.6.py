

seconds = int(input("Enter seconds: "))

hours = seconds // (60*60)
seconds_left = seconds % (60*60)
minutes = seconds_left // 60
seconds_left_now = seconds_left % 60

print(hours)
print(minutes)
print(seconds_left_now)