import subprocess
import time
import re
import os

# === CONFIGURAZIONE ===
API_KEY = os.environ.get("BROWSER_USE_API_KEY", "bu_St6-JPLOEUMFx0wGvMsPlCvoAlkDmIbwl8bRpiPlycw")
EMAIL = "sandrominori50+ulugarecexisa@gmail.com"
PASSWORD = "DDnmVV45!!"

def run_cmd(cmd, capture=False):
    """Esegue un comando shell"""
    print(f"📌 {cmd[:50]}...")
    if capture:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True)
    else:
        subprocess.run(cmd, shell=True)

def check_url():
    """Legge l'URL corrente dal browser"""
    result = run_cmd("browser-use eval 'window.location.href'", capture=True)
    url = result.stdout.strip()
    if url.startswith("result: "):
        url = url[8:].strip()
    return url

print("=" * 60)
print("🚀 Browser Use Cloud - EasyHits4U")
print("=" * 60)

# 1. Configura e connetti al cloud
print("\n1️⃣ Connessione al cloud...")
run_cmd(f"browser-use config set api_key {API_KEY}")
run_cmd("browser-use cloud connect")
time.sleep(2)

# 2. Apri la pagina di login
print("\n2️⃣ Apertura pagina...")
run_cmd("browser-use open https://www.easyhits4u.com/logon/")
time.sleep(5)

# 3. Compila il form
print("\n3️⃣ Compilazione form...")
run_cmd('browser-use keys "Tab"')
run_cmd('browser-use type "sandrominori50+ulugarecexisa@gmail.com"')
time.sleep(1)

run_cmd('browser-use keys "Tab"')
run_cmd('browser-use type "DDnmVV45!!"')
time.sleep(1)

# 4. Invia il login
print("\n4️⃣ Invio login...")
run_cmd('browser-use keys "Enter"')

# 5. ATTESA DEL REDIRECT (LA PARTE PIÙ IMPORTANTE!)
print("\n5️⃣ Attesa redirect alla dashboard...")
for i in range(20):
    time.sleep(1)
    url = check_url()
    print(f"   {i+1}s → {url}")
    if "surf" in url:
        print("   ✅ Dashboard raggiunta!")
        break
    elif "warning" in url:
        print(f"   ⚠️ Warning rilevato, continuo ad aspettare...")

# Pausa aggiuntiva per sicurezza
time.sleep(3)

# 6. Estrai tutti i cookie
print("\n6️⃣ Estrazione cookie...")
result = run_cmd("browser-use cookies get", capture=True)
output = result.stdout

# 7. Parsing dei cookie
sesids_match = re.search(r"'sesids': '([^']+)'", output)
user_id_match = re.search(r"'user_id': '([^']+)'", output)

print("\n" + "=" * 60)
print("📊 RISULTATO FINALE")
print(f"   sesids: {sesids_match.group(1) if sesids_match else '❌'}")
print(f"   user_id: {user_id_match.group(1) if user_id_match else '❌'}")
print("=" * 60)

# 8. Salva su file (opzionale)
if sesids_match and user_id_match:
    with open("/tmp/cookies.txt", "w") as f:
        f.write(f"sesids={sesids_match.group(1)}\nuser_id={user_id_match.group(1)}")
    print("\n✅ Cookie salvati in /tmp/cookies.txt")
    print(f"   sesids={sesids_match.group(1)}")
    print(f"   user_id={user_id_match.group(1)}")

print("\n✅ Fine esecuzione")
