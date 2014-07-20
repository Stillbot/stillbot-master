stillbot-master
===========

The goal of the *stillbot-master* project is to provide different ways to pre-program, control and extract data from the *stillbot-slave* PLC.

Ideally the project would be split into and/or provide:
* a RESTful interface to make calls through (a spiffy Flask/Django web2.bl0wz interface is predicated on this)
* a database for persistant data storage, enabling historical analysis of distillation runs
* a configuration mechanism for describing and controlling various disstillation setups
* a continuously running daemon that interfaces with the above services and the PLC
