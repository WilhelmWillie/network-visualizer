# LinkedIn Network Visualizer

Tool that helps you visualize your LinkedIn network and gain insights into your network. 

## Setup

1. Export your LinkedIn connections to a CSV file using [this guide](https://www.linkedin.com/help/linkedin/answer/66844/exporting-connections-from-linkedin?lang=en)
2. Place that CSV file in the root folder of this project and name it `connections.csv`
3. Run the Python script `csv_to_json.py`. This will generate a file called `network.json`
4. Run `python -m SimpleHTTPServer <port>` to spin up a local web server (defaults to port 8000)
5. Open `localhost:<port>` to see a basic visualization of your LinkedIn network

See `example_connections.csv` and `example_network.json` for examples of what these files should look like

## To-Do

- [ ] Actually build out the network D3.js visualizer 😅
- [ ] Build, train, and implement a model that will automatically extrapolate role information based off position title (ex: Full Stack Developer -> tech/engineering, Summer Business Analyst -> intern)
- [ ] Build a web service that hooks into LinkedIn's API so that users don't have to go through steps 1-3
  - [ ] Add ability to view network by education
  - [ ] Host app on Heroku or GCP or DO