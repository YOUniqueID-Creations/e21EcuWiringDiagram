# routes/connect_can_bus.py

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