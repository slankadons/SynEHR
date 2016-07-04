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