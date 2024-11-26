from ninja import Router
from .schema import HeartInputs
import pandas as pd
import pickle
from django.http import JsonResponse

router = Router()

try:
   with open("modelo_random_forest.pkl", "rb") as file:
      model, model_columns = pickle.load(file)
except FileNotFoundError:
   raise Exception("Modelo de previsão não encontrado.")
except Exception as e:
   raise Exception(f"Ocorreu um erro ao carregar o modelo: {e}")

def preprocess_input(data):
   df = pd.DataFrame(data, index=[0])  
   
   for col in model_columns:
      if col not in df.columns:
         df[col] = 0

   return df

def validate_payload(payload):
   required_fields = [
      "age", "sexo", "dor_peito", "pressao_arterial", "colesterol", 
      "acucar", "eletro", "freq_max", "angina", "vasos"
   ]
   
   for field in required_fields:
      if not hasattr(payload, field):
         raise JsonResponse({"detail": f"Campo {field} é obrigatório."}, status=400)
      
   try:
      int(payload.age)
      int(payload.sexo)
      int(payload.dor_peito)
      int(payload.pressao_arterial)
      int(payload.colesterol)
      int(payload.acucar)
      int(payload.eletro)
      int(payload.freq_max)
      int(payload.angina)
      int(payload.vasos)
   except ValueError:
      raise JsonResponse({"detail": "Todos os campos devem ser numéricos."}, status=400)

@router.post("/nova-previsao")
async def nova_previsao(request, payload: HeartInputs):
   try:
      validate_payload(payload)
      
      dados_dict = {
         "idade": payload.age,
         "sexo": payload.sexo,
         "dor_no_peito": payload.dor_peito,
         "pressao_arterial": payload.pressao_arterial,
         "nivel_colesterol": payload.colesterol,
         "acucar_no_sangue": payload.acucar,
         "resultado_eletrocardiograma": payload.eletro,
         "frequencia_cardiaca_maxima": payload.freq_max,
         "angina_induzida_por_exercicio": payload.angina,
         "vasos_afetados": payload.vasos,
      }
      
      processed_data = preprocess_input(dados_dict)
      
      prediction = model.predict(processed_data)

      return JsonResponse({"risco": str(prediction[0])})

   except Exception as e:
      return JsonResponse({"detail": f"Ocorreu um erro ao processar a previsão: {e}"}, status=500)
