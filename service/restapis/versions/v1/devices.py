
import os
import requests

from flask_restplus import Namespace, Resource
from flask_restplus.reqparse import RequestParser

from akit.integration.landscaping import Landscape
from akit.integration.agents.upnpagent import UpnpAgent

landscape = Landscape()
upnp_agent = UpnpAgent()

DEVICES_NAMESPACE_PATH = "/devices"

devices_ns = Namespace("Devices v1", description="")

from website import static as static_module

DIR_STATIC = os.path.dirname(static_module.__file__)

def try_download_icon_to_cache(cache_dir, icon_url, url_base=None):

    try:
        ext_cache_dir = cache_dir

        icon_url_parts = icon_url.split("/")
        if len(icon_url_parts) > 1:
            ext_cache_dir = os.path.join(cache_dir, *icon_url_parts[:-1])

        if not os.path.exists(ext_cache_dir):
            os.makedirs(ext_cache_dir)

        cache_filename = os.path.join(DIR_STATIC, "images", "cached", *icon_url_parts)
        if not os.path.exists(cache_filename):
            full_url = icon_url
            if url_base is not None:
                full_url = url_base + icon_url

            resp = requests.get(full_url)
            if resp.status_code == 200:
                with open(cache_filename, 'wb') as iconf:
                    iconf.write(resp.content)
    except:
        print("Error downloading file.")

    return

@devices_ns.route("/")
class AllDevicesCollection(Resource):

   def get(self):
        """
            Returns a list of devices
        """
        expected_upnp_devices = landscape.get_upnp_devices()

        exp_device_table = {}
        for exp_dev in expected_upnp_devices:
            exp_mac = exp_dev["MACAddress"]
            exp_device_table[exp_mac] = exp_dev
            exp_dev["cachedIcon"] = "/static/images/unknowndevice.png"

        other_devices = []
        for child in upnp_agent.children:
            cinfo = child.to_dict(brief=True)

            if "MACAddress" in cinfo:
                cmac = cinfo["MACAddress"]
                if cmac in exp_device_table:
                    exp_device_table[cmac] = cinfo
                else:
                    other_devices.append(cinfo)

                firstIcon = cinfo.get("firstIcon", None)
                if firstIcon is not None:
                    icon_url = firstIcon["url"]
                    replacement_url = "/static/images/cached/" + icon_url.lstrip("/")
                    cinfo["cachedIcon"] = replacement_url


                    cache_dir = os.path.join(DIR_STATIC, "images", "cached")
                    url_base = cinfo.get("URLBase", None)
                    try_download_icon_to_cache(cache_dir, icon_url, url_base=url_base)
            else:
                other_devices.append(cinfo)

        rtndata = {
            "status": "success",
            "expected": [ v for v in exp_device_table.values() ],
            "other": other_devices
        }

        return rtndata

@devices_ns.route("/<mac>")
class DeviceDetail(Resource):

   def get(self, mac):
        """
            Returns a list of devices
        """

        found_child = None
        for child in upnp_agent.children:
            cinfo = child.to_dict(brief=True)

            if "MACAddress" in cinfo:
                cmac = cinfo["MACAddress"]
                if mac == cmac:
                    found_child = child

        found_dev = found_child.to_dict(brief=False)
        firstIcon = found_dev.get("firstIcon", None)
        if firstIcon is not None:
            icon_url = firstIcon["url"]
            replacement_url = "/static/images/cached/" + icon_url.lstrip("/")
            found_dev["cachedIcon"] = replacement_url


            cache_dir = os.path.join(DIR_STATIC, "images", "cached")
            url_base = found_dev.get("URLBase", None)
            try_download_icon_to_cache(cache_dir, icon_url, url_base=url_base)
        else:
            found_dev["cachedIcon"] = "/static/images/unknowndevice.png"

        rtndata = {
            "status": "success",
            "device": found_dev
        }

        return rtndata


def publish_namespaces(version_prefix):
    ns_list = [
        (devices_ns, "".join([version_prefix, DEVICES_NAMESPACE_PATH]))
    ]
    return ns_list
