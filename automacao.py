from selenium import webdriver;
import time;

navegador = webdriver.Chrome();
navegador.get("https://www.selenium.dev/selenium/web/web-form.html")
navegador.maximize_window()

titulo = navegador.title; # exemplo de como pegar o titulo da guia
print(titulo)

text_input = navegador.find_element("id","my-text-id");
text_input.send_keys("inserindo o primeiro texto")

password_input = navegador.find_elements("class name", "form-control") # com isso consigo um array de todos os elementos da classe 
password_input[1].send_keys("senha123") 

time.sleep(5)