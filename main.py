import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

#finding angle alpha
a = round(math.atan(2 / 4), 5)
adeg = round(math.degrees(a), 5)

#finding angle beta
b = round(math.atan(5 / 4), 5)
bdeg = round(math.degrees(b), 5)

print("Angle α is: ",a," radians OR ",adeg," degrees")
print("Angle β is: ",b," radians OR ",bdeg," degrees")

#defining function for F12, F13 and F23 by change in θ
def column(th1):
    # finding F12, F13 and F23 by the given formulas
    f = 1000
    th = round(math.radians(th1),3)
    f12 = round( f * ((math.sin(a) * math.sin(th) + math.cos(a) * math.cos(th)) / (math.sin(b) * math.cos(a) - math.cos(b) * math.sin(a))), 3)
    f13 = round( f * ((math.sin(b) * math.sin(th) + math.cos(b) * math.cos(th)) / (math.sin(b) * math.cos(a) - math.cos(b) * math.sin(a))), 3)
    f23 = round(f12 * math.sin(b), 3)
    table.add_row([th1,th,f12,f13,f23])
    y12.append(f12)
    y13.append(f13)
    y23.append(f23)

#running loop for variation in value of θ and printing table
table = PrettyTable(["θ (in deg)","θ (in rad)","F12 (compressive)","F13 (tensile)","F23 (tensile)"])
x = []
y12 = []
y13 = []
y23 = []
for th1 in range(0, 95, 5):
    x.append(th1)
    column(th1)
print(table)

#graphing the graphs of θ with F12, F13 and F23
print('''Enter 1 for all plots seprately
Enter 2 for all plots seprately in same window
Enter 3 for all plots in same graph''')

ch = int(input("Enter your choice: "))

if (ch == 1):
    plt.plot(x, y12, color = 'springgreen')
    plt.xlabel('θ (in degrees)')
    plt.ylabel('F12 (in Newtons)')
    plt.title("Variation of F12 with θ")
    plt.show()

    plt.plot(x, y13, color = 'red')
    plt.xlabel('θ (in degrees)')
    plt.ylabel('F13 (in Newtons)')
    plt.title("Variation of F13 with θ")
    plt.show()

    plt.plot(x, y23, color = 'blue')
    plt.xlabel('θ (in degrees)')
    plt.ylabel('F23 (in Newtons)')
    plt.title("Variation of F23 with θ")
    plt.show()

elif (ch == 2):

    figure, axis = plt.subplots(1, 3)

    axis[0].plot(x, y12, color = 'springgreen')
    axis[0].set_title("Variation of F12 with θ")

    axis[1].plot(x, y13, color = 'red')
    axis[1].set_title("Variation of F13 with θ")

    axis[2].plot(x, y23, color = 'blue')
    axis[2].set_title("Variation of F23 with θ")

    plt.show()

elif (ch==3):
    plt.plot(x, y12, color = 'springgreen')
    plt.plot(x, y13, color = 'red')
    plt.plot(x, y23, color = 'blue')
    plt.xlabel('θ (in degrees)')
    plt.ylabel('Forces (in Newtons)')

    plt.legend(["F12","F13","F23"], loc="lower left")

    plt.show()

