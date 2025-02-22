from django.urls import path
import measurement.views

urlpatterns = [

    # path('sensors/', measurement.views.create_sensor),  # create
    # path('sensors/<pk>', measurement.views.change_sensor),     # update
    path('measurements/', measurement.views.add_measurement), # add measurement
    path('sensors/', measurement.views.List_sensors.as_view()),    # get sensors
    path('sensors/<pk>', measurement.views.find_sensor.as_view()),  # get

]
