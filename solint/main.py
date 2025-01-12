
import asyncio
from connect_to_solana import connect_to_solana
from wallet_management import load_keypair
from token_operations import AsyncToken, PublicKey, transfer_tokens
from ai_agent import ai_agent_decision

async def main():
    client = await connect_to_solana()
    wallet = load_keypair()

    # Token example (replace with an existing token mint address)
    token_mint_address = PublicKey("YourTokenMintAddress")
    token = AsyncToken(client, token_mint_address, wallet.public_key, wallet)

    target_wallet = PublicKey("TargetWalletAddress")
    await ai_agent_decision(client, token, wallet, target_wallet, 1000)  # Example call

if __name__ == "__main__":
    asyncio.run(main())
