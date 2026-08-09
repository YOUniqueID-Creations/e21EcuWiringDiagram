# components/ecu.py
import schemdraw.elements as elm


def get_microrusefi_ecu():
    """Returns the main 48-Pin microRusEFI controller block"""
    return elm.Ic(
        pins=[
            # Left Side Inputs & Power
            elm.IcPin(name='Bat Sense', pin='1', side='left'),
            elm.IcPin(name='12V Key', pin='5', side='left'),
            elm.IcPin(name='Signal GND', pin='17', side='left', color="red"),
            elm.IcPin(name='CLT Sensor', pin='18', side='left', color="red"),
            elm.IcPin(name='AN volt 4(USB 5v)', pin='19', side='left', color="red"),
            elm.IcPin(name='AN volt 5(TPS)', pin='20', side='left', color="red"),
            elm.IcPin(name='Signal GND', pin='21', side='left', color="darkgreen"),
            elm.IcPin(name='AN tmp 4', pin='22', side='left', color="darkgreen"),
            elm.IcPin(name='AN tmp 2 (IAT)', pin='23', side='left', color="darkgreen"),
            elm.IcPin(name='AN tmp 3', pin='24', side='left', color="darkgreen"),
            elm.IcPin(name='AV volt 1 (MAP/MAF)', pin='27', side='left'),
            elm.IcPin(name='AN volt 6 (WBO)', pin='30', side='left'),
            elm.IcPin(name='AN volt 8', pin='36', side='left'),
            elm.IcPin(name='AN volt 9', pin='40', side='left'),
            elm.IcPin(name='TPS 5V', pin='44', side='left', color="brown"),
            elm.IcPin(name='Crank Pos', pin='45', side='left', color="green"),
            elm.IcPin(name='Crank Pos -', pin='46', side='left', color="green"),

            # Bottom Side Power Grounds
            elm.IcPin(name='PGND', pin='2', side='bottom'),
            elm.IcPin(name='PGND', pin='6', side='bottom'),

            # Right Side Outputs & Communication
            elm.IcPin(name='Ignition 1', pin='9', side='right', color="darkblue"),
            elm.IcPin(name='Ignition 2', pin='10', side='right', color="darkblue"),
            elm.IcPin(name='Ignition 3', pin='11', side='right', color="darkblue"),
            elm.IcPin(name='Ignition 4', pin='12', side='right', color="darkblue"),
            elm.IcPin(name='Lowside 1 (VVT)', pin='7', side='right'),
            elm.IcPin(name='Lowside 2 (Idle)', pin='3', side='right'),
            elm.IcPin(name='GP Out 6', pin='13', side='right', color="lightgreen"),
            elm.IcPin(name='GP Out 5', pin='14', side='right', color="lightgreen"),
            elm.IcPin(name='Main Relay Low', pin='29', side='right'),
            elm.IcPin(name='GP Out 3 (IDLE stepper 2+)', pin='33', side='right'),
            elm.IcPin(name='GP Out 2 (IDLE stepper 1-)', pin='34', side='right'),
            elm.IcPin(name='GP Out 1 (IDLE stepper 1+)', pin='35', side='right'),
            elm.IcPin(name='Injector 1', pin='37', side='right', color="darkgrey"),
            elm.IcPin(name='Injector 2', pin='38', side='right', color="darkgrey"),
            elm.IcPin(name='Injector 3', pin='41', side='right', color="brown"),
            elm.IcPin(name='Injector 4', pin='42', side='right', color="brown"),
            elm.IcPin(name='GP Out 4 (IDLE stepper 2+)', pin='43', side='right', color="brown"),
            elm.IcPin(name='CAN L', pin='47', side='right', color="gold"),
            elm.IcPin(name='CAN H', pin='48', side='right', color="gold"),

            # Top Side Data
            elm.IcPin(name='USB w', pin='15', side='top', color="gold"),
            elm.IcPin(name='USB g', pin='16', side='top', color="gold"),


            # Unused in our application
            # elm.IcPin(name='ETB+', pin='4', side='right'),
            # elm.IcPin(name='ETB-', pin='8', side='right'),
            # elm.IcPin(name='Hall Cam', pin='25', side='left'),
            # elm.IcPin(name='AV volt 2 (TPS2)', pin='26', side='left'),
            # elm.IcPin(name='AV volt 10', pin='28', side='left'),
            # elm.IcPin(name='AN volt 7 (PPS2)', pin='30', side='left'),
            # elm.IcPin(name='AN volt 3 (PPS)', pin='31', side='left'),
            # elm.IcPin(name='MAP sensor supply', pin='39', side='left', color="darkgrey"),
        ],
        edgepadH=0.5, pinspacing=1.2
    ).label('microRusEFI ECU\n(Main Module)', loc='center')
