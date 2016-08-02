import numpy.random as npr
import numpy as np
import pandas as pd
import random
from Exceptions import SizeValueError
from Exceptions import GenderValueError
from auxillary import readCSV
from auxillary import sum_num_terms_equals_total
from data_gen import mk_data



def syn_ehr(size=1000, male_gender=None,asian=None, spanish=None, afr_amer=None, caucasian=None, native_amer_alaskan=None,
            mixed=None, min_date="1916/01/01", max_date="2014/03/01"):
    sum=0
    default={}
    listed={}
    print "In synehr"
    try:
        #if no value is specified, add it to a list of defaults else add to another list
        if(asian!=None):
            if(asian<0):
                raise ValueError
            sum+=asian
            listed['asian'] = asian
        else:
            default['asian'] = asian
        if (spanish != None):
            if (spanish < 0):
                raise ValueError
            sum += spanish
            listed['spanish'] = spanish
        else:
            default['spanish'] = spanish

        if (afr_amer != None):
            if (afr_amer < 0):
                raise ValueError
            sum += afr_amer
            listed['afr_amer'] = afr_amer
        else:
            default['afr_amer'] = afr_amer

        if (caucasian != None):
            if (caucasian < 0):
                raise ValueError
            sum += caucasian
            listed['caucasian'] = caucasian
        else:
            default['caucasian'] = caucasian

        if (mixed != None):
            if (mixed < 0):
                raise ValueError
            sum += mixed
            listed['mixed'] = mixed
        else:
            default['mixed'] = mixed

        if (native_amer_alaskan != None):
            if (native_amer_alaskan < 0):
                raise ValueError
            sum += native_amer_alaskan
            listed['native_amer_alaskan'] = native_amer_alaskan
        else:
            default['native_amer_alaskan'] = native_amer_alaskan

        if sum>1:
            raise ValueError
        if 100 >= size >= 1000000:
            raise SizeValueError
        if 0 > male_gender > 1 or male_gender!=None:
            raise GenderValueError
    except ValueError:
        print ('Sum of race values must be between 0 and 1, with each race more than 0 or None')
    else:
        if(male_gender==None):
            male_gender=npr.random()
            male_gender=round(male_gender,2)
            #print male_gender

    #default=[]
        #print "sum: ",sum
        rem=1.0-sum
        n=len(default)
        #Generate n random float numbers such that sum of n numbers equals rem.
        val=sum_num_terms_equals_total(n, rem)
        print "val: " ,val
        #sumv=sum(val)

        i=0
        for d in default:
            default[d]=round(val[i],2)
            i+=1
    default.update(listed)
    print default
    print "Reading From Database..."
    first_names_data, last_names_data = readCSV()
    last_names_data=last_names_data.dropna(how='any')
    first_names_data=first_names_data.dropna(how='any')

    print "Read Successful..."

    data=mk_data(first_names_data, last_names_data, min_date, max_date, size=size, male_gender=male_gender,race_ratio=default)

    return data
#print '__name__'
if __name__=='__main__':

        data=syn_ehr(size=100)
        print "data generated. first 5 rows:\n ",data.head()
        #print data.iloc[npr.randint(len(data),size=25)]





