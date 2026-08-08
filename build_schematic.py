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

    # 2. Compile harness segments using specialized subsystem logic
    route.wire_ecu_power_grounds(d, mre)
    route.connect_can_bus(d, mre, wbo)
    route.connect_crank_sensor(d, mre, crank)

    print("✨ Modular harness successfully compiled to microrusefi_full_harness.svg!")
