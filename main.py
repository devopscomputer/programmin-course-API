import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import engine
from app.models.course import Course  # Importando apenas Course
from app.models.user import User
from app.models.assessment import Assessment
from app.routes import course, user, module, assessment
from config import settings  # Importação correta

# Criação da aplicação FastAPI
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas
app.include_router(course.router, prefix="/api/courses", tags=["courses"])
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(module.router, prefix="/api/modules", tags=["modules"])
app.include_router(assessment.router, prefix="/api/assessments", tags=["assessments"])

# Inicialização do banco de dados
@app.on_event("startup")
def startup_event():
    import app.database.db as db
    db.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Cursos de Tecnologia Online"}

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)