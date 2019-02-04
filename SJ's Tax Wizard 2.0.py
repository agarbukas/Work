def fed(gross):
    if 0 <= gross < 75:
        return  0.00
    elif 75 <= gross < 85:
        return  1.00
    elif 85 <= gross < 95:
        return  2.00
    elif 95 <= gross < 105:
        return  3.00
    elif 105 <= gross < 115:
        return  4.00
    elif 115 <= gross < 125:
        return  5.00
    elif 125 <= gross < 135:
        return  6.00
    elif 135 <= gross < 145:
        return  7.00
    elif 145 <= gross < 155:
        return  8.00
    elif 155 <= gross < 165:
        return  9.00
    elif 165 <= gross < 175:
        return  10.00
    elif 175 <= gross < 185:
        return  11.00
    elif 185 <= gross < 195:
        return  12.00
    elif 195 <= gross < 210:
        return  13.00
    elif 210 <= gross < 220:
        return  14.00
    elif 220 <= gross < 230:
        return  15.00
    elif 230 <= gross < 240:
        return  16.00
    elif 240 <= gross < 250:
        return  17.00
    elif 250 <= gross < 260:
        return  18.00
    elif 260 <= gross < 270:
        return  20.00
    elif 270 <= gross < 280:
        return  21.00
    elif 280 <= gross < 290:
        return  22.00
    elif 290 <= gross < 300:
        return  23.00
    elif 300 <= gross < 310:
        return  24.00
    elif 310 <= gross < 320:
        return  26.00
    elif 320 <= gross < 330:
        return  27.00
    elif 330 <= gross < 340:
        return  28.00
    elif 340 <= gross < 350:
        return 29.00
    elif 350 <= gross < 360:
        return  30.00
    elif 360 <= gross < 370:
        return  32.00
    elif 370 <= gross < 380:
        return  33.00
    elif 380 <= gross < 390:
        return  34.00
    elif 390 <= gross < 400:
        return  35.00
    elif 400 <= gross < 410:
        return  36.00
    else:
        print("Gross is too high for fed calculation, use the sheet")


def sttax(gross):
    if 0 <= gross < 45:
        return 0.01
    elif 45 <= gross < 65:
        return 0.28
    elif 65 <= gross < 85:
        return 0.68
    elif 85 <= gross < 105:
        return 1.25
    elif 105 <= gross < 125:
        return 1.93
    elif 125 <= gross < 145:
        return 2.73
    elif 145 <= gross < 164:
        return 3.68
    elif 164 <= gross < 183:
        return 4.67
    elif 183 <= gross < 202:
        return 5.81
    elif 202 <= gross < 221:
        return 6.95
    elif 221 <= gross < 240:
        return 8.09
    elif 240 <= gross < 258:
        return 9.17
    elif 258 <= gross < 276:
        return 10.25
    elif 276 <= gross < 294:
        return 11.33
    elif 294 <= gross < 312:
        return 12.41
    elif 312 <= gross < 330:
        return 13.49
    elif 330 <= gross < 347:
        return 14.51
    elif 347 <= gross < 364:
        return 15.53
    elif 364 <= gross < 381:
        return 16.55
    elif 381 <= gross < 398:
        return 17.57
    elif 398 <= gross < 415:
        return 18.59
    else:
        print("Your gross is too high for state witholding calculation")


def ficacalc(gross):
    return gross * 0.0765


sentinel = 1
print("!!!!!!DISCLAIMER!!!!!!\n")
print("Thanks for the checks! Hope this helps!")
print("Version 2.0")
print("Licensed by CCC Services LLC")
print("Annual Subscription cost: Giving Andy time off to watch soccer\n")
print("****************************StartProgram***********************\n")

while sentinel == 1:
    hourly = (input("\nEnter hourly pay or 0 to enter gross wage"))
    #hours = -1
    while hourly == "" or float(hourly) < 0:
        hourly = (input("\nEnter hourly pay"))
    if float(hourly) == 0:
        gross = (input("\nEnter Gross Pay"))
        hours = 0
    #if float(hourly) == 0:
        #hours = 0
    if float(hourly) != 0:
        hours = (input("\nEnter number of hours worked"))
    while hours == "" or float(hours) < 0:
        hours = (input("\nEnter number of hours worked"))
    if hourly != 0 and hours != 0:
        gross = float(hourly) * float(hours)    #(input("\nEnter Gross Pay"))
    #while gross == "":
        #gross =(input("\nEnter Gross Pay"))
    #if gross == 0 :
        #sentinel = 0
    (federal) = float(fed(float(gross)))
    (state) = float(sttax(float(gross)))
    (fica) = float(ficacalc(float(gross)))

    print("******************START***********************\n")
    print("HOURLY-PAY was: $", hourly, "\n")
    print("\tHOURS entered were: ", hours, "\n")
    print("WAGE entered was: $", float(gross), "\n")
    print("\tFEDERAL witholdings are: $", federal, "\n")
    print("STATE witholdings are: $", state, "\n")
    print("\tFICA witholdings are: $", "%.2f" % fica, "\n")
    print("TOTAL Witholdings: $" , "%.2f" % (federal + state + fica), "\n")
    print("\tNET pay is: $", "%.2f" % (float(gross) - (federal+state+fica)), "\n")
    print("*******************END************************\n")
