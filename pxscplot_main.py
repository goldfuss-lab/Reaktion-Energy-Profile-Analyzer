#!/C/Users/goldfuss/AppData/Local/Programs/Python/Python310/python

#!/data/data/com.termux/files/usr/bin/python

# out of xtb-scan.xyz extract energies
# set arr[0] = 0 to fill it,
# then do all from 1 to end via [1:];   
# plot curve
# find minima and maxima

import re 
import sys 
#import plotext as plt 
import matplotlib.pyplot as plt 

arr=[]
arr=[0]
ARR=[]
MinInd=[]
MinARR=[]
MinSum=[]
#MinSumA={}
MaxInd=[]
MaxARR=[]
MaxSum=[]

try:
    file= open(sys.argv[1],"r")
except:
    print("dummer OpenFile Fehler")

# extract energies-2nd-word in line
# append into string array arr
for lines in file: 
#   if re.search(sys.argv[1], lines): 
   if re.search('energy:', lines): 
      arr.append(lines.split()[1])
        
file.close()

#larr= len(arr)
#print("arr-Length is " , larr)

## convert arr-string to ARR-float
## but key starts at 0
for i in arr:                          
    ARR.append(float(i))
lARR= len(ARR)
#print("ARR-Length is " , lARR)
#for i in ARR[1:]:
#    print("ARR= " , i , "at: ", ARR.index(i))

# for plotext 
# plt.theme('clear')
plt.plot(ARR[1:]) 
# plt.show()
plt.savefig('PLOT.png')

###  GLOBAL Mini and Maxi
Maxi = max(ARR[1:])
Mini = min(ARR[1:])
print("GloMax: " , Maxi, " at: ", (ARR.index(Maxi)))
print("GloMin: " , Mini, " at: ", (ARR.index(Mini)))
###    global  end   ######

# find LOCAL MINIMA in ARR-float: index-list MinInd
for i in range(2, lARR-1): 
   if (ARR[i - 1] > ARR[i] < ARR[i + 1]) and (ARR[i - 2] > ARR[i] < ARR[i + 2]): 
      MinInd.append(i)

# find LOCAL MAXIMA in ARR-float: index-list MaxInd
for i in range(2, lARR-1): 
   if (ARR[i - 1] < ARR[i] > ARR[i + 1]) and (ARR[i - 2] < ARR[i] > ARR[i + 2]): 
      MaxInd.append(i)

##  PRINT LocMinima
lMin= len(MinInd)
print("\nNumb. of LocMinima is " ,lMin)
#print("LocMin-INDEX: ", MinInd )

print("Local-Minima      at Index: " )
for i in range(0, lMin): 
     print(ARR[MinInd[i]] , " at ",MinInd[i])
     kcal = float( (ARR[MinInd[i]] - Mini) * 627.51 )
     print("%.2f" %kcal  , " kcal/mol " , "\n"+ int(kcal) * "#")

##  PRINT LocMaxima 
lMax= len(MaxInd)
print("\nNumb. of LocMaxima is " ,lMax)
#print("LocMax-INDEX: ", MaxInd )

print("Local-Maxima      at Index: " )
for i in range(0, lMax): 
     print(ARR[MaxInd[i]] , " at ",MaxInd[i])
     kcal = float( (ARR[MaxInd[i]] - Maxi) * 627.51 )
     print("%.2f" %kcal  , " kcal/mol " , "\n"+ (-1) * int(kcal) * "#")

