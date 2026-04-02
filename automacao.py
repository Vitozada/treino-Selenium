from selenium import webdriver;
from selenium.webdriver.support.select import Select ## import necessario para poder selecionar os elementos chamados Select em html
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

inputDesabilitado = navegador.find_element("name","my-readonly")
texto = inputDesabilitado.get_attribute("value") # exemplo de como pegar texto de algum input 
print(texto)

# selecionando opções em um select que permite só uma resposta
selecionar = navegador.find_element("name","my-select");
select = Select(selecionar) # para isso precisamos importar o SELECT
select.select_by_index(3) # selecionando em si pela posição da opção

# preenchendo o input de cidade
escolherCidade = navegador.find_element("name","my-datalist");
escolherCidade.click()
escolherCidade.send_keys("São paulo")

#enviando o arquivo para o input
botaoArquivo = navegador.find_element("name","my-file")
botaoArquivo.send_keys(r"C:\exemplo\teste\dados.txt")

#clickando nos CheckBox

navegador.find_element("id","my-check-1").click()
navegador.find_element("id","my-check-1").click()
navegador.find_element("id","my-check-2").click() # deixar os dois selecionados ao mesmo tempo

# clickando nos RADIO

radios = navegador.find_elements("name","my-radio")
radios[1].click()
radios[0].click()
radios[1].click()

# input colors

cor = navegador.find_element("name","my-colors")
cor.send_keys("#0000ff") # para preencher o input de color, precisa colocar o hexadecimal da cor desejada

# input de data

opcaoData = navegador.find_element("name","my-date")
opcaoData.send_keys("17/08/2006")

#input RANGE Usando javaScript
# usei o copilot para entender como mexer no input RANGE retornando esse codigo
inputRange = navegador.find_element("name","my-range")
navegador.execute_script("""  
    arguments[0].value = 9; 
    arguments[0].dispatchEvent(new Event('input'));
    arguments[0].dispatchEvent(new Event('change'));
""", inputRange) # antes de colocar o valor ver qual é o min e o max do INPUT

# enviando o formulario
enviar = navegador.find_element("css selector","button") # achando elemento pelo CSS
enviar.click()

time.sleep(5)