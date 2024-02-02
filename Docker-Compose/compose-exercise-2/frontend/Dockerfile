FROM node:20.11.0-alpine3.19
WORKDIR /app
COPY package*.json .
# COPY package.json package-lock.json .
RUN npm i 
# RUN chown -R node:node /app
COPY . .
EXPOSE 3000
RUN chmod o-r package*.json
USER node:node

CMD [ "npm", "start"]