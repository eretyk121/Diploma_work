import time
import requests
ID = 171691064
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'

class User:
    def __init__(self, token):
        self.token = token

    def get_params(self):
        return dict(
            access_token=self.token,
            v='5.52'
        )

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
        final_list = []
        for id_group in id_groups_without_friends:
            print(f'Формирую информацию о группе {id_group}')
            params['group_id'] = id_group
            params['fields'] = 'members_count'
            time.sleep(1)
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params
            )
            group_info = response.json()
            time.sleep(1)
            final_dic = {'group_id': group_info['response'][0]['id'],
                        'group_name': group_info['response'][0]['name'],
                        'count': group_info['response'][0]['members_count']}
            final_list.append(final_dic)
        return final_list

    def get_members(self):
        params = self.get_params()
        params['filter'] = 'friends'
        group_list = []
        for id in groups_id:
            print(f'Проверяю группу {id} на отсутствие друзей')
            params['group_id'] = id
            response = requests.get(
                'https://api.vk.com/method/groups.getMembers',
                params
            )
            all_groups = response.json()
            if all_groups['response']['count'] == 0:
                group_list.append(id)
        return group_list

def groups_without_friends():
    evgeny = User(TOKEN)
    all_groups = evgeny.get_groups()
    global groups_id
    groups_id = all_groups['response']['items']
    global id_groups_without_friends
    id_groups_without_friends = evgeny.get_members()
    final = evgeny.get_group_info()
    return final

with open('Groups.json', 'w', encoding='utf-8') as text:
    for group in groups_without_friends():
        text.write(f'{group} \n')
    print("Информация записана в файл")
