from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class AuthForm:
    def __init__(
        self,
        username: str = Form(title="username", default=None),
        password: str = Form(title="password", default=None)
    ):
        self.username = username
        self.password = password

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.post("/signin")
def login_to_account(form_data: AuthForm = Depends()):
    response = {"username": form_data.username, "password": form_data.password}
    print(response)
    return response
