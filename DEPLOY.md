# 🚀 Instruções de Deploy

## Status Atual do Deploy

### ✅ Backend Deployado
- **URL**: https://8xhpiqcvjzkg.manus.space
- **Status**: Funcionando (precisa configurar GOOGLE_API_KEY)
- **Health Check**: https://8xhpiqcvjzkg.manus.space/api/health

### ⏳ Frontend Preparado
- Build gerado em `frontend/dist/`
- Configurado para usar API de produção
- Pronto para publicação

## 🔧 Configuração Necessária

### 1. Configurar Variável de Ambiente no Backend

No painel de deploy do backend, configure:
```
GOOGLE_API_KEY=sua_chave_da_google_places_api
```

### 2. Publicar Frontend

O frontend está preparado para deploy. Para publicar:
1. Acesse o painel de deploy
2. Clique no botão "Publish" 
3. O frontend será publicado automaticamente

## 🧪 Testar Deploy

### Testar Backend
```bash
# Health check
curl https://8xhpiqcvjzkg.manus.space/api/health

# Buscar empresas (após configurar GOOGLE_API_KEY)
curl "https://8xhpiqcvjzkg.manus.space/api/search?city=São Paulo, SP"
```

### Usar Script de Teste
```bash
python3 test_api.py "Sua Cidade"
```

## 📋 Checklist de Deploy

- [x] Backend deployado
- [x] Frontend buildado
- [ ] GOOGLE_API_KEY configurada no backend
- [ ] Frontend publicado
- [ ] Teste end-to-end funcionando

## 🔗 URLs Finais

Após completar o deploy:

- **Frontend**: [URL será gerada após publicação]
- **Backend**: https://8xhpiqcvjzkg.manus.space
- **API Docs**: Veja README.md para endpoints

## 🆘 Solução de Problemas

### Backend retorna "GOOGLE_API_KEY não configurada"
1. Acesse o painel de deploy do backend
2. Configure a variável de ambiente `GOOGLE_API_KEY`
3. Reinicie o serviço se necessário

### Frontend não conecta com backend
1. Verifique se a URL da API está correta no código
2. Confirme se o backend está respondendo
3. Verifique configurações de CORS

### Erro 500 na API
1. Verifique logs do backend
2. Confirme se a chave da Google Places API é válida
3. Verifique se há créditos disponíveis na conta Google Cloud

## 📞 Suporte

Para problemas de deploy, verifique:
1. Logs do serviço
2. Configurações de variáveis de ambiente
3. Status dos serviços externos (Google Places API)

---

**Projeto pronto para uso em produção! 🎉**

