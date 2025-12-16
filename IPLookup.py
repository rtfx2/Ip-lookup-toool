import os
from discord.ext import commands 
import requests
import time 
from pystyle import Center, Colorate, Colors, Banner, Write
from colorama import Style, Fore


os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_purple, ('You have just opened 642 IP look up tool')))
time.sleep(0.9)
print(Colorate.Horizontal(Colors.blue_to_purple, ('Program made by rtf')))
time.sleep(0.5)
print(Colorate.Horizontal(Colors.blue_to_purple, ('642 on top')))
time.sleep(0.3)
print(Colorate.Horizontal(Colors.blue_to_purple, ('Creds: credits to to rtf for the UI')))
time.sleep(0.4)
print(Colorate.Horizontal(Colors.blue_to_purple, ('Creds: credits to to rtf for the coding the tools')))
time.sleep(0.2)
print(Colorate.Horizontal(Colors.blue_to_purple, ('Loading tool')))
time.sleep(1)

banner = """                                                        
                                                        
        66666666         444444444   222222222222222    
       6::::::6         4::::::::4  2:::::::::::::::22  
      6::::::6         4:::::::::4  2::::::222222:::::2 
     6::::::6         4::::44::::4  2222222     2:::::2 
    6::::::6         4::::4 4::::4              2:::::2 
   6::::::6         4::::4  4::::4              2:::::2 
  6::::::6         4::::4   4::::4           2222::::2  
 6::::::::66666   4::::444444::::444    22222::::::22   
6::::::::::::::66 4::::::::::::::::4  22::::::::222     
6::::::66666:::::64444444444:::::444 2:::::22222        
6:::::6     6:::::6         4::::4  2:::::2             
6:::::6     6:::::6         4::::4  2:::::2             
6::::::66666::::::6         4::::4  2:::::2       222222
 66:::::::::::::66        44::::::442::::::2222222:::::2
   66:::::::::66          4::::::::42::::::::::::::::::2
     666666666            444444444422222222222222222222
                                                        """
nm = os.getenv("USERNAME") or os.getenv("USER")




def main():
    os.system('cls')
    print(Colorate.Horizontal(Colors.blue_to_white, Center.XCenter (banner)))
    print('')
    print('')
    print(Colorate.Horizontal(Colors.purple_to_blue,Center.XCenter  ("╔═══════════════════════════════════════╗")))
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("║    [1] IP lookup                      ║")))
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("╚═══════════════════════════════════════╝")))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    choice = input(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter (f"[{nm}#root]-> ")))
    if choice == '':
        main()

    if choice == "1":

        os.system('title Ip look up')
        # This Is A Max Ip Lookup From My Tool
        ipv2 = input(Colorate.Horizontal(Colors.purple_to_blue, "                               IP: "))
        response = requests.get(f"https://ipwho.is/{ipv2}")
        data = response.json()
        address = f"{data.get('city', '')}, {data.get('region', '')}, {data.get('postal', '')}, {data.get('country', '')}"
        output = (
    f"Country: {data.get('country', 'N/A')}\n"
    f"CountryCode: {data.get('country_code', 'N/A')}\n"
    f"Region: {data.get('region', 'N/A')}\n"
    f"RegionCode: {data.get('region_code', 'N/A')}\n"
    f"City: {data.get('city', 'N/A')}\n"
    f"Zip: {data.get('postal', 'N/A')}\n"
    f"Capital: {data.get('capital', 'N/A')}\n"
    f"Continent: {data.get('continent', 'N/A')}\n"
    f"ContinentCode: {data.get('continent_code', 'N/A')}\n"
    f"Borders: {', '.join(data.get('borders', [])) if data.get('borders') else 'N/A'}\n\n"
    f"IP: {data.get('ip', 'N/A')}\n"
    f"Ip-Type: {data.get('type', 'N/A')}\n"
    f"Lat: {data.get('latitude', 'N/A')}\n"
    f"Lon: {data.get('longitude', 'N/A')}\n\n"
    f"Timezone: {data.get('timezone', {}).get('id', 'N/A')}\n"
    f"UTCOffset: {data.get('timezone', {}).get('offset', 'N/A')}\n"
    f"CurrentTime: {data.get('timezone', {}).get('current_time', 'N/A')}\n"
    f"IsDST: {data.get('timezone', {}).get('is_dst', 'N/A')}\n\n"
    f"ISP: {data.get('connection', {}).get('isp', 'N/A')}\n"
    f"Domain: {data.get('connection', {}).get('domain', 'N/A')}\n"
    f"Org: {data.get('connection', {}).get('org', 'N/A')}\n"
    f"ASN: {data.get('connection', {}).get('asn', 'N/A')}\n\n"
    f"VPN: {data.get('security', {}).get('is_vpn', 'False')}\n"
    f"Proxy: {data.get('security', {}).get('is_proxy', 'False')}\n"
    f"TOR: {data.get('security', {}).get('is_tor', 'False')}\n"
    f"Hosting: {data.get('security', {}).get('is_hosting', 'False')}\n"
    f"Flag: {data.get('flag', {}).get('emoji', 'N/A')}\n"
        f"{address}"
        
        )
        
        print(Colorate.Horizontal(Colors.purple_to_blue, output, 1)) 
        pause = input(Colorate.Horizontal(Colors.purple_to_blue, "Press Enter To Continue"))
        os.system('cls')
        main()

if __name__ == "__main__":
    main()