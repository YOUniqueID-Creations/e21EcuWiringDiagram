# routes/connect_injectors.py
from schemdraw import elements as elm


def connect_injector_1(d, mre, inj, fuse_box):
    """
    Routes injector to a +12V source and connects the injector to the dedicated ECU trigger (GND).
    """
    # +12V
    d.add(elm.Wire('-|-').at(inj.pin2).to(fuse_box.pinF3).label('15A'))

    # Wire Coil Pin A (ECU Trigger) to ECU Pin 37
    d.add(elm.Wire('|-').at(inj.pin1).to(mre.pin37))


def connect_injector_2(d, mre, inj, fuse_box):
    """
    Routes injector to a +12V source and connects the injector to the dedicated ECU trigger (GND).
    """
    # +12V
    d.add(elm.Wire('|-').at(inj.pin2).to(fuse_box.pinF3))

    # Wire Coil Pin A (ECU Trigger) to ECU Pin 38
    d.add(elm.Wire('|-').at(inj.pin1).to(mre.pin38))


def connect_injector_3(d, mre, inj, fuse_box):
    """
    Routes injector to a +12V source and connects the injector to the dedicated ECU trigger (GND).
    """
    # +12V
    d.add(elm.Wire('|-').at(inj.pin2).to(fuse_box.pinF3))

    # Wire Coil Pin A (ECU Trigger) to ECU Pin 41
    d.add(elm.Wire('|-').at(inj.pin1).to(mre.pin41))


def connect_injector_4(d, mre, inj, fuse_box):
    """
    Routes injector to a +12V source and connects the injector to the dedicated ECU trigger (GND).
    """
    # +12V
    d.add(elm.Wire('|-').at(inj.pin2).to(fuse_box.pinF3))

    # Wire Coil Pin A (ECU Trigger) to ECU Pin 42
    d.add(elm.Wire('|-').at(inj.pin1).to(mre.pin42))
