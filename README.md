# 🤖 Bot Tradutor Telegram

Um bot inteligente para o Telegram que traduz automaticamente mensagens do português para o espanhol usando a API do Google Translate.

## ✨ Funcionalidades

- **Tradução automática**: Traduz mensagens do português para o espanhol em tempo real
- **Comando /start**: Mensagem de boas-vindas para iniciar a interação
- **Interface simples**: Basta enviar qualquer mensagem em português e receber a tradução
- **Emojis**: Traduções acompanhadas de emojis para uma experiência mais amigável

## 🚀 Como usar

1. **Inicie o bot** com o comando `/start`
2. **Envie qualquer mensagem** em português
3. **Receba automaticamente** a tradução em espanhol

## 🛠️ Tecnologias utilizadas

- **Python 3.x**
- **python-telegram-bot**: Biblioteca oficial do Telegram para bots
- **deep-translator**: Biblioteca para tradução usando Google Translate
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Token de bot do Telegram
- Conta no Telegram

## 🔧 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/hbCosta/bot_tele.git
   cd bot_tele
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione seu token do Telegram:
     ```
     TELEGRAM_TOKEN=seu_token_aqui
     ```

4. **Execute o bot:**
   ```bash
   python bot.py
   ```

## 📱 Como obter o token do bot

1. Fale com o [@BotFather](https://t.me/botfather) no Telegram
2. Use o comando `/newbot`
3. Siga as instruções para criar seu bot
4. Copie o token fornecido para o arquivo `.env`

## 🏗️ Estrutura do projeto

```
bot_tele/
├── bot.py              # Arquivo principal do bot
├── translator.py       # Módulo de tradução
├── requirements.txt    # Dependências Python
├── Procfile           # Configuração para deploy (Heroku)
├── runtime.txt        # Versão do Python para deploy
└── README.md          # Este arquivo
```

## 🌐 Deploy

O projeto está configurado para deploy no Heroku com:
- `Procfile`: Configuração para executar o bot
- `runtime.txt`: Especificação da versão do Python

## 📝 Exemplo de uso

```
Usuário: Olá, como você está?
Bot: 🇪🇸: Hola, ¿cómo estás? ✨

Usuário: Bom dia! Tudo bem?
Bot: 🇪🇸: ¡Buenos días! ¿Todo bien? ✨
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Se tiver dúvidas ou problemas:
- Abra uma issue no repositório
- Entre em contato através do Telegram

---

**Desenvolvido  para facilitar a comunicação entre falantes de português e espanhol!**
