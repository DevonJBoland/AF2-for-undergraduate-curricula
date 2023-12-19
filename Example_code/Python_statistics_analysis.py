import pandas as pd
import matplotlib.pyplot as plt
import argparse as ap

parser = ap.ArgumentParser(description="Script to count Google Forms CSV")
parser.add_argument("input", type = str, help="file to be processed")
parser.add_argument("outname", type = str, help="name of the output file")

args = parser.parse_args()


def load_data(file):
    data = pd.read_csv(open(file, "r"), delimiter=",")
    return data


def count_data(datum):
    total_response_df = pd.DataFrame()
    total_response_df['Responses'] = ["Agree", "Neutral", "Disagree"]
    questions = list(datum.columns.values)
    for question in questions:
        response_list = datum[question].values.tolist()
        agree_count = response_list.count("Agree")
        neutral_count = response_list.count("Neutral")
        disagree_count = response_list.count("Disagree")
        total_response_df[question] = [agree_count, neutral_count, disagree_count]
    total_response_df.to_csv(open(args.outname, "w+"))
    return total_response_df


to_count = load_data(args.input)
processed = count_data(to_count)
print("This is a debug place holder")

##########################################################################################

import scipy
import scipy.stats as stats
import numpy as np
import csv

def load_func(file):
    with open(file, "r") as f:
        arr = np.loadtxt(f, delimiter=",", skiprows=1)
        arr = arr.T
    return arr

with open("Likert_Analysis/PreStudents.csv", "r") as f2:
    reader = csv.reader(f2)
    question_list = list(next(reader))


prestudent = load_func("Likert_Analysis/PreStudents.csv")
poststudent = load_func("Likert_Analysis/PostStudents.csv")
experts = load_func("Likert_Analysis/Experts.csv")

# test_case = prestudent[2]

def ttest_analysis(data1, data2, data3):
    with open("t-test_analysis.log", "w+") as output, open("meanstats.csv", "w+") as meantxt, open("stderrorstats.csv", "w+") as stdetxt, open("survey_questions.txt", "w+") as questions:
        for question in range(0, 31, 1):
            # Perform Pre & Post Student T-test
            prevspost = str(stats.ttest_ind(a = data1[question], b = data2[question]))
            # Perform Pre & Expert T-test
            prevsexpt = str(stats.ttest_ind(a = data1[question], b = data3[question]))
            # Perform Post & Expert T-test
            postvsexpt = str(stats.ttest_ind(a = data2[question], b = data3[question]))

            # Calculate Mean
            premean = scipy.mean(data1[question])
            postmean = scipy.mean(data2[question])
            expertmean = scipy.mean(data3[question])
            # Calculate Std error of the mean
            prestde = stats.sem(data1[question])
            poststde = stats.sem(data2[question])
            expertstde = stats.sem(data3[question])
            
            # Write output
            output.write("For Question #"+str(question)+": "+question_list[question]+"\n")
            output.write("Pre & Post Student T-test results: "+prevspost+"\n"+"Pre-Student & Exp Student T-test results: "+prevsexpt+"\n"+"Post & Expt Student T-test results: "+postvsexpt+"\n"+"\n\n")
            meantxt.write(str(premean)+","+str(postmean)+","+str(expertmean)+"\n")
            stdetxt.write(str(prestde)+","+str(poststde)+","+str(expertstde)+"\n")
            questions.write(str(question_list[question]+"\n"))
            

ttest_analysis(prestudent, poststudent, experts)
