import random
import requests
import colorama
import sys

cookies = open("cookies.txt", "r").read().splitlines()
proxies = open("proxies.txt", "r").read().splitlines()

if len(cookies) == 0:
  print(colorama.Fore.RED + "You do not have any cookies in cookies.txt!")
  sys.exit()

def main():
  val = 0
  inval = 0
  for cookie in cookies:
    r = requests.get("https://api.roblox.com/currency/balance", cookies={".ROBLOSECURITY":cookie}, proxies={"http://":random.choice(proxies), "https://":random.choice(proxies)}) #checks the cookie via the roblox api
    if r.status_code == 200: #if the status code is 200, it means it works!
      val += 1
      print(colorama.Fore.GREEN + "Found valid cookie!")
    else:
      inval += 1
      print(colorama.Fore.RED + "Found invalid cookie!")
main()
