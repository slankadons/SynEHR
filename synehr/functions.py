
import pandas as pd
import os
import random
import pip
from faker import Faker

def install(package):
    pip.main(['install', package])

def readCSV():
    """Read in master files for first name and last name"""
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_First_Names.csv')
    first_name_columns = ['first', 'gender', 'race', 'detailed_race']
    first_names = pd.read_csv(f_name, sep=',', header=0,
                     names=first_name_columns, na_values='?')
    f_name = os.path.join(
        os.path.dirname(__file__), 'data', 'Master_Last_Names.csv')
    last_name_columns = ['last', 'race', 'detailed_race']
    last_names = pd.read_csv(f_name, sep=',', header=0,
                     names=last_name_columns, na_values='?')
    return first_names, last_names

class SizeValueError(Exception):
    def __init__(self):
        Exception.__init__(self,"Size  value out of range. Please choose between 100 and 1 million.")

class GenderValueError(Exception):
    def __init__(self):
        Exception.__init__(self,"Gender value out of range. Please use percentage between 0% and 100%.")


def parameter_check(size, male_gender, asian, spanish, afr_amer, caucasian, native_amer_alaskan, mixed):
    try:
        if 1 < asian + spanish + afr_amer + caucasian + native_amer_alaskan + mixed < 0:
            raise ValueError
        if 100 >= size >= 1000000:
            raise SizeValueError
        if 0 > male_gender > 1:
            raise GenderValueError
    except ValueError:
        print ('Sum of race values bust be between 0 and 1.')
    else:
        sum_race = asian + spanish + afr_amer + caucasian + native_amer_alaskan + mixed
        random = float(1 - sum_race)
        female_gender = float(1 - male_gender)
        return random, female_gender


