import numpy.random as npr
import numpy as np
import os
import pandas as pd
#from faker import Factory
import faker
import random

from datetime import datetime

from datetime import timedelta

def readCSV():
    """Read in master files for first name and last name"""
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_First_Names_t.csv')
    first_name_columns = ['first', 'gender', 'race', 'detailed_race']
    first_names = pd.read_csv(f_name, sep=',', header=0,
                     names=first_name_columns, na_values='?')
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_Last_Names.csv')
    last_name_columns = ['last', 'race', 'detailed_race']
    last_names = pd.read_csv(f_name, sep=',', header=0,
                     names=last_name_columns, na_values='?')
    return first_names, last_names

def fake_factory(size):
    #install('Faker')
    fake = faker.Faker()
    addresses = []
    for _ in range(0, size):
        address = fake.address()
        addresses.append(address)
    return addresses

def genDOB(size):
    dob=[]
    # How many seconds between [date] and [01/03/2014]? That will be maxSeconds
    minDate=datetime.strptime("1916/01/01","%Y/%m/%d")
    #refDate = datetime.strptime(DateOfBirth.ToString(), "%d/%m/%Y %H:%M:%S")
    # In above, be careful that your locale is returning dates in a matching format
    maxDate = datetime.strptime("01/03/2014", "%d/%m/%Y")
    # Calculate the difference between the starting date and the maximum date
    timeDifference = maxDate - minDate
    maxSeconds = timeDifference.total_seconds()
    for _ in range(0,size):

        # Choose a random number between 1 and secondsMax
        randSeconds = random.randrange(0, maxSeconds)
        # Add the random number of seconds to the original date
        retDate = minDate + timedelta(seconds=randSeconds)
        dob.append(retDate)
    return dob

