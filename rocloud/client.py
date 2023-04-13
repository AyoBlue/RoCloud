import aiohttp
import asyncio
from .errors import HTTPException
from .datastore import DataStore, Entry

api = 'https://apis.roblox.com'

class Client:
    def __init__(self):
        self.api_key = None
        self.session = None

    def set_key(self, key: str):
        setattr(self, 'api_key', {
            'x-api-key': key
        })

    def set_session(self, loop: asyncio.AbstractEventLoop):
        setattr(self, 'session', aiohttp.ClientSession(loop=loop))

    def run_error_handler(self, error):
        raise HTTPException(error)
    
    async def get_entry(self,
        universe_id: int,
        datastore, 
        key, 
        scope: str = None
    ) -> None:
        params = {}
        params['universeId'] = universe_id
        params['datastoreName'] = datastore
        params['entryKey'] = key
        if scope:
            params['scope'] = scope

        response = await self.session.get(f'https://apis.roblox.com/datastores/v1/universes/{universe_id}/standard-datastores/datastore/entries/entry', params=params, headers=self.api_key)
        data = await response.json()
        _ = self.run_error_handler(data['error']) if data.get('error') != None else False
        return Entry(data)

    async def get_datastores(
        self, 
        universe_id,
        prefix: str = None,
        cursor: str = None,
        limit: int = 5
    ) -> None:
        params = {}
        if prefix:
            params['prefix'] = prefix
        if cursor:
            params['cursor'] = cursor
        if limit:
            params['limit'] = limit

        response = await self.session.get(f'https://apis.roblox.com/datastores/v1/universes/{universe_id}/standard-datastores', params=params, headers=self.api_key)
        data = await response.json()
        _ = self.run_error_handler(data['error']) if data.get('error') != None else False
        return [DataStore(self, universe_id, datastore) for datastore in data['datastores']]