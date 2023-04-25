import secrets
import subprocess

unchanged = True

while unchanged:

    new_adress = ":".join([secrets.token_hex(1) for _ in range(6)])

    unchanged = subprocess.run(["sudo", "ifconfig", "en0", "ether", new_adress]).returncode

print(f"New mac adress: {new_adress}")
