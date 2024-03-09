# DockerBD
Dockerfiles and docker-compose made for Database I classes


Depois de instalar o docker desktop, entre na pasta que você baixou do github e modifique o `docker-compose.yml` com seu nome e email do github.

* Windows
```
docker-compose up --build 
```
* Linux
```
docker compose up --build 
```
<br/>

## Comandos <br/>

Depois disso, abram outro terminal (comando pra usar o terminal)

```
docker exec -it ubuntu bash
```

Para parar o container
```
docker stop ubuntu
```

Para rodar ele depois de parar

```
docker start -i ubuntu
```


Verificar os containers ativos
```
docker ps -a
```

