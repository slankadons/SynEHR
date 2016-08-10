from auxillary import genDOB
from auxillary import genMPI
from auxillary import fake_factory
from errors import gen_errors
import numpy as np
import pandas as pd
import numpy.random as npr
import random


def data_gen(first_names_data,last_names_data,size,race_ratio,male_gender):
    ### sizes for each race

    asian_size = int(size * race_ratio['asian'])

    #print asian_size
    spanish_size = int(size * race_ratio['spanish'])
    #print spanish_size
    afr_amer_size = int(size * race_ratio['afr_amer'])
    #print afr_amer_size
    caucasian_size = int(size * race_ratio['caucasian'])
    #print caucasian_size
    native_amer_alaskan_size = int(size * race_ratio['native_amer_alaskan'])
    #print native_amer_alaskan_size
    mixed_size = int(size * race_ratio['mixed'])
    #print mixed_size


    sizes={'asian':asian_size,'spanish':spanish_size,'afr_amer':afr_amer_size,'caucasian':caucasian_size,
           'native_amer_alaskan':native_amer_alaskan_size,'mixed':mixed_size}
    print sizes






    ### sizes for each race by gender

    asian_male_size = int(sizes['asian'] * male_gender)
    asian_female_size = sizes['asian']-asian_male_size



    spanish_male_size = int(sizes['spanish'] * male_gender)
    spanish_female_size = sizes['spanish']-spanish_male_size


    afr_amer_male_size = int(sizes['afr_amer'] * male_gender)
    afr_amer_female_size = sizes['afr_amer']-afr_amer_male_size


    caucasian_male_size = int(sizes['caucasian'] * male_gender)
    caucasian_female_size = sizes['caucasian']-caucasian_male_size


    native_amer_male_size = int(sizes['native_amer_alaskan'] * male_gender)
    native_amer_female_size = sizes['native_amer_alaskan']-native_amer_male_size

    mixed_male_size = int(sizes['mixed'] * male_gender)
    mixed_female_size = sizes['mixed']-mixed_male_size


    #Collecting last names of different races and putting them in different tables

    asian_dataset_ln = last_names_data[last_names_data['race'] == 'Asian']
    spanish_dataset_ln = last_names_data[last_names_data['race'] == 'Spanish']
    afr_amer_dataset_ln = last_names_data[last_names_data['race'] == 'African_American']
    caucasian_dataset_ln = last_names_data[last_names_data['race'] == 'Caucasian']
    native_amer_alaskan_dataset_ln = last_names_data[last_names_data['race'] == 'Native_American_Alaskan']
    mixed_dataset_ln = last_names_data[last_names_data['race'] == 'Mixed']




    asian_male_fn=first_names_data.loc[(first_names_data['race']=='Asian')& (first_names_data['gender']=='M'),]
    asian_male_data=asian_male_fn.sample(n=asian_male_size,replace=True)
    asian_female_fn=first_names_data.loc[(first_names_data['race']=='Asian')& (first_names_data['gender']=='F'),]
    asian_female_data=asian_male_fn.sample(n=asian_female_size,replace=True)
    asian_data_fn=pd.concat([asian_male_data,asian_female_data])

    asian_dataset_ln = last_names_data[last_names_data['race'] == 'Asian']

    #Exract all chinese rows from data
    asian_chinese_fn=asian_data_fn.loc[(asian_data_fn['detailed_race']=='Chinese')]
    #Check how many records are there
    chinese_rows = len(asian_chinese_fn)
    #Extract Chinese Last Names
    asian_chinese_ln=asian_dataset_ln.loc[(asian_dataset_ln['detailed_race']=='Chinese')]
    #Select as many Last names randomly as you need
    last_names=asian_chinese_ln.sample(n=chinese_rows,replace=True)

    asian_chinese_fn.insert(1,'last',last_names['last'].tolist())

    chinese_rows = len(asian_chinese_fn)




    # Exract all Indian rows from data
    asian_indian_fn = asian_data_fn.loc[(asian_data_fn['detailed_race'] == 'Indian')]
    # Check how many records are there
    indian_rows = len(asian_indian_fn)
    #print "no of rows: ",indian_rows
    # Extract Indian Last Names
    asian_indian_ln = asian_dataset_ln.loc[(asian_dataset_ln['detailed_race'] == 'Indian')]
    # Select as many Last names randomly as you need
    last_names = asian_indian_ln.sample(n= indian_rows, replace=True)

    asian_indian_fn.insert(1, 'last', last_names['last'].tolist())



    asian_data_fn=pd.concat([asian_indian_fn,asian_chinese_fn])




    spanish_male_fn = first_names_data.loc[(first_names_data['race'] == 'Spanish') & (first_names_data['gender'] == 'M'),]
    spanish_male_data = spanish_male_fn.sample(n=spanish_male_size, replace=True)

    spanish_female_fn = first_names_data.loc[(first_names_data['race'] == 'Spanish') & (first_names_data['gender'] == 'F'),]
    spanish_female_data = spanish_female_fn.sample(n=spanish_female_size, replace=True)

    spanish_data_fn=pd.concat([spanish_male_data,spanish_female_data])

    spanish_ln=spanish_dataset_ln.sample(n=(spanish_male_size+spanish_female_size), replace=True)

    spanish_data_fn.insert(1,'last',spanish_ln['last'].tolist())
    print "spanish_data_fn: ", len(spanish_data_fn)
    print spanish_data_fn.isnull().any(axis=0)




    afr_amer_male_fn = first_names_data.loc[(first_names_data['race'] == 'African_American') & (first_names_data['gender'] == 'M'),]

    afr_amer_female_fn = first_names_data.loc[(first_names_data['race'] == 'African_American') & (first_names_data['gender'] == 'F'),]

    afr_amer_male_data=afr_amer_male_fn.sample(n=afr_amer_male_size,replace=True)

    afr_amer_female_data=afr_amer_female_fn.sample(n=afr_amer_female_size,replace=True)

    afr_amer_data_fn=pd.concat([afr_amer_male_data,afr_amer_female_data])

    afr_amer_ln=afr_amer_dataset_ln.sample(n=(afr_amer_male_size+afr_amer_female_size), replace=True)
    afr_amer_data_fn.insert(1,'last',afr_amer_ln['last'].tolist())

    print afr_amer_data_fn.isnull().any(axis=0)




    native_amer_male_fn=first_names_data.loc[(first_names_data['race'] == 'Native_American_Alaskan') & (first_names_data['gender'] == 'M'),]
    native_amer_female_fn = first_names_data.loc[(first_names_data['race'] == 'Native_American_Alaskan') & (first_names_data['gender'] == 'F'),]
    native_amer_male_data = native_amer_male_fn.sample(n=native_amer_male_size, replace=True)
    native_amer_female_data = native_amer_female_fn.sample(n=native_amer_female_size, replace=True)
    native_amer_data_fn = pd.concat([native_amer_male_data, native_amer_female_data])

    native_ln = native_amer_alaskan_dataset_ln.sample(n=(native_amer_male_size + native_amer_female_size), replace=True)

    native_amer_data_fn.insert(1, 'last', native_ln['last'].tolist())



    caucasian_male_fn = first_names_data.loc[(first_names_data['race'] == 'Caucasian') & (first_names_data['gender'] == 'M'),]
    caucasian_female_fn = first_names_data.loc[(first_names_data['race'] == 'Caucasian') & (first_names_data['gender'] == 'F'),]
    caucasian_male_data = caucasian_male_fn.sample(n=caucasian_male_size, replace=True)
    caucasian_female_data = caucasian_female_fn.sample(n=caucasian_female_size, replace=True)
    caucasian_data_fn = pd.concat([caucasian_male_data, caucasian_female_data])

    cauc_ln = caucasian_dataset_ln.sample(n=(caucasian_male_size + caucasian_female_size), replace=True)
    caucasian_data_fn.insert(1, 'last', cauc_ln['last'].tolist())

    mixed_dataset = first_names_data
    mixed_dataset['race'] = "Mixed"
    mixed_dataset['detailed_race']="None"

    mixed_male_fn=mixed_dataset.loc[(mixed_dataset['gender']=='M'),]
    mixed_female_fn = mixed_dataset.loc[(mixed_dataset['gender'] == 'F'),]
    mixed_male_data = mixed_male_fn.sample(n=mixed_male_size, replace=True)

    mixed_female_data = mixed_female_fn.sample(n=mixed_female_size, replace=True)
    mixed_data_fn = pd.concat([mixed_male_data, mixed_female_data])

    mixed_ln = mixed_dataset_ln.sample(n=(mixed_male_size + mixed_female_size), replace=True)
    mixed_data_fn.insert(1, 'last', mixed_ln['last'].tolist())

    Data=pd.concat([asian_data_fn, spanish_data_fn, afr_amer_data_fn, caucasian_data_fn,
                     native_amer_data_fn, mixed_data_fn],axis=0)


    print "Size of Data: ",len(Data)
    print "Name,race generated..."

    #print Data.tail()


    return Data

