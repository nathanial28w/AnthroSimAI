
from solana.rpc.async_api import AsyncClient

async def connect_to_solana():
    client = AsyncClient("https://api.mainnet-beta.solana.com")  # Replace with your desired network
    return client
