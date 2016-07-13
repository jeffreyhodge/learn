#!/usr/bin/env python
import sys
import csv

filename = sys.argv[1]
rental_list=[]

def get_pmt(purchase_price,interest,loan_years):
  p = int(purchase_price)
  i = float(float(interest)/100/12)
  n = int(loan_years * 12)
  monthly_pmt = p * (i * (1 + i)**n ) / ((1 + i)**n -1)
  return monthly_pmt

def get_int_and_princ(purchase_price,monthly_pmt,interest)

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
  print get_pmt(purchase_price,interest,loan_years)

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
####
