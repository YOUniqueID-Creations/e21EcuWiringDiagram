# routes/connect_usb.py
import schemdraw.elements as elm

def connect_usb(d, mre):
    """
    Connects the USB communication lines (USB Data+ / USB Data-)
    from the microRusEFI ECU top pins.
    """
    usb_conn = d.add(elm.Ic(
        pins=[
            elm.IcPin(name='USB Data+', pin='1', side='left'),
            elm.IcPin(name='USB Data-', pin='2', side='right'),
            elm.IcPin(name='VBUS / GND', pin='3', side='right'),
        ], w=5, h=2, pinspacing=1
    ).at((mre.absanchors['pin15'].x - 1, mre.absanchors['pin15'].y + .5)).label('USB Port\n(TunerStudio)', loc='top'))

    d.add(elm.Wire('|-').at(usb_conn.pin1).to(mre.absanchors['pin15']).label('USB D+'))
    d.add(elm.Wire('|-').at(usb_conn.pin2).to(mre.absanchors['pin16']).label('USB D-'))
