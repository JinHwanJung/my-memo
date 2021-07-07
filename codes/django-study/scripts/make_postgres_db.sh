#!/usr/bin/env bash
container_name=django_study_postgres
docker rm -f $(docker ps -a | grep $container_name | awk "{print \$1}")
docker run -itd --name $container_name -p 55432:5432 -e POSTGRES_PASSWORD=password --restart unless-stopped postgres:13
