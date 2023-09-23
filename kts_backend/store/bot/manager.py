import typing
from logging import getLogger

from kts_backend.store.vk_api.dataclasses import Message, Update

if typing.TYPE_CHECKING:
    from kts_backend.web.app import Application


class BotManager:
    def __init__(self, app: "Application"):
        self.app = app
        self.bot = None
        self.logger = getLogger("handler")

    async def handle_updates(self, updates: list[Update]):
        for update in updates:
            self.logger.info(f'Sending message {update.object.body}')
            await self.app.store.vk_api.send_message(
                Message(
                    user_id=update.object.user_id,
                    text=update.object.body,
                )
            )
            self.logger.info(f'Message {update.object.id} sendback')