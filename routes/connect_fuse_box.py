# routes/connect_fuse_box.py
import schemdraw.elements as elm


def connect_fuse_box(d, relay2, fuse_box):
    """
    Connects Relay 2's NO output (Pin 87) to the Fuse Box main power input.
    """
    d.add(elm.Wire('-|').at(relay2.pin87).to(fuse_box.pinIN).label('+12V Switched Power'))
