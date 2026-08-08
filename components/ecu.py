# components/ecu.py
import schemdraw.elements as elm


def get_microrusefi_ecu():
    """Returns the main 48-Pin microRusEFI controller block"""
    return elm.Ic(
        pins=[
            # Left Side Inputs & Power
            elm.IcPin(name='12V Key', pin='5', side='left'),
            elm.IcPin(name='Bat Sense', pin='1', side='left'),
            elm.IcPin(name='Signal GND', pin='17', side='left'),
            elm.IcPin(name='CLT Sensor', pin='18', side='left'),
            elm.IcPin(name='Crank Pos', pin='45', side='left'),

            # Bottom Side Power Grounds
            elm.IcPin(name='PGND', pin='2', side='bottom'),
            elm.IcPin(name='PGND', pin='6', side='bottom'),

            # Right Side Outputs & Communication
            elm.IcPin(name='Ignition 1', pin='9', side='right'),
            elm.IcPin(name='Ignition 2', pin='10', side='right'),
            elm.IcPin(name='Lowside 1 (VVT)', pin='7', side='right'),
            elm.IcPin(name='Lowside 2 (Idle)', pin='3', side='right'),
            elm.IcPin(name='CAN High', pin='13', side='right'),
            elm.IcPin(name='CAN Low', pin='14', side='right'),
        ],
        edgepadH=0.5, pinspacing=1.0
    ).label('microRusEFI ECU\n(Main Module)', loc='center')
