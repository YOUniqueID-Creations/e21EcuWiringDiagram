# routes/connect_clt.py

import schemdraw.elements as elm

def connect_clt(d, mre, clt):
    """
    Routes the Coolant Temperature Sensor (CLT) pins to the ECU:
    - CLT Signal (Pin 1) to ECU Pin 18
    - Signal Ground (Pin 2) to ECU Pin 17 (shared with MAF / Signal GND)
    """
    # Wire CLT Pin 1 (CLT Signal) to ECU Pin 18
    d.add(elm.Wire('|-').at(clt.pin1).to(mre.pin18))

    # Wire CLT Pin 2 (Signal GND) to ECU Pin 17
    d.add(elm.Wire('|-').color('red').at(clt.pin2).to(mre.pin17))
