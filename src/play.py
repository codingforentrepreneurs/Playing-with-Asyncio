import asyncio
import time
import random

def sync_run(name):
    random_int = random.randint(50000, 54304231)
    start_time = time.time()
    for i in range(0, random_int): # webpage
        pass
    ellapsed_time = time.time() - start_time
    print(f"{name} with {random_int} iterations took {ellapsed_time} seconds")


def run_the_sync_run():
    start_time = time.time()
    for i in range(0, 10):
        name = f"Iteration {i}"
        sync_run(name)
    ellapsed_time = time.time() - start_time
    print(f"Loop took {ellapsed_time} seconds")


# run_the_sync_run()
async def async_run(name):
    random_sleep_time = random.random()
    
    start_time = time.time()
    await asyncio.sleep(random_sleep_time)
    ellapsed_time = time.time() - start_time
    msg = f"{name} with {random_int} iterations took {ellapsed_time} seconds"
    print(msg)
    return msg

def compile_async_tasks():
    tasks = []
    
    for i in range(0, 10):
        name = f"Async Iteration {i}"
        tasks.append(
            asyncio.ensure_future(async_run(name))
        )
    print(tasks)
    return tasks

tasks = compile_async_tasks()



start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

ellapsed_time = time.time() - start_time
print(f"Async loop took {ellapsed_time} seconds")








