def check_strings(s:str):
    return s.lower().strip()

def check_payload(payload:dict):
    for k,v in payload.items():
        if isinstance(v,str):
            payload[k] = check_strings(v)
    return payload


if __name__ == "__main__":
    payload = {
        'items':" machine Learnings, sfsf "
    }
    print(check_payload(payload))