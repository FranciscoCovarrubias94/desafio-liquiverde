from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "app.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def init_db():
    from app.models import Product
    SQLModel.metadata.create_all(engine)
    print("Base de datos inicializada correctamente.")

# Esta es necesaria para los Depends en FastAPI
def get_session():
    with Session(engine) as session:
        yield session

if __name__ == "__main__":
    init_db()