def random_data_generator(first_names_data, last_names_data, size, random_percentage, female_gender, male_gender):
    ### First Name Datasets
    asian_dataset_fn = first_names_data[first_names_data['race'] == 'Asian']
    spanish_dataset_fn = first_names_data[first_names_data['race'] == 'Spanish']
    afr_amer_dataset_fn = first_names_data[first_names_data['race'] == 'African American']
    caucasian_dataset_fn = first_names_data[first_names_data['race'] == 'Caucasian']
    native_amer_alaskan_dataset_fn = first_names_data[first_names_data['race'] == 'Native American/Alaskan']
    mixed_dataset_fn = first_names_data[first_names_data['race'] == 'Mixed']

    ### Last Name Datasets
    asian_dataset_ln = last_names_data[last_names_data['race'] == 'Asian'].index.tolist()
    spanish_dataset_ln = last_names_data[last_names_data['race'] == 'Spanish'].index.tolist()
    afr_amer_dataset_ln = last_names_data[last_names_data['race'] == 'African American'].index.tolist()
    caucasian_dataset_ln = last_names_data[last_names_data['race'] == 'Caucasian'].index.tolist()
    native_amer_alaskan_dataset_ln = last_names_data[last_names_data['race'] == 'Native American/Alaskan'].index.tolist()
    mixed_dataset_ln = last_names_data[last_names_data['race'] == 'Mixed'].index.tolist()

    # male_asian_dataset = asian_dataset[asian_dataset['gender'] == 'M'].index.tolist()
    # female_asian_dataset = asian_dataset[asian_dataset['gender'] == 'F'].index.tolist()

    race_list = ['Asian', 'Spanish', 'African American', 'Caucasian', 'Native American/Alaskan', 'Mixed']
    race_dataset_fn = [asian_dataset_fn, spanish_dataset_fn, afr_amer_dataset_fn, caucasian_dataset_fn, native_amer_alaskan_dataset_fn, mixed_dataset_fn]
    race_dataset_ln = [asian_dataset_ln, spanish_dataset_ln, afr_amer_dataset_ln, caucasian_dataset_ln, native_amer_alaskan_dataset_ln, mixed_dataset_ln]

    data_columns = ['first', 'last', 'gender', 'race', 'detailed_race']
    male_first_name_randomized_data = pd.DataFrame(columns=data_columns)
    female_first_name_randomized_data = pd.DataFrame(columns=data_columns)

    print "Random Data function initiated"
    size = int(size * random_percentage)
    female_size = int(size * female_gender)
    male_size = int(size * male_gender)
    while len(male_first_name_randomized_data) < male_size:
        gender = 'M'
        race_idx = random.randint(0,len(race_list)-1)
        gender_test = race_dataset_fn[race_idx][race_dataset_fn[race_idx]['gender'] == gender].index.tolist()

        detailed_race = first_names_data.loc[random.choice(gender_test)]['detailed_race']
        print detailed_race
        if race_list[race_idx] == 'Asian':
            last_name = last_names_data.loc[random.choice(last_names_data[(last_names_data['race'] == 'Asian') & (last_names_data['detailed_race'] == detailed_race)].index.tolist())]['last']
            first_name = first_names_data.loc[random.choice(first_names_data[(first_names_data['gender'] == gender) & (first_names_data['detailed_race'] == detailed_race)].index.tolist())]['first']
        else:
            last_name = last_names_data.loc[random.choice(race_dataset_ln[race_idx])]['last']
            first_name = first_names_data.loc[random.choice(gender_test)]['first']
        male_data_row = pd.DataFrame([[first_name, last_name, gender, race_list[race_idx], detailed_race]], columns=data_columns)
        male_first_name_randomized_data = male_first_name_randomized_data.append(male_data_row, ignore_index=True)

    while len(female_first_name_randomized_data) < female_size:
        gender = 'F'
        race_idx = random.randint(0,len(race_list)-1)
        gender_test = race_dataset_fn[race_idx][race_dataset_fn[race_idx]['gender'] == gender].index.tolist()

        detailed_race = first_names_data.loc[random.choice(gender_test)]['detailed_race']
        if race_list[race_idx] == 'Asian':
            last_name = last_names_data.loc[random.choice(last_names_data[(last_names_data['race'] == 'Asian') & (last_names_data['detailed_race'] == detailed_race)].index.tolist())]['last']
            first_name = first_names_data.loc[random.choice(first_names_data[(first_names_data['gender'] == gender) & (first_names_data['detailed_race'] == detailed_race)].index.tolist())]['first']
        else:
            last_name = last_names_data.loc[random.choice(race_dataset_ln[race_idx])]['last']
            first_name = first_names_data.loc[random.choice(gender_test)]['first']
        female_data_row = pd.DataFrame([[first_name, last_name, gender, race_list[race_idx], detailed_race]], columns=data_columns)
        female_first_name_randomized_data = female_first_name_randomized_data.append(female_data_row, ignore_index=True)
    print "completed first name while loop"
    frames = [male_first_name_randomized_data, female_first_name_randomized_data]
    randomized_data = pd.concat(frames, ignore_index=True)

    print randomized_data
    return randomized_data



