## usage

```sh
git clone https://github.com/wusisu/ops.git
cd ops
docker-compose build redis_read_all_keys
cp .env.example .env
# modify .env
docker-compose run redis_read_all_keys
```