import asyncio

async def get_user_data(user_id: int) -> dict:
    import time
    await asyncio.sleep(10)
    return {"10": [user_id]}


async def get_user(user_id: int) -> dict:
    import time
    await asyncio.sleep(10)
    return {"9": [user_id]}

async def main():
    print('start')
    k = await get_user_data(10)
    f = await get_user(32)
    print(f)
    print('finish')
    print(k)

asyncio.run(main())