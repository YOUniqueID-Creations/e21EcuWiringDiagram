# components/coils.py
import schemdraw.elements as elm

def get_coil():
    return elm.Ic(
        pins=[
            elm.IcPin(name='ECU Trigger', pin='A', side='left'),
            elm.IcPin(name='Logic GND', pin='B', side='right'),
            elm.IcPin(name='Power Gnd', pin='C', side='right'),
            elm.IcPin(name='12v', pin='D', side='left'),
        ],
        w=5, h=2.5, pinspacing=1
    )

def get_coil_1(mre_x, mre_y):
    """Returns a 4-pin LS1 coil."""
    return get_coil().at((mre_x + 3, mre_y)).label('Ignition\nCoil 1', loc='center')

def get_coil_2(mre_x, mre_y):
    """Returns a 4-pin LS1 coil."""
    return get_coil().at((mre_x + 3, mre_y - 5)).label('Ignition\nCoil 2', loc='center')

def get_coil_3(mre_x, mre_y):
    """Returns a 4-pin LS1 coil."""
    return get_coil().at((mre_x + 3, mre_y - 10)).label('Ignition\nCoil 3', loc='center')

def get_coil_4(mre_x, mre_y):
    """Returns a 4-pin LS1 coil."""
    return get_coil().at((mre_x + 3, mre_y - 15)).label('Ignition\nCoil 4', loc='center')