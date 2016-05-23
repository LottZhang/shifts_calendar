__author__ = 'zhazhich'
# -*- coding: UTF-8 -*-
import calendar
import datetime
import ConfigParser
import codecs
import sys
def conf_set():
    global year, month, first_day_week, beginDate, ban
    cf=ConfigParser.ConfigParser()
    cf.readfp(codecs.open(".\conf.conf", "r", "utf-8-sig"))
    #cf.read(".\conf.conf")
    secs=cf.sections()
    opts=cf.options("shifts_calendar")
    kvs = cf.items("shifts_calendar")
    year = cf.getint("shifts_calendar", "year")
    month = cf.getint("shifts_calendar", "month")
    first_day_week = cf.getint("shifts_calendar", "first_day_week")
    beginDate = cf.get("shifts_calendar", "beginDate")
    ban = cf.get("shifts_calendar", "ban")
def formatdata(j,year,month):
        if j<10 and month <10:
            str='%s0%s0%s' %(year,month,j)
        elif j<10 and month >10:
            str='%s%s0%s' %(year,month,j)
        elif j>10 and month <10:
            str='%s0%s%s' %(year,month,j)
        else:
            str='%s%s%s' %(year,month,j)
        return str
def strtodatetime(datestr,format):
    return datetime.datetime.strptime(datestr,format)
def datediff(beginDate,endDate):
    format="%Y%m%d"
    bd=strtodatetime(beginDate,format)
    ed=strtodatetime(endDate,format)
    oneday=datetime.timedelta(days=1)
    count=0
    while bd!=ed:
        ed=ed-oneday
        count+=1
    return count
def monthday(year,month,y):
    for i in range(month,13):
        b=calendar.monthrange(year,i)
        b=list(b)
#       x=b[0]
        y.append(b[1])

def main():
    global year, month, first_day_week, beginDate, ban
    y=[]
    conf_set()
    #ban = ["白","晚","休","休"]
#    ban=["1","2","3","3"]
    ban=list(ban)
    D=""
    d=("日一二三四五六").decode("utf-8")
    monthday(year,month,y)
    reload(sys)
    sys.setdefaultencoding("utf-8")
    file = open(".\shifts_calendar_result.txt",'w')
    sys.stdout=file
    print ('%d年' %year)
    print '#'*22
    for i in y:
        print str(month)+' 月'
        print '#'*22
        for k in range(7):
            D +=("%2s" %d[k])
        print D
        D=" "
        j=0
        s=''
        for z in range(first_day_week):
            s +='   '
        while True:
            first_day_week += 1
            j += 1

            endDate=formatdata(j,year,month)
            count=datediff(beginDate,endDate)
            yu=count%len(ban)
            #if len(str(j))==1:
             #   D +=("%2s" %(str(j))+' '
            #else:
             #   D +=str(j)+' '
            D +=("%s" %(ban[yu]))+' '


            if first_day_week>6:
                print s+D
                first_day_week=0
                D=" "
                s=''
            if j==i:
                print D
                print '#'*22
                D=""
                break
        month +=1
    file.close()
if __name__ == '__main__':
    main()