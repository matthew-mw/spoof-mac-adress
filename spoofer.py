import secrets
import subprocess

changed = False

while not changed:

    parts = [hex(secrets.randbelow(256)).split("0x")[1].zfill(2) for part in range(6)]

    new_adress = ":".join(parts)

    subprocess.run(["sudo", "ifconfig", "en0", "ether", new_adress])

    changed = subprocess.getoutput("ifconfig en0 ether").split("ether ")[1].split()[0] == new_adress

print(f"New mac adress: {new_adress}")
