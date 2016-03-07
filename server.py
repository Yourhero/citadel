import threading, os, sys, time
from Mastermind import *
from config.server_config import *

class CitadelServer(MastermindServerTCP):
  def __init__(self):
    MastermindServerTCP.__init__(self, 0.5, 0.5, 10.0) #server refresh, conn refresh, conn timeout
    self.clients = {}
    self.players = {}
    self.mutex = threading.Lock()

  def add_client(self, username, connection):
    self.mutex.acquire()
    print "Adding new client, " + username + " connection: " + str(connection)
    self.clients[username] = connection
    self.mutex.release()

  def remove_client(self, username):
    self.mutex.acquire()
    del self.clients[username]
    self.mutex.release()

  def add_player(self, username, avatar_image, x = 100, y = 100):
    self.mutex.acquire()
    print "Creating player ... " + username
    self.players[username] = {'avatar' : avatar_image, 'x_pos' : x, 'y_pos' : y }
    print "Player " + username + " created, image: " + avatar_image
    self.mutex.release()

  def remove_player(self, username):
    self.mutex.acquire()
    del self.players[username]
    self.mutex.release()

  def update_player_position(self, username, x, y, x_vel, y_vel):
    self.mutex.acquire()
    self.players[username]['x_pos'] = x
    self.players[username]['y_pos'] = y
    print "Player: " + username + " pos X: " + str(x) + " Y: " + str(y) + " Vel X: " + str(x_vel) + " Y: " + str(y_vel)
    print " "
    self.mutex.release()

  def callback_connect(self):
    return super(CitadelServer,self).callback_connect()

  def callback_disconnect(self):
    return super(CitadelServer,self).callback_disconnect()

  def callback_connect_client(self, connection_object):
    return super(CitadelServer,self).callback_connect_client(connection_object)

  def callback_disconnect_client(self, connection_object):
    return super(CitadelServer,self).callback_disconnect_client(connection_object)
    
  def callback_client_receive(self, connection_object):
    return super(CitadelServer,self).callback_client_receive(connection_object)

  def callback_client_handle(self, connection_object, data):
    cmd = data[0]
    username = data[1]
    if cmd == "login":
      self.add_client(username, connection_object) # username, connection
      self.add_player(username, data[2]) # username, avatar image
      reply = ["success"]
    elif cmd == "update":
      x_pos = data[2]
      y_pos = data[3]
      x_vel = data[4]
      y_vel = data[5]
      self.update_player_position(username, x_pos, y_pos, x_vel, y_vel)
      reply = ["move", self.players[username]['x_pos'], self.players[username]['y_pos']] 
    self.callback_client_send(connection_object, reply)

  def callback_client_send(self, connection_object, data, compression=None):
    return super(CitadelServer,self).callback_client_send(connection_object, data,compression)

if __name__ == "__main__":
    print "Creatig CitadelServer...\n"
    server = CitadelServer()
    server.connect(SERVER_ADDRESS, SERVER_PORT)
    print "Server ready listening on port " + str(SERVER_PORT)
    try:
        server.accepting_allow_wait_forever()
    except:
        #Only way to break is with an exception
        pass
    print "Server shutting down.\n"
    server.accepting_disallow()
    server.disconnect_clients()
    server.disconnect()