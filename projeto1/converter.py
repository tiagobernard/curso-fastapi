import requests
from os import getenv
from fastapi import HTTPException
import aiohttp

from dotenv import load_dotenv
load_dotenv()

ALPHAVANTAGE_API_KEY = getenv("ALPHAVANTAGE_API_KEY")

def sync_converter(from_currency: str, to_currency: str, price: float):
    url = (
        f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_API_KEY}'
    )

    try:
        response = requests.get(url=url)
        response.raise_for_status()
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"Erro ao fazer requisição: {error}")
    
    data = response.json()

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Erro ao obter taxa de câmbio da API.")

    try:
        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    except (KeyError, ValueError) as error:
        raise HTTPException(status_code=500, detail=f"Erro ao processar taxa de câmbio: {error}")

    return price * exchange_rate

    #----------VERSÃO ASSINCRONA-----------

async def async_converter(from_currency: str, to_currency: str, price: float):
    url = (
        f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
        f'&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_API_KEY}'
    )

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                if response.status != 200:
                    raise HTTPException(status_code=400, detail=f"Erro HTTP: {response.status}")
                data = await response.json()
                print(data)

    except Exception as error:
        raise HTTPException(status_code=400, detail=f"Erro ao fazer requisição: {error}")

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(
            status_code=400,
            detail=f"Erro ao obter taxa de câmbio da API. - {data}")

    try:
            exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    except (KeyError, ValueError) as error:
        raise HTTPException(status_code=500, detail=f"Erro ao processar taxa de câmbio: {error}")

    return {to_currency: price * exchange_rate}