def race_data_generator(first_names_data, last_names_data, size, asian_percentage, spanish_percentage, afr_amer_percentage, caucasian_percentage, native_amer_alaskan_percentage, mixed_percentage, female_gender, male_gender):
    ### sizes for each race
    asian_size = int(size * asian_percentage)
    spanish_size = int(size * spanish_percentage)
    afr_amer_size = int(size * afr_amer_percentage)
    caucasian_size = int(size * caucasian_percentage)
    native_amer_alaskan_size = int(size * native_amer_alaskan_percentage)
    mixed_size = int(size * mixed_percentage)

    ### sizes for each race by gender
    asian_male_size = int(asian_size * male_gender)
    asian_female_size = int(asian_size * female_gender)
    spanish_male_size = int(spanish_size * male_gender)
    spanish_female_size = int(spanish_size * female_gender)
    afr_amer_male_size = int(afr_amer_size * male_gender)
    afr_amer_female_size = int(afr_amer_size * female_gender)
    caucasian_male_size = int(caucasian_size * male_gender)
    caucasian_female_size = int(caucasian_size * female_gender)
    native_amer_male_size = int(native_amer_alaskan_size * male_gender)
    native_amer_female_size = int(native_amer_alaskan_size * female_gender)
    mixed_male_size = int(mixed_size * male_gender)
    mixed_female_size = int(mixed_size * female_gender)


    ### First Name Datasets
    asian_dataset_fn = first_names_data[first_names_data['race'] == 'Asian']
    spanish_dataset_fn = first_names_data[first_names_data['race'] == 'Spanish']
    afr_amer_dataset_fn = first_names_data[first_names_data['race'] == 'African American']
    caucasian_dataset_fn = first_names_data[first_names_data['race'] == 'Caucasian']
    native_amer_alaskan_dataset_fn = first_names_data[first_names_data['race'] == 'Native American/Alaskan']
    mixed_dataset_fn = first_names_data[first_names_data['race'] == 'Mixed']

    ### Last Name Datasets
    asian_dataset_ln = last_names_data[last_names_data['race'] == 'Asian'].index.tolist()
    spanish_dataset_ln = last_names_data[last_names_data['race'] == 'Spanish'].index.tolist()
    afr_amer_dataset_ln = last_names_data[last_names_data['race'] == 'African American'].index.tolist()
    caucasian_dataset_ln = last_names_data[last_names_data['race'] == 'Caucasian'].index.tolist()
    native_amer_alaskan_dataset_ln = last_names_data[last_names_data['race'] == 'Native American/Alaskan'].index.tolist()
    mixed_dataset_ln = last_names_data[last_names_data['race'] == 'Mixed'].index.tolist()

    race_dataset_fn = [asian_dataset_fn, spanish_dataset_fn, afr_amer_dataset_fn, caucasian_dataset_fn, native_amer_alaskan_dataset_fn, mixed_dataset_fn]
    race_dataset_ln = [asian_dataset_ln, spanish_dataset_ln, afr_amer_dataset_ln, caucasian_dataset_ln, native_amer_alaskan_dataset_ln, mixed_dataset_ln]


    sizes = [[asian_male_size, asian_female_size], [spanish_male_size, spanish_female_size], [afr_amer_male_size, afr_amer_female_size],
             [caucasian_male_size, caucasian_female_size], [native_amer_male_size, native_amer_female_size], [mixed_male_size, mixed_female_size]]
    race_list = ['Asian', 'Spanish', 'African American', 'Caucasian', 'Native American/Alaskan', 'Mixed']

    data_columns = ['first', 'last', 'gender', 'race', 'detailed_race']
    asian_data = pd.DataFrame(columns=data_columns)
    spanish_data = pd.DataFrame(columns=data_columns)
    afr_amer_data = pd.DataFrame(columns=data_columns)
    caucasian_data = pd.DataFrame(columns=data_columns)
    native_amer_alaskan_data = pd.DataFrame(columns=data_columns)
    mixed_data = pd.DataFrame(columns=data_columns)

    print "Hello", sizes[0][0], sizes[0][1]

    race_data = [asian_data, spanish_data, afr_amer_data, caucasian_data, native_amer_alaskan_data, mixed_data]
    for race_size in range(len(sizes)):
        data_columns = ['first', 'last', 'gender', 'race', 'detailed_race']
        male_first_name_randomized_data = pd.DataFrame(columns=data_columns)
        female_first_name_randomized_data = pd.DataFrame(columns=data_columns)
        while len(male_first_name_randomized_data) < sizes[race_size][0]:
            gender = 'M'
            race = race_list[race_size]
            gender_test = race_dataset_fn[race_size][race_dataset_fn[race_size]['gender'] == gender].index.tolist()
            detailed_race = first_names_data.loc[random.choice(gender_test)]['detailed_race']
            if race == 'Asian':
                last_name = last_names_data.loc[random.choice(last_names_data[(last_names_data['race'] == 'Asian') & (last_names_data['detailed_race'] == detailed_race)].index.tolist())]['last']
                first_name = first_names_data.loc[random.choice(first_names_data[(first_names_data['gender'] == gender) & (first_names_data['detailed_race'] == detailed_race)].index.tolist())]['first']
            else:
                last_name = last_names_data.loc[random.choice(race_dataset_ln[race_size])]['last']
                first_name = first_names_data.loc[random.choice(gender_test)]['first']
            male_data_row = pd.DataFrame([[first_name, last_name, gender, race, detailed_race]], columns=data_columns)
            male_first_name_randomized_data = male_first_name_randomized_data.append(male_data_row, ignore_index=True)

        while len(female_first_name_randomized_data) < sizes[race_size][1]:
            gender = 'F'
            race = race_list[race_size]
            gender_test = race_dataset_fn[race_size][race_dataset_fn[race_size]['gender'] == gender].index.tolist()
            detailed_race = first_names_data.loc[random.choice(gender_test)]['detailed_race']
            if race == 'Asian':
                last_name = last_names_data.loc[random.choice(last_names_data[(last_names_data['race'] == 'Asian') & (last_names_data['detailed_race'] == detailed_race)].index.tolist())]['last']
                first_name = first_names_data.loc[random.choice(first_names_data[(first_names_data['gender'] == gender) & (first_names_data['detailed_race'] == detailed_race)].index.tolist())]['first']
            else:
                last_name = last_names_data.loc[random.choice(race_dataset_ln[race_size])]['last']
                first_name = first_names_data.loc[random.choice(gender_test)]['first']
            female_data_row = pd.DataFrame([[first_name, last_name, gender, race, detailed_race]], columns=data_columns)
            female_first_name_randomized_data = female_first_name_randomized_data.append(female_data_row, ignore_index=True)

        frames = [male_first_name_randomized_data, female_first_name_randomized_data]
        race_data[race_size] = pd.concat(frames, ignore_index=True)
    all_data = pd.concat(race_data, ignore_index=True)
    print all_data
    return all_data




