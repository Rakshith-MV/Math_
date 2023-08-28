import time
from datetime import datetime
import pytz

class DataUtility():
    
    def __init__(
            self,
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
        try:
            self.holidays = []
            f = open("C:/Users/Admin/OneDrive/Desktop/holidays.dat",'r+')
            l = f.readline()
            while l != '':
                self.holidays.append(l.split(",")[1])
                l = f.readline()
        except:
            print("No file names \"holidays\" found in the directory: ")

    def convert_timezone(self,from_timezone, to_timezone, datetime_str):
        """
        Converts date time between timezones

        :param from_timezone: The timezone of the input values.
        :type from_timezone: string("UTC" for example)
        :param to_timezone: The timezone to which the dates needs to be converted to
        :type to_timezone: string("Eastern" for example)
        :param datetime_str: Date and time that need to be converted
        :type datetime_str: string(YYYY-MM-DD HH:MM:SS)
        """
        try:
            dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            
            src_timezone = pytz.timezone(from_timezone)
            dt_src = src_timezone.localize(dt)
            
            target_timezone = pytz.timezone(to_timezone)
            dt_target = dt_src.astimezone(target_timezone)
            
            return dt_target.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        except Exception as e:
            return f"Error: {e}"


    def add_dt(self,
               Fdate:str,
               num:int
               )->dict:
        """
        Adds the given number of days to the given date, and returns the end date

        :param Fdate : Initial date
        :type Fdate: string(YYYYMMDD)
        :param num: Number of days to be added.
        :type num: integer
        """
        year,month,date = map(int,(Fdate[:4],Fdate[4:6],Fdate[6:]))

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
        """ 
        Subtracts the given number of days from the given date

        :param Fdate: Initial date
        :type  Fdate: string(YYYYMMDD)
        :param num: Number of days to be added
        :type num : integer
        """
        year,month,date = map(int,(Fdate[:4],Fdate[4:6],Fdate[6:]))

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
        """
        Returns the number of days between two dates 

        :param Fdate: Initial date
        :type Fdate : string(YYYYMMDD) 
        :param Tdate: Ending Date
        :type Tdate: string(YYYYMMDD)
        """
        start_year,start_month,start_date = map(int,(Fdate[:4],Fdate[4:6],Fdate[6:]))
        end_year,end_month,end_date = map(int,(Tdate[:4],Tdate[4:6],Tdate[6:]))

        days = 0
        days+=end_date
        end_month -=1
        print("Getdays")
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

    def get_days_Excluding_Weekends(self,
                              Fdate:str,
                              Tdate:str,
                              first_weekend:int
                              )->int:
        """
        Return number of days between two dates excluding weekends(saturday and sunday)
        :param Fdate: Initial date
        :type Fdate: string(YYYYMMDD)
        :param Tdate: Ending date
        :type Tdate:  string(YYYYMMDD)
        :param first_weekend: first occurance of a sunday from the Initial date(helps to calculate the number of weekends
                                accurately(By default it's 0))
        :type first_weekend: Integer.
        """

        start_year,start_month,start_date = map(int,(Fdate[:4],Fdate[4:6],Fdate[6:]))
        end_year,end_month,end_date = map(int,(Tdate[:4],Tdate[4:6],Tdate[6:]))

        total_days = self.get_days(Fdate,Tdate)
        print(total_days)
        NumberOf_weekend_days  = int(round((total_days-first_weekend)/7,0)*2)
        print((total_days-first_weekend)%7)
        return (total_days - NumberOf_weekend_days)
    
    
    def get_business_days(self,
                          Fdate:str,
                          Tdate:str
                          )->int:
        days_exluding_weekends = self.get_days_Excluding_Weekends(Fdate,Tdate,2)
        """
        Returns number of business days between two dates(exluding weekends)
        param Fdate: Initial date
        :type Fdate: string(YYYYMMDD)
        :param Tdate: Ending date
        :type Tdate:  string(YYYYMMDD)
        """
        start_year,start_month,start_date = map(int,(Fdate[:4],Fdate[4:6],Fdate[6:]))
        end_year,end_month,end_date = map(int,(Tdate[:4],Tdate[4:6],Tdate[6:]))

        filtered_holidays  =[]
        for i in self.holidays:
            i = i.lstrip(" ").rstrip(" ")
            yy = int(i[:4])
            mm = int(i[4:6])
            dd = int(i[6:])
            if yy <= end_year and yy >= start_year:
                if yy!=end_year and yy!= start_year:
                    filtered_holidays.append(i)
                else:
                    if mm!= start_month and mm!=end_month:
                        filtered_holidays.append(i)
                    else:
                        if mm == start_month and dd >= start_date or mm == end_month and dd<=end_date:
                            filtered_holidays.append(i)
        return days_exluding_weekends - len(filtered_holidays)

    def get_date_since_epoch(self,
                             Fdate):
        """
        Returns number of days elapsed from the start of standard unix time to the given date.
        :param Fdate: Initial date(YYYY-MM-DD) and time (HH:MM:SS)
        :type Fdate: string
        """
        epoch_date = "19700101"
        date = d.convert_timezone("US/Eastern","UTC",Fdate).split(" ")[0].split("-")
        date1 = ""
        for i in date:
            date1 += i 
        print(date)
        return self.get_days(epoch_date,date1)

if __name__ == '__main__':
    d = DataUtility()
