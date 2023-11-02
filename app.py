from http.server import HTTPServer

from setting import hostName, serverPort
from views import MyServer

if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Корректная остановка веб-сервера
    webServer.server_close()
    print("Server stopped.")