def mk_data(first_names_data, last_names_data, min_date, max_date, size,male_gender, race_ratio):
    """
    1. All races are inputted as integers to signify the percentages
    2. Generates Dataset based on user preferences."""
    # dataset list by race

    # data generator by race
    error_rate = int(0.1 * size)
    size_new=size-error_rate
    print "Calling the data generator function..."


    data = data_gen(first_names_data, last_names_data, size_new,race_ratio,male_gender)

    print "Generating address..."
    # fake factory
    size_records=len(data)
    addresses = fake_factory(size_records)


    data['address'] = addresses


    print "Generate DOB..."
    dates=genDOB(size_records,min_date,max_date)


    data['DOB']=dates

    print "Generate Master Patient Index..."
    mpi=genMPI(size_records)


    data.insert(0,'MPI',mpi)

    print "\n\nSize requested: ",size

    print "\n\nNumber of records generated: ",size_records

    print "\n\nInducing error in Data..."

    error_index=npr.randint(0,size_records,size=(size-size_records))

    print "\nerror_index length: ",len(error_index)

    data_err=data.iloc[error_index]


    #data_err=gen_typo(data_err)

    #data=pd.concat([data,data_err],axis=0,ignore_index=True)

    data_err=gen_errors(size=len(data_err),data=data_err)

    #print data_err

    data = pd.concat([data, data_err], axis=0, ignore_index=True)


    return data


