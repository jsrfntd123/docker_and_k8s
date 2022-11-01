# Specify base image
FROM node:alpine

#Install some dependencies
WORKDIR /usr/app
COPY ./package.json /usr/app
RUN npm install 
COPY ./ /usr/app

#Setup default commands
CMD ["npm","start"]