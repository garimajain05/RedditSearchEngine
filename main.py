from exa_py import Exa

#add your EXA Key

exa =  Exa('Your EXA Key Here')

#query holds the response of the user
query = input("Enter your Search query: ")

#search method from exa
response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.reddit.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()