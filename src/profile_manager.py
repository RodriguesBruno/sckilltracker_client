import logging

from src.exceptions import PlayerProfileNotFoundException
from src.models.models import PlayerProfile, Organization
from src.profile_scraper import ProfileScraper


class ProfileManager:
    def __init__(self) -> None:
        self._profile_scraper: ProfileScraper = ProfileScraper()
        self._profile_cache: dict[str, PlayerProfile] = {}

        self._verbose_logging: bool = True
        self._debug_logging: bool = False

    @property
    def verbose_logging(self) -> bool:
        return self._verbose_logging

    @verbose_logging.setter
    def verbose_logging(self, value: bool) -> None:
        self._verbose_logging = value
        logging.info(f"[PROFILE MANAGER - Verbose Logging] {'Enabled' if value else 'Disabled'}")

    @property
    def debug_logging(self) -> bool:
        return self._debug_logging

    @debug_logging.setter
    def debug_logging(self, value: bool) -> None:
        logging.info(f'[PROFILE MANAGER - Debug Logging] {"Enabled" if value else "Disabled"}')
        self._debug_logging = value

    async def get_profile(self, name: str) -> PlayerProfile:
        if name in self._profile_cache:
            if self._verbose_logging:
                logging.info(f"[PROFILE MANAGER] USING CACHED PROFILE FOR PLAYER: {name}")
            return self._profile_cache[name]

        player_profile: PlayerProfile = await self.create_profile(name=name)

        return player_profile

    async def create_profile(self, name: str) -> PlayerProfile:
        if self.verbose_logging:
            logging.info(f"[PROFILE MANAGER] CREATING PROFILE FOR PLAYER: {name}")
        await self._profile_scraper.fetch_player(name)

        org: Organization = Organization(
            name=await self._profile_scraper.get_org_name(),
            url=await self._profile_scraper.get_org_url(),
            icon_url=await self._profile_scraper.get_org_icon_url(),
            rank=await self._profile_scraper.get_org_rank()
        )

        player_profile: PlayerProfile = PlayerProfile(
            name=name,
            icon_url=await self._profile_scraper.get_player_icon_url(),
            enlisted_date=await self._profile_scraper.get_player_enlisted_date(),
            location=await self._profile_scraper.get_player_location(),
            fluency=await self._profile_scraper.get_player_fluency(),
            org=org
        )

        self._profile_cache[name] = player_profile

        return player_profile

    async def update_profile(self, name: str) -> PlayerProfile:
        if name in self._profile_cache:
            if self.verbose_logging:
                logging.info(f"[PROFILE MANAGER] UPDATING PROFILE FOR PLAYER: {name}")

            player_profile: PlayerProfile = await self.create_profile(name=name)

            self._profile_cache[name] = player_profile

            return player_profile

        raise PlayerProfileNotFoundException(f"[PROFILE MANAGER] PlayerProfile: {name} not found!")
