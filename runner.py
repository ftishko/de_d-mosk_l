from telethon import TelegramClient
import os
import random
import asyncio
from telethon import functions, types

QTY_PER_USER = 10000

if os.environ.get('API_ID') and os.environ.get('API_HASH'):
    api_id = int(os.environ.get('API_ID'))
    api_hash = os.environ.get('API_HASH')
else:
    while True:
        try:
            api_id = int(input('Введіть api_id:'))
            api_hash = input('Введіть api_hash:')
            break
        except ValueError:
            print('api_id некоректне число')


async def connector(client, user_name):

    for i in range(QTY_PER_USER):
        try:
            reason = random.choice([
                types.InputReportReasonOther(),
                types.InputReportReasonFake()
            ])
            result = await client(
                functions.account.ReportPeerRequest(
                    peer=user_name,
                    reason=reason,
                    message='Fake information about the war in Ukraine. '
                            'Murder propaganda of Ukrainians and Ukrainian soldiers.'
                )
            )
            if result is False:
                print(f'problem with user: {user_name} {i}')
            else:
                print(f'{user_name} is successfully reported {i}')
        except Exception as err:
            print(err)
        await asyncio.sleep(10)


async def main_start():
    set_of_requests = set()
    with open('dicks.txt', 'r') as file:
        dicks = file.readlines()
        for dick in dicks:
            set_of_requests.add(connector(client, dick.rstrip()))
    await asyncio.gather(*set_of_requests)
    print('finished')

client = TelegramClient('sess', api_id, api_hash,)

with client:
    client.loop.run_until_complete(main_start())
