import requests
import yaml

config=yaml.load(open('config.yaml', 'r'))

class LatencyControl(object):

    def __init__(self, wanem_ip=config['WANem_url']):
        self.wanem_ip=wanem_ip

    def change_latency(self,latency1,latency2):
        def build_url():
            return "http://{}/WANem/index-basic.php".format(self.wanem_ip)
        body="txtBandwidthAuto1=Other&txtBandwidth1=0&txtDelay1=0&txtSrc1=any&txtDest1=any" \
             "&txtPort1=any&txtBandwidthAuto2=Other&txtBandwidth2=0&txtDelay2=0&txtSrc2=any" \
             "&txtDest2=any&txtPort2=any&txtBandwidthAuto3=Other&txtBandwidth3=0&txtDelay3=0" \
             "&txtSrc3=any&txtDest3=any&txtPort3=any&txtBandwidthAuto4=1304000&txtBandwidth4=1304000" \
             "&txtDelay4={}&txtSrc4=any&txtDest4=any&txtPort4=any&txtBandwidthAuto5=1304000" \
             "&txtBandwidth5=1304000&txtDelay5={}&txtSrc5=any&txtDest5=any&txtPort5=any" \
             "&txtBandwidthAuto6=1304000&txtBandwidth6=1304000&txtDelay6=0&txtSrc6=any&txtDest6=any" \
             "&txtPort6=any&txtBandwidthAuto7=Other&txtBandwidth7=0&txtDelay7=0&txtSrc7=any" \
             "&txtDest7=any&txtPort7=any&btnApply=Apply+settings".format(latency2,latency1)
        headers={'Content-Type': 'application/x-www-form-urlencoded'}

        result=requests.post(build_url(),body,headers=headers)
        if result.status_code>=300:
            result.raise_for_status()
        return True