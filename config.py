class Config:
    def __init__(self, env):

        SUPPORTED_ENVS = ["dev", "qa"]

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f"{env} is not a supported environment (supported envs: {SUPPORTED_ENVS})")

        self.base_url = {
            "dev": "http://rozhkovqa.tilda.ws/test_form",
            "qa": "http://rozhkovqa.tilda.ws/test_form"
        }[env]

        self.app_port = {
            "dev": 8080,
            "qa": 8080
        }[env]
