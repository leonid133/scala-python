import sys
sys.path.append('gen-py/scala_calc_thrift')
import ScalaCalcService

from thrift import Thrift

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class Calculator:
  def add(self, n1, n2):
    print 'add(%d,%d)' % (n1, n2)
    return n1+n2

handler = Calculator()
processor = ScalaCalcService.Processor(handler)
transport = TSocket.TServerSocket(port=1234)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
server.serve()
