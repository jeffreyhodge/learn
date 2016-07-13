#!/usr/bin/env python
import sys
import csv

filename = sys.argv[1]
rental_list=[]

def get_depr(purchase_price,pct_val_of_structure_to_purchase_price,months):
  p = float(purchase_price)
  n = float(loan_years)
  pct = float(float(pct_val_of_structure_to_purchase_price) / 100)
  p = p * pct
  month = 1
  depreciation_list = []
  max_months = 27.5 * 12
  while month <= max_months and month <= float(months):
    depreciation_list.append((month, p / max_months))
    month += 1
  return depreciation_list

def get_pmt(loan_amt,interest,loan_years):
  l = float(loan_amt)
  i = float(float(interest)/100/12)
  n = int(loan_years * 12)
  monthly_pmt = l * (i * (1 + i)**n ) / ((1 + i)**n -1)
  return monthly_pmt

def get_loan_amt(purchase_price,down_pmt):
  p = float(purchase_price)
  d = float(down_pmt)
  return p - (p * d / 100)

def get_int_and_princ(loan_amt,monthly_pmt,interest,num_month):
  l = float(loan_amt)
  m = float(monthly_pmt)
  i = float(float(interest)/100/12)
  n = int(num_month)
  amort_list = []
  month = 1
  while month <= n:
    interest_paid = l * i
    principal_paid = m - interest_paid
    amort_list.append(( month, principal_paid, interest_paid ))
    l = l - principal_paid
    month += 1
  return amort_list
    

with open(filename, 'rb') as f:
  raw_data = csv.reader(f, delimiter=':')
  for row in raw_data:
    rental_list.append(row)

rental_list.pop(0)
for property in rental_list:
  name = property[0]
  street = property[1]
  city = property[2]
  state = property[3]
  zip = property[4]
  purchase_price = property[5]
  #down_pmt = property[6] || 20
  down_pmt = 20
  num_units = property[7]
  rent_per_unit = property[8]
  #mgmt_fee_pct_unit_monthly = property[9] || 10
  mgmt_fee_pct_unit_monthly = 8
  #hoa_fee_monthly = property[10] || 0
  hoa_fee_monthly = 0
  interest = property[11]
  #loan_years = property[12] || 30
  loan_years = 30
  pct_val_of_structure_to_purchase_price = 80
  num_month = 12
  loan_amt = get_loan_amt(purchase_price,down_pmt)
  monthly_pmt =  get_pmt(loan_amt,interest,loan_years)
  amort_list = get_int_and_princ(loan_amt,monthly_pmt,interest,num_month)
  for (month, principal_paid, interest_paid) in amort_list:
    print "Month: %d | Principal paid: %f | Interest paid: %f" % (month, principal_paid, interest_paid)
  depreciation_list = get_depr(purchase_price,pct_val_of_structure_to_purchase_price,num_month)
  for (month, depreciation) in depreciation_list:
    print "Month: %d | Depreciation: %f" % (month, depreciation)

#### CSV format
#0 Property name
#1 Street Address
#2 City
#3 State
#4 ZipCode
#5 Purchase Price
#6 %down 20 default
#7 rentable units in property
#8 rent per unit
#9 management fee% 10 default
#10 HOA monthly 0 default
#11 interest
#12 loan years
####
