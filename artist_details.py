import requests

access_token = 'BQCq_Ur9MarS5VS4dU6fOtrwAvj8uBh2y162eKXeSIMNlRo3Rvq9yblgBlc1Ofip1M2Ux7qGj2GJd0t76E4cM_Ek5qiqX8pGDF8i7UKL5nVk0CA2FEQ'

headers = {
    'Authorization': f'Bearer {access_token}'
}

query = 'Lisa'
search_type = 'track'
url = f'https://api.spotify.com/v1/search?q={query}&type={search_type}'
response = requests.get(url, headers=headers)
if response.status_code == 200:
    search_results = response.json()
    print(search_results)
else:
    print('Failed to search for tracks:', response.status_code)
    print(response.json())
