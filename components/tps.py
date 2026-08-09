# components/tps.py
import schemdraw.elements as elm

def get_tps_sensor(mre_x, mre_y):
    """Returns a 1984 NISSAN 300ZX 3.0L V6 3-pin throttle position sensor"""
    return elm.Ic(
        pins=[
            elm.IcPin(name='+5V', pin='1', side='right', color='darkorange'),
            elm.IcPin(name='TPS', pin='2', side='right'),
            elm.IcPin(name='SGND', pin='3', side='right', color='darkblue'),
        ],
        w=1.5, h=2.0, pinspacing=0.8
    ).at((mre_x - 8, mre_y - 0.5)).label('TPS', loc='center')
