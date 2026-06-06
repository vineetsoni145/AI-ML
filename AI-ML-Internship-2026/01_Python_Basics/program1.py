import pandas as pd

data = pd.read_csv('orders.csv')

# print(len(data))

# app = 0
# website = 0
# mobile = 0

# for i in data["channel"]:
#     if i == "App":
#         app = app + 1
#     if i == "Website":
#         website = website + 1
#     if i == "Mobile Web":
#         mobile = mobile + 1
    

# print(app)
# print(website)
# print(mobile)

# print(app+website+mobile)

#find count & list of people whose order amount is below average

avgs = data['total_amount'].mean()
print(avgs)

aboveavg = 0
belowavg = 0

for i in data['total_amount']:
    if i > avgs:
        belowavg = belowavg + 1
    if i < avgs:
        aboveavg = aboveavg + 1

print(belowavg)
print(aboveavg)

belowavg = pd.to_csv('orders.csv')
print(belowavg)

    
