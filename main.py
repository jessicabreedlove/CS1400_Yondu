'''
Project Name: Yondu Udonta
Author: Jessica Reece
Due Date: 02/05/2021
Course: CS1400-601

This program will calculate the amount of units(money) that need to be given to Yondu, Peter and the rest of the Reavers crew after they get their plunder.
You will need to enter positive integers, and will need atleast 3 Reavers. The test threw me for a second, but then it was just a typo :)
'''


def main():

    try:
        #input total reavers
        reavers = int(input("Enter number of Reavers: "))
        #input total units
        units = int(input("Enter number of units: "))
    except ValueError:
        print("Enter postive integers for reavers and units.")
        return
    
    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return 
    #give 3 units to all crew members other than Yondu and Peter
    crew = (reavers-2)*3
    units -= crew
    #Calculate Yondus share
    yondu_share = int(units * 0.13)
    units -= yondu_share
    #Calculate Peters share
    peter_share = int(units * 0.11)
    units -= peter_share
    crew_share = units//reavers
    yondu_share += units//reavers
    peter_share += units//reavers
    rbf = int(units % reavers)
    print("Yondu's share:", yondu_share)
    print("Peter's share:", peter_share)
    print("Crew's share:", crew_share)
    print("RBF//'s share:", rbf)

    

if __name__ == "__main__":
    main()
