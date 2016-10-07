import Der

user = Der.DerivID ("http://api.vk.com/method","users.get")
user.params="user_ids="+input('Введите username пользователя: ')
resp_user=user.execute()
id=user.find_id(resp_user.text)
print("id: ",id)
friends=Der.DerivFriends("http://api.vk.com/method","friends.get")
friends.params="user_id="+id+"&fields=bdate"
resp_friends=friends.execute()
friends.build_gist(resp_friends)