def mk_data(first_names_data, last_names_data, size=20, male_gender=.50, asian=0.0, spanish=0, afr_amer=0, caucasian=0, native_amer_alaskan=0, mixed=0):
    """
    1. All races are inputted as integers to signify the percentages
    2. Either random is used, or input of percentages for race be entered"""
    # dataset list by race
    asian_dataset = first_names_data[first_names_data['race'] == 'Asian']
    spanish_dataset = first_names_data[first_names_data['race'] == 'Spanish']
    afr_amer_dataset = first_names_data[first_names_data['race'] == 'African American']
    caucasian_dataset = first_names_data[first_names_data['race'] == 'Caucasian']
    native_amer_alaskan_dataset = first_names_data[first_names_data['race'] == 'Native American/Alaskan']
    mixed_dataset = first_names_data[first_names_data['race'] == 'Mixed']

    # checks parameters are met and raises errors
    asian = float(asian)
    spanish = float(spanish)
    afr_amer = float(afr_amer)
    caucasian = float(caucasian)
    native_amer_alaskan = float(native_amer_alaskan)
    mixed = float(mixed)
    male_gender = float(male_gender)
    random_percentage, female_gender = parameter_check(size, male_gender, asian, spanish, afr_amer, caucasian, native_amer_alaskan, mixed)

    # random data generator
    random_generator = random_data_generator(first_names_data, last_names_data, size, random_percentage, female_gender, male_gender)

    # data generator by race
    race_generator = race_data_generator(first_names_data, last_names_data, size, asian, spanish, afr_amer, caucasian, native_amer_alaskan, mixed, female_gender, male_gender)

    # fake factory
    addresses = fake_factory(size)

    frames = [random_generator, race_generator]
    data = pd.concat(frames, ignore_index=True)
    data['address'] = pd.DataFrame(addresses)
    print data
    f_name = os.path.join(os.path.dirname(__file__), 'test1.csv')
    data.to_csv(f_name)
    return data

def fake_factory(size):
    install('Faker')
    fake = Faker()
    addresses = []
    for _ in range(0, size):
        address = fake.address()
        addresses.append(address)
    return addresses

if __name__ == "__main__":
    first_names_data, last_names_data = readCSV()
    # print first_names_data
    # print last_names_data
    # fake_pip_install = fake_factory()
    mk_data(first_names_data, last_names_data, size=50, male_gender=.50, asian=.50, spanish=.25, afr_amer=.25, caucasian=0, native_amer_alaskan=0, mixed=0)