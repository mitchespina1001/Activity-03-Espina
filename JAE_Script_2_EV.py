class EvCalculate():
    def EVComputation (stat, modifier, level, base, iv, ev):
        D= (((2*base)+iv+(ev/4))*(level/100))
        return ((((((stat/modifier)-D)*400))/level)/4) *4
