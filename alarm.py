#!/usr/bin/env python3

X = int(input())
H = int(input())
M = int(input())
# X-user sleep minutes, H-user current time (hours), M- user current time (minutes)
Fhh = X//60
# Full hours in user X input
Fmm = X - Fhh*60
# Full minutes in user X input
Z = (((Fmm + M)//60)*60)
# 60 or 0. Need for alarm minutes 
print ((X + (H*60) + M)//60)
print (M + Fmm - Z)
# Shows time for alarm. Hours and minutes
