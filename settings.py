from pydantic import BaseModel, BaseSettings, Field

BASE_URL = 'http://51.250.91.47/'


class TestAdmin(BaseModel):
    login: str
    password: str


class Settings(BaseSettings):
    base_url: str = Field(..., env='BASE_URL')
    admin_login: str = Field(..., env='TEST_ADMIN_LOGIN')
    admin_password: str = Field(..., env='TEST_ADMIN_PASSWORD')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'

    @property
    def user(self) -> TestAdmin:
        return TestAdmin(
            login=self.admin_login,
            password=self.admin_password
        )


base_settings = Settings()
