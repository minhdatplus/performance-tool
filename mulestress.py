from locust import HttpUser, TaskSet, task
import json


class UserBehavior(TaskSet):
    @task(1)
    def create_post(self):
        headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip'}
        self.client.post("/customers", data=json.dumps({
            "MsgReqHdr": {
                "TxId": "8a076a8a-d4c2-4695-aac1-669222ccddcb",
                "AppHdr": {
                    "CharSet": "UTF-8",
                    "Fr": {
                        "OrgId": {
                            "Nm": "SystemA"
                        }
                    },
                    "To": {
                        "OrgId": {
                            "Nm": "SystemB"
                        }
                    },
                    "BizMsgIdr": "Techcombank",
                    "MsgDefIdr": "InqAccBalance",
                    "BizSvc": "Account",
                    "CreDt": "2020-12-20T09:30:47Z"
                }
            },
            "MessageId": "TB1010001",
            "Document": {
                "CustomerId": "12345678",
                "Category": "ALL"
            }
        }),
                         headers=headers,
                         name="Create a new post")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
