# Lichess Data API Ingestion Pipeline

Lichess is one of the two most popular online chess websites (second to chess.com). They have a public API, as well as a database of player/game data as shown [here](https://database.lichess.org). Since COVID lockdowns and the rising popularity of chess personalities, chess has seen a resurgence in the number of players. This means that more data is becoming available (although there wasn't a lack of it before) to study and analyze. In this repo, we create an example pipeline for Lichess data ingestion and cleaning so that people may use the data more easily.

## Pipeline

In order to create a pipeline, we employ `GCP` as our cloud service provider, `mage` as our orchestrator, `terraform` for IaC, and `Looker Studio` for visualizations. 
![pipeline](https://i.gyazo.com/6b569fae95a403c5fead55f558d98c9a.png)
It is of note that although there is a large amount of chess data, we chose to only use January of 2014 in order to save costs (free trial ran out). The data itself was under 1Gb so it was decided not to use partitioning as it may have been a waste of resources for how little the data was getting queried by us.

## Getting Started

In order to get started, you will need to have a couple of things installed and set up:
- set up a [`GCP`](https://cloud.google.com/?hl=en) account
- install [`Docker`](https://www.docker.com/) (as well as `docker-compose`)
- install [`Terraform`](https://www.terraform.io/)

To start the pipeline, go through the following steps:
1. create a project in `GCP`
2. put the project name in the respective `variables.tf` and `.env` (note, a couple of the `mage` DAGs may need manual updating)
3. create a service account as well as its respective credentials
4. replace the empty `lichess_gcp.json` with your own credentials (keep the same name)
5. create the resources using `terraform`
6. create a `docker` instance using `docker-compose`
7. open the local `mage` instance with [http://localhost:6789/](http://localhost:6789/)
8. trigger a run of the pipeline
9. once the run is done, `GCS` and `bigquery` will have the data loaded
10. visualize the data whichever way you choose

## Visualization

To visualize the data, we used [Google Looker Studio](https://lookerstudio.google.com). An example dashboard is linked [here](https://lookerstudio.google.com/reporting/702eda50-4333-4fd6-a6ce-21e10200dc84), as well a screenshot to see what it looks like. The data can be played around with and a more creative individual can find better things to visualize.
![dashboard](https://i.gyazo.com/b19eb82859e74b2017a6d6aa9c596ea9.png)
