#5 errors: Character insertion, omission, substitution, transposition, gender misclassification
from auxillary import sum_num_terms_equals_total
import random
import numpy as np
import pandas as pd
import collections
import operator
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
    gender_mis_index=np.random.randint(low=0,high=len(data),size=errors['gender_mis'])
    gender_mis_data=data.iloc[gender_mis_index]
    gender_mis_error=gender_misclassification(gender_mis_data)

    char_sub_index = np.random.randint(low=0, high=len(data), size=errors['substitution'])
    char_sub_data=data.iloc[char_sub_index]

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
    col_addr=omission_addr['address']
    omission_addr['address']=char_omission(col_addr)
    omission_err=pd.concat([omission_first,omission_last,omission_addr])



    data_err=pd.concat([gender_mis_error,omission_err])
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

def character_substitution(data):
    """
    Function to induce character substitution error
    :param data: pandas dataframe
    :return: data: pandas dataframe
    """
    charactersalpha = 'qwertyuioplkjhgfdsazxcvbnm'
    charnum = '1234567890'
    error_data={'first':0,'last':0,'DOB':0,'address':0}
    val=sum_num_terms_equals_total(4,len(data))
    i=0
    for item in error_data:
        error_data[item]=val[i]
        i+=1
    sub_first=data.sample(n=error_data['first'])
    sub_first


    return

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
            if (random.randint(0, 2) == 1):
                rnd = random.randint(2, len(x) - 2)
                # print rnd
                tmp1 = random.randint(0, len(characters))
                rndCharacter = characters[tmp1:tmp1 + 1]
                # print rndCharacter
                # x[rnd:rnd+1] = rndCharacter
                x = x[0:rnd] + rndCharacter + x[rnd + 1:]
                arr[i] = x
    return arr


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