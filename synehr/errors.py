# 5 errors: Character insertion, omission, substitution, transposition, gender misclassification
from auxillary import sum_num_terms_equals_total
import random
import numpy as np
import pandas as pd
import collections
import operator
import datetime


def gen_errors(size, data):
    """ A function to generate the different types of errors in the data

    Args:
        size (int): The number of randomly selected records to induce errors to.
        data (pandas dataframe): The generated synthetic data records.

    Returns:
        The error induced synthetic data.
    """
    # initializing a dictionary of all the errors to be generated
    errors = {'insertion': 0, 'omission': 0, 'substitution': 0, 'transposition': 0, 'gender_mis': 0}

    val = sum_num_terms_equals_total(5, size)
    i = 0
    for item in errors:
        errors[item] = val[i]
        i += 1
    sume = sum(errors.values())

    if sume != size:
        item = random.choice(errors.keys())
        if sume > size:
            rem = sume - size
            errors[item] -= rem
        else:
            rem = size - sume
            errors[item] += rem
    print "Errors: ",errors
    #Initializing flags to indicate if error has been induced.
    flag_insert=False
    flag_gendermis=False
    flag_omission=False
    flag_transpo=False
    flag_sub=False

    # Insertion Code
    #Call the insertion code, only if insertion error percentage is greater than zero.
    if errors['insertion']>0:
        flag_insert=True
        insertion_index = np.random.randint(low=0, high=len(data), size=errors['insertion'])
        insertion_data = data.iloc[insertion_index]
        insertion_err = {'first': 0, 'last': 0, 'address': 0}
        val = sum_num_terms_equals_total(3, len(insertion_data))

        i = 0
        for item in insertion_err:
            insertion_err[item] = val[i]
            i += 1
        print "inserton_err: ",insertion_err
        flag_first = False
        flag_last = False
        flag_address = False
        if insertion_err['first'] > 0:
            insertion_first = insertion_data.sample(n=insertion_err['first'])
            col_first = insertion_first['first'].tolist()
            print "len of col first: ",len(col_first)
            insertion_first['first'] = char_insertion_str(col_first)
            flag_first = True

        if insertion_err['last'] > 0:
            insertion_last = insertion_data.sample(n=insertion_err['last'])
            col_last = insertion_last['last'].tolist()
            print "len of col last: ",len(col_last)
            insertion_last['last'] = char_insertion_str(col_last)
            flag_last = True

        if insertion_err['address'] > 0:
            insertion_addr = insertion_data.sample(n=insertion_err['address'])
            col_addr = insertion_addr['address'].tolist()
            insertion_addr['address'] = char_insertion_str(col_addr)
            flag_address = True
        #In an event that all zeros are generated, force induce errors
        if(not (flag_first)):
            if(not flag_last):
                if(not flag_address):
                    choice=np.random.randint(0,3)
                    if choice==0:
                        insertion_first = insertion_data.sample(n=errors['insertion'])
                        col_first = insertion_first['first'].tolist()
                        insertion_first['first'] = char_insertion_str(col_first)
                        flag_first = True
                    elif choice==1:
                        insertion_last = insertion_data.sample(n=errors['insertion'])
                        col_last = insertion_last['last'].tolist()
                        insertion_last['last'] = char_insertion_str(col_last)
                        flag_last = True
                    elif choice==2:
                        insertion_addr = insertion_data.sample(n=errors['insertion'])
                        col_addr = insertion_addr['address'].tolist()
                        insertion_addr['address'] = char_insertion_str(col_addr)
                        flag_address = True




        if (flag_first):
            insertion_error = insertion_first
            if (flag_last):
                insertion_error = pd.concat([insertion_error, insertion_last])
            if (flag_address):
                insertion_error = pd.concat([insertion_error, insertion_addr])
        elif (flag_last):
            insertion_error = insertion_last
            if (flag_address):
                insertion_error = pd.concat([insertion_error, insertion_addr])
        elif (flag_address):
            insertion_error = insertion_addr
        flag_insert=True


    if errors['gender_mis']>0:
        flag_gendermis=True
        gender_mis_index = np.random.randint(low=0, high=len(data), size=errors['gender_mis'])
        gender_mis_data = data.iloc[gender_mis_index]
        gender_mis_error = gender_misclassification(gender_mis_data)

    if errors['substitution']>0:

        char_sub_index = np.random.randint(low=0, high=len(data), size=errors['substitution'])
        char_sub_data = data.iloc[char_sub_index]
        sub_err = {'first': 0, 'last': 0, 'DOB': 0, 'address': 0}
        val = sum_num_terms_equals_total(4, len(char_sub_data))
        flag_first = False
        flag_last = False
        flag_address = False
        flag_DOB=False

        i = 0
        for item in sub_err:
            sub_err[item] = int(val[i])
            i += 1

        print "sub_err: ",sub_err

        if sub_err['first'] > 0:
            flag_first=True

            sub_first = char_sub_data.sample(n=sub_err['first'])
            col_first = sub_first['first'].tolist()
            sub_first['first'] = char_sub_str(col_first)

        if sub_err['last']>0:
            flag_last=True
            sub_last = char_sub_data.sample(n=sub_err['last'])
            col_last = sub_last['last'].tolist()
            sub_last['last'] = char_sub_str(col_last)

        if sub_err['address']>0:
            flag_address=True
            sub_addr = char_sub_data.sample(n=sub_err['address'])
            col_addr = sub_addr['address'].tolist()
            sub_addr['address'] = char_sub_str(col_addr)
        if sub_err['DOB']>0:
            flag_DOB=True
            sub_DOB = char_sub_data.sample(n=sub_err['DOB'])
            col_DOB = sub_DOB['DOB'].tolist()
            sub_DOB['DOB'] = char_sub_date(col_DOB)

        if (flag_first):
            sub_error = sub_first
            if (flag_last):
                sub_error = pd.concat([sub_error, sub_last])
            if (flag_address):
                sub_error = pd.concat([sub_error, sub_addr])
            if (flag_DOB):
                sub_error=pd.concat([sub_error,sub_DOB])
        elif (flag_last):
            sub_error = sub_last
            if (flag_address):
                sub_error = pd.concat([sub_error, sub_addr])
                sub_error = pd.concat([sub_error,sub_DOB])
        elif (flag_address):
            sub_error = sub_addr
            if(flag_DOB):
                sub_error=pd.concat([sub_error,sub_DOB])
        elif (flag_DOB):
            sub_error=sub_DOB
        flag_sub = True




    #sub_err = pd.concat([sub_first, sub_last, sub_addr, sub_DOB])
    if(errors['omission']>0):

        char_omission_index = np.random.randint(low=0, high=len(data), size=errors['omission'])
        char_omission_data = data.iloc[char_omission_index]
        omission_err = {'first': 0, 'last': 0, 'address': 0}
        val = sum_num_terms_equals_total(3, len(char_omission_data))

        flag_first = False
        flag_last = False
        flag_address = False
        i = 0
        for item in omission_err:
            omission_err[item] = int(val[i])
            i += 1
        if(omission_err['first']>0):
            flag_first=True
            omission_first = char_omission_data.sample(n=omission_err['first'])
            col_first = omission_first['first'].tolist()
            omission_first['first'] = char_omission(col_first)
        if(omission_err['last']>0):
            flag_last=True
            omission_last = char_omission_data.sample(n=omission_err['last'])
            col_last = omission_last['last'].tolist()
            omission_last['last'] = char_omission(col_last)
        if(omission_err['address']>0):
            flag_address=True
            omission_addr = char_omission_data.sample(n=omission_err['address'])
            col_addr = omission_addr['address'].tolist()
            omission_addr['address'] = char_omission(col_addr)

        if (flag_first):
            omission_error = omission_first
            if (flag_last):
                omission_error = pd.concat([omission_error, omission_last])
            if (flag_address):
                omission_error = pd.concat([omission_error, omission_addr])
        elif (flag_last):
            omission_error = omission_last
            if (flag_address):
                omission_error = pd.concat([omission_err, omission_addr])
        elif (flag_address):
            omission_error = omission_addr
        flag_omission = True


    if(errors['transposition']>0):

        char_transpo_index = np.random.randint(low=0, high=len(data), size=errors['transposition'])
        char_transpo_data = data.iloc[char_transpo_index]
        transpo_err = {'first': 0, 'last': 0, 'DOB': 0, 'address': 0}
        val = sum_num_terms_equals_total(4, len(char_transpo_data))

        i = 0
        for item in transpo_err:
            transpo_err[item] = int(val[i])
            i += 1
        flag_first = False
        flag_last = False
        flag_address = False
        flag_DOB=False

        if(transpo_err['first']>0):
            flag_first=True
            transpo_first = char_transpo_data.sample(n=transpo_err['first'])
            col_first = transpo_first['first'].tolist()
            transpo_first['first'] = char_transpo_str(col_first)
        if(transpo_err['last']>0):
            flag_last=True
            transpo_last = char_transpo_data.sample(n=transpo_err['last'])
            col_last = transpo_last['last'].tolist()
            transpo_last['last'] = char_transpo_str(col_last)
        if(transpo_err['address']>0):
            flag_address=True
            transpo_addr = char_transpo_data.sample(n=transpo_err['address'])
            col_addr = transpo_addr['address'].tolist()
            transpo_addr['address'] = char_transpo_str(col_addr)
        if(transpo_err['DOB']>0):
            flag_DOB=True
            transpo_DOB = char_transpo_data.sample(n=transpo_err['DOB'])
            col_DOB = transpo_DOB['DOB'].tolist()
            transpo_DOB['DOB'] = char_transpo_date(col_DOB)

        if (flag_first):
            transpo_error = transpo_first
            if (flag_last):
                transpo_error = pd.concat([transpo_error, transpo_last])
            if (flag_address):
                transpo_error = pd.concat([transpo_error, transpo_addr])
            if (flag_DOB):
                transpo_error = pd.concat([transpo_error, transpo_DOB])
        elif (flag_last):
            transpo_error = transpo_last
            if (flag_address):
                transpo_error = pd.concat([transpo_error, transpo_addr])
            if(flag_DOB):
                transpo_error = pd.concat([transpo_error, transpo_DOB])
        elif (flag_address):
            transpo_error = transpo_addr
            if (flag_DOB):
                transpo_error = pd.concat([transpo_error, transpo_DOB])
        elif (flag_DOB):
            transpo_error = transpo_DOB
        flag_transpo = True


    #transpo_err = pd.concat([sub_first, sub_last, sub_addr, sub_DOB])

    if(flag_insert):
        data_err=insertion_error
        if(flag_omission):
            data_err=pd.concat([data_err,omission_error])
        if(flag_sub==True):
            data_err=pd.concat([data_err,sub_error])
        if(flag_gendermis):
            data_err=pd.concat([data_err,gender_mis_error])
        if(flag_transpo):
            data_err=pd.concat([data_err,transpo_error])
    elif (flag_omission):
        data_err = omission_error
        if (flag_sub):
            data_err = pd.concat([data_err, sub_error])
        if (flag_gendermis):
            data_err = pd.concat([data_err, gender_mis_error])
        if (flag_transpo):
            data_err = pd.concat([data_err, transpo_error])
    elif (flag_sub):
        data_err = sub_error
        if (flag_gendermis):
            data_err = pd.concat([data_err, gender_mis_error])
        if (flag_transpo):
            data_err = pd.concat([data_err, transpo_error])
    elif (flag_gendermis):
        data_err = gender_mis_error
        if (flag_transpo):
            data_err = pd.concat([data_err, transpo_error])
    elif (flag_transpo):
            data_err = transpo_error




    #data_err = pd.concat([insertion_err, gender_mis_error, omission_err, sub_err, transpo_err])

    return data_err


