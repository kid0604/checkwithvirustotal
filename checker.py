""" ----- coding:utf-8 -----
@author: Kid0604

"""
import threading
import time
import sys
import requests


class VTChecker(threading.Thread):
    def __init__(self, UI):
        threading.Thread.__init__(self)
        self.UI = UI
        pass

    def run(self):
        # get filename
        if len(sys.argv) < 2:
            self.UI.label.setText("error")
            time.sleep(10)
            sys.exit(1)
        else:
            file_name = sys.argv[1]
            file_name = file_name.replace("\\", "/")

        # send file
        params = {'apikey': 'b743bf32a25fa1a43232f26fcc7d41676d12e8ed2eb76505001301482ddaacdc'}
        files = {'file': (file_name, open(file_name, 'rb'))}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
        json_response = response.json()
        resource = json_response['resource']
        # update label
        self.UI.label.setText("Checking...")

        # retrieving file scan reports
        response_code = 0
        while not response_code:
            params = {'apikey': 'b743bf32a25fa1a43232f26fcc7d41676d12e8ed2eb76505001301482ddaacdc', 'resource': resource}
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "gzip,  My Python requests library example client or username"
            }
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)

            if response.status_code == 200:
                json_response = response.json()
            else:
                time.sleep(5)
                continue

            response_code = json_response['response_code']
            if response_code == 0:
                time.sleep(10)
                continue

            positives = json_response['positives']
            total = json_response['total']
            final_result = "Detected: " + str(positives) + "/" + str(total)

        # update label
        self.UI.label.setText(final_result)
        pass
