import argparse
import math

# command line input flags
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--money", type=float, nargs='?', const=0, default=0, help="How much money do you want to spend?")
parser.add_argument("-d", "--days", type=int, nargs='?', const=0, default=0, help="How many days do you need it to last?")

args = parser.parse_args()

# amount each pet eats per day
peanut = 5
llewyn = 3
napoleon = 2

# amount per can
can = 12.5

# cost of cans
cost = 3.78
tax = 0.06

# calculate it!
daily = peanut + llewyn + napoleon
cans_day = daily/can 

if args.money:
  total_cans = math.floor(round(args.money/(cost + cost*tax),2))
  total_days = math.floor(total_cans/cans_day)
  print("You can buy {} cans, which will last {} days.".format(
    total_cans, total_days
    ))
elif args.days:
  total_cans = math.ceil(args.days*cans_day)
  total_cost = round(total_cans*(cost + cost*tax),2)
  print("You need {} cans, which will cost ${}".format(
    total_cans, total_cost
  ))
else:
  print("Please only specify one flag.")