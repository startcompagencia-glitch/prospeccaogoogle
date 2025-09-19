#!/usr/bin/env python3
"""
Script de teste para a API de Prospecção de Empresas
"""

import requests
import json
import sys

def test_health_check(base_url):
    """Testa o endpoint de health check"""
    print("🔍 Testando Health Check...")
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health Check OK: {data['message']}")
            return True
        else:
            print(f"❌ Health Check falhou: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro no Health Check: {e}")
        return False

def test_search_api(base_url, city):
    """Testa o endpoint de busca"""
    print(f"🔍 Testando busca para: {city}")
    try:
        response = requests.get(f"{base_url}/api/search", params={"city": city})
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                businesses = data.get('businesses', [])
                total = data.get('total', 0)
                print(f"✅ Busca OK: {total} empresas encontradas")
                
                # Mostrar primeiras 3 empresas
                for i, business in enumerate(businesses[:3]):
                    print(f"  {i+1}. {business['name']}")
                    print(f"     📍 {business['address'][:50]}...")
                    print(f"     📞 {business['phone']}")
                    print(f"     🗺️  {'No Maps' if business['is_on_maps'] else 'Não cadastrada'}")
                    print()
                
                return True
            else:
                print(f"❌ Busca falhou: {data}")
                return False
        else:
            print(f"❌ Busca falhou: {response.status_code}")
            print(f"Resposta: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Erro na busca: {e}")
        return False

def main():
    """Função principal"""
    # URLs para teste
    local_url = "http://localhost:5000"
    prod_url = "https://8xhpiqcvjzkg.manus.space"
    
    # Cidade para teste
    test_city = "São Paulo, SP"
    
    if len(sys.argv) > 1:
        test_city = sys.argv[1]
    
    print("🚀 Iniciando testes da API de Prospecção de Empresas")
    print("=" * 60)
    
    # Testar ambiente local
    print("\n📍 Testando ambiente LOCAL:")
    local_health = test_health_check(local_url)
    if local_health:
        test_search_api(local_url, test_city)
    
    # Testar ambiente de produção
    print("\n🌐 Testando ambiente de PRODUÇÃO:")
    prod_health = test_health_check(prod_url)
    if prod_health:
        test_search_api(prod_url, test_city)
    
    print("\n" + "=" * 60)
    print("✨ Testes concluídos!")

if __name__ == "__main__":
    main()

