from matplotlib import pyplot as plt
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
# create the line graph :
plt.plot(x_values, y_values)
# display the graph :
plt.show()


### 1 line ###
days = range(7)
money_spent = [10, 12, 12, 10, 14, 22, 24]

plt.plot(days, money_spent)

plt.show()

#### 2 lines ###
# Days of the week:
days = [0, 1, 2, 3, 4, 5, 6]
# Your Money:
money_spent = [10, 12, 12, 10, 14, 22, 24]
# Your Friend's Money:
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
# Plot your money:
plt.plot(days, money_spent)
# Plot your friend's money:
plt.plot(days, money_spent_2)
# Display the result:
plt.show()

# another example
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()

#### style ####
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')

# Dashed:
plt.plot(x_values, y_values, linestyle='--')
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
# No line:
plt.plot(x_values, y_values, linestyle='')

# A circle:
plt.plot(x_values, y_values, marker='o')
# A square:
plt.plot(x_values, y_values, marker='s')
# A star:
plt.plot(x_values, y_values, marker='*')

#all this
from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='purple', linestyle='--')
plt.plot(time, costs, color='#82edc9', marker='s')
plt.show()

#### ZOOM ###
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
# plt.axis [minimum x-value, maximum x-value, minimum y-value, maximum y-value]
plt.axis([0, 3, 2, 5])
plt.show()

### Labeling the Axes ###

#We can label the x- and y- axes by using plt.xlabel and plt.ylabel. 
#The plot title can be set by using plt.title.
hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
happiness = [9.8, 9.9, 9.2, 8.6, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]
plt.plot(hours, happiness)
plt.xlabel('Time of day')
plt.ylabel('Happiness Rating (out of 10)')
plt.title('My Self-Reported Happiness While Awake')
plt.show()

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My last Twelve Years of Coffee Drinking')
plt.show()

### Subplots ####
# plt.subplot(number of rows, number of columns, index of the subplot) 

# Data sets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
plt.title('Second Subplot')

# Display both subplots
plt.show()

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 2, 1)
plt.plot(months, temperature, color='green')
plt.title('Temperature per month')

plt.subplot(1, 2, 2)
plt.plot(months, flights_to_hawaii, color='steelblue')
plt.title('Flights to Hawaii per month')

plt.show()

####### SPACING BETWEEN OUR SUBPLOTS ######
# par défaut :
# plt.subplots_adjust(left=0.125, right=0.9, bottom=0.2, top=0.9, wspace=0.2, hspace=0.2)
# wspace — the horizontal space between adjacent subplots, with a default of 0.2
# hspace — the vertical space between adjacent subplots, with a default of 0.2

# Left Plot
plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Right Plot
plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Subplot Adjust
plt.subplots_adjust(wspace=0.35)

plt.show()

#autre essai
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()

#### LEGENDS #######

plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
plt.legend(['parabola', 'cubic'])
plt.show()


plt.legend(['parabola', 'cubic'], loc=6)
plt.show()

plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16],
         label="parabola")
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64],
         label="cubic")
plt.legend() # Still need this command!
plt.show()

# autre test
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

legend_labels=["Hyrule", "Kakariko", "Gerudo Valley"]
plt.legend(legend_labels, loc=9)
plt.show()

###### MODIFY TICKS (REPERES SUR LES DIFFERENTS AXES) ########

ax = plt.subplot()
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
ax.set_xticks([1, 2, 4])
plt.show()

# autre exemple
ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])
plt.show()

# autre exemple
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])
plt.show()

####### FIGURES ##########

# close all plots
plt.close('all')
# create new figures and size them how we want
# plt.figure(figsize=(width, height))
plt.figure(figsize=(4, 10))
# save it to png, svg, or pdf
# plt.savefig('name_of_graph.png')
plt.plot(x, parabola)
plt.savefig('tall_and_narrow.png')

# exemple
word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')
plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')

plt.figure(figsize=(3, 7))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')

##### REVIEW ######
x = range(6)
y1 = [1, 2, 3, 4, 5, 6]
y2 = [-1, 1, 3, 4, 4, 4]

plt.plot(x, y1, marker='o', color='pink')
plt.plot(x, y2, marker='o', color='gray')

plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(["Y1","Y2"], loc=4)

plt.show()


