
from spl.token.async_client import AsyncToken
from solana.publickey import PublicKey

async def create_token(client, payer_keypair):
    # Define token parameters
    mint_authority = payer_keypair.public_key
    decimals = 6  # Adjust as needed

    # Create the token
    token = await AsyncToken.create_mint(
        client,
        payer_keypair,
        mint_authority,
        freeze_authority=None,
        decimals=decimals,
    )
    print(f"Token Mint Address: {token.pubkey}")
    return token

async def transfer_tokens(client, token, source, destination, amount, payer):
    tx = await token.transfer(
        source=source,
        dest=destination,
        owner=payer,
        amount=amount,
    )
    print(f"Transaction Signature: {tx}")

async def get_token_balance(client, token, owner):
    balance = await token.get_balance(owner)
    print(f"Token Balance: {balance['result']['value']} tokens")
