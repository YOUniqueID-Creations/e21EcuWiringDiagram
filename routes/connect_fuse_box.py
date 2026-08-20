# routes/connect_fuse_box.py
import schemdraw.elements as elm


def connect_fuse_box(d, relay2, fuse_box):
    """
    Connects Relay 2's NO output (Pin 87) to the Fuse Box main power input.
    """
    if isinstance(relay2, (list, tuple)):
        relay2 = relay2[1]  # Relay 2 (0-indexed position 1)
    elif isinstance(relay2, dict):
        relay2 = relay2.get('relay2', relay2.get('Relay 2', list(relay2.values())[1]))

    d.add(elm.Wire('|-').at(relay2.pin87).to(fuse_box.pinIN).label('+12V Switched Power'))
