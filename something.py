

class DataUtility():
    
    def __init__(
            self,
            t,
            file="holidays"):
        self.months = [i for i in range(12)]
        self.days = [31,28,31,
                     30,31,30,
                     31,31,30,
                     31,30,31]
        self.days_leap = [31,29,31,
                     30,31,30,
                     31,31,30,
                     31,30,31]
        self.Time_zone = t
        self.holidays = []
        f = open(file+".dat",'r')
        l = f.readline()
        while l != '':
            self.holidays.append(l.split(",")[1])
            l = f.readline()


    def convert_dt():
        None

    def add_dt(self,
               Fdate:str,
               num:int
               )->dict:
        year = int(Fdate[:4])
        month = int(Fdate[4:6])
        date = int(Fdate[6:])
        while True:
            day_info = self.days
            if year%4 == 0:
                day_info = self.days_leap
            
            if num+date <= day_info[month-1]:
                date+=num
                break
            else:
                num = num+date - day_info[month-1]
                date = 0

                check_year = month +1
                month= (month + 1)%12
                if check_year!= month:
                    year+=1
        return {str(year)+str(month)+str(date)}                
            

    def sub_dt(self,
               Fdate:str,
               num:int
               )->dict:
        year = int(Fdate[:4])
        month = int(Fdate[4:6])
        date = int(Fdate[6:])
        while True:
            day_info = self.days
            if year%4 == 0:
                day_info = self.days_leap
            if date-num > 0 :
                date-=num
                break
            else:
                num = num-date
                date = day_info[self.month-2]
                
                check_year = month - 1
                month = (month-1)%12
                if month == 0:
                    month = 12
                if check_year != month:
                    year-=1

        return {str(year)+str(month)+str(date)}                

    def get_days(self,
                 Fdate,
                 Tdate
                 )->int:
        start_year = int(Fdate[:4])
        start_month = int(Fdate[4:6])
        start_date = int(Fdate[6:])
        end_year = int(Tdate[:4])
        end_month = int(Tdate[4:6])
        end_date = int(Tdate[6:])
        days = 0
        days+=end_date
        end_month -=1

        while end_year!=start_year:
            day_info = self.days
            if end_year%4 == 0:
                day_info = self.days_leap

            for i in range(end_month):
                days+=day_info[i]
            # print(end_year,days)
            end_year-=1
            # print(end_year)
            end_month = 12

        while end_month!=start_month:
            days+=day_info[end_month-1]
            # print(end_month,days)
            end_month-=1

        end_date = day_info[end_month-1]

        while end_date != start_date:
            days+=1
            # print(end_date)

            end_date-=1
        return days

    def get_days_ExcludingWeekends(self,
                              Fdate:str,
                              Tdate:str,
                              first_weekend:int
                              )->int:
        start_year = int(Fdate[:4])
        start_month = int(Fdate[4:6])
        start_date = int(Fdate[6:])
        end_year = int(Tdate[:4])
        end_month = int(Tdate[4:6])
        end_date = int(Tdate[6:])

        total_days = self.get_days(Fdate,Tdate)
        print(total_days)
        NumberOf_weekend_days  = ((total_days-first_weekend)//7)*2
        return (total_days - NumberOf_weekend_days)
    
    #a bit of altertion is required.

    
    def get_business_days(self,
                          Fdate:str,
                          Tdata:str
                          )->int:
        


if __name__ == '__main__':
    d = DataUtility(13.50)

    print(d.get_business_days("20030515","20230827"))

