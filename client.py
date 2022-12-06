import socket as s

def roundWinner(clientParity, sum):
  if((clientParity == "even" and sum % 2 == 0) or (clientParity == "odd" and sum % 2 != 0)):
    return "Client"
  else:
    return "Server"

HOST, PORT = s.gethostname(), 1234

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.connect((HOST, PORT))

scoreClient, scoreServer = 0, 0
play = True

while play == True:
  clientParity = input("Choose your parity (even or odd): ")
  if(clientParity != "even" and clientParity != "odd"):
    print("Invalid parity!")
    continue
  sock.sendall(bytes(clientParity, 'utf8'))

  clientNumber = int(input("Choose your number: "))
  sock.sendall(bytes(str(clientNumber), 'utf8'))

  serverNumber = int(sock.recv(1024))

  sum = clientNumber + serverNumber
  result = roundWinner(clientParity, sum)

  if(result == "Client"):
    scoreClient += 1
  elif(result == "Server"):
    scoreServer += 1

  print("Client: " + str(clientNumber) + " x Server: " + str(serverNumber) + " -- Winner: " + str(result))

  play = input("Do you want to play again? (y/n): ")
  sock.sendall(bytes(play, 'utf8'))
  if(play == "y"):
    play = True
  else:
    play = False

sock.close()

print("Final Score: Client: " + str(scoreClient) + " x Server: " + str(scoreServer))

if(scoreClient > scoreServer):
  print("Client wins!")

elif(scoreClient < scoreServer):
  print("Server wins!")

else:
  print("Tie!")