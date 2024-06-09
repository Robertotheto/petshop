from src.server.server import create_app
from src.models.users import Users
from src.models.token_block_list import TokenBlockList
from src.models.pets import Pets

app = create_app()

if __name__ == '__main__':
    print("Running app")
    app.run()
