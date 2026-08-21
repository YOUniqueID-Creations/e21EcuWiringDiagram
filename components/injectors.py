# components/injectors.py
import schemdraw.elements as elm

def get_injector():
    """Returns a 2-pin Injector coil."""
    return elm.Ic(
        pins=[
            elm.IcPin(name='ECU', pin='1', side='left'),
            elm.IcPin(name='+12V', pin='2', side='right'),
        ],
        w=2, h=1, pinspacing=1
    )

def get_injector_1(mre_x, mre_y):

    return get_injector().at((mre_x + 9, mre_y - 1.8)).label('Injector 1', loc='center')

def get_injector_2(mre_x, mre_y):
    return get_injector().at((mre_x + 9.2, mre_y)).label('Injector 2', loc='center')

def get_injector_3(mre_x, mre_y):
    return get_injector().at((mre_x + 9.1, mre_y + 2)).label('Injector 3', loc='center')

def get_injector_4(mre_x, mre_y):
    return get_injector().at((mre_x + 9, mre_y + 4)).label('Injector 4', loc='center')
