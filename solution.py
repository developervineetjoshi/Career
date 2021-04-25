import datetime
D = {'2020-01-01':6, '2020-01-04': 12, '2020-01-05': 14, '2020-01-06': 2, '2020-01-07':4} #sample Input
outputD={}
missingList=[]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] # for days traversal
dayInNo = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6} #for getting the index of days with day name

#function to increase days no as the no have to be again 0 after index 6 has reached
def increasedDayNo(dayno):
    if(dayno==6):
        return 0
    else:
        return dayno+1

#function to decrease days no as the no have to be again 6 after index 0 has reached
def decreasedDayNo(dayno):
    if(dayno==0):
        return 6
    else:
        return dayno-1
    
#function to calculate and add the missing values
def calAndAddMissingValues(dict,day):
    noday=dayInNo[day]
    previousDay=decreasedDayNo(noday)
    # print(previousDay)
    nextDay=increasedDayNo(noday)
    # print(nextDay)
    while not (isPresent(dict,days[previousDay])):
        previousDay=decreasedDayNo(previousDay)
    while not (isPresent(dict,days[nextDay])):
        nextDay=increasedDayNo(nextDay)
    # print(f"previous day is {days[previousDay]} and next day is {days[nextDay]}")
    # print(f"value of outputD[days[previousDay]] = {outputD[days[previousDay]]} and outputD[days[nextDay]] = {outputD[days[nextDay]]}")
    outputD[day] = ( outputD[days[previousDay]] + outputD[days[nextDay]] ) // 2 #finding mean of closest days and appending it to dictionary


#function to check whether a key is present in a dictionary or not
def isPresent(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

#function to create the list of missing values
def createMissingList(dict) :
    for i in days :
        if not (isPresent(dict,i)):
            missingList.append(i)
            

#looping for the given input
for key in D:
    dobject = datetime.datetime.strptime(key, '%Y-%m-%d') #for obtaining date object
    intDay = datetime.date(year=dobject.year, month=dobject.month, day=dobject.day).weekday() #for getting the day from the date
    #conditional statements to add the values if same key appears again
    if(isPresent(outputD,days[intDay])) :
        outputD[days[intDay]] = outputD[days[intDay]] + D[key]
    else :
        outputD[days[intDay]]=D[key]

createMissingList(outputD) #creating missing list so that we can use it to add missing values to the dictionary
missingList.reverse()
if not (len(missingList)==0) :
    for misval in missingList :
        calAndAddMissingValues(outputD,misval)

print(outputD)
