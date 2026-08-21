# routes/connect_oxygen_sensor.py
import schemdraw.elements as elm

def connect_oxygen_sensor(d, wbo, o2_sensor):
    """
    Connects the rusEFI 042 Mini Wideband controller to the LSU 4.9 Oxygen Sensor:
    - WBO Pin 3 (LSU Heat-) -> O2 Sensor Pin 1 (HEAT-)
    - WBO Pin 4 (LSU Heat+) -> O2 Sensor Pin 2 (HEAT+)
    - WBO Pin 2 (LSU Ip)    -> O2 Sensor Pin 3 (IP)
    - WBO Pin 8 (LSU Vm)    -> O2 Sensor Pin 4 (VM)
    """
    d.add(elm.Wire('-').at(wbo.pin3).to(o2_sensor.pin1).label('Heat-', loc='bottom'))
    d.add(elm.Wire('-').at(wbo.pin4).to(o2_sensor.pin2).label('Heat+', loc='top'))
    d.add(elm.Wire('-').at(wbo.pin2).to(o2_sensor.pin3).label('Ip', loc='bottom'))
    d.add(elm.Wire('-').at(wbo.pin8).to(o2_sensor.pin4).label('Vm', loc='top'))
