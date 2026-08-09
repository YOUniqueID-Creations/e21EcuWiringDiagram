# routes/connect_coils.py
from schemdraw import elements as elm


def connect_coil_1(d, mre, coil):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 9
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin9))

    # Wire Coil Pin B (Logic GND) and C (Power GND)
    d.add(elm.Line().right().at(coil.pinC).length(0.2))

    # Grounds
    engine_gnd = d.add(elm.Ground().label('Engine GND', loc='right'))
    d.add(elm.Line().right().to(engine_gnd.start))


    # Wire Coil Pin D (12v)
    # d.add(elm.Line().right().to(mre.pin17))


def connect_coil_2(d, mre, coil):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 10
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin10))

    # Wire Coil Pin B (Logic GND) and C (Power GND)
    # d.add(elm.Line().right().at(coil.pinB).length(0.5))
    d.add(elm.Line().right().at(coil.pinC).length(0.2))

    # Grounds
    engine_gnd = d.add(elm.Ground().label('Engine GND', loc='right'))
    d.add(elm.Line().right().to(engine_gnd.start))


    # Wire Coil Pin D (12v)
    # d.add(elm.Line().right().to(mre.pin17))


def connect_coil_3(d, mre, coil):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 11
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin11))

    # Wire Coil Pin B (Logic GND) and C (Power GND)
    # d.add(elm.Line().right().at(coil.pinB).length(0.5))
    d.add(elm.Line().right().at(coil.pinC).length(0.2))

    # Grounds
    engine_gnd = d.add(elm.Ground().label('Engine GND', loc='right'))
    d.add(elm.Line().right().to(engine_gnd.start))


    # Wire Coil Pin D (12v)
    # d.add(elm.Line().right().to(mre.pin17))


def connect_coil_4(d, mre, coil):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 12
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin12))

    # Wire Coil Pin B (Logic GND) and C (Power GND)
    d.add(elm.Line().right().at(coil.pinC).length(0.2))

    # Grounds
    engine_gnd = d.add(elm.Ground().label('Engine GND', loc='right'))
    d.add(elm.Line().right().to(engine_gnd.start))


    # Wire Coil Pin D (12v)
    # d.add(elm.Line().right().to(mre.pin17))
