# Api de envio de mensagem no Whatsapp
Este script automatiza o envio de mensagens pelo WhatsApp Web utilizando Python, Selenium e uma planilha Excel como fonte de dados. Ele realiza as seguintes etapas:

Carregamento de Dados:

Lê uma planilha Excel (Pasta1.xlsx) que contém as colunas:
Nome: Nome da pessoa.
Número: Número de telefone no formato internacional (com código do país).
Mensagem: Mensagem personalizada a ser enviada.
Abertura do WhatsApp Web:

Abre o WhatsApp Web no navegador Google Chrome.
Aguarda o escaneamento do QR Code pelo usuário para autenticação.
Envio de Mensagens:

Para cada linha da planilha:
Extrai o nome, número e mensagem.
Gera um link com o texto da mensagem usando a API do WhatsApp Web.
Acessa o link e envia a mensagem automaticamente.
Automação com Selenium:

Utiliza o Selenium para interagir com os elementos da interface do WhatsApp Web, como o campo de texto e o botão de envio.
Espera e Controle:

Inclui verificações e pausas para garantir que o WhatsApp Web esteja pronto antes de enviar cada mensagem.
Requisitos
Bibliotecas Python:
pandas: Para manipulação da planilha Excel.
selenium: Para automação do navegador.
urllib: Para codificar o texto da mensagem na URL.
Planilha Excel:
Deve estar no caminho especificado e conter as colunas Nome, Número e Mensagem.
Google Chrome e ChromeDriver:
O ChromeDriver deve ser compatível com a versão do navegador instalado.
Observações
Certifique-se de que os números de telefone estão no formato internacional (ex.: +5511999999999).
O script requer que o usuário escaneie o QR Code do WhatsApp Web manualmente antes de iniciar o envio das mensagens.
