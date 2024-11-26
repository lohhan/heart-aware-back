import pytest
import json
from django.test import AsyncClient

@pytest.mark.asyncio
async def test_nova_previsao_valid_input(sample_payload):
    client = AsyncClient()  
    response = await client.post(
        "/api/previsao/nova-previsao",
        data=json.dumps(sample_payload),  
        content_type="application/json",  
    )
    assert response.status_code == 200
    assert "risco" in response.json()

@pytest.mark.asyncio
async def test_nova_previsao_missing_fields(sample_payload_missing):
    client = AsyncClient()
    response = await client.post(
        "/api/previsao/nova-previsao",
        data=json.dumps(sample_payload_missing),
        content_type="application/json",
    )
    assert response.status_code == 422  

@pytest.mark.asyncio
async def test_nova_previsao_invalid_data_types(sample_payload_invalid):
   client = AsyncClient()
   response = await client.post(
      "/api/previsao/nova-previsao",
      data=json.dumps(sample_payload_invalid),
      content_type="application/json",
   )
   assert "detail" in response.json()  


@pytest.fixture
def sample_payload():
   return {
      "age": "45",
      "sexo": "1",
      "dor_peito": "3",
      "pressao_arterial": "120",
      "colesterol": "240",
      "acucar": "0",
      "eletro": "1",
      "freq_max": "150",
      "angina": "0",
      "vasos": "0",
   }

@pytest.fixture
def sample_payload_missing():
   return {
      "age": "45",
      "sexo": "1",
      "dor_peito": "3",
      "pressao_arterial": "120",
      "colesterol": "240",
      "acucar": "0",
      "eletro": "1",
      "freq_max": "150",
      "angina": "0",
   }

@pytest.fixture
def sample_payload_invalid():
   return {
      "age": "forty-five", 
      "sexo": "1",
      "dor_peito": "3",
      "pressao_arterial": "120",
      "colesterol": "240",
      "acucar": "0",
      "eletro": "1",
      "freq_max": "150",
      "angina": "0",
      "vasos": "0",
   }
