import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

complaint_data = pd.read_csv("E:\\DocumentsForLongTermStorage\\Consumer_Complaints.csv")
print(complaint_data.head(12))
print(complaint_data.columns)
print(len(complaint_data['Date received']))
complaint_data['Date received'] = pd.to_datetime(complaint_data['Date received'])
date_name = 'date_received'
product = 'product'
sub_product = 'sub_product'
issue = 'issue'
sub_issue = 'sub_issue'
consumer_comp_narrative = 'consumer_comp_narrative'
company_response = 'company_response'
company = 'company'
state = 'state'
zip_code = 'zip_code'
tags = 'tags'
consumer_consent_provided = 'consumer_consent_provided'
submitted_via = 'submitted_via'
date_sent_to_company = 'date_sent_to_company'
company_response_to_consumer = 'company_response_to_consumer'
timely_response = 'timely_response'
consumer_disputed = 'consumer_disputed'
complaint_id = 'complaint_id'
column_names = [date_name, product, sub_product, issue, sub_issue, consumer_comp_narrative, company_response, company, state, zip_code,
                tags, consumer_consent_provided, submitted_via, date_sent_to_company, company_response_to_consumer, timely_response,
                consumer_disputed, complaint_id]
old_names = complaint_data.columns
for i in range(len(column_names)):
    old_name = old_names[i]
    new_name = column_names[i]
    complaint_data.rename({old_name: new_name}, axis=1, inplace=True)
complaint_data.columns
debt_collection_total = complaint_data.loc[complaint_data[product] == 'Debt collection']
print(len(debt_collection_total))
debt_not_yours = debt_collection_total.loc[debt_collection_total[sub_issue] == 'Debt is not yours']
print(debt_not_yours[company].unique)
debt_not_yours_dictionary = {}
for company_name in debt_not_yours[company]:
    if company_name in debt_not_yours_dictionary:
        debt_not_yours_dictionary[company_name] += 1
    if company_name not in debt_not_yours_dictionary:
        debt_not_yours_dictionary[company_name] = 1

sorted_debt_not_yours = sorted(debt_not_yours_dictionary, key=debt_not_yours_dictionary.get)
top_ten = {}
for i in range(10):
    top_ten[sorted_debt_not_yours[i]] = debt_not_yours_dictionary[sorted_debt_not_yours[i]]

print(sorted_debt_not_yours.pop(0))
