from unittest.mock import AsyncMock, patch

import pytest

from src.profile_scraper import ProfileScraper
from tests.conftest_profile_scraper import (
    pilot_with_no_corp_profile,
    pilot_with_corp_and_location_profile,
    pilot_with_custom_icon_profile,
    npc_profile,
    pilot_nanoart_with_corp,
    pilot_with_redacted_corp,
    astrotemplar_player,
    pilot_with_more_than_one_fluency,
    pilot_with_weird_long_org_name,
    pilot_with_and_symbol_in_org_name
)


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_from_pilot_with_no_corp_returns_dash(pilot_with_no_corp_profile):

    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_no_corp_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_name()

        expected_result = '-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_enlisted_date_from_pilot_returns_date(pilot_with_no_corp_profile):
    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_no_corp_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_enlisted_date()

        expected_result = 'Feb 17, 2021'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_location_from_pilot_with_no_location_returns_dash(pilot_with_no_corp_profile):
    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_no_corp_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_location()

        expected_result = '-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_icon_url_from_pilot_with_returns_something(pilot_with_no_corp_profile):
    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_no_corp_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_icon_url()

        expected_result = 'https://robertsspaceindustries.com/media/0rixm629l5bwwr/heap_infobox/A5ce2752-Ce33-446e-Ae18-2dab9f9ead8a.jpg'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_enlisted_date_from_pilot_with_corp_returns_date(
        pilot_with_corp_and_location_profile):
    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_corp_and_location_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_enlisted_date()

        expected_result = 'May 5, 2017'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_location_from_pilot_with_location_returns_location(
        pilot_with_corp_and_location_profile):
    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_corp_and_location_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_location()

        expected_result = 'Finland, Uusimaa'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_from_pilot_with_corp_returns_dash(pilot_with_corp_and_location_profile):

    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_corp_and_location_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_name()

        expected_result = 'SCS'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_url_from_pilot_with_corp_returns_corp_url(
        pilot_with_corp_and_location_profile):

    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_corp_and_location_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_url()

        expected_result = 'https://robertsspaceindustries.com/orgs/SCSFIN'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_icon_url_from_pilot_with_default_icon_returns_default_icon_url(
        pilot_with_corp_and_location_profile):

    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_corp_and_location_profile

        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_icon_url()

        expected_result = 'https://cdn.robertsspaceindustries.com/static/images/account/avatar_default_big.jpg'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_icon_url_from_pilot_with_custom_icon_returns_custom_icon_url(pilot_with_custom_icon_profile):

    pilot_name = "CBCORP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_custom_icon_profile


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_icon_url()

        expected_result = 'https://robertsspaceindustries.com/media/va66xhawk8k9mr/heap_infobox/D528d0f9e6560e707aecc9c1ae9d84ae.jpg'
        assert result == expected_result

# [NPC]


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_from_npc_returns_dash(npc_profile):

    pilot_name = "NPC"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = npc_profile


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_url()

        expected_result = '-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_icon_url_from_npc_returns_dash(npc_profile):

    pilot_name = "NCP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = npc_profile


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_icon_url()

        expected_result = '-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_icon_url_from_npc_returns_dash(npc_profile):

    pilot_name = "NCP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = npc_profile


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_icon_url()

        expected_result = '-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_enlisted_date_from_npc_returns_dash(npc_profile):

    pilot_name = "NCP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = npc_profile


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_enlisted_date()

        expected_result = '-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_location_from_npc_returns_dash(npc_profile):

    pilot_name = "NCP"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = npc_profile


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_location()

        expected_result = '-'
        assert result == expected_result


# [NANOART PILOT]


@pytest.mark.asyncio
async def test_profile_scrapper_get_location_from_pilot_nanoart_with_corp_returns_location(pilot_nanoart_with_corp):

    pilot_name = "Nanoart"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_nanoart_with_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_location()

        expected_result = 'Thailand, Krung Thep Maha Nakhon [Bangkok]'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_enlisted_date_from_pilot_nanoart_with_corp_returns_enlisted_date(pilot_nanoart_with_corp):

    pilot_name = "Nanoart"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_nanoart_with_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_enlisted_date()

        expected_result = 'Jan 21, 2022'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_from_pilot_nanoart_with_corp_returns_org_name(pilot_nanoart_with_corp):

    pilot_name = "Nanoart"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_nanoart_with_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_name()

        expected_result = 'Invicta Corporation'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_icon_url_from_pilot_nanoart_with_corp_returns_url(pilot_nanoart_with_corp):

    pilot_name = "Nanoart"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_nanoart_with_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_icon_url()

        expected_result = 'https://robertsspaceindustries.com/media/9yuww3zgrjvw2r/heap_infobox/IDSCORP-Logo.png'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_url_from_pilot_nanoart_with_corp_returns_url(pilot_nanoart_with_corp):

    pilot_name = "Nanoart"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_nanoart_with_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_url()

        expected_result = 'https://robertsspaceindustries.com/orgs/IDSCORP'
        assert result == expected_result

# [PILOT WITH REDACTED ORG]


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_from_pilot_with_redacted_corp_returns_redacted_corp(pilot_with_redacted_corp):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_redacted_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_name()

        expected_result = '-R-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_url_from_pilot_with_redacted_corp_returns_dash(pilot_with_redacted_corp):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_redacted_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_url()

        expected_result = '-'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_icon_url_from_pilot_with_redacted_corp_returns_redacted_icon_url(pilot_with_redacted_corp):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_redacted_corp


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_icon_url()

        expected_result = 'https://cdn.robertsspaceindustries.com/static/images/organization/public-orgs-thumb-redacted-bg.png'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_icon_url_from_pilot_with_redacted_corp_returns_redacted_icon_url(astrotemplar_player):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = astrotemplar_player


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_icon_url()

        expected_result = 'https://cdn.robertsspaceindustries.com/static/images/organization/defaults/logo/faith.jpg'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_with_one_fluency_from_pilot_returns_english(astrotemplar_player):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = astrotemplar_player


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_fluency()

        expected_result = 'English'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_with_two_fluency_from_pilot_returns_french_and_english(pilot_with_more_than_one_fluency):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_more_than_one_fluency


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_player_fluency()

        expected_result = 'French, English'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_rank_with_chamberlain_rank_returns_chamberlain(astrotemplar_player):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = astrotemplar_player


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_rank()

        expected_result = 'Chamberlain'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_with_weird_long_org_name_returns_org_name(pilot_with_weird_long_org_name):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_weird_long_org_name


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_name()

        expected_result = 'Vanguard'
        assert result == expected_result


@pytest.mark.asyncio
async def test_profile_scrapper_get_pilot_org_with_and_symbol_returns_org_name(pilot_with_and_symbol_in_org_name):

    pilot_name = "doesnt_matter"

    with patch("src.profile_scraper.get_from_url", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = pilot_with_and_symbol_in_org_name


        scrapper = ProfileScraper()
        await scrapper.fetch_player(pilot_name)

        result = await scrapper.get_org_name()

        expected_result = 'SOCIETE REPARATIONS & EXTRACTIONS'
        assert result == expected_result