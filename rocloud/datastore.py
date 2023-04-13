class DataStore:
    __slots__ = (
        'name',
        'created_at',
        'universe_id',
        'default_params',
        '_client'
    )
    def __init__(self, client, universe_id, data):
        self.universe_id = universe_id
        self.name = data.get('name')
        self.created_at = data.get('createdTime')
        self._client = client
        self.default_params = {
            'datastoreName': self.name,
            'universeId': self.universe_id
        }

    async def list_entries(
        self,
        prefix: str = None,
        cursor: str = None,
        scope: str = 'global',
        all_scopes: bool = True,
        limit: int = 10,
    ):
        params = self.default_params.copy()
        if prefix:
            params['prefix'] = prefix
        if cursor:
            params['cursor'] = prefix

        params['scope'] = scope
        params['limit'] = limit if limit < 100 else 100
        params['allScopes'] = 'true' if all_scopes == True else 'false'

        response = await self._client.session.get(f'https://apis.roblox.com/datastores/v1/universes/{self.universe_id}/standard-datastores/datastore/entries', params=params, headers=self._client.api_key)
        data = await response.json()
        _ = self._client.run_error_handler(data['error']) if data.get('error') != None else False
        return Entry(data)

    async def get_entry(
        self,
        key: str, 
        scope: str = None
    ):
        params = self.default_params.copy()
        params['entryKey'] = key
        if scope:
            params['scope'] = scope

        response = await self._client.session.get(f'https://apis.roblox.com/datastores/v1/universes/{self.universe_id}/standard-datastores/datastore/entries/entry', params=params, headers=self._client.api_key)
        data = await response.json()
        _ = self._client.run_error_handler(data['error']) if data.get('error') != None else False
        return Entry(data)

class Entry:
    def __init__(self, data):
        for key, var in data.items():
            setattr(self, key, var)