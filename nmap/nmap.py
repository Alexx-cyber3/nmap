import os
def print_heading():
    title = " ALEXANDER THE CYBER TECH"
    line = "=" * len(title)
    print(line)
    print(title)
    print(line)

print_heading()


def run_nmap_scan(option, target):
    scans = {
        "1": f"nmap -sS {target}",          # TCP SYN Scan
        "2": f"nmap -sT {target}",          # TCP Connect Scan
        "3": f"nmap -sU {target}",          # UDP Scan
        "4": f"nmap -sA {target}",          # ACK Scan
        "5": f"nmap -sF {target}",          # FIN Scan
        "6": f"nmap -sX {target}",          # Xmas Scan
        "7": f"nmap -sN {target}",          # Null Scan
        "8": f"nmap -sn {target}",          # Ping Scan (No Port Scan)
        "9": f"nmap -sY {target}",          # SCTP INIT Scan
        "10": f"nmap -sZ {target}",         # SCTP COOKIE-ECHO Scan
        "11": f"nmap -sO {target}",         # IP Protocol Scan
        "12": f"nmap -PR {target}",         # ARP Scan
        "13": f"nmap -sV {target}",         # Version Detection
        "14": f"nmap -O {target}",          # OS Detection
        "15": f"nmap -sC {target}",         # Default Script Scan
    }

    command = scans.get(option)
    if command:
        print(f"🛠 Running: {command}")
        os.system(command)
    else:
        print("❌ Invalid option selected.")

def main():
    print("\n🔎 Nmap Scan Options:")
    print(" 1. TCP SYN Scan (-sS)")
    print(" 2. TCP Connect Scan (-sT)")
    print(" 3. UDP Scan (-sU)")
    print(" 4. TCP ACK Scan (-sA)")
    print(" 5. TCP FIN Scan (-sF)")
    print(" 6. Xmas Scan (-sX)")
    print(" 7. Null Scan (-sN)")
    print(" 8. Ping Scan (-sn)")
    print(" 9. SCTP INIT Scan (-sY)")
    print("10. SCTP COOKIE-ECHO Scan (-sZ)")
    print("11. IP Protocol Scan (-sO)")
    print("12. ARP Scan (-PR)")
    print("13. Version Detection (-sV)")
    print("14. OS Detection (-O)")
    print("15. Default Script Scan (-sC)\n")

    choice = input("Enter the scan number (1–15): ").strip()
    target = input("Enter the target IP or domain: ").strip()
    run_nmap_scan(choice, target)

if __name__ == "__main__":
    main()