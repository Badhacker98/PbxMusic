from pyrogram import Client

from config import Config
from Music.utils.exceptions import PbxBotException

from .logger import LOGS


class PbxClient(Client):
    def __init__(self):
        self.app = Client(
            "PbxMusic",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=100,
        )

        self.user = Client(
            "PbxClient",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.PBXBOT_SESSION,
            no_updates=True,
        )

    async def start(self):
        LOGS.info("\x3e\x3e\x20\x42\x6f\x6f\x74\x69\x6e\x67\x20\x75\x70\x20\x50\x62\x78\x4d\x75\x73\x69\x63\x2e\x2e\x2e")
        if Config.BOT_TOKEN:
            await self.app.start()
            me = await self.app.get_me()
            self.app.id = me.id
            self.app.mention = me.mention
            self.app.name = me.first_name
            self.app.username = me.username
            LOGS.info(f"\x3e\x3e\x20{self.app.name}\x20\x69\x73\x20\x6f\x6e\x6c\x69\x6e\x65\x20\x6e\x6f\x77\x21")
        if Config.PBXBOT_SESSION:
            await self.user.start()
            me = await self.user.get_me()
            self.user.id = me.id
            self.user.mention = me.mention
            self.user.name = me.first_name
            self.user.username = me.username
            try:
                await self.user.join_chat("PBX_CHAT")
                await self.user.join_chat("HEROKUBIN_01")
            except:
                pass
            LOGS.info(f"\x3e\x3e\x20{self.user.name}\x20\x69\x73\x20\x6f\x6e\x6c\x69\x6e\x65\x20\x6e\x6f\x77\x21")
        LOGS.info("\x3e\x3e\x20\x42\x6f\x6f\x74\x65\x64\x20\x75\x70\x20\x50\x62\x78\x4d\x75\x73\x69\x63\x21")

    async def logit(self, hash: str, log: str, file: str = None):
        log_text = f"#{hash.upper()} \n\n{log}"
        try:
            if file:
                await self.app.send_document(
                    Config.LOGGER_ID, file, caption=log_text
                )
            else:
                await self.app.send_message(
                    Config.LOGGER_ID, log_text, disable_web_page_preview=True
                )
        except Exception as e:
            raise PbxBotException(f"[PbxBotException]: {e}")


Pbxbot = PbxClient()
