## Full stack app project real life application
- log all event(incomming http request) in a separate file
- use the celery task to read the log file and send new update to streaming endpoint
- which streaming protocol would be better; sse(because other way direction communication is not needed) or websocket
- in the case of sse : when does the backend stop sendng update ?

## Five next feature to add and test
- logs file autodiscovery
- logs chunks merging and push to remote instance
- 

# Future update on log streaming
- when pushing a single line to the client how to tie it with the file is coming from
- is the actual process optimal ?
- what will happen when a new celery beat will happen does all the files and all their content be pushed again -> keep track of the last read point