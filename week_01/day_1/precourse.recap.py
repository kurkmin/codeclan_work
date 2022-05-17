city = "Seoul"
month = 5 
ave_hi_temp = 23.6
ave_lo_temp = 13.5

def average_temp(city, month, ave_high, ave_low):
    ave_temp = (ave_high + ave_low) / 2 
    print("The average temperature in " + city + " in " + str(month) + " is " + str(ave_temp))

average_temp(city, month, ave_hi_temp, ave_lo_temp)