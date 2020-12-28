The  data store will  support the following functional requirement:
1. It can be initialized using a optional file path if existing otherwise it will choose current directory as location.
2. A new key-value pair can be added using CREATE function. the key is always a string  and the value is always a JSON object.
3. If CREATE is invoked using existing key, suitable error is shown.
4. A READ operation can be performed by providing key and receiving the value as a response.
5. A DELETE operation can be performed by providing key.
6. Appropriate error responses are always returned to the client.

This data store will also support the following non-functional requirements:
1. Size of the file storing data shall never exceed 1GB.
2. More than on client is allowed to access data store file at the same time.
