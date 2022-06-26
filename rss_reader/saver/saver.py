

class AbstractSaveHandler(ISaveHandler):
    
    _next_handler: Optional[ISaveHandler] = None
