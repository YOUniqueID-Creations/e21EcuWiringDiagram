# routes/connect_tps.py
import schemdraw.elements as elm

def connect_tps(d, mre, tps):
    """
    Routes the throttle position signal back to the ECU,
    routes the +5V pin to the dedicated +5V TPS supply on the ECU,
    and returns its ground to the isolated Signal Ground rail.
    """
    # Wire TPS Pin 1 (+5V) directly to ECU Pin 44 (TPS Supply)
    d.add(elm.Line().right().at(tps.pin1).to(mre.pin44))

    # Wire TPS Signal
    d.add(elm.Wire('|-').at(tps.pin2).to(mre.pin20))

    # Wire TPS Pin 3 (GND) back to ECU Pin 17 (Signal GND)
    d.add(elm.Wire('|-').color('red').at(tps.pin3).to(mre.pin17))
