# routing.py
import schemdraw.elements as elm


def connect_can_bus(d, mre, wbo):
    """
    Routes the high-speed twisted pair communication network
    between the microRusEFI ECU and the 042 Mini Wideband.
    """
    # Wire Main ECU CAN High (Pin 13) to Wideband CAN H (Pin 11)
    d.add(elm.Line().right().at(mre.pin13).tox(wbo.pin11.x - 1.0))
    d.add(elm.Line().down().toy(wbo.pin11.y))
    d.add(elm.Line().right().to(wbo.pin11).label('CAN High Bus', loc='top'))

    # Wire Main ECU CAN Low (Pin 14) to Wideband CAN L (Pin 12)
    d.add(elm.Line().right().at(mre.pin14).tox(wbo.pin11.x - 0.7))
    d.add(elm.Line().down().toy(wbo.pin12.y))
    d.add(elm.Line().right().to(wbo.pin12).label('CAN Low Bus', loc='bottom'))


def connect_crank_sensor(d, mre, crank):
    """
    Routes the engine position trigger signal back to the ECU,
    and returns its ground to the isolated Signal Ground rail.
    """
    # Wire Crank Sensor Pin 1 (SIG) directly to ECU Pin 45 (Crank Pos)
    d.add(elm.Line().right().at(crank.pin1).to(mre.pin45))

    # Wire Crank Sensor Pin 2 (GND) back to ECU Pin 17 (Signal GND)
    d.add(elm.Line().right().at(crank.pin2).length(0.5))
    d.add(elm.Line().down().toy(mre.pin17.y))
    d.add(elm.Line().right().to(mre.pin17))


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
