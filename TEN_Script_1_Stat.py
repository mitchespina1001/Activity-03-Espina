class StatCalculate():
    def Health (base, iv, ev, level):
        return ((((2*base)+ iv +(ev/4) *level)/100)) + level +10
    
    def OtherStat(base, iv, ev, level, nature):
        return ((((((2*base)+ iv +(ev/4))* level))/100)+5) * nature