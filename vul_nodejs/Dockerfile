# Use Node:12.22.9-alpine as the base image
FROM node:12.22.9-alpine

# Set /usr/src/app as the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install the dependencies from the JSON file using npm
RUN npm install

# Copy everything to the container
COPY . .

# Expose port 8000
EXPOSE 3000

# Start the node application using the start script
CMD ["npm", "start"]
