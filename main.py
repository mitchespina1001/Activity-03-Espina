from pstats import Stats
import TEN_Script_1_Stat as ST
import JAE_Script_2_EV as EV
import math

def ProceedOrExit():
    Choose = int(input("\n Want to try again?? Choose [1] if YES and [0] if NO \nOPTION: "))
    if Choose == 1: main()
    elif Choose == 0: exit()
    else:
        print("INVALID IS INPUT!!!!!")
        ProceedOrExit()
    
def main():
    print ("WELCOME TO POKEMON STAT AND EV CALCULATOR!!!!!!!")
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
            print("Proceeding!!!!")
            break
    
    while True:
        Option = int(input("\nPokemon Calculator Type: \nType [0] if STAT Type and [1] if EV Type: \nOPTION: "))

        if Option == 0:
            print("\n CHOOSE OTHER STAT?? TYPE [1] IF YES AND [2] IF NO.")
            take = int(input("\n CHOICE: "))
            if take == 1:
                print ("\nOPTIONS: \n[1]ATTACK, [2]SPECIAL ATTACK, [3]DEFENSE, [4]SPECIAL DEFENSE, [5]SPEED")
                tk = int(input("\n [STAT] What would you like to compute? "))
                if tk == 1:
                    name = 'ATTACK'
                    tke = int(input("\n[1] for Beneficial or [2] for Hindering "))
                    if tke == 1:
                        nature = 1.1

                    elif tke ==2:
                        nature = 0.9
                if tk == 2:
                    name = 'SPECIAL ATTACK'
                    tke = int(input("\n[1] for Beneficial or [2] for Hindering "))
                    if tke == 1:
                        nature = 1.1

                    elif tke ==2:
                        nature = 0.9

                if tk == 3:
                    name = 'DEFENSE'
                    tke = int(input("\n[1] for Beneficial or [2] for Hindering "))
                    if tke == 1:
                        nature = 1.1

                    elif tke ==2:
                        nature = 0.9

                if tk == 4:
                    name = 'SPECIAL DEFENSE'
                    tke = int(input("\n[1] for Beneficial or [2] for Hindering "))
                    if tke == 1:
                        nature = 1.1

                    elif tke ==2:
                        nature = 0.9

                if tk == 5:
                    name = 'SPEED'
                    tke = int(input("\n[1] for Beneficial or [2] for Hindering "))
                    if tke == 1:
                        nature = 1.1

                    elif tke ==2:
                        nature = 0.9

                totalOtherStatComputation = ST.StatCalculate.OtherStat(base, iv, ev, level, nature)
                if totalOtherStatComputation <=510:
                    print("\nCALCULATING", name , "VALUE :", totalOtherStatComputation)

                else:
                    print("POKEMON's TOTAL EV EXCEEDS!!!!")
                ProceedOrExit()

            elif take == 2:
                ten = ST.StatCalculate.Health(base, iv, ev, level)
                if ten <=510:
                    print("HP VALUE: ",ten)
                else:
                    print("POKEMONS's TOTAL STAT EXCEEDS!!!!!")                    
                ProceedOrExit()

            else:
                print("INVALID INPUT!!!!!!!")

        elif Option == 1:
            stat = int(input("STAT: "))
            print("Choose [1] for Beneficial or [2] for Hindering")
            Choice = int(input("\n Modifier:"))
            if Choice == 1:
                modifier = 1.1
            
            elif Choice == 2:
                modifier = 0.9

            else:
                print("INVALID INPUT!!!!")

            totalEVComputation = EV.EvCalculate.EVComputation(stat, modifier, level, base, iv, ev)
            if totalEVComputation <=510:
                print("TOTAL EV: ", totalEVComputation)
            
            else:
                print("POKEMON's TOTAL EV ALREADY EXCEEDS!!!!!!!")
            ProceedOrExit()


        else:
            print("INVALID INPUT!!!!!!!!!!!!")

main()

