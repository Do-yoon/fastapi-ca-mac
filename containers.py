from fastapi import BackgroundTasks
from user.application.email_service import EmailService
from dependency_injector import containers, providers
from user.infra.repository.user_repo import UserRepository
from note.infra.repository.note_repo import NoteRepository
from user.application.user_service import UserService
from note.application.note_service import NoteService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["user"],
    )
 
    user_repo = providers.Factory(UserRepository)
    user_service = providers.Factory(UserService, user_repo=user_repo)
    note_repo = providers.Factory(NoteRepository)
    note_service = providers.Factory(NoteService, note_repo=note_repo)  
    email_service = providers.Factory(EmailService)
    user_service = providers.Factory(
        UserService,
        user_repo=user_repo,
        email_service=email_service
    )
