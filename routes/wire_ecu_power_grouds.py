# routes/wire_ecu_power_grounds.py

from schemdraw import elements as elm

def wire_ecu_power_grounds(d, mre):
    """
    Maps foundational power delivery, fusing, and main chassis
    grounds required by the microRusEFI controller.
    """
    # Switched Ignition Source (Pin 5)
    d.add(elm.Line().left().at(mre.pin5).length(1.0))
    d.add(elm.Fuse().left().label('15A Fuse', loc='top'))
    d.add(elm.Line().left().length(0.5).label('+12V Switched', loc='left'))

    # Constant Battery Sense (Pin 1)
    d.add(elm.Line().left().at(mre.pin1).length(1.5).label('+12V Constant', loc='left'))

    # High-Current Power Grounds (Pins 2 & 6) tied to engine block/chassis
    d.add(elm.Line().down().at(mre.pin2).length(1.0))
    gnd = d.add(elm.Ground().label('Chassis GND', loc='bottom'))

    d.add(elm.Line().down().at(mre.pin6).length(0.5))
    d.add(elm.Line().left().to(gnd.start))
