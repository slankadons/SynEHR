#5 errors: Character insertion, omission, substitution, transposition, gender misclassification
from auxillary import sum_num_terms_equals_total
import random
import numpy as np
import pandas as pd
import collections
import operator
import datetime
def gen_errors(size,data):
    """
    A function to generate the different types of errors in the data
    :param size: int,data: pandas dataframe
    :return: data_err: pandas dataframe
    """
    #initializing a dictionary of all the errors to be generated
    errors={'insertion':0,'omission':0,'substitution':0,'transposition':0,'gender_mis':0}
    val=sum_num_terms_equals_total(5,size)
    i=0
    for item in errors:
        errors[item]=int(val[i])
        i+=1
    sume=sum(errors.values())
    if sum!=size:
        item=random.choice(errors.keys())
        if sume>size:
            rem=sume-size
            errors[item]-=rem
        else:
            rem=size-sume
            errors[item]+=rem
    #print errors
    #print sum(errors.values())

    # Insertion Code
    insertion_index = np.random.randint(low=0,high=len(data), size=errors['insertion'])
    insertion_data = data.iloc[insertion_index]
    insertion_err={'first':0,'last':0,'DOB':0,'address':0}
    val = sum_num_terms_equals_total(4, len(insertion_data))
    # print val
    i = 0
    for item in insertion_err:
        insertion_err[item] = int(val[i])
        i += 1
    insertion_first = insertion_data.sample(n=insertion_err['first'])
    col_first = insertion_first['first'].tolist()
    insertion_first['first'] = char_insertion_str(col_first)

    insertion_last = insertion_data.sample(n=insertion_err['last'])
    col_last = insertion_last['last'].tolist()
    insertion_last['last'] = char_insertion_str(col_last)

    insertion_addr = insertion_data.sample(n=insertion_err['address'])
    col_addr = insertion_addr['address'].tolist()
    insertion_addr['address'] = char_insertion_str(col_addr)

    insertion_err = pd.concat([insertion_first, insertion_last, insertion_addr])


    gender_mis_index=np.random.randint(low=0,high=len(data),size=errors['gender_mis'])
    gender_mis_data=data.iloc[gender_mis_index]
    gender_mis_error=gender_misclassification(gender_mis_data)

    char_sub_index = np.random.randint(low=0, high=len(data), size=errors['substitution'])
    char_sub_data=data.iloc[char_sub_index]
    sub_err={'first':0,'last':0,'DOB':0,'address':0}
    val = sum_num_terms_equals_total(4, len(char_sub_data))
    # print val
    i = 0
    for item in sub_err:
        sub_err[item] = int(val[i])
        i += 1
    sub_first = char_sub_data.sample(n=sub_err['first'])
    col_first = sub_first['first'].tolist()
    sub_first['first'] = char_sub_str(col_first)
    # print omission_first['first']

    sub_last = char_sub_data.sample(n=sub_err['last'])
    col_last = sub_last['last'].tolist()
    sub_last['last'] = char_sub_str(col_last)

    sub_addr = char_sub_data.sample(n=sub_err['address'])
    col_addr = sub_addr['address'].tolist()
    sub_addr['address'] = char_sub_str(col_addr)

    sub_DOB=char_sub_data.sample(n=sub_err['DOB'])
    col_DOB=sub_DOB['DOB'].tolist()
    sub_DOB['DOB']=char_sub_date(col_DOB)
    print "date error: ",sub_DOB.head()

    sub_err = pd.concat([sub_first, sub_last, sub_addr])

    char_omission_index=np.random.randint(low=0,high=len(data),size=errors['omission'])
    char_omission_data=data.iloc[char_omission_index]
    omission_err={'first':0,'last':0,'address':0}
    val=sum_num_terms_equals_total(3,len(char_omission_data))
    #print val
    i=0
    for item in omission_err:
        omission_err[item]=int(val[i])
        i+=1
    omission_first=char_omission_data.sample(n=omission_err['first'])
    col_first=omission_first['first'].tolist()
    omission_first['first']=char_omission(col_first)
    #print omission_first['first']
    omission_last=char_omission_data.sample(n=omission_err['last'])
    col_last=omission_last['last'].tolist()
    omission_last['last']=char_omission(col_last)
    omission_addr=char_omission_data.sample(n=omission_err['address'])
    col_addr=omission_addr['address'].tolist()
    omission_addr['address']=char_omission(col_addr)
    omission_err=pd.concat([omission_first,omission_last,omission_addr])



    data_err=pd.concat([insertion_err, gender_mis_error,omission_err,sub_err])
    return data_err

