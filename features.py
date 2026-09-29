import re
from urllib.parse import urlparse


SUSPICIOUS_WORDS = [
    "login",
    "signin",
    "verify",
    "verification",
    "secure",
    "account",
    "update",
    "banking",
    "confirm",
    "password"
]


def extract_features(url):

    # Convert URL to string and lowercase it
    url = str(url).lower()

    # Parse URL into parts
    parsed_url = urlparse(url)

    domain = parsed_url.netloc
    path = parsed_url.path

    # 1. Total URL length
    url_length = len(url)

    # 2. Number of dots
    dot_count = url.count(".")

    # 3. Number of hyphens
    hyphen_count = url.count("-")

    # 4. Number of digits
    digit_count = sum(char.isdigit() for char in url)

    # 5. Number of special characters
    special_char_count = len(
        re.findall(r'[^a-zA-Z0-9]', url)
    )

    # 6. Check whether URL contains @
    contains_at = 1 if "@" in url else 0

    # 7. Check whether HTTPS is used
    uses_https = 1 if parsed_url.scheme == "https" else 0

    # 8. Check whether domain is an IP address
    contains_ip = 1 if re.fullmatch(
        r"\d{1,3}(\.\d{1,3}){3}",
        domain.split(":")[0]
    ) else 0

    # 9. Count suspicious words
    suspicious_word_count = sum(
        1 for word in SUSPICIOUS_WORDS
        if word in url
    )

    # 10. Path length
    path_length = len(path)

    return [
        url_length,
        dot_count,
        hyphen_count,
        digit_count,
        special_char_count,
        contains_at,
        uses_https,
        contains_ip,
        suspicious_word_count,
        path_length
    ]


if __name__ == "__main__":

    test_url = "https://paypal-account-verify.xyz/login?id=12345"

    features = extract_features(test_url)

    print("URL:", test_url)
    print("Features:", features)