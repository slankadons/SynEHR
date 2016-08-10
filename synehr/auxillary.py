import os
import faker
import datetime
import numpy as np
import random
import pandas as pd
import numpy.random as npr

def readCSV():
    """Read in master files for first name and last name"""
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_First_Names.csv')
    first_name_columns = ['first', 'gender', 'race', 'detailed_race']
    first_names = pd.read_csv(f_name, sep=',', header=0,
                     names=first_name_columns, na_values='?',encoding='utf-8')
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_Last_Names.csv')
    last_name_columns = ['last', 'race', 'detailed_race']
    last_names = pd.read_csv(f_name, sep=',', header=0,
                     names=last_name_columns, na_values='?',encoding='utf-8')
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

def sum_num_terms_equals_total(num_terms, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    num = []
    if type(total) == float:
        while (total >= 0):
            term = round(random.uniform(0, total), 2)
            # print term
            num += [term]
            total -= term
            num_terms -= 1
            # print "num_terms: ", num_terms
            if (num_terms == 1):
                num += [round(total, 2)]
                break;
        # print "num: ", num


    elif type(total) == int:

        while (total >= 0):
            term = np.random.randint(0, total)
            print term
            num += [term]
            total -= term
            num_terms -= 1
            # print "num_terms: ", num_terms
            if (num_terms == 1):
                num += [total]
                break;
    return num

def genMPI(size):
    """
    Generates a Master Patient Index for the dataset
    :param size:
    :return: List of Master Patient Indices
    """
    hosp="HOSP"
    MPI=[]
    for i in range(size):
        mpi=hosp+str(i)
        MPI+=[mpi]

    return MPI

