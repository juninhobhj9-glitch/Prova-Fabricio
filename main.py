import asyncio
from database import db


async def main():
    try:
        resposta = await db.command("ping")
        print("Conectado ao MongoDB:", resposta)
        print("Banco usado:", db.name)
        colecoes = await db.list_collection_names()
        print("Collections encontradas:", colecoes)
    except Exception as e:
        print("Erro ao conectar:", e)


if __name__ == "__main__":
    asyncio.run(main())
