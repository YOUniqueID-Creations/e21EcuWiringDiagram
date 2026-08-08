# build_schematic.py
import schemdraw
import components as comp  # Imports the entire components package directory cleanly
import routing as route

with schemdraw.Drawing(file='microrusefi_full_harness.svg') as d:
    d.config(unit=2.0, fontsize=10)

    # 1. Fetch hardware instances cleanly from the components package
    mre = d.add(comp.get_microrusefi_ecu())

    # Position accessories downstream using absolute pixel-anchors from the ECU module
    wbo = d.add(comp.get_rusefi_wbo(mre.absanchors['pin13'].x, mre.absanchors['pin13'].y))
    crank = d.add(comp.get_crank_sensor(mre.absanchors['pin45'].x, mre.absanchors['pin45'].y))

    # Coils
    coil_1 = d.add(comp.get_coil_1(mre.absanchors['pin9'].x, mre.absanchors['pin9'].y))
    coil_2 = d.add(comp.get_coil_2(mre.absanchors['pin10'].x, mre.absanchors['pin10'].y))
    coil_3 = d.add(comp.get_coil_3(mre.absanchors['pin11'].x, mre.absanchors['pin11'].y))
    coil_4 = d.add(comp.get_coil_4(mre.absanchors['pin12'].x, mre.absanchors['pin12'].y))

    # 2. Compile harness segments using specialized subsystem logic
    route.wire_ecu_power_grounds(d, mre)
    route.connect_can_bus(d, mre, wbo)
    route.connect_crank_sensor(d, mre, crank)
    # TODO: Fix.
    route.connect_coil_1(d, mre, coil_1)
    route.connect_coil_2(d, mre, coil_2)
    route.connect_coil_3(d, mre, coil_3)
    route.connect_coil_4(d, mre, coil_4)

    print("✨ Modular harness successfully compiled to microrusefi_full_harness.svg!")
