# build_schematic.py
import schemdraw
import components as comp  # Imports the entire components package directory cleanly
import routes as rt

with schemdraw.Drawing(file='microrusefi_full_harness.svg') as d:
    d.config(unit=2.0, fontsize=10)

    # 1. Fetch hardware instances cleanly from the components package
    mre = d.add(comp.get_microrusefi_ecu())

    # Position accessories downstream using absolute pixel-anchors from the ECU module
    wbo = d.add(comp.get_rusefi_wbo(mre.absanchors['pin13'].x, mre.absanchors['pin13'].y))
    crank = d.add(comp.get_crank_sensor(mre.absanchors['pin45'].x, mre.absanchors['pin45'].y))
    tps = d.add(comp.get_tps_sensor(mre.absanchors['pin44'].x, mre.absanchors['pin44'].y))

    # Injectors
    inj1 = d.add(comp.get_injector_1(mre.absanchors['pin37'].x, mre.absanchors['pin37'].y))
    inj2 = d.add(comp.get_injector_2(mre.absanchors['pin38'].x, mre.absanchors['pin38'].y))
    inj3 = d.add(comp.get_injector_3(mre.absanchors['pin41'].x, mre.absanchors['pin41'].y))
    inj4 = d.add(comp.get_injector_4(mre.absanchors['pin42'].x, mre.absanchors['pin42'].y))

    # Coils
    coil_1 = d.add(comp.get_coil_1(mre.absanchors['pin9'].x, mre.absanchors['pin9'].y))
    coil_2 = d.add(comp.get_coil_2(mre.absanchors['pin10'].x, mre.absanchors['pin10'].y))
    coil_3 = d.add(comp.get_coil_3(mre.absanchors['pin11'].x, mre.absanchors['pin11'].y))
    coil_4 = d.add(comp.get_coil_4(mre.absanchors['pin12'].x, mre.absanchors['pin12'].y))

    # Draws ground near coil_1.
    engine_ground = d.add(comp.get_engine_gnd(coil_1.absanchors['pinC'].x, coil_1.absanchors['pinC'].y))


    # 2. Compile harness segments using specialized subsystem logic
    rt.wire_ecu_power_grouds.wire_ecu_power_grounds(d, mre)
    rt.connect_can_bus(d, mre, wbo)
    rt.connect_crank_sensor(d, mre, crank)
    rt.connect_tps(d, mre, tps)

    rt.connect_injector_1(d, mre, inj1)
    rt.connect_injector_2(d, mre, inj2)
    rt.connect_injector_3(d, mre, inj3)
    rt.connect_injector_4(d, mre, inj4)

    rt.connect_coil_1(d, mre, coil_1, engine_ground)
    rt.connect_coil_2(d, mre, coil_2, engine_ground)
    rt.connect_coil_3(d, mre, coil_3, engine_ground)
    rt.connect_coil_4(d, mre, coil_4, engine_ground)

    print("✨ Modular harness successfully compiled to microrusefi_full_harness.svg!")
