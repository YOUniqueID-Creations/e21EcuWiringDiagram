# routes/connect_can_bus.py

import schemdraw.elements as elm

def connect_can_bus(d, mre, wbo, fuse_box):
    """
    Routes the high-speed twisted pair communication network
    between the microRusEFI ECU and the 042 Mini Wideband.
    """
    # Wire Main ECU CAN High (Pin 48) to Wideband CAN H (Pin 11)
    d.add(elm.Wire('|-').at(wbo.pin11).to(mre.pin48).label('CAN High Bus'))

    # Wire Main ECU CAN Low (Pin 47) to Wideband CAN L (Pin 12)
    d.add(elm.Wire('-|').at(wbo.pin12).to(mre.pin47).label('CAN Low Bus'))

    # Wire Wideband 12v supply (Pin 6) to fuse 5
    d.add(elm.Wire('|-').at(wbo.pin6).to(fuse_box.pinF5).label('10A'))
