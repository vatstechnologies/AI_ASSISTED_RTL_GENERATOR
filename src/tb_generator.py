def generate_tb(info):

    module_name = info["module"]

    tb = f"""
module tb;
"""

    for signal in info["inputs"]:
        tb += f"reg {signal};\n"

    for signal in info["outputs"]:
        tb += f"wire {signal};\n"

    tb += f"\n{module_name} dut(\n"

    port_connections = []

    for signal in info["inputs"]:
        port_connections.append(
            f".{signal}({signal})"
        )

    for signal in info["outputs"]:
        port_connections.append(
            f".{signal}({signal})"
        )

    tb += ",\n".join(port_connections)

    tb += "\n);\n"

    tb += """
initial begin
    $dumpfile("wave.vcd");
    $dumpvars(0,dut);
end
endmodule
"""

    return tb
