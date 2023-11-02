from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    """обработка входящих данных"""
    def get_html(self):
        html_file = open('index.html', encoding='utf-8')
        data = html_file.read()
        html_file.close()
        return data
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.get_html()
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8")) # ответ