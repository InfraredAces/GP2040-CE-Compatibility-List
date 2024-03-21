import pandas as pd
import shutil

shutil.copyfile("TEMPLATE.md", "README.md")

ps5_compatibility = pd.read_csv(
    'GP2040-CE Compatibility List - PS5 Games.csv', keep_default_na=False, usecols=[*range(1, 4, 1)])

usb_passthrough_devices = pd.read_csv(
    'GP2040-CE Compatibility List - USB Passthrough.csv', keep_default_na=False, usecols=[*range(1, 6, 1)])

xboxone_passthrough_devices = pd.read_csv(
    'GP2040-CE Compatibility List - Xbox One Passthrough.csv', keep_default_na=False, usecols=[*range(1, 6, 1)])

for index, url in enumerate(usb_passthrough_devices['Link'].values):
    usb_passthrough_devices['Link'].values[index] = f"[Link]({url})"

for index, url in enumerate(xboxone_passthrough_devices['Link'].values):
    xboxone_passthrough_devices['Link'].values[index] = f"[Link]({url})"

with open('README.md', 'r') as readme:
    data = readme.read()

    ps5_compatibility_replace_txt = "--Playstation 5 Compatibility Table--"
    data = data.replace(ps5_compatibility_replace_txt, ps5_compatibility.to_markdown(
        index=False, colalign=("left", "center", "left",)))

    usb_passthrough_devices_replace_text = "--PS Passthrough Authentication Device Table--"
    data = data.replace(usb_passthrough_devices_replace_text, usb_passthrough_devices.to_markdown(
        index=False, colalign=("center", "left", "center", "left", "left",)))

    xboxone_passthrough_devices_replace_text = "--Xbox One Passthrough Authentication Device Table--"
    data = data.replace(xboxone_passthrough_devices_replace_text, xboxone_passthrough_devices.to_markdown(
        index=False, colalign=("center", "left", "center", "left", "left",)))

with open(r'README.md', 'w') as readme:
    readme.write(data)
