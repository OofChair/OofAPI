# OofAPI

This API was created as a fun side project by [OofChair](https://github.com/OofChair). <br><br> 
### This is **NOT FINISHED** and may not be for a while.

#### This was created using [FastAPI](https://fastapi.tiangolo.com) and uses the [sr_api](https://pypi.org/project/sr_api) pip package.

#### Want to run this yourself?

##### Easy, make a new venv. (On Ubuntu)
###### If not already installed, install python3-venv.
`sudo apt install python3-venv`<br>
`python -m venv ~/venv` <br>
`source ~/venv/bin/activate`<br>
`git clone https://github.com/PwnBot/OofAPI && cd PwnAPI`<br>
`pip install fastapi uvicorn[standard] sr_api`<br>
`cd source`<br>
`uvicorn main:api` <br>
##### To run it so your changes happen in real time, run `uvicorn main:api --reload`.
