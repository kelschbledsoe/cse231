    ###########################################################
    #  Computer Project #1
    #
    #  Algorithm
    #    prompt for an integer
    #    input an integer
    #    convert integer to float   
    #    conversions
    #       integer inputted converted to other measurements of length
    #    conversions rounded
    #    print conversion results
    ###########################################################


#Input
rod_str = input("Input rods: ")
rod_flt = float(rod_str)
print ("You input", rod_flt, "rods.")
print()

#Convert rod to meter
meter_num = (5.0292 * rod_flt)

#Convert rod to furlong
furlong_num = (rod_flt / 40)

#Convert rod to mile
mile_num = (meter_num / 1609.34)

#Convert rod to foot
foot_num = (meter_num / 0.3048)

#Convert rod to time
time_num = ((mile_num / 3.1) * 60)

#Round conversions
meter_num = round (meter_num, 3)
furlong_num = round (furlong_num, 3)
mile_num = round (mile_num, 3)
foot_num = round (foot_num, 3)
time_num = round (time_num, 3)


#Printing conversion results
print ("Conversions")
print("Meters:", meter_num)
print("Feet:", foot_num)
print("Miles:", mile_num)
print("Furlongs:", furlong_num)
print("Minutes to walk", rod_flt, "rods:", time_num)