import pandas as pd

def get_all():
    url = 'G:\\DS\\3.Personal_Projects\\Blood_Donor_Recommendation_Engine\\donor_data.csv'
    data = pd.read_csv(url)
    data = data[data['Availability']==1]
    data['rating'] = data['Donate'] / data['Request']
    return data

def top10(blood, district):
    df = get_all()
    df = df[(df['Blood Group'] == blood) & (df['District'] == district)].sort_values('rating', ascending=False)
    return df[['Name', 'Blood Group', 'Phone']].head(20)

def near_you(blood, district, desired_loc):
    df = get_all()
    near_you = df[(df['Blood Group'] == blood) & (df['Blood Group'] == blood) &((df['Postal Code'] < desired_loc + 8) & (df['Postal Code'] > desired_loc - 8))]
    return near_you[['Name', 'Blood Group', 'Phone']]





