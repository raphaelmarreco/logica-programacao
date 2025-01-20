Calculadora executável em Python - Shell Script

Bem vindo(a)! Siga as instruções para executar a calculadora:

1. Baixe ambos arquivos: 'calculadora.sh' e 'script_calculadora.py';

2. Edite o caminho, dentro do arquivo .sh, para o arquivo Python, de forma que ao executar o Shell Script, o arquivo .py seja encontrado. Ex: os arquivos foram salvos na pasta Download. Deve-se editar a linha 11 para "/home/user/downloads/script_calculadora.py". Salve-o.

3. Para executar a calculadora, dê o comando "./calculadora.sh". É fundamental que, ao executar o comando, esteja no diretório do arquivo .sh. Utilize, por exemplo, o comando "cd /directory/of/your/file", substituindo pelo real caminho até o diretório onde seu arquivo está.

4. O código da calculadora é iniciado com (1) a definição de duas variáveis, num1 e num2, a serem definidas pelo usuário. As variáveis são obtidas em 'float', ponto flutuante. 
Então, (2) é solicitada a operação desejada pelo usuário, podendo escolher entre adição, subtração, multiplicação e divisão, assim como a opção de sair. As opções podem ser escolhidas por texto ou número (apresentadas via função 'print' ao usuário). Caso haja erro de digitação, será solicitada novamente a operação ao usuário. Essa estrutura é feita com o laço de repetição 'if/else', permitindo a realização de mais de uma operação sem que o programa precise ser iniciado novamente.
