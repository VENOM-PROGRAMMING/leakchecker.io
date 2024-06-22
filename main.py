import asyncio
import time
from aiomultiprocess import Pool
from colorama import Fore, init; init()
import json
import os
from datetime import datetime as dt
import subprocess

from client import RUNING



PU = []
with open('username.txt', 'a+' , encoding='utf-8') as username:
    username.seek(0)
    for i, line in enumerate(username, start=1):
        line = line.rstrip()
        PU.append(f'{i}:{line}')


async def main(data):
    try:
        leak_auth_key = '08a30f79fa03bb5912128352f698c107fdeeef32'
        counter= data.split(':')[0]
        username = data.split(':')[1]
        followers = data.split(':')[2]
        following = data.split(':')[3]
        ximages = data.split(':')[4]
        imageshttps = data.split(':')[5]
        images = f'{ximages}:{imageshttps}'
        client = RUNING(username, counter, followers,following, images, leak_auth_key)
        runing = await client.run()
        # runing = await client.get_password('lisahirth17@gmail.com')
        await client.close()
    except Exception as e:
        with open('RESULT_RANDOM/error.txt', 'a', encoding='utf-8', errors='ignore') as f:
            data_s = f'{data}'
            f.write(data_s + '\n')
        print(e)
        pass
        
async def x():
    n = 3
    final = [PU[i * n:(i + 1) * n] for i in range((len(PU) + n - 1) // n )]
    for x in final:
        async with Pool() as pool:
            async for result in pool.map(main,x):
                continue
            
            
if __name__ == "__main__":
    try:
        asyncio.run(x())
    except Exception as e:
        print(f'1 {e}')
        pass