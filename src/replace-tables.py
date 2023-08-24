import pandas as pd

ps5_compatibility = pd.read_csv('GP2040-CE Compatibility List - PS5 Games.csv', keep_default_na=False, usecols=[*range(0, 3, 1)],colalign=("left", "center", "left"))
usb_passthrough_devices = pd.read_csv('GP2040-CE Compatibility List - USB Passthrough.csv', keep_default_na=False, usecols=[*range(0, 4, 1)], colalign=("center", "left", "center", "right", "center"))


with open('README.md', 'r') as readme:
    data = readme.read()

    ps5_compatibility_replace_txt = "--Playstation 5 Compatibility Table--"
    data = data.replace(ps5_compatibility_replace_txt, ps5_compatibility.to_markdown(index=False))

    usb_passthrough_devices_replace_text = "--USB Passthrough Authentication Device Table--"
    data = data.replace(usb_passthrough_devices_replace_text, usb_passthrough_devices.to_markdown(index=False))
with open(r'README.md', 'w') as readme:
    readme.write(data)