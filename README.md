# Vdoubleu's Rubik's Cube Timer

Hi, this is the server for my Rubik's Cube Timer.

This server is built using Flask and stores data in MongoDB atlas. The client for this app is built using React and can be found [here](https://github.com/vdoubleu/cube-timer2-client)
The password and usernames for mongodb atlas are stored in the environment of the production instance so if you are running it locally yourself, you will need to add in those variables yourself to your own instance.

This server has several routes:
 - addtimes (adds a single time if a user to the database, is called when the user completes a solve)
 - gettimes (gets all the solves of a particular user)
 - deleteone (deletes the most recent solve time by a user)
 - deleteall (deletes all solves by a user)
 - health (ping this to check if server is up and running, heroku turns of dynos that aren't used in a while)
