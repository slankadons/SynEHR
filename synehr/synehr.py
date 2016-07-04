import numpy.random as npr
import numpy as np
import os
import pandas as pd
from faker import Faker
import random

def readCSV():
    """Read in master files for first name and last name"""
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_First.csv')
    first_name_columns = ['first', 'gender', 'race', 'detailed_race']
    first_names = pd.read_csv(f_name, sep=',', header=0,
                     names=first_name_columns, na_values='?')
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_Last.csv')
    last_name_columns = ['last', 'race', 'detailed_race']
    last_names = pd.read_csv(f_name, sep=',', header=0,
                     names=last_name_columns, na_values='?')
    return first_names, last_names

def fake_factory(size):
    #install('Faker')
    fake = Faker()
    addresses = []
    for _ in range(0, size):
        address = fake.address()
        addresses.append(address)
    return addresses

def data_gen(first_names_data,last_names_data,size,)


def mk_data(first_names_data, last_names_data, size=20, male_gender=.50, asian=0.0, spanish=0, afr_amer=0, caucasian=0, native_amer_alaskan=0, mixed=0):
    """
    1. All races are inputted as integers to signify the percentages
    2. Generates Dataset based on user preferences."""
    # dataset list by race
    female_gender=1-male_gender
    # data generator by race
    race_generator = race_data_generator(first_names_data, last_names_data, size, asian, spanish, afr_amer, caucasian, native_amer_alaskan, mixed, female_gender, male_gender)

    # fake factory
    addresses = fake_factory(size)

    #frames = [random_generator, race_generator]
    data = race_generator
    data['address'] = pd.DataFrame(addresses)
    print data
    #f_name = os.path.join(os.path.dirname(__file__), 'test1.csv')
    #data.to_csv(f_name)
    return data


def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    num=[]
    suml=0
    for i in range(n):
        k = npr.random()
        k = round(k, 2)
        num += [k]

    suml = sum(num)

    for i in range(n):
        num[i] = (num[i] / suml)

        num[i] *= total
        num[i] = round(num[i], 3)

    return num

class SizeValueError(Exception):
    def __init__(self):
        Exception.__init__(self,"Size  value out of range. Please choose between 100 and 1 million.")

class GenderValueError(Exception):
    def __init__(self):
        Exception.__init__(self,"Gender value out of range. Please use percentage between 0% and 100% or select None")

def syn_ehr(size=100,male_gender=None,asian=None, spanish=None, afr_amer=None, caucasian=None, native_amer_alaskan=None, mixed=None):
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

    #default=[]
        rem=1.0-sum
        n=len(default)
        #Generate n random float numbers such that sum of n numbers equals rem.
        val=constrained_sum_sample_pos(n, rem)
        i=0
        for d in default:
            default[d]=val[i]
            i+=1
    default.update(listed)
    print "Reading From Database..."
    first_names_data, last_names_data = readCSV()
    print "Read Successful..."
    #print "Asian: ",default['asian']
    #print default[asian]
    mk_data(first_names_data, last_names_data, size=size, male_gender=male_gender, asian=default['asian'],
            spanish=default['spanish'], afr_amer=default['afr_amer'],caucasian=default['caucasian'],
            native_amer_alaskan=default['native_amer_alaskan'], mixed=default['mixed'],race_ratio=default)

    return
#print '__name__'
if __name__=='__main__':

        syn_ehr()