def gender_misclassification(data):
    """
    Function to generate gender misclassification errors
    :param size: int, data: pandas dataframe
    :return: data_gen: pandas dataframe
    """
    #print "Before swap: ",data['gender']
    data['gender'].replace('M','O', inplace=True)
    data['gender'].replace('F','M', inplace=True)
    data['gender'].replace('O', 'F', inplace=True)
    #print "after swap: ",data['gender']
    #return data


def char_omission(col_data):
    """
    Function Omits a character at random
    :param col_data: column of  dataframe: column to induce the error in
    :return: col_data: error induced column
    """
    for i in range(len(col_data)):
        c=col_data[i]
        #print "c: ",c
        letters=collections.Counter(c)
        #print letters
        maxValue = max(letters.values())
        keys=[key for key in letters if letters[key]==maxValue]
        key=random.choice(keys)

        #print "keys: ",keys

        ind=c.find(key)
        #print "index: ", ind
        #print c[0:ind]
        #print c[(ind+1):]
        c=c[0:ind]+c[(ind+1):]
        col_data[i]=c
        #print col_data[i]
    return col_data


def char_sub_str(arr):
    """
    Generates characters substitution error in string
    :param Data:
    :return:
    """
    characters = 'qwertyuioplkjhgfdsazxcvbnm'

    for i in range(0, len(arr)):
        x = arr[i]
        # print x
        # print len(x)
        if len(x) > 3:
            rnd = random.randint(2, len(x) - 2)
            # print rnd
            tmp1 = random.randint(0, len(characters))
            rndCharacter = characters[tmp1:tmp1 + 1]
            # print rndCharacter
            # x[rnd:rnd+1] = rndCharacter
            x = x[0:rnd] + rndCharacter + x[rnd + 1:]
            arr[i] = x
    return arr


def char_sub_date(col_date):
    """
    Function to induce character substitution error in date column
    :param col_date: array
    :return:
    """
    new_dates=[]
    for date in col_date:
        date=date.strftime('%Y/%m/%d')
        year,month,day=date.split('/')
        #year=int(year[-2:])
        month=(month)
        day=(day)
        ind=[0,1,2]
        choice=random.choice(ind)
        if choice == 0:
            c=random.randint(0,9)
            ind=random.randint(2,3)
            year=list(year)
            #print "split year: ",year
            year[ind]=str(c)
            year=''.join(year)
            #print "Error induced year: ",year
        elif choice == 1:
            month=str(random.randint(1,12))
            #print "error induced month: ",month
        elif choice == 2:
            if int(month) in [1,3,5,7,8,10,12]:
                day=str(random.randint(1,31))
            elif int(month) in [4,6,9,11]:
                day=str(random.randint(1,30))
            else:
                day=str(random.randint(1,28))
        date_err='/'.join([year,month,day])
        date=datetime.datetime.strptime(date_err,"%Y/%m/%d")
        new_dates+=[date]
    return new_dates


def char_insertion_str(arr):
    """
    Generates characters substitution error in string
    :param Data:
    :return:
    """
    characters = 'qwertyuioplkjhgfdsazxcvbnm'
    print "insertion before", arr
    for i in range(0, len(arr)):
        x = arr[i]
        # print x
        # print len(x)
        if len(x) > 3:
            rnd = random.randint(2, len(x) - 2)
            # print rnd
            tmp1 = random.randint(0, len(characters))
            rndCharacter = characters[tmp1:tmp1 + 1]
            # print rndCharacter
            # x[rnd:rnd+1] = rndCharacter
            x = x[0:rnd] + rndCharacter + x[rnd:]
            arr[i] = x
    print "insertion after: ", arr
    return arr






