def voucher_gen():
    f = open("/var/log/voucher_gen","r+")
    job=f.read()
    job1=int(job)
    names = ['Benson Kamaus day','Mercy Nicholass day','James Ngatias day','Njoroge Wamitis day','your day off ','your day off ','your day off ','your day off ','Benard Githathis day','Solomon Kamanis day','Kennedy Wingas day','Daniel Mosabis day','your day off ','your day off ','your day off '] 
    if job1 < len(names):
        print(f'Today is {names[job1]} :)')
        f1 = open("/var/log/voucher_gen","w+")
        f1.write(str(job1+1))
        f1.close()
        f2 = open("/var/www/html/index.html","w+")
        f2.write(f"<!DOCTYPE html><html><body><h1>Today is {names[job1]} </h1></body></html>")
        f2.close()
    else:
        f1 = open("/var/log/voucher_gen","w+")
        f1.write(str(0))
        f1.close()
        f2 = open("/var/www/html/index.html","w+")
        f2.write(f"<!DOCTYPE html><html><body><h1>Today is your day off </h1></body></html>")
        f2.close()
        print('Today is your day off')
voucher_gen()
