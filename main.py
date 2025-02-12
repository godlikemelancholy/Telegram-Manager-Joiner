import tg
import os
import shutil
import loguru
import asyncio


async def main():
    sessions = os.listdir('sessions/new')
    with open('channels.txt') as f:
        channels = f.readlines()
        for i in range(len(channels)):
            channels[i] = channels[i].rstrip()

    for channel in channels:
        for session in sessions:
            try:
                acc = tg.Telegram(f'sessions/new/{session}')
                await acc.join_channel(channel)
                logger.success(session + '   -> Done!')
            except Exception as e:
                if 'deactivated' in str(e):
                    shutil.move(f'sessions/new/{session}', f'sessions/invalid/{session}')
                logger.error(e)
            finally:
                await asyncio.sleep(2)

if __name__ == '__main__':
    logger = loguru.logger
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())