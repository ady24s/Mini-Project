#!/usr/bin/env python3
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_0123456789"

while (True):
     password_len = int(input("Enter Length of the password:"))
     password_count = int(input("Enter the number of passwords needed:"))
     for x in range(0,password_count):
         password = ""
         for x in range (0,password_len):
             password_char = random.choice(chars)
             password = password + password_char
         print("Random password generated:",password)
