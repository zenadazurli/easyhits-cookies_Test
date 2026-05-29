import subprocess
import time
import re

API_KEY = "bu_MN6wlSbFKdRNKvxB349PKTYLjrHGjXGEt3DHrT91cD0"
EMAIL = "sandrominori50+ulugarecexisa@gmail.com"
PASSWORD = "DDnmVV45!!"

def run_cmd(cmd, capture=False):
    if capture:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True)
    else:
        subprocess.run(cmd, shell=True)

print("🚀 Test Browser Use Cloud su Render")

# 1. Connetti
run_cmd(f"browser-use config set api_key {API_KEY}")
run_cmd("browser-use cloud connect")
run_cmd("browser-use open https://www.easyhits4u.com/logon/")
time.sleep(5)

# 2. Compila form
run_cmd('browser-use keys "Tab"')
run_cmd('browser-use type "sandrominori50+ulugarecexisa@gmail.com"')
time.sleep(1)
run_cmd('browser-use keys "Tab"')
run_cmd('browser-use type "DDnmVV45!!"')
time.sleep(1)

# 3. Login
run_cmd('browser-use keys "Enter"')
time.sleep(10)

# 4. Cookie
result = run_cmd("browser-use cookies get", capture=True)

# 5. Estrai
sesids_match = re.search(r"'sesids': '([^']+)'", result.stdout)
user_id_match = re.search(r"'user_id': '([^']+)'", result.stdout)

print(f"sesids: {sesids_match.group(1) if sesids_match else '❌'}")
print(f"user_id: {user_id_match.group(1) if user_id_match else '❌'}")
