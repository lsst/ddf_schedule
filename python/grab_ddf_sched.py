__all__ = ("grab_ddf_sched",)

import numpy as np
import requests
import os

CONFIG_URL = "https://github.com/lsst-ts/ts_config_scheduler/blob/develop/Scheduler/feature_scheduler/maintel/fbs_config_lsst_survey.py"
DDF_URL_BASE = "https://s3df.slac.stanford.edu/data/rubin/sim-data/ddf_arrays/"


def grab_ddf_sched(config_url=CONFIG_URL, ddf_array_url_base=DDF_URL_BASE):
    """
    Get the current DDF schedule.

    Parameters
    ----------
    config_url : `str`
        URL where the current telescope configuration can be found.
    DDF_URL_BASE : `str`
        The base URL for where ddf .npz files are stored.

    Returns
    -------
    numpy array with the information for each scheduled DDF visit
    """

    # Grab the config page from github
    config_page = requests.get(config_url)

    indx = config_page.content.find(b"expected_hex_digest")
    str_pad = 100
    hex_str = (
        config_page.content[indx : indx + str_pad]
        .split(b'"')[1]
        .decode()
        .replace("\\", "")
    )

    ddf_array_file = "ts_ddf_array_%s.npz" % hex_str
    url = ddf_array_url_base + ddf_array_file

    # Download the file
    if not os.path.isfile(ddf_array_file):
        print("Downloading %s" % url)
        response = requests.get(url, stream=True, timeout=30)
        with open(ddf_array_file, "wb") as f:
            f.write(response.content)
    else:
        print("Using file %s" % ddf_array_file)

    ddf_load = np.load(ddf_array_file)
    obs_array = ddf_load["obs_array"]
    ddf_load.close()

    return obs_array
