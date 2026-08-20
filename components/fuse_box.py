# components/fuse_box.py
import schemdraw.elements as elm


def get_fuse_box(x=0, y=0):
    """
    Returns a Fuse Box component powered by Relay 2.
    """
    return elm.Ic(
        pins=[
            elm.IcPin(name='12V IN', pin='IN', side='left'),
            elm.IcPin(name='Fuse 1 (ECU)', pin='F1', side='right'),
            elm.IcPin(name='Fuse 2 (MAF)', pin='F2', side='right'),
            elm.IcPin(name='Fuse 3 (Injectors)', pin='F3', side='right'),
            elm.IcPin(name='Fuse 4 (Coils)', pin='F4', side='right'),
            elm.IcPin(name='Fuse 5 (WBO)', pin='F5', side='right'),
            elm.IcPin(name='Fuse 6 (Aux)', pin='F6', side='right'),
        ],
        w=2.8, h=2.8, pinspacing=0.6
    ).at((x, y)).label('Fuse Box', loc='center')
