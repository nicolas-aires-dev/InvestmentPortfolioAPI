# Investment Portfolio API

## 🎯 Objetivo
API para gerenciamento de carteira de investimentos, permitindo registro de transações, cálculo de posição e lucro/prejuízo.  
Integração com API da bolsa para precificação em tempo real.

## ⚙️ Tecnologias
- 🐍 Python  
- 🚀 Django / FastAPI  
- 🗄️ PostgreSQL  
- 🐳 Docker  
- 🐇 Celery + Redis  
- 🧪 Pytest  

## 🧱 Funcionalidades (fase 1)
- Cadastro de ativos  
- Registro de transações  
- Listagem de operações  

## 🧠 Estrutura mental
- **Ativo**: representa uma ação ou título.  
- **Transação**: compra ou venda de um ativo.  
- **Posição**: quantidade acumulada de um ativo.  
- **Lucro/Prejuízo**: diferença entre preço médio e preço atual.  

## 📍 Roadmap
- [x] CRUD de ativos  
- [x] Registro de transações  
- [ ] Cálculo de posição  
- [ ] Cálculo de lucro/prejuízo  
- [ ] Processamento assíncrono  
- [ ] Autenticação JWT  
- [ ] Integração com API da bolsa  
