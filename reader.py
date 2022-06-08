import sys
import asyncio
import pathlib

from bleak import BleakClient
from bleak.uuids import uuid16_dict

uuid16_dict = {v: k for k, v in uuid16_dict.items()}
filename = "ble_data.txt"

USER_DATA_SERVICE_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(
    uuid16_dict.get("User Data")  # 0x181C
)

STRING_CHARACTERISTIC_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(
    uuid16_dict.get("String")  # 0x2A3D
)

async def main(address: str):
    while True:
        print("Connecting to device...")
        try:
            async with BleakClient(address) as client:
                
                async def coordinates_handler(_, data):
                    data_str = data.decode("utf-8") 
                    print(data_str)

                    pathlib.Path("out").mkdir(parents=True, exist_ok=True)
                    with open(f"out/{filename}", "a+") as f:
                        f.write(data_str + "\n\n")
                        f.close()

                print(f"Connected: {client.is_connected}")
                try:
                    while client.is_connected:
                        ids_service = (await client.get_services()).get_service(USER_DATA_SERVICE_UUID)
                        coordinates_char = ids_service.get_characteristic(STRING_CHARACTERISTIC_UUID)
                        await client.start_notify(coordinates_char, coordinates_handler)
                        await asyncio.sleep(1.0)
                        await client.stop_notify(coordinates_char)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        filename = sys.argv[2] if len(sys.argv) == 3 else filename
        asyncio.run(main(sys.argv[1]))
    else:
        print("Usage: pipenv run read <address> [<filename>]")
            