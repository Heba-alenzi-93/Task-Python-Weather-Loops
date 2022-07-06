

weather_list = [73.4,75.2,77,86,87.8]




# printer(elements)
# - Accepts a list
# - Prints every element of the list
def printer(elements):
    # Your code here
    for x in range(len(elements)):
        print (elements[x])
    


#printer(weather_list)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):
    ftoc=[]
    for x in range(len(temperatures)):
        result = ((temperatures[x]-32)* (5/9)//1)
        ftoc.append(result)
    print("The tempreture in celsius are : " )
    print(ftoc)
    return ftoc

to_celsius(weather_list)
    


# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
def hottest_days(temperatures, threshold):
    hotpoint=[]
    for x in range(len(temperatures)):
        if(temperatures[x] > threshold):
            hotpoint.append(temperatures[x])
    print("The lsit of hotest point are: " )
    print(hotpoint)
    return hotpoint


hottest_days(weather_list,80)  


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshhold):
    result =[]
    result = to_celsius(temperatures)
    hottest_days(result,threshhold)

    
    

    

print_hottest_days(weather_list,30)
