
from datetime import datetime as dt
from datetime import timedelta

def recurringTask(firstDate, k, daysOfTheWeek, n):

    curr_date = dt.strptime(firstDate, "%d/%m/%Y").date()
    
    weekday_dict = {"Monday" : 0,
                    "Tuesday" : 1,
                    "Wednesday" : 2,
                    "Thursday" : 3,
                    "Friday" : 4,
                    "Saturday" : 5,
                    "Sunday" : 6}

    n_dates = [curr_date.strftime("%d/%m/%Y")]
    weekday_name = curr_date.strftime("%A")
    curr_cycle_start = curr_date
    dow_index = daysOfTheWeek.index(weekday_name)
    dow_index = (dow_index + 1) % len(daysOfTheWeek)

    for i in range(n-1):
        if daysOfTheWeek[dow_index] == weekday_name:
            curr_cycle_start = curr_cycle_start + timedelta(days=k*7)
            curr_date = curr_cycle_start
            n_dates.append(curr_date.strftime("%d/%m/%Y"))
        else:
            next_day_index = weekday_dict[daysOfTheWeek[dow_index]]
            tdelta = (next_day_index - curr_date.weekday() + 7) % 7
            curr_date = curr_date + timedelta(days=tdelta)
            n_dates.append(curr_date.strftime("%d/%m/%Y"))
        dow_index = (dow_index + 1) % len(daysOfTheWeek)

    return n_dates



"""
Test 1
Input:
firstDate: "01/01/2015"
k: 2
daysOfTheWeek: ["Monday", "Thursday"]
n: 4
Output: Empty
Expected Output: ["01/01/2015", "05/01/2015", "15/01/2015", "19/01/2015"]
Console Output: Empty
****
recurringTask("01/01/2015", 2, ["Monday", "Thursday"], 4)
****

Test 4
Input:
firstDate: "01/02/2100"
k: 4
daysOfTheWeek: ["Sunday", "Monday"]
n: 4
Output: Empty
Expected Output: ["01/02/2100", "07/02/2100", "01/03/2100", "07/03/2100"]
Console Output: Empty
****
recurringTask("01/02/2100", 4, ["Sunday", "Monday"], 4)
****

Test 5
Input:
firstDate: "23/02/2000"
k: 2
daysOfTheWeek: ["Wednesday", "Friday"]
n: 4
Output: Empty
Expected Output: ["23/02/2000", "25/02/2000", "08/03/2000", "10/03/2000"]
Console Output: Empty
****
recurringTask("23/02/2000", 2, ["Wednesday", "Friday"], 4)
****

Test 2 - PASSED
Input:
firstDate: "30/05/1995"
k: 4
daysOfTheWeek: ["Tuesday"]
n: 1
Output: Empty
Expected Output: ["30/05/1995"]
Console Output: Empty
****
recurringTask("30/05/1995", 4, ["Tuesday"], 1)
****

***Test 3*** - PASSED
Input:
firstDate: "22/02/2020"
k: 1
daysOfTheWeek: ["Saturday"]
n: 2
Output: Empty
Expected Output: ["22/02/2020", "29/02/2020"]
Console Output: Empty
****
recurringTask("22/02/2020", 1, ["Saturday"], 2)
****


Test 6 - PASSED
Input:
firstDate: "31/12/2999"
k: 1
daysOfTheWeek: ["Tuesday"]
n: 2
Output: Empty
Expected Output: ["31/12/2999", "07/01/3000"]
Console Output: Empty
****
recurringTask("31/12/2999", 1, ["Tuesday"], 2)
****


If you have a task that you need to complete on a regular basis,
you can set it up in Asana as a recurring task. One option is to schedule 
the task to repeat every k weeks on specified days of the week.

It would be useful to be able to view the first n dates for which the task 
is scheduled. Given the first date for which the task is scheduled, return an 
array of the first n dates.

In this task, you'll likely need month lengths and weekday names, provided here:

Month lengths from January to December:
31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

During leap years February has 29 days.
Names of weekdays: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
"Friday", "Saturday".

January 1, 2015 was a Thursday.

Example

For firstDate = "01/01/2015", k = 2, daysOfTheWeek = ["Monday", "Thursday"] 
and n = 4, the output should be

recurringTask(firstDate, k, daysOfTheWeek, n) = 
    ["01/01/2015", "05/01/2015", "15/01/2015", "19/01/2015"]

firstDate falls on a Thursday. The first Monday after it is "05/01/2015". 
Since k = 2, the next two days for which the task is scheduled are Thursday, 
January 15, and Monday, January 19.

Input/Output

[time limit] 4000ms (py)
[input] string firstDate

A string in the format "dd/mm/yyyy", representing some date either in the past, 
or in the future. It is guaranteed that the date is between 1900 and 3999, both 
inclusive.

[input] integer k

A positive integer.

Constraints:

1 ≤ k ≤ 20.

[input] array.string daysOfTheWeek

Array containing from 1 to 7 distinct elements, inclusive, each of which equals 
a weekday name. Weekdays appear in the same order they are given in the description.

It's guaranteed that the day of the week on which the firstDate falls is 
present in this list.

Constraints:

1 ≤ daysOfTheWeek.length ≤ 7.

[input] integer n

Constraints:

1 ≤ n ≤ 15.

[output] array.string

Array containing the first n dates (including the first one) on which the task 
is scheduled in the chronological order.

    # n_dates = []

    # if len(daysOfTheWeek) <= 1:
    #     for i in rage(n):
    #         n_dates.append(curr_date.strftime("%d/%m/%Y"))
    #         curr_date = curr_date + timedelta(days=k*7)
    #     return n_dates

"""


