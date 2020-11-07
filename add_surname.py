# Dan Wu
# 11/6/2020
# Write a function named add_surname that takes as a parameter a list of first names

def add_surname(lst):
 """use a list comprehension to return a list that contains only those names that start with a "K"""
 return [x+"Kardashian" for x in lst if x[0].lower()=="k"]

