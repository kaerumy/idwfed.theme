from collective.grok import gs
from idwfed.theme import MessageFactory as _

@gs.importstep(
    name=u'idwfed.theme', 
    title=_('idwfed.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('idwfed.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