def data_gen(first_names_data,last_names_data,size,race_ratio,male_gender):
    ### sizes for each race
    female_gender=1-male_gender

    asian_size = int(size * race_ratio['asian'])
    #print asian_size
    spanish_size = int(size * race_ratio['spanish'])
    afr_amer_size = int(size * race_ratio['afr_amer'])
    print afr_amer_size
    caucasian_size = int(size * race_ratio['caucasian'])
    native_amer_alaskan_size = int(size * race_ratio['native_amer_alaskan'])
    mixed_size = int(size * race_ratio['mixed'])
    #print mixed_size

    ### sizes for each race by gender

    asian_male_size = int(asian_size * male_gender)
    asian_female_size = int(asian_size * female_gender)
    spanish_male_size = int(spanish_size * male_gender)
    #print spanish_male_size
    spanish_female_size = int(spanish_size * female_gender)
    afr_amer_male_size = int(afr_amer_size * male_gender)
    print "afr_amer_male_size: ",afr_amer_male_size
    afr_amer_female_size = int(afr_amer_size * female_gender)
    print "afr_amer_female_size: ",afr_amer_female_size
    caucasian_male_size = int(caucasian_size * male_gender)
    caucasian_female_size = int(caucasian_size * female_gender)
    #print caucasian_male_size
    native_amer_male_size = int(native_amer_alaskan_size * male_gender)
    native_amer_female_size = int(native_amer_alaskan_size * female_gender)
    #print native_amer_female_size
    mixed_male_size = int(mixed_size * male_gender)
    mixed_female_size = int(mixed_size * female_gender)

    #Collecting last names of different races and putting them in tables

    asian_dataset_ln = last_names_data[last_names_data['race'] == 'Asian']
    spanish_dataset_ln = last_names_data[last_names_data['race'] == 'Spanish']
    afr_amer_dataset_ln = last_names_data[last_names_data['race'] == 'African_American']
    caucasian_dataset_ln = last_names_data[last_names_data['race'] == 'Caucasian']

    #print caucasian_dataset_ln

    native_amer_alaskan_dataset_ln = last_names_data[last_names_data['race'] == 'Native_American_Alaskan']
    mixed_dataset_ln = last_names_data[last_names_data['race'] == 'Mixed']




    asian_male_fn=first_names_data.loc[(first_names_data['race']=='Asian')& (first_names_data['gender']=='M'),]
    asian_male_data=asian_male_fn.sample(n=asian_male_size,replace=True)
    asian_female_fn=first_names_data.loc[(first_names_data['race']=='Asian')& (first_names_data['gender']=='F'),]
    asian_female_data=asian_male_fn.sample(n=asian_female_size,replace=True)
    asian_data_fn=pd.concat([asian_male_fn,asian_female_fn])
    #print "Asian First Names Data: ",asian_data_fn.tail()
    asian_dataset_ln = last_names_data[last_names_data['race'] == 'Asian']
    #print asian_dataset_ln.head()

    #Exract all chinese rows from data
    asian_chinese_fn=asian_data_fn.loc[(asian_data_fn['detailed_race']=='Chinese')]
    #Check how many records are there
    chinese_rows=len(asian_chinese_fn)
    #print "no of rows: ",chinese_rows
    #Extract Chinese Last Names
    asian_chinese_ln=asian_dataset_ln.loc[(asian_dataset_ln['detailed_race']=='Chinese')]
    #Select as many Last names randomly as you need
    last_names=asian_chinese_ln.sample(n=chinese_rows,replace=True)
    #print "LAst names: ",len(last_names)
    #print last_names['last']
    #print asian_chinese_fn.head()
    asian_chinese_fn.insert(1,'last',last_names['last'].tolist())
    #print "Chinese Data Head: ",asian_chinese_fn.head()

    # Exract all Indian rows from data
    asian_indian_fn = asian_data_fn.loc[(asian_data_fn['detailed_race'] == 'Indian')]
    # Check how many records are there
    indian_rows = len(asian_indian_fn)
    print "no of rows: ",indian_rows
    # Extract Chinese Last Names
    asian_indian_ln = asian_dataset_ln.loc[(asian_dataset_ln['detailed_race'] == 'Indian')]
    # Select as many Last names randomly as you need
    last_names = asian_indian_ln.sample(n= indian_rows, replace=True)
    # print "LAst names: ",len(last_names)
    # print last_names['last']
    # print asian_chinese_fn.head()
    asian_indian_fn.insert(1, 'last', last_names['last'].tolist())
    #print "Indian Data Head: ",asian_indian_fn.head()
    asian_data_fn=pd.concat([asian_indian_fn,asian_chinese_fn])
    #print "Asian_data head: ", asian_data_fn.head()



    spanish_male_fn = first_names_data.loc[(first_names_data['race'] == 'Spanish') & (first_names_data['gender'] == 'M'),]
    spanish_male_data = spanish_male_fn.sample(n=spanish_male_size, replace=True)
    #print len(spanish_male_data)
    spanish_female_fn = first_names_data.loc[(first_names_data['race'] == 'Spanish') & (first_names_data['gender'] == 'F'),]
    spanish_female_data = spanish_male_fn.sample(n=spanish_female_size, replace=True)
    #print len(spanish_female_data)
    spanish_data_fn=pd.concat([spanish_male_data,spanish_female_data])
    #print spanish_male_size+spanish_female_size

    spanish_ln=spanish_dataset_ln.sample(n=(spanish_male_size+spanish_female_size), replace=True)
    #print len(spanish_ln)
    #print "spanish_data_fn: ",len(spanish_data_fn)
    spanish_data_fn.insert(1,'last',spanish_ln['last'].tolist())
    #print "Spanish Data Head: ",spanish_data_fn.head()



    afr_amer_male_fn = first_names_data.loc[(first_names_data['race'] == 'African_American') & (first_names_data['gender'] == 'M'),]
    print "afro male:", len(afr_amer_male_fn)
    afr_amer_female_fn = first_names_data.loc[(first_names_data['race'] == 'African_American') & (first_names_data['gender'] == 'F'),]
    print "afro female: ",len(afr_amer_female_fn)
    afr_amer_male_data=afr_amer_male_fn.sample(n=afr_amer_male_size,replace=True)
    print len(afr_amer_male_data)
    afr_amer_female_data=afr_amer_female_fn.sample(n=afr_amer_female_size,replace=True)
    print len(afr_amer_female_data)
    afr_amer_data_fn=pd.concat([afr_amer_male_data,afr_amer_female_data])

    afr_amer_ln=afr_amer_dataset_ln.sample(n=(afr_amer_male_size+afr_amer_female_size), replace=True)
    afr_amer_data_fn.insert(1,'last',afr_amer_ln['last'].tolist())
    print "African American Head: ",afr_amer_female_fn.head()



    native_amer_male_fn=first_names_data.loc[(first_names_data['race'] == 'Native_American_Alaskan') & (first_names_data['gender'] == 'M'),]
    native_amer_female_fn = first_names_data.loc[(first_names_data['race'] == 'Native_American_Alaskan') & (first_names_data['gender'] == 'F'),]
    native_amer_male_data = native_amer_male_fn.sample(n=native_amer_male_size, replace=True)
    native_amer_female_data = native_amer_female_fn.sample(n=native_amer_female_size, replace=True)
    native_amer_data_fn = pd.concat([native_amer_male_data, native_amer_female_data])
    print "nat fn len: ",len(native_amer_data_fn)

    native_ln = native_amer_alaskan_dataset_ln.sample(n=(native_amer_male_size + native_amer_female_size), replace=True)
    print native_ln.head()
    print "Length of Nat last names:",len(native_ln)
    native_amer_data_fn.insert(1, 'last', native_ln['last'].tolist())

    print native_amer_data_fn.head()

    caucasian_male_fn = first_names_data.loc[(first_names_data['race'] == 'Caucasian') & (first_names_data['gender'] == 'M'),]
    caucasian_female_fn = first_names_data.loc[(first_names_data['race'] == 'Caucasian') & (first_names_data['gender'] == 'F'),]
    caucasian_male_data = caucasian_male_fn.sample(n=caucasian_male_size, replace=True)
    caucasian_female_data = caucasian_female_fn.sample(n=caucasian_female_size, replace=True)
    caucasian_data_fn = pd.concat([caucasian_male_data, caucasian_female_data])

    cauc_ln = caucasian_dataset_ln.sample(n=(caucasian_male_size + caucasian_female_size), replace=True)
    caucasian_data_fn.insert(1, 'last', cauc_ln['last'].tolist())

    mixed_dataset = first_names_data.sample(n=mixed_size * 1000, replace=True)
    mixed_dataset['race'] = "Mixed"
    mixed_dataset['detailed_race']="None"

    mixed_male_fn=mixed_dataset.loc[(mixed_dataset['gender']=='M'),]
    mixed_female_fn = mixed_dataset.loc[(mixed_dataset['gender'] == 'F'),]
    mixed_male_data = mixed_male_fn.sample(n=mixed_male_size, replace=True)
    print "Mixed Male: ",mixed_male_data.head()
    mixed_female_data = mixed_female_fn.sample(n=mixed_female_size, replace=True)
    print "Mixed Female: ",mixed_female_data.head()
    mixed_data_fn = pd.concat([mixed_male_data, mixed_female_data])
    print "Mixed Lastnames Length: ",len(mixed_dataset_ln)
    mixed_ln = mixed_dataset_ln.sample(n=(mixed_male_size + mixed_female_size), replace=True)
    mixed_data_fn.insert(1, 'last', mixed_ln['last'].tolist())

    Data=pd.concat([asian_data_fn, spanish_data_fn, afr_amer_data_fn, caucasian_data_fn,
                     native_amer_data_fn, mixed_data_fn])

    print "Final Data looks like this: ", Data.head()

    print Data.tail()


    return Data

def mk_data(first_names_data, last_names_data, size, male_gender,race_ratio={}):
    """
    1. All races are inputted as integers to signify the percentages
    2. Generates Dataset based on user preferences."""
    # dataset list by race

    # data generator by race
    #print first_names_data.head()
    #print last_names_data.head()
    #print size
    #print race_ratio
    race_generator = data_gen(first_names_data, last_names_data, size,race_ratio,male_gender)

    # fake factory
    addresses = fake_factory(size)

    #frames = [random_generator, race_generator]
    data = race_generator
    data['address'] = pd.DataFrame(addresses)
    print data.head()

    dates=genDOB(size)
    #f_name = os.path.join(os.path.dirname(__file__), 'test1.csv')
    #data.to_csv(f_name)
    data['DOB']=pd.DataFrame(dates)
    print data.head()
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
    #print first_names_data.head()
    #print last_names_data.head()
    print "Read Successful..."
    #print "Asian: ",default['asian']
    #print default[asian]
    mk_data(first_names_data, last_names_data, size=size, male_gender=male_gender,race_ratio=default)

    return
#print '__name__'
if __name__=='__main__':

        syn_ehr()




