# build_schematic.py
import schemdraw
import components as comp  # Imports the entire components package directory cleanly
import routes as rt

with schemdraw.Drawing(file='microrusefi_full_harness.svg') as d:
    d.config(unit=2.0, fontsize=10)

    # 1. Fetch hardware instances cleanly from the components package
    mre = d.add(comp.get_microrusefi_ecu())

    # Position accessories downstream using absolute pixel-anchors from the ECU module
    gnd_bus = d.add(comp.get_gnd_bus(mre.absanchors['pin2'].x, mre.absanchors['pin2'].y))
    wbo = d.add(comp.get_rusefi_wbo(mre.absanchors['pin48'].x, mre.absanchors['pin48'].y))
    o2_sensor = d.add(comp.get_oxygen_sensor(wbo.absanchors['pin3'].x + 3, wbo.absanchors['pin3'].y - 1.0))
    crank = d.add(comp.get_crank_sensor(mre.absanchors['pin45'].x, mre.absanchors['pin45'].y))
    maf = d.add(comp.get_maf(mre.absanchors['pin27'].x, mre.absanchors['pin27'].y))
    tps = d.add(comp.get_tps_sensor(mre.absanchors['pin44'].x, mre.absanchors['pin44'].y))
    clt = d.add(comp.get_clt_sensor(mre.absanchors['pin18'].x, mre.absanchors['pin18'].y))
    stepper = d.add(comp.get_stepper().at((mre.absanchors['pin35'].x + 3, mre.absanchors['pin35'].y - 3)))

    # Injectors (shifted further right to make space for wideband and O2 sensor)
    inj_offset_x = 4.0
    inj1 = d.add(comp.get_injector_1(mre.absanchors['pin37'].x + inj_offset_x, mre.absanchors['pin37'].y))
    inj2 = d.add(comp.get_injector_2(mre.absanchors['pin38'].x + inj_offset_x, mre.absanchors['pin38'].y))
    inj3 = d.add(comp.get_injector_3(mre.absanchors['pin41'].x + inj_offset_x, mre.absanchors['pin41'].y))
    inj4 = d.add(comp.get_injector_4(mre.absanchors['pin42'].x + inj_offset_x, mre.absanchors['pin42'].y))

    # Coils
    coil_1 = d.add(comp.get_coil_1(mre.absanchors['pin9'].x, mre.absanchors['pin9'].y))
    coil_2 = d.add(comp.get_coil_2(mre.absanchors['pin10'].x, mre.absanchors['pin10'].y))
    coil_3 = d.add(comp.get_coil_3(mre.absanchors['pin11'].x, mre.absanchors['pin11'].y))
    coil_4 = d.add(comp.get_coil_4(mre.absanchors['pin12'].x, mre.absanchors['pin12'].y))

    # Draws ground near coil_1.
    engine_ground = d.add(comp.get_engine_gnd(coil_1.absanchors['pinC'].x, coil_1.absanchors['pinC'].y))

    # Power Delivery: Battery, Circuit Breaker, Relay Box (6 relays), and Fuse Box
    battery = d.add(comp.get_battery(mre.absanchors['pin1'].x - 28, mre.absanchors['pin1'].y + 6))
    breaker = d.add(comp.get_circuit_breaker(mre.absanchors['pin1'].x - 24, mre.absanchors['pin1'].y + 6))
    relay_box = [d.add(r) for r in comp.get_relay_box(mre.absanchors['pin1'].x - 19, mre.absanchors['pin1'].y + 6, spacing=3.0)]
    fuse_box = d.add(comp.get_fuse_box(mre.absanchors['pin1'].x - 14, mre.absanchors['pin1'].y + 3))
    fan = d.add(comp.get_fan_controller(relay_box[2].absanchors['pin87a'].x, relay_box[2].absanchors['pin87a'].y))


    # 2. Compile harness segments using specialized subsystem logic
    rt.connect_relays(d, battery, breaker, relay_box, gnd_bus, mre)
    rt.connect_fuse_box(d, relay_box[1], fuse_box)

    rt.wire_ecu_power_grouds.wire_ecu_power_grounds(d, mre)
    rt.connect_can_bus(d, mre, wbo, fuse_box, gnd_bus)
    rt.connect_oxygen_sensor(d, wbo, o2_sensor)
    rt.connect_fan(d, fan, relay_box[2])
    rt.connect_usb(d, mre)
    rt.connect_crank_sensor(d, mre, crank)
    rt.connect_maf(d, mre, maf, gnd_bus, fuse_box)
    rt.connect_tps(d, mre, tps)
    rt.connect_clt(d, mre, clt)
    rt.connect_stepper(d, mre, stepper)

    rt.connect_injector_1(d, mre, inj1, fuse_box)
    rt.connect_injector_2(d, mre, inj2, fuse_box)
    rt.connect_injector_3(d, mre, inj3, fuse_box)
    rt.connect_injector_4(d, mre, inj4, fuse_box)

    rt.connect_coil_1(d, mre, coil_1, engine_ground, gnd_bus, fuse_box)
    rt.connect_coil_2(d, mre, coil_2, engine_ground, gnd_bus, fuse_box)
    rt.connect_coil_3(d, mre, coil_3, engine_ground, gnd_bus, fuse_box)
    rt.connect_coil_4(d, mre, coil_4, engine_ground, gnd_bus, fuse_box)

    print("✨ Modular harness successfully compiled to microrusefi_full_harness.svg!")
