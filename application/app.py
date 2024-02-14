import os
import time

from application.mongo.mongo_actions import MongoActions


class App:
    def __init__(self):
        self.routes = os.getenv("ROUTES", {})

    def boot_application(self):
        path = os.getenv("PATH_INFO")
        method = os.getenv("REQUEST_METHOD")
        print("path", path)
        print("method", method)
        print("routes", self.routes)
        return {"routes": self.routes}


if __name__ == "__main__":
    app = App()
    while True:
        mongo_client = MongoActions()
        # mongo_client.set_collection('collection')
        # print("mongo_cli", mongo_client)
        mongo_client.insert({"name": "test"})
        app.boot_application()
        time.sleep(10)
