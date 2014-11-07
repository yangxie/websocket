import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

class WSHandler(tornado.websocket.WebSocketHandler):
	clients = set()

	def open(self):
		print "new connection"
		self.write_message("Hello World")
		clients.add(self)
		print "The num of connection is %d" % len(clients)
      
	def on_message(self, message):
		print "message received %s" % message
 
	def on_close(self):
		print "connection closed"
		clients.remove(self)
		print "The num of connection is %d" % len(clients)


application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8009)
    tornado.ioloop.IOLoop.instance().start()