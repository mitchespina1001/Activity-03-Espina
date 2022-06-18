import TEN_Script_1_Stat as ST
import JAE_Script_2_EV as EV
import math

def main():
    print ("WELCOME TO POKEMON STAT AND EV CALCULATOR!!!!!!!")
    print ("Kindly fill in the following:\n")
    while True:
        base = int(input("BASE HP: "))
        level = int(input("LEVEL: "))
        ev = int(input("EV must be [0-255]. \nEV: "))
        if ev >255:
            print("EV EXCEEDS!!!!!\n")
            main()
        iv = int(input("IV must be [0-31]. \nIV: "))
        if iv >31:
            print("IV EXCEEDS!!!\n")
            main()
        else:
            break

    while True:
        print("\nType [0] if STAT Type and [1] if EV Type:")
        Option = int(input("OPTION: "))

        if Option == 0:
            print("\n******************************STAT CALCULATOR******************************\n")
            print("\n[1]Other Stat    [2]Proceed with the original stat")
            take = int(input("CHOICE: "))

            if take == 1:
                print ("\n[a] ATTACK  [b] SPECIAL ATTACK  [c] DEFENSE  [d] SPECIAL DEFENSE  [e] SPEED")
                tk = str(input("What would you like to compute? "))

                if tk == 'a':
                    n = 'ATTACK'
                    tke = str(input("\n[ben] Beneficial - [hin] Hindering \nCHOICE: "))
                    if tke == 'ben':
                        nme = 'BENEFICIAL'
                        nature = 1.1
                    elif tke =='hin':
                        nme = 'HINDERING'
                        nature = 0.9

                if tk == 'b':
                    n = 'SPECIAL ATTACK'
                    tke = str(input("\n[ben] Beneficial - [hin] Hindering \nCHOICE: "))
                    if tke == 'ben':
                        nme = 'BENEFICIAL'
                        nature = 1.1
                    elif tke =='hin':
                        nme = 'HINDERING'
                        nature = 0.9

                if tk == 'c':
                    n = 'DEFENSE'
                    tke = str(input("\n[ben] Beneficial - [hin] Hindering \nCHOICE: "))
                    if tke == 'ben':
                        nme = 'BENEFICIAL'
                        nature = 1.1
                    elif tke =='hin':
                        nme = 'HINDERING'
                        nature = 0.9

                if tk == 'd':
                    n = 'SPECIAL DEFENSE'
                    tke = str(input("\n[ben] Beneficial - [hin] Hindering \nCHOICE: "))
                    if tke == 'ben':
                        nme = 'BENEFICIAL'
                        nature = 1.1
                    elif tke =='hin':
                        nme = 'HINDERING'
                        nature = 0.9

                if tk == 'e':
                    n = 'SPEED'
                    tke = str(input("\n[ben] Beneficial - [hin] Hindering \nCHOICE: "))
                    if tke == 'ben':
                        nme = 'BENEFICIAL'
                        nature = 1.1
                    elif tke =='hin':
                        nature = 0.9

                totalOtherStatComputation = ST.StatCalculate.OtherStat(base, iv, ev, level, nature)
                if totalOtherStatComputation <=510:
                    print(nme , ": " , nature)
                    print(n , "CALCULATION :", totalOtherStatComputation)

                else:
                    print("TOTAL OTHER STAT EXCEEDS!!!!")
                PE()

            elif take == 2:
                ten = ST.StatCalculate.Health(base, iv, ev, level)
                if ten <=510:
                    print("HP VALUE: ",ten)
                else:
                    print("TOTAL STAT EXCEEDS!!!!!")                    
                PE()

            else:
                print("INVALID INPUT!!!!!!!")

        elif Option == 1:
            print("\n******************************EV CALCULATOR******************************\n")
            stat = int(input("STAT: \n"))
            print("[ben] Beneficial - [hin] Hindering")
            Choice = str(input("\nModifier:"))
            if Choice == 'ben':
                name = 'BENEFICIAL'
                modifier = 1.1

            elif Choice == 'hin':
                modifier = 0.9
                name = 'HINDERING'

            else:
                print("INVALID INPUT!!!!")

            totalEVComputation = EV.EvCalculate.EVComputation(stat, modifier, level, base, iv, ev)
            if totalEVComputation <=510:
                print(name ,": ", modifier , "\nTOTAL EV: ", totalEVComputation)

            else:
                print("TOTAL EV ALREADY EXCEEDS!!!!!!!")
            PE()


        else:
            print("INVALID INPUT!!!!!!!!!!!!")

def PE():
    Choose = int(input("\nWould you like to compute again?? \n[1] if YES - [0] if NO \nOPTION: "))
    if Choose == 1: main()
    elif Choose == 0: 
        print ("\n\nThank you for using POKEMON STAT/EV CALCULATOR, SEE YAAAH")
        exit()
    else:
        print("INVALID IS INPUT!!!!!")
        PE()
main()