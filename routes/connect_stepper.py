# routes/connect_stepper.py
import schemdraw.elements as elm


def connect_stepper(d, mre, stepper):
    """
    Routes the Jeep idle stepper motor to the ECU IDLE stepper pins.
    - S1 (Coil 1) -> ECU Pin 35 (IDLE stepper 1+)
    - S3 (Coil 2) -> ECU Pin 34 (IDLE stepper 1-)
    - S4 (Coil 2) -> ECU Pin 33 (IDLE stepper 2+)
    - S2 (Coil 1) -> ECU Pin 43 (IDLE stepper 2-)
    """
    d.add(elm.Wire('-|').at(stepper.pinS1).to(mre.pin35).label('1A+'))
    d.add(elm.Wire('-|').at(stepper.pinS3).to(mre.pin34).label('1B-'))
    d.add(elm.Wire('-|').at(stepper.pinS4).to(mre.pin33).label('2A+'))
    d.add(elm.Wire('|-').at(stepper.pinS2).to(mre.pin43).label('2B-'))
