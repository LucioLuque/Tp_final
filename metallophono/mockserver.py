from xylophone.server.server import MockXyloServer

server = MockXyloServer(host='localhost', port=8080)

server.start()