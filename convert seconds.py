time=int(input("enter your seconds:"))
day=time//(24*3600)
time= time% (24*3600)
time%=24*3600
hours=time//3600
time%=3600
minute=time//60
time%=60
seconds=1
time%=1
print("days:%dhour:%dminute:%dsecond:%d"%(day,hours,minute,seconds))