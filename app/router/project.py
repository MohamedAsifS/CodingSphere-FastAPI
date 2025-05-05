from fastapi import APIRouter,Depends,status ,HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import database
from ..schema import project_schema,token_schema
from ..auth import OAuth2
from ..repository import project_repo


router=APIRouter(
    prefix='/project',
    tags=['Project']
)



@router.get('/',status_code=status.HTTP_200_OK,response_model=List[project_schema.ProjectShow])
def get_all_projects(db:Session=Depends(database.get_db),current_user:token_schema.Token=Depends(OAuth2.get_current_user)):
    return project_repo.get_all(db)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_project(request:project_schema.ProjectBase,db:Session=Depends(database.get_db),current_user:token_schema.Token=Depends(OAuth2.get_current_user)):
    print(current_user)
    if current_user.role =='admin':
        return project_repo.create(request,db)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not authorized to perform this action")
    
    
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(request:project_schema.ProjectBase,id:int,db:Session=Depends(database.get_db),current_user:token_schema.Token=Depends(OAuth2.get_current_user)):
    if(current_user.role=='admin'):
        return project_repo.update(request,id,db)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not authorized to perform this action")
    
@router.delete('/{id}',status_code=status.HTTP_200_OK)
def delete(id:int,db:Session=Depends(database.get_db),current_user:token_schema.Token=Depends(OAuth2.get_current_user)):
    if current_user.role=='admin':
        return project_repo.delete(id,db)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not authorized to perform this action")