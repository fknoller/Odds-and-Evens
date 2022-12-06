import socket as s
import random

def roundWinner(clientParity, sum):
  if((clientParity == "even" and sum % 2 == 0) or (clientParity == "odd" and sum % 2 != 0)):
    return "Client"
  else:
    return "Server"

HOST, PORT = s.gethostname(), 1234

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.bind((HOST, PORT))

sock.listen(5)
print("Waiting player to connect:")
conn, ender = sock.accept()

scoreClient, scoreServer = 0, 0

while True:
  data = conn.recv(1024)
  clientParity = data.decode('utf8')
  
  clientNumber = int(conn.recv(1024))
  serverNumber = random.randint(0, 10)

  conn.sendall(bytes(str(serverNumber), 'utf8'))

  sum = clientNumber + serverNumber
  result = roundWinner(clientParity, sum)

  if(result == "Client"):
    scoreClient += 1
  elif(result == "Server"):
    scoreServer += 1

  print("Client: " + str(clientNumber) + " x Server: " + str(serverNumber) + " -- Winner: " + str(result))

  data = conn.recv(1024)
  play = data.decode('utf8')
  if(play == "y"):
    continue
  else:
    break

conn.close()
sock.close()

print("Final Score: Client: " + str(scoreClient) + " x Server: " + str(scoreServer))

if(scoreClient > scoreServer):
  print("Client wins!")

elif(scoreClient < scoreServer):
  print("Server wins!")

else:
  print("Tie!")