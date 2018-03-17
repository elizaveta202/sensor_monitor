import socket
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg["consumer_key"], cfg["consumer_secret"])
  auth.set_access_token(cfg["access_token"], cfg["access_token_secret"])
  return tweepy.API(auth)

def tweet(data):

  cfg = {
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : ""
    }

  api = get_api(cfg)
  tweet = "This is the first tweet"
  status = api.update_status(status=data)


if __name__ == "__main__":
    s = socket.socket()
    s.bind(('', 9090))
    s.listen(1)
    conn, addr = s.accept()
    print ('connected to'+'str(addr)')
    while True:
        data = conn.recv(1024)
        if data:
            print(data)
            tweet(data)
            conn.send('Ok!')
    conn.close()