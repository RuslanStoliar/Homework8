from datetime import datetime,timedelta

users =[
    {'name':'Ruslan','birthday' : datetime(year=1990, month=10, day=6)},
    {'name':'Vadim' ,'birthday' : datetime(year=1991, month=11, day=9)},
    {'name':'Andriy','birthday' : datetime(year=1992, month=11, day=8)},
    {'name':'Egor'  ,'birthday' : datetime(year=1993, month=11, day=9 )},
    {'name':'Maria' ,'birthday' : datetime(year=1994, month=11, day=10)},
    {'name':'Olga'  ,'birthday' : datetime(year=1995, month=11, day=11)},
    {'name':'Yana'  ,'birthday' : datetime(year=1996, month=11, day=12)}, 
    {'name':'Valet' ,'birthday' : datetime(year=1997, month=11, day=12)},
    {'name':'Mark',  'birthday' : datetime(year=1998, month=11, day=13)},
    {'name':'Ivan'  ,'birthday' : datetime(year=1999, month=12, day=14)},
    {'name':'Marine','birthday' : datetime(year=2000, month=11, day=13)},
    {'name':'Katya' ,'birthday' : datetime(year=2001, month=11, day=13)},
    {'name':'Yanina','birthday' : datetime(year=2002, month=11, day=15)}
]
weekday = {}
current_datetime = datetime.now()

def get_birthdays_per_week():
    
    for item in users:
            
        data = item['birthday'].replace(year =current_datetime.year )
        difference = (data -  current_datetime) + timedelta(days=1)
        format_day =  data.strftime('%A')
        if 0 < difference.days <=7:
            
            if  format_day in("Saturday","Sunday"):
                format_day = "Monday"
            if format_day in weekday:
                weekday[format_day].append(item['name'])
            else:
                weekday[format_day] = [item['name']]
                
    
    for key,value in weekday.items():
        print(f'{key} : {", ".join(value)}')          

if __name__ == "__main__":
   get_birthdays_per_week() 