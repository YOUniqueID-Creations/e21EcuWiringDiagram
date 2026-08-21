# components/fan.py
import schemdraw.elements as elm

def get_fan_controller(x=0, y=0):
    """Returns a Fan Controller / Fan unit component"""
    return elm.Ic(
        pins=[
            elm.IcPin(name='Power (+12V)', pin='1', side='left'),
            elm.IcPin(name='Probe / Signal', pin='2', side='bottom'),
            elm.IcPin(name='Ground', pin='3', side='bottom'),
        ],
        w=2.0, h=1.5, pinspacing=0.6
    ).at((x + 2, y - 2)).label('Fan Controller', loc='center')

