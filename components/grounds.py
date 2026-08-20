import schemdraw.elements as elm

def get_engine_gnd(coil_1_x, coil_1_y):
    return elm.Ground().label('Engine GND 1', loc="right").at((coil_1_x + 2, coil_1_y))

def get_gnd_bus(mre_x, mre_y):
    return elm.Ground().label('GND Bus', loc="bottom").at((mre_x, mre_y - 7))
