import schemdraw.elements as elm

def get_engine_gnd(dmre_x, mre_y):
    return elm.Ground().label('Engine GND 1', loc="right").at((dmre_x + 2, mre_y))
