FROM node:14.16.0-alpine3.13
USER node:node
WORKDIR /app
COPY package*.json .
# COPY package.json package-lock.json .
RUN npm i 
# RUN chown -R node:node /app
COPY . .
EXPOSE 3000
# RUN chmod o-r package*.json

CMD [ "npm", "start"]