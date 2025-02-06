# Use official Node.js 18 image as base
FROM node:18

# Set the working directory inside the container
WORKDIR /

# Copy the rest of the application code
COPY . .

# Set environment variable for port
ENV PORT=8000

# Expose the port specified in the environment variable
EXPOSE $PORT

# Command to run the application (you can put lots of extra args in the actual dockerfile to hide the flag some)
CMD ["node", "server.js", "server_max_limit=600", "language=Reptilian", "version=1.0.0",  "flag=swampCTF{Unic0d3_F0r_Th3_W1n}", "shutdown_condition=never"]