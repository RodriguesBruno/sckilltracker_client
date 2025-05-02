import pytest

from src.models.models import PlayerProfile
from src.profile_manager import ProfileManager


@pytest.mark.asyncio
async def test_profile_manager_get_profile_from_russian_player_returns_player_profile():
    player_name= 'Fianino'

    profile_manager = ProfileManager()

    result = await profile_manager.get_profile(player_name)

    print(result)
    assert isinstance(result, PlayerProfile)