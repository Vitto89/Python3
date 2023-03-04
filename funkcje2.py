import time
def welcome_basic()
    time.sleep(1.5)
    print('przygotowaie obrazu systemu')
    time.sleep(1.5)
    print('sprawdzanie bedow w systemie')
    time.sleep(1.5)
    print('siema')

def welcome_full(imie, wiek)
    if wiek >= 18:
        print('Dzien dobry', imie)
    else:
        print('Czesc', imie)
def stan_zdrowia(waga, wzrost):
    BMI = waga / (wzrost**2)
    return BMI >35:
elif BMI >28:
    return 2
return 3