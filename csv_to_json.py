import csv
import json

# Dictionary of connections where key is company and value is connection info
connections = {}

# Dictionary where key is company and value is frequency in company name (ex: Apple, 8)
companyFrequency = {}

# Dictionary where key is word and value is frequency in position titles (ex: intern, 12)
keywordFrequency = {}

def addToConnections(name, company, position):
  if company in connections:
    connections[company].append({
        'name': name,
        'position': position
      })

    companyFrequency[company] = companyFrequency[company] + 1
  else:
    connections[company] = [{
      'name': name,
      'position': position
    }]

    companyFrequency[company] = 1

def processPositionTitle(position):
  for keyword in position.lower().split():
    if keyword.isalnum():
      if keyword in keywordFrequency:
        keywordFrequency[keyword] = keywordFrequency[keyword] + 1
      else:
        keywordFrequency[keyword] = 1

# Main method eeeeeeyuh
if __name__ == '__main__':
  # Read the connections CSV file and process the data
  with open('connections.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
      name = row['First Name'] + ' ' + row['Last Name']
      company = row['Company']
      position = row['Position']

      if company == '':
        company = 'N/A'
      if position == '':
        position = 'N/A'

      addToConnections(name, company, position)
      processPositionTitle(position)

  # Put processed data into an object for JSON export purposes
  network = {
    'connections': connections,
    'companyFrequency': companyFrequency,
    'keywordFrequency': keywordFrequency
  }

  # Export network object to JSON
  with open('network.json', 'w') as jsonFile:
    json.dump(network, jsonFile)


