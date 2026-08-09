# routes/connect_maf.py

import schemdraw.elements as elm

def connect_maf(d, mre, maf, gnd_bus):
    """
    Routes the maf to 12v fuse,
    routes to the ground bus,
    and routes MAF Signal, IAT Signal, and SGND back to the ECU.
    """
    # Pin A No Op
    # TODO: Wire Pin B (+12V fuse)

    # Wire MAF Pin C to GND Bus.
    d.add(elm.Wire('|-').at(maf.pinC).to(gnd_bus.start))

    # Wire MAF Pin D (SIG) directly to ECU Pin 27 (AN Volt 1/MAP - We reprogram to MAF in TunerStudio)
    d.add(elm.Wire('|-').at(maf.pinD).to(mre.pin27))

    # Wire MAF Pin E (IAT) back to ECU Pin 23 (AN Temp 2/IAT)
    d.add(elm.Wire('|-').at(maf.pinE).to(mre.pin23))

    # Wire MAF Pin F (IAT Signal GND) to ECU Pin 17 (Signal GND - shared with TPS)
    d.add(elm.Wire('|-').at(maf.pinF).to(mre.pin17))