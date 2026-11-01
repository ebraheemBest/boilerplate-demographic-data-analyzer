import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. How many people of each race?
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(), 1
    )

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    # 4. Separate people with advanced and lower education
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']

    higher_education = df[
        df['education'].isin(advanced_education)
    ]

    lower_education = df[
        ~df['education'].isin(advanced_education)
    ]

    # 5. Percentage of people with advanced education earning >50K
    higher_education_rich = round(
        (higher_education['salary'] == '>50K').sum()
        / len(higher_education) * 100, 1
    )

    # 6. Percentage of people without advanced education earning >50K
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').sum()
        / len(lower_education) * 100, 1
    )

    # 7. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 8. Percentage of minimum-hour workers earning >50K
    num_min_workers = df[
        df['hours-per-week'] == min_work_hours
    ]

    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').sum()
        / len(num_min_workers) * 100, 1
    )

    # 9. Country with the highest percentage of people earning >50K
    country_count = df['native-country'].value_counts()

    country_rich = df[
        df['salary'] == '>50K'
    ]['native-country'].value_counts()

    country_percentage = country_rich / country_count * 100

    highest_earning_country = country_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_percentage.max(), 1
    )

    # 10. Most popular occupation for people earning >50K in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:

        print("Number of each race:\n", race_count)

        print("Average age of men:", average_age_men)

        print(
            "Percentage with Bachelors degrees:",
            percentage_bachelors
        )

        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )

        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )

        print("Min work time:", min_work_hours, "hours/week")

        print(
            "Percentage of rich among those who work fewest hours:",
            rich_percentage
        )

        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )

        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }