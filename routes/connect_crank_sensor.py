# routes/connect_crank_sensor.py
import schemdraw.elements as elm

def connect_crank_sensor(d, mre, crank):
    """
    Routes the engine position trigger signal back to the ECU (Crank VR+),
    and returns its ground to the dedicated Crank VR- pin.
    """
    # Wire Crank Sensor Pin 1 (SIG) directly to ECU Pin 45 (Crank Pos/Crank VR+)
    d.add(elm.Wire('|-').at(crank.pin1).to(mre.pin45))

    # Wire Crank Sensor Pin 2 (GND) back to ECU Pin 46 (Crank VR-)
    d.add(elm.Wire('|-').at(crank.pin2).to(mre.pin46))
