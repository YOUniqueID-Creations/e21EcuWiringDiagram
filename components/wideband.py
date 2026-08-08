# components/wideband.py
import schemdraw.elements as elm

def get_rusefi_wbo(mre_x, mre_y):
    """Returns the rusEFI 042 Mini wideband lambda module"""
    return elm.Ic(
        pins=[
            elm.IcPin(name='CAN H', pin='11', side='left'),
            elm.IcPin(name='CAN L', pin='12', side='left'),
            elm.IcPin(name='Chassis GND', pin='1', side='bottom'),
            elm.IcPin(name='12V Supply', pin='6', side='top'),
            elm.IcPin(name='LSU Heat-', pin='3', side='right'),
            elm.IcPin(name='LSU Heat+', pin='4', side='right'),
            elm.IcPin(name='LSU Ip', pin='2', side='right'),
            elm.IcPin(name='LSU Vm', pin='8', side='right'),
        ],
        edgepadH=1, pinspacing=1
    ).at((mre_x + 5.0, mre_y - 2.0)).label('rusEFI WBO\n042 Mini', loc='center')
