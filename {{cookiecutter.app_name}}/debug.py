import uvicorn


if __name__ == '__main__':
    """
    Used to debug via pycharm configuration. Run this script 
    and it will allow for reloading and debugging
    """
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, debug=True)