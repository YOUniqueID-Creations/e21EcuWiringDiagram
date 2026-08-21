# components/stepper.py
import schemdraw.elements as elm


def get_stepper():
    """Returns a Jeep 4-pin idle stepper motor.
    Pins (left to right): S1, S3, S4, S2
    - Outer pins (S1, S2) = Coil 1
    - Inner pins (S3, S4) = Coil 2
    """
    return elm.Ic(
        pins=[
            elm.IcPin(name='S2', pin='S2', side='left'),
            elm.IcPin(name='S4', pin='S4', side='left'),
            elm.IcPin(name='S3', pin='S3', side='left'),
            elm.IcPin(name='S1', pin='S1', side='left'),
        ],
        w=4, h=2, pinspacing=1
    ).label('Idle\nStepper', loc='center')
