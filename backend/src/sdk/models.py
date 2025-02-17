from dataclasses import dataclass, asdict, field
import logging
from typing import Any, Optional, List

from flask import Response

from src.sdk.enums import CallbackResultType


@dataclass
class LoginConfig:
    custom_state: Optional[dict[str, str]] = None
    default_tenant_custom_domain: Optional[str] = None
    default_tenant_domain: Optional[str] = None

@dataclass
class LoginState:
    state: str
    code_verifier: str
    redirect_uri: str
    return_url: Optional[str]
    custom_state: Optional[dict[str, str]]

    def to_dict(self) -> dict[str, str | dict[str, str]]:
        return asdict(self)

@dataclass
class AuthConfig:
    client_id: str
    client_secret: str
    login_state_secret: str
    login_url: str
    redirect_uri: str
    wristband_application_domain: str

    custom_application_login_page_url: Optional[str] = None
    dangerously_disable_secure_cookies: bool = False
    root_domain: Optional[str] = None
    scopes: List[str] = field(default_factory=lambda: ['openid', 'offline_access', 'email'])
    use_custom_domains: bool = False
    use_tenant_subdomains: bool = False

@dataclass
class CallbackData:
    access_token: str
    id_token: str
    expires_in: int
    tenant_domain_name: str
    user_info: dict[str, Any]

    custom_state: Optional[dict[str, str]]
    refresh_token: Optional[str]
    return_url: Optional[str]
    tenant_custom_domain: Optional[str]

@dataclass
class CallbackResult:
    callback_data: Optional[CallbackData]
    type: CallbackResultType
    redirect_response: Optional[Response]

@dataclass
class TokenResponse:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    id_token: str
    scope: str

    @staticmethod
    def from_api_response(response: dict[str, Any]) -> 'TokenResponse':
        logging.info(f'Token response: {response}')
        return TokenResponse(
            access_token=response['access_token'],
            token_type=response['token_type'],
            expires_in=response['expires_in'],
            refresh_token=response['refresh_token'],
            id_token=response['id_token'],
            scope=response['scope']
        )