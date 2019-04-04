def voucher_gen():
    f = open("/var/log/voucher_gen","r+")
    job=f.read()
    job1=int(job)
    names = ['Benson Kamau"s day','Mercy Nicholas"s day','James Ngatia"s day','Njoroge Wamiti"s day','your day off ','your day off ','your day off ','your day off ','Benard Githathi"s day','Solomon Kamani"s day','Kennedy Winga"s day','Daniel Mosabi"s day','your day off ','your day off ','your day off ']
    if job1 < len(names):
        print(f'Today is {names[job1]} :)')
        f1 = open("/var/log/voucher_gen","w+")
        f1.write(str(job1+1))
        f1.close()
    else:
        f1 = open("/var/log/voucher_gen","w+")
        f1.write(str(0))
        f1.close()
        print('Today is your day off')
