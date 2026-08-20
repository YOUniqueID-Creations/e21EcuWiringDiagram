# components/clt.py
import schemdraw.elements as elm

def get_clt_sensor(mre_x, mre_y):
    """Returns a 2-pin Coolant Temperature Sensor (CLT)"""
    return elm.Ic(
        pins=[
            elm.IcPin(name='Signal GND', pin='2', side='right'),
            elm.IcPin(name='CLT Signal', pin='1', side='right'),
        ],
        w=1.5, h=1.5, pinspacing=0.8
    ).at((mre_x - 12, mre_y - 2)).label('CLT', loc='left')
