
from solana.keypair import Keypair

def load_keypair():
    # Load your private key securely (e.g., from environment variable or file)
    private_key = [1, 2, 3, ...]  # Replace with your actual private key
    keypair = Keypair.from_secret_key(bytes(private_key))
    return keypair
