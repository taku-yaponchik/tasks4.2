def make_car(**kwargs): #kwargs - key word arguments
    for key, value in kwargs.items():
        print(key.title()+':',value.title())

make_car(name='subaru',volume='outback', color="blue", weight=str(1500)) 
