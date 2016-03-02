
import sys
sys.path.append('gen-py/scala_calc_thrift')
import ScalaCalcService

from thrift import Thrift

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
	
  transport = TSocket.TSocket('localhost', 1234)
  transport = TTransport.TBufferedTransport(transport)
  transport.open()
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = ScalaCalcService.Client(protocol)
  print client.add(2.0, 3.0) 
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)
