from selenium import webdriver;
import time;

navegador = webdriver.Chrome();
navegador.get("https://www.selenium.dev/selenium/web/web-form.html")
navegador.maximize_window()

titulo = navegador.title; # exemplo de como pegar o titulo da guia
print(titulo)

# primeiro input
text_input = navegador.find_element("id","my-text-id");
text_input.send_keys("inserindo o primeiro texto")

# input de senha
password_input = navegador.find_elements("class name", "form-control") # com isso consigo um array de todos os elementos da classe 
password_input[1].send_keys("senha123") 

# preenchendo o text area
areaTexto = navegador.find_element("name","my-textarea");
areaTexto.send_keys("Um texto sendo colocado no textArea da pagina de treinar preenchimento de formulario entregue na documentação do Selenium!!")


time.sleep(5)