##Docker compose allow to you create multiple containers and the netowrks that connect them. It is an abstraction of docker-cli and his objetive is avoid tons of code and configurations in docker-cli.

#RUN COMPOSE
docker-compose up

#RUN IN BACKGROUND
docker-compose up -d
 
#RUN COMPOSE AND REBUILD
docker-compose up --build

#STOP CONTAINERS
docker-compose down

#CONTAINER STATUS
docker-compose ps



