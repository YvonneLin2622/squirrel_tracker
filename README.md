# Squirrel Tracker Web App

## General Information
This Squirrel Tracker web app is built from Django framework to keep track of all squirrels in Central Park at New York City. The data source is from [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).
The app has customized management commands to allow users to import and export squirrel data. It also displays the location of the squirrel sightings on an [OpenStreets](https://www.openstreetmap.org/about/) map and gives users access to view, add, and edit the information of a squirrel.

## Features Description
### Management Commands
- import_squirrel_data
  - Users can import Squirrel Data using this command. Note the file path should be specified at the command line after the name of the management command.
- export_squirrel_data
  - Users can export the existing Squirrel Data in the database using this command. Note the file path should be specified at the command line after the name of the management command.
   
### App Features
- Views
  - General Statistics of Squirrel Data
    - Located at /sightings/stats
    - Statistics displayed:
      - Totoal Number of Squirrels in the sightings
      - Center of the Map
      - Total Number of Adult Squirrels
      - Total Number of Juvenile Squirrels
      - How many squirrels are running, chasing, climbing, eating or foraging


## Project Group
- Group 46 Section 1
- UNIs: [ll3367, zm2335]

## Server Link


    
 
