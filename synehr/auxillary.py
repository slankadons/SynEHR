import os
import faker
import datetime
import numpy as np
import random
import pandas as pd

def readCSV():
    """Read in master files for first name and last name"""
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_First_Names.csv')
    first_name_columns = ['first', 'gender', 'race', 'detailed_race']
    first_names = pd.read_csv(f_name, sep=',', header=0,
                     names=first_name_columns, na_values='?',encoding='latin-1')
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_Last_Names.csv')
    last_name_columns = ['last', 'race', 'detailed_race']
    last_names = pd.read_csv(f_name, sep=',', header=0,
                     names=last_name_columns, na_values='?',encoding='latin-1')
    return first_names, last_names

def fake_factory(size):
    #install('Faker')
    fake = faker.Faker()
    addresses = []
    for _ in range(0, size):
        address = fake.address()
        addresses.append(address)
    return addresses

def genDOB(size,min_Date,max_Date):
    dob=[]
    # How many seconds between [date] and [01/03/2014]? That will be maxSeconds
    minDate=datetime.datetime.strptime(min_Date,"%Y/%m/%d")
    #refDate = datetime.strptime(DateOfBirth.ToString(), "%d/%m/%Y %H:%M:%S")
    # In above, be careful that your locale is returning dates in a matching format
    maxDate = datetime.datetime.strptime(max_Date, "%Y/%m/%d")
    # Calculate the difference between the starting date and the maximum date
    timeDifference = maxDate - minDate
    maxSeconds = timeDifference.total_seconds()
    for _ in range(0,size):

        # Choose a random number between 1 and secondsMax
        randSeconds = random.randrange(0, maxSeconds)
        # Add the random number of seconds to the original date
        retDate = minDate + datetime.timedelta(seconds=randSeconds)
        dob.append(retDate)
    return dob

def constrained_sum_sample_pos(num_terms, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    num=np.random.dirichlet(np.ones(num_terms), size=1)
    num=num[0]
    num/=num.sum()
    num*=total
    #print "sum before rounding and correction: ",num.sum()

    for item in num:
        item=round(item,2)
    sum=num.sum()
    if(sum!=total):
        k = random.choice(range(0, num_terms))
        if sum>total:
            rem=sum-total
            num[k]-=rem
        else:
            rem=total-sum
            num[k]+=sum

    #print "After correction: ",num.sum()
    return num
