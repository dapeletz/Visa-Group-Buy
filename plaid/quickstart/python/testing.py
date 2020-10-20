from plaid import Client

# Available environments are 'sandbox', 'development', and 'production'.
client = Client(client_id='5f89a53e79118c0012813c68', secret='568ec48582e1217a59bfea025d7340', environment='sandbox')

# response = client.Item.public_token.exchange(public_token)
# access_token = response['access_token']
# item_id = response['item_id']

configs = {
  'user': {
      'client_user_id': '5f89a53e79118c0012813c68',
  },
  'products': ['accounts'],
  'client_name': "Plaid Test App",
  'country_codes': ['US'],
  'language': 'en',
  'webhook': 'https://sample-webhook-uri.com',
  'link_customization_name': 'default',
  'account_filters': {
      'depository': {
          'account_subtypes': ['checking', 'savings'],
      },
  },
}
# create link token
response = client.LinkToken.create(configs)
link_token = response['link_token']


# response = client.Accounts.get(access_token)
# accounts = response['accounts']
