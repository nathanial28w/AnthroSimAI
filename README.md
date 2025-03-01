

# AnthroSimAI: Bridging AI and Anthropology to Simulate the Story of Humanity.

<p align="center" width="100%">
<img src="cover.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>
AnthroSimAI is an innovative simulation platform that blends advanced artificial intelligence with anthropological research to model, analyze, and predict human behavior, cultural dynamics, and societal evolution. 
By leveraging cutting-edge machine learning and simulation techniques, AnthroSimAI provides researchers, educators, and policymakers with powerful tools to explore complex human systems, foster understanding, and drive data-informed decision-making.
Below, we document the steps for setting up the simulation environment on your local machine and for replaying the simulation as a demo animation.


Interactive applications can benefit greatly from realistic proxies of human behavior, enabling experiences such as immersive environments, interpersonal communication rehearsal tools, and prototyping systems. In this work, we present generative agents—computational software entities designed to mimic believable human behaviors. These agents perform daily activities such as waking up, cooking breakfast, and going to work; artists create art, authors write stories, and agents engage in social interactions, forming opinions, noticing each other, initiating conversations, and reflecting on past experiences while planning for the future.

To enable generative agents, we propose an architecture that integrates a large language model with mechanisms for storing a comprehensive record of the agent’s experiences in natural language. These records are synthesized over time into higher-level reflections and dynamically retrieved to inform behavior planning. We implemented generative agents in an interactive sandbox environment inspired by The Sims, allowing users to interact with a simulated small town of 25 agents using natural language.

Our evaluation demonstrates that generative agents exhibit believable individual and emergent social behaviors. For instance, starting with a single user-defined goal—one agent planning to host a Valentine's Day party—the agents autonomously spread invitations, form new relationships, ask each other out on dates, and coordinate to attend the party together at the appropriate time. Ablation studies highlight the critical role of key architectural components, including observation, planning, and reflection, in achieving believable behavior.

By combining large language models with computational, interactive agents, this work introduces novel architectural and interaction paradigms for simulating human-like behavior in interactive applications.

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Isabella_Rodriguez.png" alt="Generative Isabella">   Setting Up the Environment 
To set up your environment, you will need to generate a `utils.py` file that contains your OpenAI API key and download the necessary packages.

### Step 1. Generate Utils File
In the `reverie/backend_server` folder (where `reverie.py` is located), create a new file titled `utils.py` and copy and paste the content below into the file:
```
# Copy and paste your OpenAI API Key
openai_api_key = "<Your OpenAI API>"
# Put your name
key_owner = "<Name>"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True
```
Replace `<Your OpenAI API>` with your OpenAI API key, and `<name>` with your name.
 
### Step 2. Install requirements.txt
Install everything listed in the `requirements.txt` file (I strongly recommend first setting up a virtualenv as usual). A note on Python version: we tested our environment on Python 3.9.12. 

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Klaus_Mueller.png" alt="Generative Klaus">   Running a Simulation 
To run a new simulation, you will need to concurrently start two servers: the environment server and the agent simulation server.

### Step 1. Starting the Environment Server
Again, the environment is implemented as a Django project, and as such, you will need to start the Django server. To do this, first navigate to `environment/frontend_server` (this is where `manage.py` is located) in your command line. Then run the following command:

    python manage.py runserver

