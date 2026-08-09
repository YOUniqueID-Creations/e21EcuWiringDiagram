# routes/connect_crank_sensor.py
import schemdraw.elements as elm

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
