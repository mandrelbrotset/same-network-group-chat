# Group Chat App Tutorial(YouTube)

## Running the code
### Starting the server
In the commandline, start the server with ```python3 server.py```. Change ```localhost``` in server.py to ```0.0.0.0``` to be able to accept connections from other computers.

### Starting the client app
In the commandline, start the server with ```python3 client.py```

### Connecting to the server
- If "Hostname" is not specified, ```localhost``` is used
- Enter "Port" field or leave empty to use ```5555```
- Enter "Nickname" or leave empty to generate one based on the clients hostname
- Click the ```connect``` button.

- Create multiple instances of the client for messages to be sent and received by each client

## Generating ```.py``` files from ```.ui``` files
Run ```pyuic5 test.ui -o test.py```

