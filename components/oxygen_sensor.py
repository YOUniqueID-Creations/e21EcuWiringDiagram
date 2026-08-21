# components/oxygen_sensor.py
import schemdraw.elements as elm

def get_oxygen_sensor(x=0, y=0):
    """Returns the LSU 4.9 / Wideband Oxygen Sensor component"""
    return elm.Ic(
        pins=[
            elm.IcPin(name='HEAT-', pin='1', side='left'),
            elm.IcPin(name='HEAT+', pin='2', side='left'),
            elm.IcPin(name='IP / Pump', pin='3', side='left'),
            elm.IcPin(name='VM / Nernst', pin='4', side='left'),
        ],
        w=2.0, h=1.8, pinspacing=0.6
    ).at((x, y)).label('Oxygen Sensor\n(LSU 4.9)', loc='center')
