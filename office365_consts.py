# File: office365_consts.py
# Copyright (c) 2017-2019 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.


TC_STATUS_SLEEP = 2
PHANTOM_SYS_INFO_URL = "{url}rest/system_info"
PHANTOM_ASSET_INFO_URL = "{url}rest/asset/{asset_id}"
O365_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
MSGOFFICE365_RUN_CONNECTIVITY_MSG = "Please run test connectivity first to complete authorization flow and generate a token that the app can use to make calls to the server "

MSGOFFICE365_INVALID_LIMIT = "Please provide non-zero positive integer in limit"
