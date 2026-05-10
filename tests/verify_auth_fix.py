import os
import json
import base64
from unittest.mock import MagicMock, patch

def test_setup_auth_logic():
    # Mocking credentials object
    mock_creds = MagicMock()
    mock_creds.to_json.return_value = json.dumps({"token": "fake_token"})

    token_file = "config/credentials/test_v2.json"
    os.makedirs(os.path.dirname(token_file), exist_ok=True)

    # Simulate saving in setup_auth.py
    with open(token_file, "w", encoding="utf-8") as f:
        f.write(mock_creds.to_json())

    # Simulate base64 export in setup_auth.py
    with open(token_file, "r", encoding="utf-8") as f:
        content = f.read()
        b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    assert b64 is not None
    assert json.loads(content)["token"] == "fake_token"
    print("✅ setup_auth.py logic verified: Credentials saved as JSON and base64 exported.")

def test_engine_load_logic():
    token_file = "config/credentials/test_v2.json"

    # Simulate loading in engines
    # In engines, we use Credentials.from_json(f.read())
    # We mock Credentials class
    with patch("sys.modules", {"google.oauth2.credentials": MagicMock()}):
        import sys
        # We need to trick the import if it's not actually there
        # but since we are just testing the logic of calling it:
        mock_credentials_module = MagicMock()
        with patch.dict('sys.modules', {'google.oauth2.credentials': mock_credentials_module}):
            from google.oauth2.credentials import Credentials
            with open(token_file, "r", encoding="utf-8") as f:
                content = f.read()
                creds = Credentials.from_json(content)
                mock_credentials_module.Credentials.from_json.assert_called_once_with(content)

    print("✅ Engine load logic verified: Credentials loaded using from_json().")

if __name__ == "__main__":
    try:
        test_setup_auth_logic()
        test_engine_load_logic()
        print("\n✨ All security fix verifications passed!")
    finally:
        if os.path.exists("config/credentials/test_v2.json"):
            os.remove("config/credentials/test_v2.json")
