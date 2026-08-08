# components/sensors.py
import schemdraw.elements as elm

def get_crank_sensor(mre_x, mre_y):
    """Returns a generic 2-pin VR/Hall Crank position sensor"""
    return elm.Ic(
        pins=[
            elm.IcPin(name='SIG', pin='1', side='right'),
            elm.IcPin(name='GND', pin='2', side='right'),
        ],
        w=1.5, h=2.0, pinspacing=0.8
    ).at((mre_x - 3.5, mre_y - 0.5)).label('Crank\nSensor', loc='center')
