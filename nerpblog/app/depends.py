from fastapi import Depends
from typing import Annotated
from nerpblog.app.uow import UnitOfWork, AbsUnitOfWork

uowdep = Annotated[AbsUnitOfWork, Depends(UnitOfWork)]