def gender_misclassification(data):
    """ A function to induce gender misclassification errors on the synthetic data.
    Args:
        data (pandas dataframe): The generated synthetic data records.
    Returns:
        The induced gender misclassification errors dataset.
    """
    # print "Before swap: ",data['gender']
    data['gender'].replace('M', 'O', inplace=True)
    data['gender'].replace('F', 'M', inplace=True)
    data['gender'].replace('O', 'F', inplace=True)
    # print "after swap: ",data['gender']
    return data


def char_sub_str(arr):
    """ A function to induce character substitution error in dataset records.
    Args:
        arr (array): The array of randomly selected synthetic records.
    Returns:
        The error induced character substitution list.
    """
    characters = 'qwertyuioplkjhgfdsazxcvbnm'
    arr_res = []
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
            arr_res.append(x)
    return arr_res


def char_omission(col_data):
    """ A function to induce a random character omission.
    Args:
        col_data (pandas dataframe): The generated synthetic data records.
    Returns:
        The induced character omission error dataset.
    """
    res_data = []
    for i in range(len(col_data)):
        c = col_data[i]
        # print "c: ",c
        letters = collections.Counter(c)
        # print letters
        maxValue = max(letters.values())
        keys = [key for key in letters if letters[key] == maxValue]
        key = random.choice(keys)

        # print "keys: ",keys

        ind = c.find(key)
        # print "index: ", ind
        # print c[0:ind]
        # print c[(ind+1):]
        c = c[0:ind] + c[(ind + 1):]
        res_data.append(c)
        # print col_data[i]
    return res_data


