
import asyncio
import os
import random
import re
import sys
import aiohttp
from leakcheck import LeakCheckAPI
import platform
from datetime import datetime; 
from colorama import Fore, init; init()
class RUNING:
    def __init__(self,username,counter,followers,following,images, leak_auth_key):
        
        self.username = username
        self.counter = counter
        self.leak_auth_key = leak_auth_key
        self.version = "1.0.2"
        self.session = aiohttp.ClientSession()
        self.timeouts = 20
        self.followers = followers
        self.following = following
        self.images = images
        self.url = "https://leakcheck.io"
        
    async def get_email(self):
        assert (len(self.leak_auth_key) == 40), "A key is invalid, it must be 40 characters long"
        headers = {'X-API-Key': self.leak_auth_key, 'Accept': 'application/json', "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0"}
        async with self.session.get(f'https://leakcheck.io/api/v2/query/{self.username}?type=username', headers=headers, timeout=self.timeouts) as response:
            if response.status != 200:
                if response.status == 429:
                    raise Exception(f"MAX LIMIT EXCEEDED")
                raise Exception(f"Invalid response code ({response.status}) instead of 200")
            
            result =  await response.json()
            if result.get('success') == False:
                if result.get("error") == "Not found":
                    err = result.get("error")
                    raise Exception(f"Error {err}")
                return []
            else:
                return result
    
    
    
        
           
            
    def extract_emails(self, text):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(pattern, text)
        return emails

    def save_username_email(self,x):
        with open('RESULT_RANDOM/username-email.txt', 'a', encoding='utf-8', errors='ignore') as f:
            data_s = f'{self.username}:{x}:{self.followers}:{self.following}:{self.images}'
            f.write(data_s + '\n')
    
    def save_email(self,x):
        with open('RESULT_RANDOM/email.txt', 'a', encoding='utf-8', errors='ignore') as f:
            data_s = f'{x}'
            f.write(data_s + '\n')
            
    def save_username(self):
        with open('RESULT_RANDOM/notFound.txt', 'a', encoding='utf-8', errors='ignore') as f:
            data_s = f'{self.username}:{self.followers}:{self.following}:{self.images}'
            f.write(data_s + '\n')
    
    def save_error(self):
        with open('RESULT_RANDOM/error.txt', 'a', encoding='utf-8', errors='ignore') as f:
            data_s = f'{self.username}:{self.followers}:{self.following}:{self.images}'
            f.write(data_s + '\n')
    
    
    def save_combo(self,email,pwd):
        with open('RESULT_COMBO/combo.txt', 'a', encoding='utf-8', errors='ignore') as f:
            data_s = f'{self.username}:{email}:{pwd}:{self.followers}:{self.following}:{self.images}'
            f.write(data_s + '\n')
    
    
    async def get_password(self, email):
        assert (len(self.leak_auth_key) == 40), "A key is invalid, it must be 40 characters long"
        headers = {'X-API-Key': self.leak_auth_key, 'Accept': 'application/json', "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0"}
        data = {'key': self.leak_auth_key, 'type': 'email', "check": email}
        async with self.session.get(f'{self.url + "/api"}',params=data, headers=headers, timeout=self.timeouts) as response:
            data =  await response.json()
            if response.status != 200:
                if response.status == 429:
                    raise Exception(f"MAX LIMIT EXCEEDED")
                raise Exception(f"Invalid response code ({response.status}) instead of 200")
            
            arr_data = []
            count_result = 0
            if data['success']:
                for line in data['result']:
                    if line['line'].lower() != email.lower() or line['line'].upper() != email.upper():
                        combo = line['line']
                        if combo:
                            password  = combo.split(':')[1]
                            if len(password) >= 7:
                                if all(char.isdigit() or char == '.' for char in password):
                                    pass
                                elif ' ' not in password:
                                    arr_data.append(password.lower())
                                    arr_data.append(password.capitalize())
                                    arr_data.append(f'{password}!')
                                    arr_data.append(f'{password}!!')
                                    arr_data.append(f'{password.lower()}!')
                                    arr_data.append(f'{password.lower()}!!')
                                    arr_data.append(f'{password.capitalize()}!')
                                    arr_data.append(f'{password.capitalize()}!!')
                                    count_result +=1
            
        
    
    
    async def run(self):
        try:
            RESULT_SAVE = []
            res = await self.get_email()
            if res['success']:
                SUCCES = res['success']
                FOUND = res['found']
                extracted_emails = self.extract_emails(str(res))
                datas = datetime.now()
                nows = datas.strftime('%Y-%m-%d %H:%M:%S')
                if len(extracted_emails) > 10:
                    for x in extracted_emails[:10]:
                        RESULT_SAVE.append(x)
                        # data = await self.get_password(x)
                    print(f'{Fore.CYAN}[{Fore.YELLOW} {nows} {Fore.CYAN}]  [{Fore.GREEN} {self.username}{Fore.CYAN} ] [ {Fore.WHITE}SUCCES:{Fore.GREEN} {SUCCES}{Fore.CYAN} ] [ {Fore.WHITE}FOUND:{Fore.GREEN} {FOUND}{Fore.CYAN} ] [ {Fore.WHITE}EXTRACTED:{Fore.GREEN} {len(extracted_emails[:10])}{Fore.CYAN} ]{Fore.RESET}')
                elif len(extracted_emails) == 0:
                    self.save_username()
                    print(f'{Fore.CYAN}[{Fore.YELLOW} {nows} {Fore.CYAN}]  [{Fore.LIGHTBLUE_EX} {self.username}{Fore.CYAN} ] [ {Fore.WHITE}SUCCES:{Fore.LIGHTBLUE_EX} {SUCCES}{Fore.CYAN} ] [ {Fore.WHITE}FOUND:{Fore.LIGHTBLUE_EX} {FOUND}{Fore.CYAN}] [ {Fore.WHITE}EXTRACTED:{Fore.LIGHTBLUE_EX} {len(extracted_emails[:10])}{Fore.CYAN} ]{Fore.RESET}')
                else:
                    for x in extracted_emails:
                        RESULT_SAVE.append(x)
                        # data = await self.get_password(x)
                    print(f'{Fore.CYAN}[{Fore.YELLOW} {nows} {Fore.CYAN}]  [{Fore.GREEN} {self.username}{Fore.CYAN} ] [ {Fore.WHITE}SUCCES:{Fore.GREEN} {SUCCES}{Fore.CYAN} ] [ {Fore.WHITE}FOUND:{Fore.GREEN} {FOUND}{Fore.CYAN} ] [ {Fore.WHITE}EXTRACTED:{Fore.GREEN} {len(extracted_emails[:10])}{Fore.CYAN} ]{Fore.RESET}')
            
                for d in set(RESULT_SAVE):
                    self.save_username_email(d)
                    self.save_email(d)
            else:
                print('ERROR')
        except Exception as e:
            self.save_error()
            print(e)
            
    async def close(self):
         if self.session:
            if not self.session.closed:
                await self.session.close()