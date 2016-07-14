#5 errors: Character insertion, omission, substitution, transposition, gender misclassification
from auxillary import sum_num_terms_equals_total
import random
import numpy as np
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
    print errors
    print sum(errors.values())
    gender_mis_index=np.random.randint(low=0,high=len(data),size=errors['gender_mis'])
    gender_mis_data=data.iloc[gender_mis_index]
    gender_mis_error=gender_misclassification(gender_mis_data)
    data_err=gender_mis_error
    return data_err

def gender_misclassification(data):
    """
    Function to generate gender misclassification errors
    :param size: int, data: pandas dataframe
    :return: data_gen: pandas dataframe
    """
    print "Before swap: ",data['gender']
    data['gender'].replace('M','O', inplace=True)
    data['gender'].replace('F','M', inplace=True)
    data['gender'].replace('O', 'F', inplace=True)
    print "after swap: ",data['gender']
    return data

