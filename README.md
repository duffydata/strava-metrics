# strava-metrics

The Strava-Metrics repositary provides a Strava API Client and a notebook to analyse your running activities, using heart rate data. 
**How To Use**

The Strava API uses OAUTH for authenication so you require the following before you can retrieve your data: 
- Strava Client ID
- Strava Client Secret
- Strava Athlete ID

To retrieve these you will first need to create a Strava API Application which takes a few mins to set up: https://www.strava.com/settings/api 
Please see Strava Documentation for more information:  https://developers.strava.com/docs/getting-started/

**Dependency Managment**

We use Poetry for dependency management, however you can use pip if preferred. 

```
poetry env use python3.x  # use versions greater than 3.8
poetry install
poetry shell
poetry add ipywidgets
poetry add voila
poetry add pandas
poetry add plotly
poetry add numpy
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```
 




