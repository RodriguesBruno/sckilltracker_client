import logging
import re
import httpx

async def get_from_url(url: str) -> str:
    async with httpx.AsyncClient(verify=False) as client:
        try:
            response = await client.get(url)
            return response.text

        except httpx.RequestError as e:
            logging.error(f"Request failed: {e}")


class ProfileScrapper:
    def __init__(self) -> None:
        self._url = f"https://robertsspaceindustries.com/en/citizens"
        self._player_data: str = ""

    async def fetch_player(self, name: str) -> None:
        logging.info(f"[PROFILE SCRAPPER] FETCHING DATA FOR PLAYER: {name}")
        url = f"{self._url}/{name}"
        html = await get_from_url(url)

        self._player_data = html

    async def get_player_icon_url(self) -> str:
        pattern = re.compile(
            r'<div class="thumb">\s+<img src="(?P<icon_url>.*?)"\s/>\s+<span class=',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            result = match.group('icon_url').strip()
            if '/media/'in result:
                res = f'https://robertsspaceindustries.com{result}'
                return res

            return result

        return '-'

    async def get_org_name(self) -> str:

        if 'NO MAIN ORG FOUND IN PUBLIC RECORDS' in self._player_data:
            return '-'

        if '-redacted-bg.png' in self._player_data:
            return '-R-'

        pattern = re.compile(
            r'px\scenter">(?P<org>.*?)</a>\s+</p>',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            res = match.group('org').strip()
            if '&equiv;'in res:
                return res.replace('&equiv;', '').replace('\\', '').replace('/', '').strip()

            return res

        return '-'

    async def get_org_url(self) -> str:

        if 'NO MAIN ORG FOUND IN PUBLIC RECORDS' in self._player_data:
            return '-'

        pattern = re.compile(
            r'<p class="entry">\s+<a href="/(?P<org_url>.*?)"\sclass="value\s',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            result =match.group('org_url').strip()
            return f"https://robertsspaceindustries.com/{result}"

        return '-'

    async def get_org_icon_url(self):

        if 'NO MAIN ORG FOUND IN PUBLIC RECORDS' in self._player_data:
            return '-'

        if 'thumb-redacted-bg.png' in self._player_data:
            return 'https://cdn.robertsspaceindustries.com/static/images/organization/public-orgs-thumb-redacted-bg.png'

        pattern = re.compile(
            r'"><img src="(?P<org_icon_url>.*?)"\s/></a>\s+<span\s+class=',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            result = match.group('org_icon_url').strip()
            if '//cdn.' in result:
                return result

            return f"https://robertsspaceindustries.com{result}"

        return '-'

    async def get_player_enlisted_date(self):

        pattern = re.compile(
            r'<span\s+class="label">\s*Enlisted\s*</span>\s*<strong\s+class="value">\s*(?P<enlisted_date>.*?)\s*</strong>',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            return match.group('enlisted_date').strip()

        return '-'

    async def get_player_location(self):

        pattern = re.compile(
            r'<span\s+class="label">\s*Location\s*</span>\s*<strong\s+class="value">\s*(?P<location>.*?)\s*</strong>',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            res = match.group('location').strip()
            if ',' in res:
                entries = res.split(',')
                res = entries[0].replace('\n', ' ').replace(' ', '') + ', ' + entries[1].strip()
                return res
            else:
                return res.replace('\n', '').replace(' ', '').replace(',', ', ')

        return '-'

    async def get_player_fluency(self) -> str:

        pattern = re.compile(
            r'<span\s+class="label">Fluency</span>\s*<strong\s+class="value">\s*(?P<fluency>.*?)\s*</strong>',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            res = match.group('fluency').strip()
            if "," in res:
                return ", ".join([item.strip() for item in res.split(',')])

            return res

        return '-'

    async def get_org_rank(self) -> str:

        pattern = re.compile(
            r'<span[^>]*>Organization rank</span>\s*<strong[^>]*>\s*(?P<rank>.*?)\s*</strong>',
            re.DOTALL
        )

        match = pattern.search(self._player_data)

        if match:
            res = match.group('rank').strip()
            if "," in res:
                return ", ".join([item.strip() for item in res.split(',')])

            return res

        return '-'