# Set the base image for the app
FROM node:alpine

# Set the working directory
WORKDIR /app

# Copy the app's source code into the container
COPY package.json package-lock.json ./
COPY src ./src
COPY public ./public

# Install dependencies
RUN npm install

# Build the app
RUN npm run build

# Expose the port
EXPOSE 3000

# Set the command to start the app
CMD ["npm", "start"]
