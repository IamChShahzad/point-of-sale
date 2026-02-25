import requests
import uuid
# from config import TPN, AUTH_KEY

# import chardet

def credit_sale(tpn, auth_key, amount, callback_url=""):
    url = "https://api.spinpos.net/v2/Payment/Sale"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "Amount": amount,
        "TipAmount": None,
        "ExternalReceipt": "",
        "PaymentType": "Credit",
        "ReferenceId": str(uuid.uuid4().hex[:12]),  # unique 12-char reference ID
        "PrintReceipt": "No",
        "GetReceipt": "No",
        "MerchantNumber": None,
        "InvoiceNumber": "",
        "CaptureSignature": False,
        "GetExtendedData": True,
        "CallbackInfo": {
            "Url": callback_url  # Optional: Webhook if needed
        },
        "Tpn": tpn,
        "Authkey": auth_key,
        "SPInProxyTimeout": None,
        "CustomFields": {}
    }

    # response = requests.post(url, headers=headers, json=payload)
    # response.raise_for_status()
    # return response.json()
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {
            "success": True,
            "status": response.json().get("Status", "Unknown"),
            "message": response.json()
        }
    except requests.HTTPError as http_err:
        return {
            "success": False,
            "status": "HTTP Error",
            "message": http_err.response.text
        }
    except Exception as err:
        return {
            "success": False,
            "status": "Exception",
            "message": str(err)
        }


def ebt_cash(tpn, auth_key, amount, callback_url=""):
    url = "https://api.spinpos.net/v2/Payment/Sale"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "Amount": amount,
        "TipAmount": None,
        "ExternalReceipt": "",
        "PaymentType": "EBT_Cash",  # "Credit", "EBT", "EBT_Cash"
        "ReferenceId": str(uuid.uuid4().hex[:12]),
        "PrintReceipt": "No",
        "GetReceipt": "No",
        "MerchantNumber": None,
        "InvoiceNumber": "",
        "CaptureSignature": False,
        "GetExtendedData": True,
        "CallbackInfo": {
            "Url": callback_url
        },
        "Tpn": tpn,
        "Authkey": auth_key,
        "SPInProxyTimeout": None,
        "CustomFields": {}
    }

    # response = requests.post(url, headers=headers, json=payload)
    # response.raise_for_status()
    # return response.json()

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {
            "success": True,
            "status": response.json().get("Status", "Unknown"),
            "message": response.json()
        }
    except requests.HTTPError as http_err:
        return {
            "success": False,
            "status": "HTTP Error",
            "message": http_err.response.text
        }
    except Exception as err:
        return {
            "success": False,
            "status": "Exception",
            "message": str(err)
        }




def cash(tpn, auth_key, amount, callback_url=""):
    url = "https://api.spinpos.net/v2/Payment/Sale"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "Amount": amount,
        "TipAmount": None,
        "ExternalReceipt": "",
        "PaymentType": "Cash",
        "ReferenceId": str(uuid.uuid4().hex[:12]),
        "PrintReceipt": "No",
        "GetReceipt": "No",
        "MerchantNumber": None,
        "InvoiceNumber": "",
        "CaptureSignature": False,
        "GetExtendedData": True,
        "CallbackInfo": {
            "Url": callback_url
        },
        "Tpn": tpn,
        "Authkey": auth_key,
        "SPInProxyTimeout": None,
        "CustomFields": {}
    }

    # response = requests.post(url, headers=headers, json=payload)
    # response.raise_for_status()
    # return response.json()
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {
            "success": True,
            "status": response.json().get("Status", "Unknown"),
            "message": response.json()
        }
    except requests.HTTPError as http_err:
        return {
            "success": False,
            "status": "HTTP Error",
            "message": http_err.response.text
        }
    except Exception as err:
        return {
            "success": False,
            "status": "Exception",
            "message": str(err)
        }







def refund_sale(tpn, auth_key, amount, reference_id=None, callback_url=""):
    url = "https://api.spinpos.net/v2/Gift/Refund"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "Amount": amount,
        "ReferenceId": reference_id or str(uuid.uuid4().hex[:12]),
        "GetReceipt": "No",
        "PrintReceipt": "No",
        "InvoiceNumber": "",
        "GetExtendedData": False,
        "CallbackInfo": {
            "Url": callback_url
        },
        "Tpn": tpn,
        "Authkey": auth_key,
        "SPInProxyTimeout": None,
        "CustomFields": {}
    }

    try:
        response = requests.post(
            "https://api.spinpos.net/v2/Gift/Refund",
            headers={"Content-Type": "application/json"},
            json=payload
        )
        data = response.json()
        return {
            "success": True,
            "status": data.get("GeneralResponse", {}).get("Message", "Unknown"),
            "message": data.get("GeneralResponse", {}).get("DetailedMessage", ""),
        }
    except Exception as e:
        return {"success": False, "message": str(e)}



def void_sale(tpn, auth_key, amount, reference_id, callback_url=""):
    url = "https://api.spinpos.net/v2/Payment/Void"
    headers = {"Content-Type": "application/json"}

    payload = {
        "Amount": amount,
        "PaymentType": "Credit",  # Could also be "EBT" or "EBT_Cash" if needed
        "ReferenceId": reference_id,
        "PrintReceipt": "No",
        "GetReceipt": "No",
        "MerchantNumber": None,
        "CaptureSignature": False,
        "GetExtendedData": True,
        "CallbackInfo": {
            "Url": callback_url
        },
        "Tpn": tpn,
        "Authkey": auth_key,
        "SPInProxyTimeout": None,
        "CustomFields": {}
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {
            "success": True,
            "status": response.json().get("Status", "Unknown"),
            "message": response.json()
        }
    except requests.HTTPError as http_err:
        return {
            "success": False,
            "status": "HTTP Error",
            "message": http_err.response.text
        }
    except Exception as err:
        return {
            "success": False,
            "status": "Exception",
            "message": str(err)
        }


def settle_batch_out(reference_id, tpn, auth_key):
    url = "https://api.spinpos.net/v2/Payment/Settle"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "ReferenceId": reference_id,
        "GetReceipt": False,
        "SettlementType": "Close",  # Or "Open" if partial
        "Tpn": tpn,
        "Authkey": auth_key,
        "SPInProxyTimeout": None,
        "CustomFields": {}
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()




if __name__ == "__main__":
    TPN = "248925801908"
    AUTH_KEY = "Z8Ed2sfg98"
    AMOUNT = 0.10  # test transaction

    try:
        response = credit_sale(TPN, AUTH_KEY, AMOUNT)
        print("SPIn Sale Response:", response)
    except requests.HTTPError as e:
        print("HTTP error:", e.response.json())
    except Exception as ex:
        print("Error:", str(ex))
