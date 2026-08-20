# components/relay_box.py
import schemdraw.elements as elm


def get_relay(name="Relay"):
    """
    Returns a 5-pin SPDT relay block.
    Pins:
      - 85: Ground
      - 86: Power / Switch
      - 87a: Normally Closed (NC)
      - 87: Normally Open (NO)
      - 30: Common (Connects to Circuit Breaker)
    """
    return elm.Ic(
        pins=[
            elm.IcPin(name='85 GND', pin='85', side='left'),
            elm.IcPin(name='86 SW', pin='86', side='left'),
            elm.IcPin(name='30 COM', pin='30', side='left'),
            elm.IcPin(name='87a NC', pin='87a', side='right'),
            elm.IcPin(name='87 NO', pin='87', side='right'),
        ],
        w=2.5, h=2.2, pinspacing=0.6
    ).label(name, loc='center')


def get_relay_1(x=0, y=0):
    return get_relay("Relay 1").at((x, y))


def get_relay_2(x=0, y=0):
    return get_relay("Relay 2").at((x, y))


def get_relay_3(x=0, y=0):
    return get_relay("Relay 3").at((x, y))


def get_relay_4(x=0, y=0):
    return get_relay("Relay 4").at((x, y))


def get_relay_5(x=0, y=0):
    return get_relay("Relay 5").at((x, y))


def get_relay_6(x=0, y=0):
    return get_relay("Relay 6").at((x, y))


def get_relay_box(x=0, y=0, spacing=3.0):
    """
    Returns a list of 6 relays positioned sequentially starting at (x, y).
    """
    relays = []
    for i in range(1, 7):
        relay_y = y - (i - 1) * spacing
        relay = get_relay(f"Relay {i}").at((x, relay_y))
        relays.append(relay)
    return relays


def get_battery(x=0, y=0):
    """Returns a 12V Battery component."""
    return elm.Battery().at((x, y)).label('12V Battery', loc='bottom')


def get_circuit_breaker(x=0, y=0):
    """Returns a Main Circuit Breaker component."""
    return elm.Breaker().at((x, y)).label('Main Circuit Breaker', loc='top')
