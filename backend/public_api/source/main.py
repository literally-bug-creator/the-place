import config
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        config.APP_PATH,
        host=config.HOST,
        port=config.PORT,
        reload=config.SHOULD_RELOAD,
    )
