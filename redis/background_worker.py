import redis

REDIS_HOST = 'Localhost'
REDIS_PORT = 6369


with redis.Redis() as client:
    while True:
        problem = client.brpop('problems')[1].decode('utf-8')
        answer = eval(problem)

        client.lpush('answers', answer)
