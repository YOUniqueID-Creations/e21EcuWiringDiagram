# routes/connect_fan.py
import schemdraw.elements as elm
import components as comp

def connect_fan(d, fan, relay_3):
    """
    Connects the Fan Controller:
    - Fan Controller Power (+12V) connects to Relay 3 Normally Open (Pin 87).
    """

    # Wire Relay 3 Pin 87 (NO) to Fan Controller Power (pin 1)
    d.add(elm.Wire('-|').at(relay_3.pin87).to(fan.pin1).label('Fan Power'))
