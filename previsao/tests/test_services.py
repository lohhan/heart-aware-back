import pandas as pd
import pytest
from ..api import preprocess_input

def test_preprocess_input():
    input_data = {
         "idade": 45,
         "sexo": 1,
         "dor_no_peito": 3,
         "pressao_arterial": 120,
         "nivel_colesterol": 0,
         "acucar_no_sangue": 0,
         "resultado_eletrocardiograma": 2,
         "frequencia_cardiaca_maxima": 120,
         "angina_induzida_por_exercicio": 1,
         "vasos_afetados": 1,
      } 

    expected_df = pd.DataFrame([{
        "idade": 45,
         "sexo": 1,
         "dor_no_peito": 3,
         "pressao_arterial": 120,
         "nivel_colesterol": 0,
         "acucar_no_sangue": 0,
         "resultado_eletrocardiograma": 2,
         "frequencia_cardiaca_maxima": 120,
         "angina_induzida_por_exercicio": 1,
         "vasos_afetados": 1,
    }])

    result = preprocess_input(input_data)

    pd.testing.assert_frame_equal(result, expected_df)
