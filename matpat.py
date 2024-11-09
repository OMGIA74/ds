import matplotlib.pyplot as plt
import numpy as np
import pandas
students = ["tucaca","rui","nene","emu","mafufu","kanade","ena","mizuki5"]
marks = [89,78,90,90,100,12,53,64]
print(marks)
def chart_of_students_and_marks():
    plt.plot(students,marks, marker = 'o', ms = 10,mec ='#FF007F', linestyle = 'dotted', c = '#FF69B4')
    plt.title("studenty mark")
    plt.xlabel("studenty nem")
    plt.ylabel("studenty mawk")
    plt.show()
chart_of_students_and_marks()

def bar_chart():
    plt.bar(students,marks, color = '#63E5FF', width = 0.5,linewidth=5,edgecolor = '#659BDF')
    plt.title("studenty mark")
    plt.xlabel("studenty nem")
    plt.ylabel("studenty mawk")
    plt.show()
bar_chart()