"""
FastAPI default application class.
"""
from typing import Any, Dict, Optional, Sequence

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi


class FastAPIApp:
    """
    Default FastAPI application class.
    """

    def __init__(
        self,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_prefix: str = "",
        openapi_tags: Optional[Sequence[Dict[str, Any]]] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[Dict[str, Any]] = None,
        license_info: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the FastAPI application.
        """
        self.app = FastAPI(
            title=title,
            description=description,
            version=version,
            docs_url=docs_url,
            redoc_url=redoc_url,
            openapi_url=openapi_url,
            openapi_prefix=openapi_prefix,
            openapi_tags=openapi_tags,
            terms_of_service=terms_of_service,
            contact=contact,
            license_info=license_info,
            **kwargs,
        )

    def add_middleware(
        self,
        middleware_class: type,
        **kwargs: Any,
    ) -> None:
        """
        Add middleware to the application.
        """
        self.app.add_middleware(middleware_class, **kwargs)

    def add_cors_middleware(
        self,
        allow_origins: Sequence[str] = ("*",),
        allow_credentials: bool = True,
        allow_methods: Sequence[str] = ("*",),
        allow_headers: Sequence[str] = ("*",),
    ) -> None:
        """
        Add CORS middleware to the application.
        """
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=allow_origins,
            allow_credentials=allow_credentials,
            allow_methods=allow_methods,
            allow_headers=allow_headers,
        )

    def add_gzip_middleware(
        self,
        minimum_size: int = 500,
    ) -> None:
        """
        Add GZip middleware to the application.
        """
        self.app.add_middleware(GZipMiddleware, minimum_size=minimum_size)

    def add_https_redirect_middleware(self) -> None:
        """
        Add HTTPS redirect middleware to the application.
        """
        self.app.add_middleware(HTTPSRedirectMiddleware)

    def add_trusted_host_middleware(
        self,
        allowed_hosts: Sequence[str],
    ) -> None:
        """
        Add trusted host middleware to the application.
        """
        self.app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)

    def get_app(self) -> FastAPI:
        """
        Get the FastAPI application instance.
        """
        return self.app