Then, on your favorite browser, go to [http://localhost:8000/](http://localhost:8000/). If you see a message that says, "Your environment server is up and running," your server is running properly. Ensure that the environment server continues to run while you are running the simulation, so keep this command-line tab open! (Note: I recommend using either Chrome or Safari. Firefox might produce some frontend glitches, although it should not interfere with the actual simulation.)

### Step 2. Starting the Simulation Server
Open up another command line (the one you used in Step 1 should still be running the environment server, so leave that as it is). Navigate to `reverie/backend_server` and run `reverie.py`.

    python reverie.py
This will start the simulation server. A command-line prompt will appear, asking the following: "Enter the name of the forked simulation: ". To start a 3-agent simulation with Isabella Rodriguez, Maria Lopez, and Klaus Mueller, type the following:
    
    base_the_ville_isabella_maria_klaus
The prompt will then ask, "Enter the name of the new simulation: ". Type any name to denote your current simulation (e.g., just "test-simulation" will do for now).

    test-simulation
Keep the simulator server running. At this stage, it will display the following prompt: "Enter option: "

### Step 3. Running and Saving the Simulation
On your browser, navigate to [http://localhost:8000/simulator_home](http://localhost:8000/simulator_home). You should see the map of Smallville, along with a list of active agents on the map. You can move around the map using your keyboard arrows. Please keep this tab open. To run the simulation, type the following command in your simulation server in response to the prompt, "Enter option":

    run <step-count>
Note that you will want to replace `<step-count>` above with an integer indicating the number of game steps you want to simulate. For instance, if you want to simulate 100 game steps, you should input `run 100`. One game step represents 10 seconds in the game.


Your simulation should be running, and you will see the agents moving on the map in your browser. Once the simulation finishes running, the "Enter option" prompt will re-appear. At this point, you can simulate more steps by re-entering the run command with your desired game steps, exit the simulation without saving by typing `exit`, or save and exit by typing `fin`.

The saved simulation can be accessed the next time you run the simulation server by providing the name of your simulation as the forked simulation. This will allow you to restart your simulation from the point where you left off.

### Step 4. Replaying a Simulation
You can replay a simulation that you have already run simply by having your environment server running and navigating to the following address in your browser: `http://localhost:8000/replay/<simulation-name>/<starting-time-step>`. Please make sure to replace `<simulation-name>` with the name of the simulation you want to replay, and `<starting-time-step>` with the integer time-step from which you wish to start the replay.

For instance, by visiting the following link, you will initiate a pre-simulated example, starting at time-step 1:  
[http://localhost:8000/replay/July1_the_ville_isabella_maria_klaus-step-3-20/1/](http://localhost:8000/replay/July1_the_ville_isabella_maria_klaus-step-3-20/1/)

### Step 5. Demoing a Simulation
You may have noticed that all character sprites in the replay look identical. We would like to clarify that the replay function is primarily intended for debugging purposes and does not prioritize optimizing the size of the simulation folder or the visuals. To properly demonstrate a simulation with appropriate character sprites, you will need to compress the simulation first. To do this, open the `compress_sim_storage.py` file located in the `reverie` directory using a text editor. Then, execute the `compress` function with the name of the target simulation as its input. By doing so, the simulation file will be compressed, making it ready for demonstration.

To start the demo, go to the following address on your browser: `http://localhost:8000/demo/<simulation-name>/<starting-time-step>/<simulation-speed>`. Note that `<simulation-name>` and `<starting-time-step>` denote the same things as mentioned above. `<simulation-speed>` can be set to control the demo speed, where 1 is the slowest, and 5 is the fastest. For instance, visiting the following link will start a pre-simulated example, beginning at time-step 1, with a medium demo speed:  
[http://localhost:8000/demo/July1_the_ville_isabella_maria_klaus-step-3-20/1/3/](http://localhost:8000/demo/July1_the_ville_isabella_maria_klaus-step-3-20/1/3/)

### Tips
We've noticed that OpenAI's API can hang when it reaches the hourly rate limit. When this happens, you may need to restart your simulation. For now, we recommend saving your simulation often as you progress to ensure that you lose as little of the simulation as possible when you do need to stop and rerun it. 

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Maria_Lopez.png" alt="Generative Maria">   Simulation Storage Location
All simulations that you save will be located in `environment/frontend_server/storage`, and all compressed demos will be located in `environment/frontend_server/compressed_storage`. 

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Sam_Moore.png" alt="Generative Sam">   Customization

There are two ways to optionally customize your simulations. 

### Author and Load Agent History
First is to initialize agents with unique history at the start of the simulation. To do this, you would want to 1) start your simulation using one of the base simulations, and 2) author and load agent history. More specifically, here are the steps:

#### Step 1. Starting Up a Base Simulation 
There are two base simulations included in the repository: `base_the_ville_n25` with 25 agents, and `base_the_ville_isabella_maria_klaus` with 3 agents. Load one of the base simulations by following the steps until step 2 above. 

#### Step 2. Loading a History File 
Then, when prompted with "Enter option: ", you should load the agent history by responding with the following command:

    call -- load history the_ville/<history_file_name>.csv
Note that you will need to replace `<history_file_name>` with the name of an existing history file. There are two history files included in the repo as examples: `agent_history_init_n25.csv` for `base_the_ville_n25` and `agent_history_init_n3.csv` for `base_the_ville_isabella_maria_klaus`. These files include semicolon-separated lists of memory records for each of the agents—loading them will insert the memory records into the agents' memory stream.

#### Step 3. Further Customization 
To customize the initialization by authoring your own history file, place your file in the following folder: `environment/frontend_server/static_dirs/assets/the_ville`. The column format for your custom history file will have to match the example history files included. Therefore, we recommend starting the process by copying and pasting the ones that are already in the repository.

### Create New Base Simulations
For a more involved customization, you will need to author your own base simulation files. The most straightforward approach would be to copy and paste an existing base simulation folder, renaming and editing it according to your requirements. This process will be simpler if you decide to keep the agent names unchanged. However, if you wish to change their names or increase the number of agents that the Smallville map can accommodate, you might need to directly edit the map using the [Tiled](https://www.mapeditor.org/) map editor.

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Klaus_Mueller.png" alt="Generative Klaus">   Solana Integration Setup

Step 1. Install Required Dependencies

Ensure you have the following Python packages installed:

pip install solana spl-token async-solana

Step 2. Connect to Solana

Create a Python file named connect_to_solana.py and use the following code to establish a connection to the Solana cluster:

from solana.rpc.async_api import AsyncClient

async def connect_to_solana():
    client = AsyncClient("https://api.mainnet-beta.solana.com")  # Replace with your desired network
    return client
Step 3. Manage Wallet Keys

Create another file named wallet_management.py for securely managing your wallet:

from solana.keypair import Keypair

def load_keypair():
    # Load your private key securely (e.g., from environment variable or file)
    private_key = [1, 2, 3, ...]  # Replace with your actual private key
    keypair = Keypair.from_secret_key(bytes(private_key))
    return keypair
    
Step 4. Token Operations

For token creation, transfer, and balance fetching, create a file token_operations.py with the following code:

from spl.token.async_client import AsyncToken
from solana.publickey import PublicKey

async def create_token(client, payer_keypair):
    mint_authority = payer_keypair.public_key
    decimals = 6  # Adjust as needed

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

Step 5. AI Agent Integration

Integrate Solana functionality into your AI agents. Create a file ai_agent.py with the following:

async def ai_agent_decision(client, token, wallet, target_wallet, amount):
    balance = await token.get_balance(wallet.public_key)
    if balance['result']['value'] > amount:
        print("Balance sufficient. Proceeding with transfer.")
        await transfer_tokens(client, token, wallet.public_key, target_wallet, amount, wallet)
    else:
        print("Insufficient balance. Skipping transfer.")

Step 6. Main Script

Create a main.py to tie it all together:

import asyncio
from connect_to_solana import connect_to_solana
from wallet_management import load_keypair
from token_operations import AsyncToken, PublicKey, transfer_tokens
from ai_agent import ai_agent_decision

async def main():
    client = await connect_to_solana()
    wallet = load_keypair()

    token_mint_address = PublicKey("YourTokenMintAddress")
    token = AsyncToken(client, token_mint_address, wallet.public_key, wallet)

    target_wallet = PublicKey("TargetWalletAddress")
    await ai_agent_decision(client, token, wallet, target_wallet, 1000)  # Example call

if __name__ == "__main__":
    asyncio.run(main())

Additional Notes

Replace placeholders like YourTokenMintAddress and TargetWalletAddress with actual values.

Use a secure method to manage and load private keys.

Ensure sufficient SOL balance for transaction fees.

## <img src="https://joonsungpark.s3.amazonaws.com:443/static/assets/characters/profile/Eddy_Lin.png" alt="Generative Eddy">   Original Authors and Citation 

**A big thank you to the original Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein

```
@inproceedings{Park2024GenerativeAgents,  
author = {Park, Joon Sung and O'Brien, Joseph C. and Cai, Carrie J. and Morris, Meredith Ringel and Liang, Percy and Bernstein, Michael S.},  
title = {Generative Agents: Interactive Simulacra of Human Behavior},  
year = {2024},  
publisher = {Association for Computing Machinery},  
address = {New York, NY, USA},  
booktitle = {In the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '24)},  
keywords = {Human-AI interaction, agents, generative AI, large language models},  
location = {San Francisco, CA, USA},  
series = {UIST '24}
}
```




