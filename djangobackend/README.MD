## Full stack app project real life application
- log all event(incomming http request) in a separate file
- use the celery task to read the log file and send new update to streaming endpoint
- which streaming protocol would be better; sse(because other way direction communication is not needed) or websocket
- in the case of sse : when does the backend stop sendng update ?

## Five next feature to add and test
- logs file autodiscovery
- logs chunks merging and push to remote instance
- 