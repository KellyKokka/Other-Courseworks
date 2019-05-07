# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 01:36:31 2018

@author: kelly
"""
#phase1
def myHealthcare(n):
    import random
    id,temp,heart,pulse,blood,respi,oxyg,ph,health_list=[],[],[],[],[],[],[],[],[]
    random.seed(404)
    for j in range(n):
        id.append(j)
        temp.append(random.randint(36,39))
        heart.append(random.randint(55,100))
        pulse.append(random.randint(55,100))
        blood.append(random.randint(120,121))
        respi.append(random.randint(11,17))
        oxyg.append(random.randint(93,100))
        ph.append(round(random.uniform(7.1, 7.6),1))
        health_list+=[[id[j],temp[j],heart[j],pulse[j],blood[j],respi[j],oxyg[j],ph[j]]]   
    from matplotlib import pyplot as plt #i used this code in order to show some results in phase2
    plt.scatter(id,pulse)
    plt.title("Random pulse rate")
    plt.xlabel("id")
    plt.ylabel("pulse")
    plt.show()
    return health_list     
phase1=myHealthcare(1000)

#phase2
def AbnormalSignAnalytics(health_list):
    import random
    random.seed(404)
    samp1=random.sample(health_list,50)
    samp2=random.sample(health_list,50)
    search_pulse,search_blood,pulse,id,search=[],[],[],[],[]
    for i in range(50):
        pulse+=[health_list[i][3]]
        id+=[health_list[i][0]]#I used it only in plots 
        if (samp1[i][3]>=55 and samp1[i][3]<=59) or samp1[i][3]==100:
            search_pulse+=[[samp1[i][0],samp1[i][3]]]
            search+=[samp1[i][3]]#used only in plots
        if samp2[i][4]==120:
            search_blood+=[[samp2[i][0],samp2[i][4]]]
    from matplotlib import pyplot as plt #some plots 
    plt.hist(pulse)
    plt.title("Frequency Histogram")
    plt.xlabel("Pulse")
    plt.ylabel("Frequency")
    plt.show()
    plt.hist(search)
    plt.title("Frequency Histogram")
    plt.xlabel("Pulse")
    plt.ylabel("Frequency")
    plt.show()
    plt.boxplot(search_pulse)
    plt.title("Boxplot of abnormal pulse")
    plt.xlabel("Pulse")
    plt.ylabel("id")
    plt.show()
    plt.scatter(search_pulse[0],search_pulse[1])
    plt.title("Frequency Histogram of sample=50 ")
    plt.xlabel("Abnormal values of Pulse")
    plt.ylabel("Frequency")
    plt.show()  
    plt.scatter(id,pulse)
    plt.title("Random values chosen for a sample=50 ")
    plt.xlabel("id")
    plt.ylabel("Abnormal values of pulse")
    plt.show()       
    return search_pulse
    return search_blood        
print(AbnormalSignAnalytics(phase1))
#Phase3
def healthAnalyzer(health_list):
    lst,coeur=[],[]
    for i in range(len(health_list)):
       if health_list[i][3]==56:
          lst+=[health_list[i]]
          coeur+=[health_list[i][2]]
    from matplotlib import pyplot as plt
    plt.hist(coeur)
    plt.title("Frequency Histogram of heart rate values for pulse=56")
    plt.xlabel("Heart rates")
    plt.ylabel("Frequency")
    plt.show()
    return lst
print(healthAnalyzer(phase1))
#phase4
def benchmarking(n):
    import time
    start=time.time()
    import random
    id,temp,heart,pulse,blood,respi,oxyg,ph,health_list=[],[],[],[],[],[],[],[],[]
    random.seed(404)
    for j in range(n):
        id.append(j)
        temp.append(random.randint(36,39))
        heart.append(random.randint(55,100))
        pulse.append(random.randint(55,100))
        blood.append(random.randint(120,121))
        respi.append(random.randint(11,17))
        oxyg.append(random.randint(93,100))
        ph.append(round(random.uniform(7.1, 7.6),1))
        health_list+=[[id[j],temp[j],heart[j],pulse[j],blood[j],respi[j],oxyg[j],ph[j]]]
    end=time.time()
    return end-start
timer=[]
values=[1000,2500,5000,7500,10000]
timer=[benchmarking(1000),benchmarking(2500),benchmarking(5000),benchmarking(7500),benchmarking(10000)]
from matplotlib import pyplot as plt
plt.scatter(values,timer)
plt.title("Time")
plt.xlabel("Values")
plt.ylabel("Time")
plt.show()   