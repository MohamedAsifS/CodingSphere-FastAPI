from fastapi import HTTPException,status 
from ..models import project_model
from sqlalchemy.orm import Session
from ..schema import project_schema 

def create(request:project_schema.ProjectBase,db:Session):
    new_project=project_model.Project(name=request.name,description=request.description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
def get_all(db:Session):
    projects=db.query(project_model.Project).all()
    return projects

def update(request:project_schema.ProjectBase,id:int,db:Session):
    project=db.query(project_model.Project).filter(project_model.Project.id==id)
    if project.first():
        project.update(request.dict())
        db.commit()
        return {"created":f"Project updated successfully  - {project.first().id}"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Project not found")
    
def delete(id:int,db:Session):
    project=db.query(project_model.Project).filter(project_model.Project.id==id)
    if project.first():
        project.delete(synchronize_session=False)
        db.commit()
        return {"deleted":f"Project deleted successfully - {id}"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Project not found")