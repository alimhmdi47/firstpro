from fastapi import FastAPI

import book
import users,customer,author


app = FastAPI()

"""app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""


@app.get("/")
def welcome():
    return "welcome"

app.include_router(users.router)
app.include_router(customer.router)
app.include_router(author.router)
app.include_router(book.router)


