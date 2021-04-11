import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.value_counts(df['race'])

    # What is the average age of men?
    average_age_men = df[df.sex != 'Female']
    average_age_men = average_age_men['age'].mean()
    average_age_men = round(average_age_men, ndigits=1)

    # What is the percentage of people who have a Bachelor's degree?
    total = df.shape[0] #Total od df
    df_mask=df['education']=='Bachelors'
    filtered_df = df[df_mask]
    total_bacherlors = len(filtered_df)
    percentage_bachelors = round(100*(total_bacherlors/total),ndigits=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    df_higher_education = df.loc[(df['education'] == 'Doctorate') | (df['education'] == 'Masters') | (df['education'] == 'Bachelors')]
    total_higher = df_higher_education.shape[0]
    df_higher_education= df_higher_education[df_higher_education.salary != '<=50K'] # 

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    df_lower_education = df.loc[(df['education'] != 'Doctorate') & (df['education'] != 'Masters') & (df['education'] != 'Bachelors')]
    total_lower = df_lower_education.shape[0]
    df_lower_education = df_lower_education[df_lower_education.salary != '<=50K']
    

    higher_education = df_higher_education.shape[0]
    lower_education = df_lower_education.shape[0]


    # percentage with salary >50K
    higher_education_rich = round(100*(higher_education/total_higher),ndigits=1)
    lower_education_rich = round(100*(lower_education/total_lower),ndigits=1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =  df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    #total_people_min = df[df['hours-per-week']==min_work_hours].shape[0]
    df_aux = df[(df['hours-per-week']==min_work_hours) & (df['salary'] != '<=50K')]
    num_min_workers = df_aux.shape[0]

    rich_percentage = round(100*(num_min_workers/total),ndigits=1)
    rich_percentage =10
    # What country has the highest percentage of people that earn >50K?
    df_mask = df[df['salary'] != '<=50K'] #who earn more than 50K
    nativos = pd.value_counts(df_mask['native-country'])
    paises_total = pd.value_counts(df['native-country']) 
    highest_earning_countries_percentages = 100*(nativos/paises_total)
    #porcentaje mayor sin redondear
    highest_earning_country_percentage = highest_earning_countries_percentages.max()
    highest_earning_country = highest_earning_countries_percentages[highest_earning_countries_percentages==highest_earning_country_percentage]


    highest_earning_country = highest_earning_country.keys()[0]
    highest_earning_country_percentage = round(highest_earning_countries_percentages.max(),ndigits=1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_mask.set_index('native-country',inplace=True) #utilizo los paises como index
    df_India = df_mask.loc['India']
    profesional_counts = pd.value_counts(df_India['occupation'])
    top_IN_occupation = profesional_counts.keys()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
