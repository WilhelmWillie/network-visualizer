# LinkedIn Network Visualizer

Tool that helps you visualize your LinkedIn network and gain insights into your network. 

## Setup

1. Export your LinkedIn connections to a CSV file using [this guide](https://www.linkedin.com/help/linkedin/answer/66844/exporting-connections-from-linkedin?lang=en)
2. Place that CSV file in the root folder of this project and name it `connections.csv`
3. If Flask isn't already installed, run `pip install flask`
4. Run `export FLASK_APP=server.py` then `flask run`
5. Open `localhost:5000` in your browser 

## To-Do

- [ ] Actually build out the network D3.js visualizer 😅
- [ ] Build, train, and implement a model that will automatically extrapolate role information based off position title (ex: Full Stack Developer -> tech/engineering, Summer Business Analyst -> intern)
- [ ] Build a web service that hooks into LinkedIn's API so that users don't have to go through steps 1-3
  - [ ] Add ability to view network by education
  - [ ] Host app on Heroku or GCP or DO