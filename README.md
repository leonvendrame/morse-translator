# Morse Translator
Tradutor de arquivos morse

.txt para .morse e .wav  
.wav para .morse e .txt  
.morse para .txt e .wav  

### Execução
O script pode ser executado por:  
```./app.py arquivo_de_entrada```  
```python3 app.py arquivo_de_entrada```  
Onde o arquivo de entrada é um arquivo do tipo .txt .morse ou .wav  
Cada tipo de arquivo gerará os outros dois tipos restantes  

### Constantes
Para a geração do áudio foram utilizadas as seguintes constantes:  
- **Amplitude**: 16000
- **Taxa de Amostragem**: 48000
- **Número de Amostras**: 12000
- **Frequência**: 440Hz

### Testes e Amostras
Foram incluídos dois testes utilizando a biblioteca *__unittest__*. Os testes correspondem a transformação de texto/morse e morse/texto.  
Foram incluídos alguns arquivos de amostras para execuções, armazenados no diretório *__samples__*.  

#