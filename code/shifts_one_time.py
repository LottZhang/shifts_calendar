__author__ = 'zhazhich'
# -*- coding: UTF-8 -*-
import datetime
def strtodatetime(datestr,format):
    return datetime.datetime.strptime(datestr,format)
def datediff(beginDate,endDate):
    format="%Y%m%d";
    bd=strtodatetime(beginDate,format)
    ed=strtodatetime(endDate,format)
    oneday=datetime.timedelta(days=1)
    count=0
    while bd!=ed:
        ed=ed-oneday
        count+=1
    return count
def main():
    ban=["白","晚","休","休"]
    beginDate='20160506'
    endDate='20170101'
    count=datediff(beginDate,endDate)
    yu=count%4
    print endDate
    print count
    print ban[yu]
if __name__ == '__main__':
    main()