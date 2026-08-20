# routes/connect_relays.py
import schemdraw.elements as elm


def connect_relays(d, battery, circuit_breaker, relays, gnd_bus):
    """
    Connects main power and ground for the relay box:
    - Battery (+) connects to Main Circuit Breaker.
    - Battery (-) connects to Ground Bus.
    - Main Circuit Breaker connects to Pin 30 (Common) of all 6 relays.
    - Pin 85 (Ground) of all 6 relays connects to the Ground Bus.
    """
    # 1. Connect Battery (+) to Circuit Breaker input
    if hasattr(battery, 'end'):
        bat_pos = battery.end
    elif hasattr(battery, 'pinPOS'):
        bat_pos = battery.pinPOS
    else:
        bat_pos = battery.start

    if hasattr(circuit_breaker, 'start'):
        cb_in = circuit_breaker.start
        cb_out = circuit_breaker.end
    else:
        cb_in = circuit_breaker.pinIN
        cb_out = circuit_breaker.pinOUT

    d.add(elm.Wire('|-').at(bat_pos).to(cb_in).label('+12V Battery Main'))

    if hasattr(gnd_bus, 'start'):
        gnd_ref = gnd_bus.start
    else:
        gnd_ref = gnd_bus


    # Convert relays argument if dict or single
    if isinstance(relays, dict):
        relay_list = list(relays.values())
    elif isinstance(relays, (list, tuple)):
        relay_list = list(relays)
    else:
        relay_list = [relays]

    # 3. Connect Main Circuit Breaker output to Pin 30 (Common) of all relays
    # and connect Pin 85 (Ground) of all relays to Ground Bus
    for relay in relay_list:
        d.add(elm.Wire('|-').at(cb_out).to(relay.pin30))
        d.add(elm.Wire('|-').at(relay.pin85).to(gnd_ref))
