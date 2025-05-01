import logging

from src.models.models import PlayerProfile, Organization
from src.profile_scraper import ProfileScrapper


class ProfileManager:
    def __init__(self) -> None:
        self._profile_scrapper: ProfileScrapper = ProfileScrapper()
        self._profile_cache: dict[str, PlayerProfile] = {}

    async def get_profile(self, name: str) -> PlayerProfile:
        if name in self._profile_cache:
            logging.info(f"[PROFILE MANAGER] USING CACHED PROFILE FOR PLAYER: {name}")
            return self._profile_cache[name]

        player_profile: PlayerProfile = await self.create_profile(name=name)

        return player_profile

    async def create_profile(self, name: str) -> PlayerProfile:
        logging.info(f"[PROFILE MANAGER] CREATING PROFILE FOR PLAYER: {name}")
        await self._profile_scrapper.fetch_pilot(name)

        org: Organization = Organization(
            name=await self._profile_scrapper.get_pilot_org(),
            url=await self._profile_scrapper.get_pilot_org_url(),
            icon_url=await self._profile_scrapper.get_pilot_org_icon_url(),
            rank=await self._profile_scrapper.get_pilot_org_rank()
        )

        player_profile: PlayerProfile = PlayerProfile(
            name=name,
            icon_url=await self._profile_scrapper.get_pilot_icon_url(),
            enlisted_date=await self._profile_scrapper.get_enlisted_date(),
            location=await self._profile_scrapper.get_location(),
            fluency=await self._profile_scrapper.get_fluency(),
            org=org
        )

        self._profile_cache[name] = player_profile

        return player_profile

    async def update_profile(self, name: str) -> PlayerProfile:
        if name in self._profile_cache:
            logging.info(f"[PROFILE MANAGER] UPDATING PROFILE FOR PLAYER: {name}")

            player_profile: PlayerProfile = await self.create_profile(name=name)

            self._profile_cache[name] = player_profile

            return player_profile
