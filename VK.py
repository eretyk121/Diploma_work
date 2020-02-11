import datetime
import time
import requests
from pprint import pprint
ID = 171691064
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
class User:
    def __init__(self, token, first_name=None, last_name=None):
        self.token = token
        self.first_name = first_name
        self.last_name = last_name

    def get_params(self):
        return dict(
            access_token=self.token,
            v='5.52'
        )

    def get_info(self):
        params = self.get_params()
        params['user_id'] = ID
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        self.first_name = response.json()['response'][0]['first_name']
        self.last_name = response.json()['response'][0]['last_name']
        return response.json()

    def get_groups(self):
        params = self.get_params()
        params['user_id'] = ID
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        return response.json()

    def get_group_info(self):
        params = self.get_params()
        params['fields'] = 'id, name, counters'
        final_list = []
        for id_group in members:
            print('формирую список групп')
            params['group_id'] = id_group
            time.sleep(1)
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params
            )
            time.sleep(1)
            response_2 = requests.get(
                'https://api.vk.com/method/groups.getMembers',
                params
            )
            p_2 = int(response_2.json()['response']['count'])
            p = response.json()
            # pprint(p)
            # print(p_2)
            final_1 = {'group_id': p['response'][0]['id'],
                                'group_name': p['response'][0]['name'],
                                'count': p_2}
            final_list.append(final_1)
        pprint(final_list)
            # pprint(final_1)

    def get_members(self):
        params = self.get_params()
        params['filter'] = 'friends'
        group_list = []
        for id in groups_id:
            print('ищу группы без друзей...')
            params['group_id'] = id

            response = requests.get(
                'https://api.vk.com/method/groups.getMembers',
                params
            )
            all_groups = response.json()
            if all_groups['response']['count'] == 0:
                group_list.append(id)
                # print(id)
        # print(group_list)
        return group_list
evgeny = User(TOKEN)
groups = evgeny.get_groups()
groups_id = groups['response']['items']
members = evgeny.get_members()
final = evgeny.get_group_info()

