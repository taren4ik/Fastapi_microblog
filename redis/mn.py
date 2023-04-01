import redis

REDIS_HOST = 'Localhost'
REDIS_PORT = 6369

with redis.Redis() as client:
    while True:
        problem = input(':::')
        client.lpush('problems', problem)

        answer = client.brpop('answers')[1].decode('utf-8')
        print(f'Answer: {answer}')
