from app import create_app

app = create_app()

if __name__ == '__main__':
    from uvicorn import run

    # Uvicorn Docs
    # https://www.uvicorn.org/settings/#implementation
    run(
        app,
        host='0.0.0.0',
        port=8000,
        ws_max_queue=32,  # Default Value
        ws_max_size=16777216,  # Default Value
        ws_ping_timeout=None,  # for Eternal
        ws_ping_interval=None,  # for Eternal
    )
