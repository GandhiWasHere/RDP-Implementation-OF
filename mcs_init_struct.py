import struct
import binascii
from impacket.structure import Structure


class ServerResponseParser(Structure):
    commonHdr = (
        ('Version', 'B=3'),
        ('Reserved', 'B=0'),
        ('Length', '>H=len(TPDU)+4'),
        ('_TPDU', '_-TPDU', 'self["Length"]-4'),
        ('length', 'B=0'),
        ('pduType', 'B=0'),
        ('Length', 'B'),
        ('TPDUnumber', 'B'),
        ('response', 'B'),
        ('rt', 'B'),
        ('ca', 'B'),
        ('idk', 'B'),
        ('idk', 'L'),
        ('idk', 'L'),
        ('idk', 'L'),
        ('idk', 'L'),
        ('d', 'd'),
        ('d', 'd'),
        ('d', 'd'),
        ('headerType', 'H'),
        ('headerLength', 'H'),
        ('versionMajor', 'H'),
        ('versionMinor', 'H'),
        ('ClientRequestProtocols', 'I'),
        ('serverNetworkData', ':=""'),
    )