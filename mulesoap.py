from locust import HttpUser, TaskSet, task
import json

data_raw = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">   <soapenv:Header />   <soapenv:Body>      <tns:InqAccBalanceReq xmlns:tns="http://www.techcombank.com.vn/Core/Banking/V1">         <tns:MsgReqHdr>            <tns:TxId>8a076a8a-d4c2-4695-aac1-669222ccddcb</tns:TxId>            <tns:AppHdr>               <tns:CharSet>UTF-8</tns:CharSet>               <tns:Fr>                  <tns:OrgId>                     <tns:Nm>SystemA</tns:Nm>                  </tns:OrgId>               </tns:Fr>               <tns:To>                  <tns:OrgId>                     <tns:Nm>SystemB</tns:Nm>                  </tns:OrgId>               </tns:To>               <tns:BizMsgIdr>Techcombank</tns:BizMsgIdr>               <tns:MsgDefIdr>InqAccBalance</tns:MsgDefIdr>               <tns:BizSvc>Account</tns:BizSvc>               <tns:CreDt>2020-12-20T09:30:47Z</tns:CreDt>            </tns:AppHdr>         </tns:MsgReqHdr>         <tns:MessageId>TB1010001</tns:MessageId>         <tns:Document>            <tns:CustomerId>12345678</tns:CustomerId>            <tns:Category>ALL</tns:Category>         </tns:Document>      </tns:InqAccBalanceReq>   </soapenv:Body></soapenv:Envelope>'


class UserBehavior(TaskSet):
    @task(1)
    def create_post(self):
        headers = {'content-type': 'application/xml', 'Accept-Encoding': 'gzip'}
        self.client.post("/customers/soap", data=data_raw,
                         headers=headers,
                         name="Create a new post")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
