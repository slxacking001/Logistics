# Setting FastAPI Environment

## Step1:
Create your project folder manually or used cmd

```
mkdir my_fastapi_project
```

## Step2:
Open CMD/Terminal inside the folder or cd into the folder

```
cd my_fastapi_project
```

## Step3:
Create virtual environment

```
python -m venv .venv 
```

## Step4: 

Activate enviroment

### For windows

```
env\Scripts\activate
```

### macOS/Linux:

```
source .venv/bin/activate
```

## Step5: 

Install FastAPI and Uvicorn

```
pip install fastapi uvicorn
```

## Step6:

Create folders in this structure

```
my_fastapi_project/
│
├── app/
│   ├── __init__.py
│   └── routes/
│   |   └── __init__.py
|   ├── models/
│   |   └── __init__.py
|   ├── schema/
│       └── __init__.py
├── main.py
├── requirements.txt
└── README.md
```


Add folders and structures accordingly as you move

## Step7: 

 Stage 1: Core Fundamentals

Aim: To help them confidently build simple, clean APIs.
Topic	What to Cover

```
✅ Path & Query Parameters	/items/{id}, ?limit=10
✅ Request Body	POST/PUT with Pydantic models
✅ Response Models	Returning structured JSON using response_model=
✅ Status Codes	Using status_code=201, handling 404s
✅ Tags and Metadata	For Swagger docs, grouping endpoints
✅ Error Handling	HTTPException, custom exceptions
✅ Dependency Injection	Depends(), common logic (e.g., auth checks)
```

# Creating Database and Models

With your Virtual enviroment activated run

```
pip install sqlalchemy psycopg2-binary alembic

```
Add installed models to `requirements.txt`

```
pip freeze > requirements.txt
```

##  Configure SQLAlchemy and Database Connection
Create file ```database.py``` inside app/ folder

paste the following

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://username:password@localhost:5432/your_db_name"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

## Create Your First Database Model
inside `app/models/user.py` create `user.py` if not existing and paste the following inside

```
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
```

Then import the created model in `app/models/__init__.py` like this:

```
from app.models.users import User

```

## Initialize Alembic

In the virtual enviroment, run alembic initialization in the terminal:

```
alembic init alembic

```

This creates an `alembic/` folder and `alembic.ini` in your root folder.

## Configure Alembic
Open `alembic.ini`

Find this line:

`sqlalchemy.url = driver://user:pass@localhost/dbname`

Replace it with your actual DB URL:

`sqlalchemy.url = postgresql://username:password@localhost:5432/your_db_name`
we will create an autual database later on


Then open `alembic/env.py` dont modify anything just paste the following at the top before `config = context.config` to import your Base:

```
from app.database import Base
from app import models

target_metadata = Base.metadata
```

## Set up Postgres Database on your pc



## Create and Apply Migration

Create initial migration:

```
alembic revision --autogenerate -m "create users table"
```

You’ll see output about the detected changes.

## Apply the migration:

```
alembic upgrade head
```

Your users table should now be created in the DB 🎉