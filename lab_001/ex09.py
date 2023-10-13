# 9) Write a Python program to display the astrological sign for a given date of birth.
# Expected Result:
# Birthday entrance: 15
# Entry Month of birth (e.g. March, July, etc.): May 
# Your astrological sign is: Taurus

signs = [
    # Aquarius — Jan 20 - Feb 18
    {
        "name": "Aquarius", 
        "months" : [
            {"month":1, "min":20,"max":31}, 
            {"month":2, "min":1,"max":18}
        ]
    },
    # Pisces — Feb 19 - March 20
    {
        "name": "Pisces", 
        "months" : [
            {"month":2, "min":19,"max":29}, 
            {"month":3, "min":1,"max":20}
        ]
    },
    # Aries — March 21 - April 19.
    {
        "name": "Aries", 
        "months" : [
            {"month":3, "min":21,"max":31}, 
            {"month":4, "min":1,"max":19}
        ]
    },
    # Taurus — April 20 - May 20.
    {
        "name": "Taurus", 
        "months" : [
            {"month":4, "min":20,"max":30}, 
            {"month":5, "min":1,"max":20}
        ]
    },
    # Gemini — May 21 - June 20.
    {
        "name": "Gemini", 
        "months" : [
            {"month":5, "min":21,"max":31}, 
            {"month":6, "min":1,"max":20}
        ]
    },
    # Cancer — June 21-July 22.
    {
        "name": "Cancer", 
        "months" : [
            {"month":6, "min":21,"max":30}, 
            {"month":7, "min":1,"max":22}
        ]
    },
    # Leo — July 23-August 22.
    {
        "name": "Leo", 
        "months" : [
            {"month":7, "min":23,"max":31}, 
            {"month":8, "min":1,"max":22}
        ]
    },
    # Virgo — August 23 - September 22.
    {
        "name": "Virgo", 
        "months" : [
            {"month":8, "min":23,"max":31}, 
            {"month":9, "min":1,"max":22}
        ]
    },
    # Libra — September 23 - October 22.
    {
        "name": "Libra", 
        "months" : [
            {"month":9, "min":23,"max":30}, 
            {"month":10, "min":1,"max":22}
        ]
    },
    # Scorpio — October 23 - November 21
    {
        "name": "Scorpio", 
        "months" : [
            {"month":10, "min":23,"max":31}, 
            {"month":11, "min":1,"max":21}
        ]
    },
    # Sagittarius — November 22 - December 21
    {
        "name": "Sagittarius", 
        "months" : [
            {"month":11, "min":22,"max":30}, 
            {"month":12, "min":1,"max":21}
        ]
    },
    # Capricorn — December 22 - January 19.
    {
        "name": "Sagittarius", 
        "months" : [
            {"month":12, "min":22,"max":31}, 
            {"month":1, "min":1,"max":19}
        ]
    },
]


months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
birthday = int(input("Birthday entrance: "))
month = input("Entry Month of birth (e.g. March, July, etc.): ")
month_int = months.index(month.lower()) + 1

for s in signs:
    for m in s["months"]:
        if(m["month"] == month_int and (birthday >= m["min"] and birthday <= m["max"])):
            print(s["name"])


