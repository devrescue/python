#Snippet 1: Python F String with Variables and Arithmetic
name = "King"
width = 76
length = 80
print(f"The dimensions of a {name} Sized bed is {width}x{length} inches") #variables
print(f"The dimensions of a {name} Sized bed is {width*2.54}x{length*2.54} centimeters") #arithmetic
print("\n\n") #new line

#Output
#The dimensions of a King Sized bed is 76x80 inches
#The dimensions of a King Sized bed is 193.04x203.2 centimeters

#Snippet 2: Python F String with Functions
def farenheit_to_celsius(input):
    return ((input - 32) * 5/9)

farenheit = 90
print(f"{farenheit}F converted to celsius is {round(farenheit_to_celsius(farenheit),2)}°") #nested function

farenheit = 70
print(f"{farenheit}F converted to celsius is {round(farenheit_to_celsius(farenheit),2)}°") #nested function

farenheit = 100
print(F'{farenheit}F converted to celsius is {round((lambda f: (f-32)*5/9)(farenheit))}°') #lambda function

print("\n\n") #new line

#Output
#90F converted to celsius is 32.22°
#70F converted to celsius is 21.11°
#100F converted to celsius is 38°

#Snippet 3: Python F String with Dates
from datetime import *
from dateutil import tz

cometName = 'comet 13p/olbers'
desc='Halley-type'
passingDate = date(2024, 6, 30)

#Using format codes to present the date
print(f'A Halley-type comet called {cometName.upper()}, will next pass earth on {passingDate:%A, %B %d, %Y}.') 


LA = tz.gettz('America/Los_Angeles')
now = datetime.now(LA)
print(f'The current date and time in Los Angeles is {now:%a %d %b %Y %I:%M:%S.%f %p %z}.') 


#Output
#A Halley-type comet called COMET 13P/OLBERS, will next pass earth on Sunday, June 30, 2024.
#The current date and time in Los Angeles is Tue 06 Jul 2021 06:14:08.180515 AM -0700.

#Snippet 4: Python F String with Quotes and Brackets
print(f'California is nicknamed the {"Golden State"!r}')
print(f"California is nicknamed the {'Golden State'!r}")
print(f"California is nicknamed the \"{'Golden State'}\"")

#Output
#California is nicknamed the 'Golden State'
#California is nicknamed the 'Golden State'
#California is nicknamed the "Golden State"

#################################

print(f"4 ∉ {{2,3,5,7,11}}")
print(f"{{{{1,2,3,4,5}}}}")
print(f"{(2,3,5,7,11)}")

#Output
#4 ∉ {2,3,5,7,11}
#{{1,2,3,4,5}}
#(2, 3, 5, 7, 11)

#################################

#Snippet 5: Python F String with Multiple Lines
countryList = {
  1: "USA",
  2: "China",
  3: "Japan"
}

rankingList = (
f"Top 3 World Economies as at 2020 are: "
f"{countryList[1]} "
f"{countryList[2]} "
f"{countryList[3]} "
)

print(rankingList)
print("\n")

#Output 
#Top 3 World Economies as at 2020 are: USA China Japan

betterRankingList = (
 f"""
 Top 3 World Economies by Size in 2020 are: 
 {countryList[1]}
 {countryList[2]} 
 {countryList[3]} 
 """
)

print(betterRankingList)
print("\n")

#Output
#Top 3 World Economies by Size in 2020 are:
#USA
#China
#Japan

#Snippet 6: Python F String with Numbers

world_population = 7794798739

#Separator
print(f"{world_population:,}")
print(f"{world_population:,.2f}")

#Precision
print(f"{3248935030.778899:.3f}")

from decimal import *

#Scientific
print( f"{Decimal('7794798739'):.2E}")
print( f"{Decimal(world_population):.2e}")

#Percent
print( f"{Decimal('0.9999'):%}")
print( f"{Decimal('25'):%}")
print( f"{Decimal('0.33'):%}")

#Hexadecimal
print( f"{255:x}")
print( f"{100+55:x}")
print( f"{155:x}")

#Binary
print( f"{1000:b}")
print( f"{100:b}")
print( f"{10:b}")

#Leading Zeros
num = 2999

print(f"{num:05}") 
print(f'{num:+011}')
print( f'{num:-011}')
print(f"{num:011}") 

num = -2999
print(f"{num:05}") 
print(f'{num:+011}')
print( f'{num:-011}')
print(f"{num:011}") 

#Output
# 7,794,798,739
# 7,794,798,739.00
# 3248935030.779
# 7.79E+9
# 7.79e+9
# 99.99%
# 2500%
# 33%
# ff
# 9b
# 9b
# 1111101000
# 1100100
# 1010
# 02999
# +0000002999
# 00000002999
# 00000002999
# -2999
# -0000002999
# -0000002999
# -0000002999

#Snippet 7: Python F String  with Text Layout
countryGDPList = {
  "USA": "22,675,271",
  "China":"16,642,318",
  "Japan":"5,378,136"
}

#The :<X Left aligns output within the available space specified by X characters eg. :<20 left align within 20 character space.
betterRankingList = (
 f"""
 Top 3 World Economies by GDP (2021 est.) are: 
 {'COUNTRY':<10} {'GDP (US$ M) per IMF':<20}
 {'USA':<11}{countryGDPList["USA"]:<20}
 {'China':<11}{countryGDPList["China"]:<20}
 {'Japan':<11}{countryGDPList["Japan"]:<20}
 """
)

print(betterRankingList)
print("\n")

#Output
#Top 3 World Economies by GDP (2021 est.) are:
#  COUNTRY    GDP (US$ M) per IMF
#  USA        22,675,271
#  China      16,642,318
#  Japan      5,378,136

##############################################
#The :>X Right aligns output within the available space specified by X characters eg. :>20 right align within 20 character space.
betterRankingList = (
 f"""
 Top 3 World Economies by GDP (2021 est.) are: 
 {'COUNTRY':<10} {'GDP (US$ M) per IMF':>20}
 {'USA':<11}{countryGDPList["USA"]:>20}
 {'China':<11}{countryGDPList["China"]:>20}
 {'Japan':<11}{countryGDPList["Japan"]:>20}
 """
)

print(betterRankingList)
print("\n")

#Output
#Top 3 World Economies by GDP (2021 est.) are:
#  COUNTRY     GDP (US$ M) per IMF
#  USA                  22,675,271
#  China                16,642,318
#  Japan                5,378,136

##############################################
#The :^X Center aligns output within the available space specified by X characters eg. :^20 center align within 20 character space. 

betterRankingList = (
 f"""
 Top 3 World Economies by GDP (2021 est.) are: 
 {'COUNTRY':<10} {'GDP (US$ M) per IMF':^20}
 {'USA':<11}{countryGDPList["USA"]:^20}
 {'China':<11}{countryGDPList["China"]:^20}
 {'Japan':<11}{countryGDPList["Japan"]:^20}
 """
)

print(betterRankingList)
print("\n")

#Top 3 World Economies by GDP (2021 est.) are:
#  COUNTRY    GDP (US$ M) per IMF
#  USA             22,675,271
#  China           16,642,318
#  Japan            5,378,136

##############################################