# routes/connect_coils.py
from schemdraw import elements as elm


def connect_coil_1(d, mre, coil, engine_gnd, gnd_bus, fuse_box):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 9
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin9))

    # Grounds
    d.add(elm.Wire('|-').at(coil.pinB).to(gnd_bus.start))
    d.add(elm.Wire('-|').at(coil.pinC).to(engine_gnd.start))

    # Power
    d.add(elm.Wire('-|').color('indigo').at(coil.pinD).to(fuse_box.pinF4).label('15A'))

def connect_coil_2(d, mre, coil, engine_gnd, gnd_bus, fuse_box):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 10
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin10))

    # Grounds
    d.add(elm.Wire('|-').at(coil.pinB).to(gnd_bus.start))
    d.add(elm.Wire('-|').at(coil.pinC).to(engine_gnd.start))

    # Power
    d.add(elm.Wire('-|').color('indigo').at(coil.pinD).to(fuse_box.pinF4))

def connect_coil_3(d, mre, coil, engine_gnd, gnd_bus, fuse_box):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 11
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin11))

    # Grounds
    d.add(elm.Wire('|-').at(coil.pinB).to(gnd_bus.start))
    d.add(elm.Wire('-|').at(coil.pinC).to(engine_gnd.start))

    # Power
    d.add(elm.Wire('-|').color('indigo').at(coil.pinD).to(fuse_box.pinF4))

def connect_coil_4(d, mre, coil, engine_gnd, gnd_bus, fuse_box):
    """
    Routes the ECU signal to the coil and grounds the coil.
    """
    # Wire Coil Pin A (ECU Trigger) to ECU Pin 12
    d.add(elm.Wire('|-').at(coil.pinA).to(mre.pin12))

    # Grounds
    d.add(elm.Wire('|-').at(coil.pinB).to(gnd_bus.start))
    d.add(elm.Wire('-|').at(coil.pinC).to(engine_gnd.start))

    # Power
    d.add(elm.Wire('-|').color('indigo').at(coil.pinD).to(fuse_box.pinF4))