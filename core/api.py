from ninja import NinjaAPI
from previsao.api import router

api = NinjaAPI()

api.add_router("/previsao/", router)
