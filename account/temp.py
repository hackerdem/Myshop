from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode




if __name__ == "__main__":
    uid64 = "VGhpcyBpcyBhIHRlc3Q="

    uid = urlsafe_base64_decode(uid64)


    # print(
    #      uid64.encode('utf-8')
    # )

    print(uid)

