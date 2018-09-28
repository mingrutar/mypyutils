#! /bin/python
import os.path
import argparse
import xml.etree.ElementTree as ET
DEFAULT_FILENAME = os.path.join("\\","workspace", "tctsbDevelopment",
    "CONWAY_SERVICE_SHIPMENTNOTIFICATION_REST", "api_specification",
    "ServiceContracts", "LTLAPI", "LTLShipmentNotificationPOCAPI", "1.0",
    "ServiceContract-subscribeShipmentNotification.xml")
#    "ServiceContract-createShipmentNotificationSubscription.xml")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", nargs='+',
        default=DEFAULT_FILENAME,
        help="service contract")
    args = parser.parse_args()
    tree = ET.parse(args.filename)    # 'input_data.xml'
    root = tree.getroot()
    bModified = False
    for elem in tree.iter():
        if (not list(elem)) and elem.text:
            ttt = elem.text.strip()
            if ttt != elem.text:
                print("Need clean! {} = +{}+".format(elem.tag, elem.text))
                elem.text = ttt
                bModified = True
    if bModified:
        tree.write(args.filename)
        print('Fixed the extra spaces')
    else:
        print("No extra spaces found")
