from ninja import Router
from .schema import HeartInputs
import sklearn
import pandas as pd
import pickle

router = Router()

with open("modelo_random_forest.pkl", "rb") as file:
   model, model_columns = pickle.load(file)

def preprocess_input(data):
   df = pd.DataFrame(data, index=[0])  
   
   for col in model_columns:
      if col not in df.columns:
         df[col] = 0

   return df

@router.post("/nova-previsao")
async def nova_previsao(request, payload: HeartInputs):
   try: 
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

      return {"risco": f"{prediction}"}

   except Exception as e:
      return f"Ocorreu um erro: {e}"

   