def char_sub_str(arr):
    """ A function to induce character substitution error in dataset records.
    Args:
        arr (array): The array of randomly selected synthetic records.
    Returns:
        The error induced character substitution list.
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
    """ A function to induce character substitution error in a date column.
    Args:
        col_date (array): The array of randomly selected synthetic records.
    Returns:
        Returns the error induced character substitution array
    """
    new_dates = []
    for date in col_date:
        date = date.strftime('%Y/%m/%d')
        year, month, day = date.split('/')
        # year=int(year[-2:])
        month = (month)
        day = (day)
        ind = [0, 1, 2]
        choice = random.choice(ind)
        if choice == 0:
            c = random.randint(0, 9)
            ind = random.randint(2, 3)
            year = list(year)
            # print "split year: ",year
            year[ind] = str(c)
            year = ''.join(year)
            # print "Error induced year: ",year
        elif choice == 1:
            if int(day) == 31:
                months_with_31_days = ["1", "3", "5", "7", "8", "10", "12"]
                month = str(random.choice(months_with_31_days))
            elif int(day) == 30 or int(day) == 29:
                months_with_30_days = ["1", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
                month = str(random.choice(months_with_30_days))
            else:
                month = str(random.randint(1, 12))
            # print "error induced month: ",month
        elif choice == 2:
            if int(month) in [1, 3, 5, 7, 8, 10, 12]:
                day = str(random.randint(1, 31))
            elif int(month) in [4, 6, 9, 11]:
                day = str(random.randint(1, 30))
            else:
                day = str(random.randint(1, 28))
        date_err = '/'.join([year, month, day])
        date = datetime.datetime.strptime(date_err, "%Y/%m/%d")
        new_dates += [date]
    return new_dates


def char_transpo_str(col_data):
    """
    Function to induce character transposition errors
    :param col_data: list, column to induce errors in.
    :return: col_data
    """
    new_col = []
    # print col_data
    for record in col_data:
        print record
        if len(record) > 3:
            rnd = random.randint(2, len(record) - 2)
            # print rnd
            # random.choice(range(1,len(record)))
            ind = random.choice([1, -1])
            recordl = list(record)
            buf = recordl[rnd]
            recordl[rnd] = record[rnd + ind]
            recordl[rnd + ind] = buf
            record = ''.join(recordl)
        new_col += [record]

    return new_col


def char_transpo_date(col_date):
    """
    Function to randomly transpose date characters
    :param col_date: list of dates
    :return: new_date: list of error induced dates
    """
    new_dates = []
    print col_date
    for date in col_date:
        date = date.strftime('%Y/%m/%d')
        # print "Date before error: ", date
        year, month, day = date.split('/')
        # year=int(year[-2:])
        month = (month)
        day = (day)
        ind = [0, 2]
        choice = random.choice(ind)
        if choice == 0:

            year = list(year)
            if abs(int(year[2]) - int(year[3])) == 1 or random.randint(0, 10) == 1:
                buf = year[3]
                year[3] = year[2]
                year[2] = buf
            year = ''.join(year)
            # print "Error induced year: ",year

        elif choice == 2:
            dayl = list(day)
            if len(day) == 1 and int(day) <= 2:
                day *= 10
            elif abs(int(dayl[0]) - int(dayl[1])) == 1 or random.randint(0, 10) == 1:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if (int(dayl[1] + dayl[0]) < 31):
                        buf = dayl[0]
                        dayl[0] = dayl[1]
                        dayl[1] = buf
                        day = ''.join(dayl)
                elif month in [4, 6, 9, 11]:
                    if (int(dayl[1] + dayl[0]) < 30):
                        buf = dayl[0]
                        dayl[0] = dayl[1]
                        dayl[1] = buf
                        day = ''.join(dayl)
                elif int(month) == 2:
                    if ((int(dayl[1] + dayl[0]) < 28) or (int(year) % 400 == 0 and int(dayl[1] + dayl[0]) < 29)):
                        buf = dayl[0]
                        dayl[0] = dayl[1]
                        dayl[1] = buf
                        day = ''.join(dayl)

        date_err = '/'.join([year, month, day])
        date = datetime.datetime.strptime(date_err, "%Y/%m/%d")
        new_dates += [date]
        # print new_dates
    return new_dates


def char_insertion_str(arr):
    """ A function that induces character insertion errors in dataset records.
    Arg:
        arr (array): The array of randomly selected synthetic records.
    Returns:
        Returns the error induced character insertion array
    """
    characters = 'qwertyuioplkjhgfdsazxcvbnm'
    close_keys = {"a": ["a","q","w","s","z","x"],
                  "b": ["b","v","g","h","n"],
                  "c": ["c","x","d","f","v"],
                  "d": ["d","s","e","r","f","x","c"],
                  "e": ["e","w","s","d","r"],
                  "f": ["f","r","t","d","g","c","v"],
                  "g": ["g","t","y","f","h","v","b"],
                  "h": ["h","y","u","g","j","b","n"],
                  "i": ["i","u","j","k","o"],
                  "j": ["j","u","i","h","k","n","m"],
                  "k": ["k","i","o","j","l","m"],
                  "l": ["l","o","p","k"],
                  "m": ["m","n","j","k"],
                  "n": ["n","b","h","j","m"],
                  "o": ["o","i","k","l","p"],
                  "p": ["p","o","l"],
                  "q": ["q","a","w"],
                  "r": ["r","e","d","f","t"],
                  "s": ["s","w","e","a","d","z","x"],
                  "t": ["t","r","f","g","y"],
                  "u": ["u","y","h","j","i"],
                  "v": ["v","c","f","g","b"],
                  "w": ["w","q","a","s","e"],
                  "x": ["x","z","s","d","c"],
                  "y": ["y","t","g","h","u"],
                  "z": ["z","a","s","x"]}
    print "insertion before", arr
    arr_res = []
    for i in range(0, len(arr)):
        x = arr[i].lower()
        print x
        print len(x)
        if len(x) > 3:
            rnd = random.randint(1, len(x) - 1)
            if x[rnd].isalpha():
                rnd_close_letter = random.choice(close_keys[x[rnd].lower()])
                x = x[0:rnd] + rnd_close_letter + x[rnd:]
                arr_res.append(x)
            else:
                insertion = random.randint(0, len(characters))
                rndCharacter = characters[insertion:insertion + 1]
                x = x[0:rnd] + rndCharacter + x[rnd:]
                arr_res.append(x)
        else:
            arr_res.append(x)
    print "insertion after: ", arr_res
    return arr_res


