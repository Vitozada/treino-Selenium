from selenium import webdriver;
import time;

navegador = webdriver.Chrome();
navegador.get("https://www.pichau.com.br/");
navegador.maximize_window();

botao_departamento = navegador.find_elements("class name","MuiButtonBase-root")
time.sleep(5)
botao_departamento[4].click() ## clicou em departamentos

barra = navegador.find_elements("class name", "mui-tjklty-arrow")
barra[0].click()

time.sleep(10)
