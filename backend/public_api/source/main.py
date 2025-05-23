from config import get_app_settings
import uvicorn

settings = get_app_settings()

if __name__ == "__main__":
    uvicorn.run(
        app=settings.path,
        host=settings.host,
        port=settings.port,
        reload=settings.should_reload,
    )
