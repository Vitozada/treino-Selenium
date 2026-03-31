from selenium import webdriver;
import time;

navegador = webdriver.Chrome();
navegador.maximize_window();
navegador.get("https://www.pichau.com.br/");

botao_departamento = navegador.find_elements("class name","MuiButtonBase-root")
botao_departamento[4].click() ## clicou em departamentos

time.sleep(10)
