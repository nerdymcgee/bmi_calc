#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#  
#  Copyright 2014 Andre Chang <chang.r.andre@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


# figure out how to run a bmi calculator in python


#allows for float
from __future__ import division

print "this is a BMI calculator."


print "Welcome to the BMI calculator! Follow the instructions below."

# takes and stores the user input for their weight & height

pounds = raw_input ("How much do you weigh?")

height = raw_input("How tall are you ?(in inches)")


#transforms user input to integer

pounds = float(pounds)
height = float(height)
# takes weight & height and finds BMI
#  BMI = ( Weight in Pounds / ( Height in inches x Height in inches ) ) x 703
total_bmi = (float(pounds) / (height*height)) *703


#turns total_bmi into integer
total_bmi = float(total_bmi) 
# pounds / height**2


print ""
print ""
print "OK!"
print ""
print "If you are %s inches tall and %s pounds heavy,your total BMI should be approximately %s" % (height,pounds,total_bmi)

print ""
print ""
print ""

# alerts user to BMI classification, gives in fo
#Underweight = <18.5
#Normal weight = 18.5–24.9
#Overweight = 25–29.9
#Obesity = BMI of 30 or greater


def bmi_ranking():
	print "Here is more info about your BMI."
	print ""
	print ""
	if total_bmi < 18.5:
		print "UNDERWEIGHT DIAGNOSIS"
		print "-----------------------"
		print "-----------------------"
		print "Your BMI is less than 18.5. A lean BMI can indicate that your weight maybe too low"
		print "You should consult your physician to determine if you should gain weight, as low body mass can decrease your body's immune system, which could lead to ilness such as disappearance of periods (women), bone loss, malnutrition and other conditions. "
		print "The lower your BMI the greater these risks become."
		print ""
		print "In order to gain weight, you will have to eat more calories."
		print "You will need to include regular exercise and strength training into your lifestyle in order to prevent gaining too much weight as fat. "
		print "And, as I mentioned, those extra calories should come mainly from additional carbohydrates."
		print "It is best to gain weight slowly and steadily. This will help to ensure that your weight gain is in the form of lean body mass and not excessive fat. "
		print "Don't try to gain more than 1/2 pound a week,ok?"
		print ""
		print ""
		print "--------------------------------------------------------"
		print "---------------------MORE TIPS--------------------------"
		print "--------------------------------------------------------"
		print "-----Drink 6-8 glasses of distilled water a day.--------"
		print "----------Eat frequent but small meals..----------------"
		print "--------Eat lots of raw fruit and vegatables.-----------"
		print "--------------------------------------------------------"
		print "--------------------------------------------------------"
		print "--------------------------------------------------------"
		print "--------------------------------------------------------"
	if total_bmi >=18.5 and total_bmi<= 24.9:
		print "NORMAL WEIGHT RANGE"
		print "-----------------------"
		print "-----------------------"
		print "Congratulations!"
		print "You've been keeping your BMI in the good place:18.5-24.9."
		print "Keep it up!"
	if total_bmi >=25 and total_bmi<29.9:
		print "OVERWEIGHT DIAGNOSIS"
		print "-----------------------"
		print "-----------------------"
		print "The method of treatment depends on your level of obesity, overall health condition, and motivation to lose weight."
		print "f you are overweight, losing as little as 7-10 percent of your body weight may improve many of the problems linked to being overweight, such as high blood pressure and diabetes."
		print "Slow and steady weight loss of no more than 1-2 pounds per week is the safest way to lose weight."
		print "Rapid weight loss can cause you to lose muscle rather than fat." 
		print "It also increases your chances of developing other problems, such as gallstones and nutrient deficiencies."
		print "Making long-term changes in your eating and physical activity habits is the only way to lose weight and keep it off!"
		print ""
		print ""
		print "Whether you are trying to lose weight or maintain your weight, you must improve your eating habits."
		print " Eat a variety of foods, such as pasta, rice, wholemeal bread, and other whole-grain foods."
		print "Reduce your fat-intake."
		print " You should also eat lots of fruits and vegetables."
		print "Making physical activity a part of your daily life is an important way to help control your weight."
		print "Eat a variety of foods, such as pasta, rice, wholemeal bread, and other whole-grain foods. Reduce your fat-intake. "
		print "You should also eat lots of fruits and vegetables."

		print "Making physical activity a part of your daily life is an important way to help control your weight." 
		print "Try to do at least 30 minutes of physical activity a day on most days of the week. "
		print "The activity does not have to be done all at once."
		print " It can be done in stages: 10 minutes here, 20 minutes there, providing it adds up to 30 minutes a day."
		

bmi_ranking()
