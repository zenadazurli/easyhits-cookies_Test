import subprocess
import time
import re
import os

API_KEY = os.environ.get("BROWSER_USE_API_KEY", "bu_St6-JPLOEUMFx0wGvMsPlCvoAlkDmIbwl8bRpiPlycw")
EMAIL = "sandrominori50+ulugarecexisa@gmail.com"
PASSWORD = "DDnmVV45!!"

def run_cmd(cmd, capture=False):
    print(f"📌 {cmd[:50]}...")
    if capture:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True)
    else:
        subprocess.run(cmd, shell=True)

# === CHIUDI SESSIONI PRECEDENTI ===
print("🧹 Pulizia sessioni precedenti...")
run_cmd("browser-use close --all")
time.sleep(2)

print("=" * 60)
print("🚀 Browser Use Cloud - EasyHits4U")
print("=" * 60)

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

# 4. Attendi dashboard
print("⏳ Attesa redirect...")
for i in range(20):
    time.sleep(1)
    result = run_cmd("browser-use eval 'window.location.href'", capture=True)
    url = result.stdout.strip()
    print(f"   {i+1}s → {url[:50]}")
    if "surf" in url:
        print("✅ Dashboard raggiunta!")
        break

time.sleep(3)

# 5. Cookie
result = run_cmd("browser-use cookies get", capture=True)
output = result.stdout

sesids_match = re.search(r"'sesids': '([^']+)'", output)
user_id_match = re.search(r"'user_id': '([^']+)'", output)

print("\n" + "=" * 60)
print("📊 RISULTATO")
print(f"   sesids: {sesids_match.group(1) if sesids_match else '❌'}")
print(f"   user_id: {user_id_match.group(1) if user_id_match else '❌'}")
print("=" * 60)

# 6. Chiudi sessione
run_cmd("browser-use close --all")
print("✅ Fine esecuzione")
