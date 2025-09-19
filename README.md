# 🏢 Prospecção de Empresas Locais

Sistema completo para prospecção de empresas locais que ainda não estão cadastradas no Google Maps. O projeto inclui frontend React moderno e backend Flask com integração à Google Places API.

## 🚀 Funcionalidades

- **Busca por cidade**: Digite o nome de qualquer cidade brasileira
- **Listagem de empresas**: Visualize empresas locais com nome, endereço e telefone
- **Filtro inteligente**: Mostre apenas empresas não cadastradas no Google Maps
- **Exportação CSV**: Exporte os resultados para análise posterior
- **Interface responsiva**: Funciona perfeitamente em desktop e mobile
- **API REST**: Backend robusto com endpoints documentados

## 🛠️ Tecnologias Utilizadas

### Frontend
- **React 18** com Vite
- **Tailwind CSS** para estilização
- **shadcn/ui** para componentes
- **Lucide React** para ícones

### Backend
- **Flask** (Python)
- **Flask-CORS** para CORS
- **Google Places API** para busca de empresas
- **Requests** para chamadas HTTP

## 📁 Estrutura do Projeto

```
meu-projeto/
├── frontend/                 # Aplicação React
│   ├── src/
│   │   ├── components/ui/   # Componentes shadcn/ui
│   │   ├── App.jsx         # Componente principal
│   │   └── main.jsx        # Ponto de entrada
│   ├── dist/               # Build de produção
│   └── package.json
├── api/                     # Backend Flask
│   ├── search.py           # Endpoint principal
│   └── requirements.txt    # Dependências Python
├── src/                    # Estrutura para deploy
│   └── main.py            # Arquivo principal Flask
├── .env.example           # Exemplo de variáveis de ambiente
├── .env                   # Variáveis de ambiente (não commitado)
├── requirements.txt       # Dependências raiz
└── README.md             # Esta documentação
```

## 🔧 Configuração Local

### Pré-requisitos

- Node.js 18+ e pnpm
- Python 3.11+
- Chave da Google Places API

### 1. Obter Chave da Google Places API

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a **Google Places API**
4. Vá em **Credenciais** > **Criar Credenciais** > **Chave de API**
5. Copie a chave gerada

### 2. Configurar Variáveis de Ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua chave
GOOGLE_API_KEY=sua_chave_aqui
```

### 3. Instalar Dependências

**Backend:**
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
pnpm install
```

## 🚀 Executar Localmente

### 1. Iniciar Backend (Terminal 1)

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Exportar variável de ambiente
export GOOGLE_API_KEY=sua_chave_aqui

# Iniciar servidor Flask
cd api
python search.py
```

O backend estará disponível em: `http://localhost:5000`

### 2. Iniciar Frontend (Terminal 2)

```bash
cd frontend
pnpm run dev
```

O frontend estará disponível em: `http://localhost:5173`

## 🧪 Testar a API

### Health Check
```bash
curl http://localhost:5000/api/health
```

### Buscar Empresas
```bash
curl "http://localhost:5000/api/search?city=Ijuí, RS"
```

## 📱 Como Usar a Aplicação

1. **Acesse a aplicação** no navegador
2. **Digite o nome da cidade** (ex: "São Paulo, SP")
3. **Clique em "Buscar"** para encontrar empresas
4. **Use o filtro** para ver apenas empresas não cadastradas
5. **Exporte os resultados** em CSV para análise

## 🌐 Deploy em Produção

### Backend Deployado

O backend já está disponível em produção:
- **URL**: https://8xhpiqcvjzkg.manus.space
- **Health Check**: https://8xhpiqcvjzkg.manus.space/api/health
- **Endpoint de Busca**: https://8xhpiqcvjzkg.manus.space/api/search?city=CIDADE

### Deploy do Frontend

O frontend está preparado para deploy. Para publicar:

1. O build já foi gerado em `frontend/dist/`
2. Configure a variável de ambiente `GOOGLE_API_KEY` no painel de deploy
3. O frontend usará automaticamente a API em produção

### Variáveis de Ambiente em Produção

Configure no painel de deploy:
```
GOOGLE_API_KEY=sua_chave_da_google_places_api
```

## 📊 Endpoints da API

### GET /api/health
Verifica se a API está funcionando.

**Resposta:**
```json
{
  "status": "OK",
  "message": "API funcionando corretamente"
}
```

### GET /api/search?city=CIDADE
Busca empresas em uma cidade específica.

**Parâmetros:**
- `city` (obrigatório): Nome da cidade

**Resposta:**
```json
{
  "success": true,
  "businesses": [
    {
      "name": "Nome da Empresa",
      "address": "Endereço completo",
      "phone": "Telefone ou 'Não disponível'",
      "place_id": "ID único do Google Places",
      "is_on_maps": true
    }
  ],
  "total": 20
}
```

## 🔒 Segurança

- **CORS habilitado** para todas as origens
- **Validação de parâmetros** obrigatórios
- **Tratamento de erros** robusto
- **Rate limiting** da Google Places API

## 🐛 Solução de Problemas

### Erro "GOOGLE_API_KEY não configurada"
- Verifique se a variável de ambiente está definida
- Confirme se a chave da API está correta

### Erro "Erro ao consultar Google Places API"
- Verifique se a Google Places API está ativada
- Confirme se há créditos disponíveis na conta Google Cloud
- Verifique se a chave tem permissões para Places API

### Frontend não conecta com backend
- Confirme se o backend está rodando na porta correta
- Verifique se não há bloqueio de CORS
- Teste a API diretamente com curl

## 📈 Melhorias Futuras

- [ ] Cache de resultados para otimizar performance
- [ ] Paginação para grandes volumes de dados
- [ ] Filtros avançados (categoria, avaliação, etc.)
- [ ] Integração com outras APIs de dados empresariais
- [ ] Dashboard com métricas e analytics
- [ ] Sistema de autenticação e usuários
- [ ] Notificações por email dos resultados

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, abra uma issue no repositório ou entre em contato.

---

**Desenvolvido com ❤️ para facilitar a prospecção de empresas locais**

