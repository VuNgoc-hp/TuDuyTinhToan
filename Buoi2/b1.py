# 1. Convert 42 minutes 42 seconds to seconds
m=42
s=42+m*60

print(s)
# 2. Convert 10 kilometers to miles
km=10
miles=10*1.61
print(miles)
# 3. Calculate average pace in seconds per mile
pace=s/miles
print(pace)
# 4.1. Find the value of x
# 4.1. Find the value of y
x=pace//60
y=pace%60
print(x,y)
# 5. Calculate average speed in miles per hour
h=s/3600
mph=miles/h
print(mph)