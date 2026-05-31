import re
def analyze_rtl(rtl_code):

    module_match = re.search(
        r"module\s+(\w+)",
        rtl_code
    )

    module_name = module_match.group(1)

    inputs = re.findall(
        r"input\s+(?:reg\s+|wire\s+)?(?:\[\d+:\d+\]\s+)?(\w+)",
        rtl_code
    )

    outputs = re.findall(
        r"output\s+(?:reg\s+|wire\s+)?(?:\[\d+:\d+\]\s+)?(\w+)",
        rtl_code
    )

    return {
        "module": module_name,
        "inputs": inputs,
        "outputs": outputs
    }
