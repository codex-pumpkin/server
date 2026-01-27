
from src.business.impl import InferenceManager
import asyncio
import time

async def main():
    m = InferenceManager()
    now = time.time()
    res = await m.get_llm_response_and_validate("Generate a complete SPICE netlist for a common-emitter NPN amplifier using a 12 V DC supply. The circuit should include a voltage divider bias, an input coupling capacitor, an output coupling capacitor, and a load resistor. Use realistic component values and include a transient analysis command.")

    for i in range(5):
        print()

    print(res)


    print()
    print()
    print(time.time() - now)

if __name__ == "__main__":
    asyncio.run(main())
