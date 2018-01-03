##### SIMPLE BAR CHART ########
from matplotlib import pyplot as plt
days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
plt.bar(range(len(days_in_year)), days_in_year)
plt.show()

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
plt.bar(range(len(drinks)), sales)
plt.show()

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
plt.bar(range(len(drinks)), sales)
# rotation pour que les xticklabels soient en biais
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks, rotation=30)
plt.show()

###### SIDE-BY-SIDE BARS ########

# China Data (blue bars)
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
x_values1 = [t*element + w*n for element in range(d)]

# US Data (orange bars)
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
x_values2 = [t*element + w*n for element in range(d)]
# This is called a list comprehension. It's a special way of generating a list from a formula.

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
x_values = [t*element + w*n for element
             in range(d)]
store1_x = x_values
plt.bar(store1_x, sales1)

n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
x_values = [t*element + w*n for element
             in range(d)]
store2_x = x_values
plt.bar(store2_x, sales2)

plt.show()

#### STACKEDBARS (BARRES EMPILEES)

video_game_hours = [1, 2, 2, 1, 2]
plt.bar(range(len(video_game_hours)), video_game_hours)

book_hours = [2, 3, 4, 2, 1]
plt.bar(range(len(book_hours)), book_hours, bottom=video_game_hours)

### autre exemple
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)), sales1, label="Location 1")
plt.bar(range(len(drinks)), sales2, bottom=sales1, label="Location 2")
plt.legend()

plt.show()

######## ERROR BARS #######
values = [10, 13, 11, 15, 20]
yerr = 2
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()

## autre exemple ##
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

yerr = 0.1
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)
plt.show()

###### FILL BETWEEN #######
x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]

plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error. alpha (between 0 and 1) = transparency 
plt.plot(x_values, y_values) #this is the line itself
plt.show()

# In order to correctly add or subtract from a list, we need to use list comprehension:
y_lower = [i - 2 for i in y_values]
y_upper = [i + 2 for i in y_values]

# autre exemple
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

plt.plot(range(len(month_names)), revenue)
ax= plt.subplot()
ax.set_xticks(range(len(month_names)))
ax.set_xticklabels(month_names)

y_lower = [0.9 * i for i in revenue]
y_upper = [1.1 *i for i in revenue]

plt.fill_between(range(len(month_names)), y_lower, y_upper, alpha=0.2) 

plt.show()

#### PIE CHART #####
budget_data = [500, 1000, 750, 300, 100]
plt.pie(budget_data)
plt.axis('equal')
plt.show()


# '%0.2f' — 2 decimal places, like 4.08
# '%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. You need two consecutive percent signs because the first one acts as an escape character, so that the second one gets displayed on the chart.
# '%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.axis('equal')
plt.show()

##### HISTOGRAM #####
# plt.hist finds the minimum and the maximum values in your dataset and creates 10 equally-spaced bins between those values.
plt.hist(dataset) 
plt.show()
# if we wanted to take our data from the last example and make a new histogram that just displayed the values from 66 to 69, divided into 40 bins (instead of 10) :
plt.hist(dataset, range=(66,69), bins=40)
# Histograms are best for showing the shape of a dataset. For example, you might see that values are close together, or skewed to one side. With this added intuition, we often discover other types of analysis we want to perform.


# Multiple histograms
# with transparency
plt.hist(a, range=(55, 75), bins=20, alpha=0.5)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5)

# or with a simple line
plt.hist(a, range=(55, 75), bins=20, histtype='step')
plt.hist(b, range=(55, 75), bins=20, histtype='step')

# Si les échelles des deux histogrammes sont très différences, on peut les normaliser avec normed=True
a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=100000)

plt.hist(a, range=(55, 75), bins=20, alpha=0.5, normed=True)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5, normed=True)
plt.show()




