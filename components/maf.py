# components/maf.py
import schemdraw.elements as elm

def get_maf(mre_x, mre_y):
    """Returns a Hitachi MAF for the given coordinates."""
    return elm.Ic(
        pins=[
            elm.IcPin(name='no op', pin='A', side='left',),
            elm.IcPin(name='+12V', pin='B', side='top'), # Fuse Block
            elm.IcPin(name='GND', pin='C', side='bottom'), # Ground Bus

            # ECU
            elm.IcPin(name='IAT Signal GND', pin='F', side='right'),  # Share with TPS pin 3
            elm.IcPin(name='IAT', pin='E', side='right'),
            elm.IcPin(name='MAF +5V Signal', pin='D', side='right'),  # Connect to MAP signal reprogram in TunerStudio

        ],
        w=1.5, h=2.0, pinspacing=0.8
    ).at((mre_x - 11, mre_y - 2.1)).label('MAF', loc='center')
